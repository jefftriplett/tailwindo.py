import re
from .framework.bootstrap_framework import BootstrapFramework


class Converter:
    def __init__(self, content="", classesOnly: bool=False, generateComponents: bool=False, prefix="", framework="bootstrap"):
        self.changes = 0
        self.isCssClassesOnly = classesOnly
        self.generateComponents = generateComponents
        self.prefix = prefix

        self.framework = self.setFramework(framework)

        if content:
            self.setContent(content)

    def setContent(self, content: str):
        self.givenContent = content
        self.lastSearches = []
        self.components = []
        return self

    def setFramework(self, framework: str):
        """
        sets framework, 
        Only checks for to bootstrap...
        """
        if framework.lower() == "bootstrap":
            self.framework = BootstrapFramework()

        return self.framework

    def classesOnly(self, value: bool):
        """Is the given content a CSS content or HTML content."""
        self.isCssClassesOnly = value
        return self

    # * The prefix option allows you to add a custom prefix to all of
    # Tailwind's generated utility classes. This can be really useful when
    # layering Tailwind on top of existing CSS where there might be naming
    # conflicts.
    # *
    # * @param string $prefix
    # *
    # * @return Converter

    def setPrefix(self, prefix: str):
        prefix = prefix.strip()
        if prefix:
            self.prefix = prefix

        return self

    def convert(self):
        for item in self.framework.get():
            for search, replace in item.items():
                self._searchAndReplace(search, replace)

        return self

    def get(self, getComponents=False) -> str:
        # * Get the converted content.
        if getComponents:
            return self.getComponents()

        self.givenContent = re.sub(r"{tailwindo\|([^}]+)}", "\1", self.givenContent)

        return self.givenContent

    def getComponents(self) -> str:
        result = ""
        if not self.generateComponents:
            return result

        # TODO
        for selector, classes in self.components:
            if selector == classes:
                continue

            # improve??
            result += "".join([".", selector, "{\n\t@apply ", classes, ";\n}\n"])

        return result


    def changes(self) -> int:
        """Get the number of committed changes."""
        return self.changes

    #
    # * search for a word in the last searches.
    # */
    def _isInLastSearches(self, searchFor: str, limit: int = 0) -> bool:
        for i, search in enumerate(self.lastSearches):
            if searchFor in search:
                return True
            if i >= limit and limit > 0:
                return False
        return False

    @staticmethod
    def stripslashes(s: str) -> str:
        r = re.sub(r"\\(n|r)", "\n", s)
        r = re.sub(r"\\", "", r)
        return r

    def _addToLastSearches(self, search):
        self.changes += 1

        search = self.stripslashes(search)

        if self._isInLastSearches(search):
            return

        self.lastSearches = search

        if len(self.lastSearches) >= 50:
            # array_shift(self.lastSearches)
            self.lastSearches.pop(0)

    

    # * Search the given content and replace.
    # *
    # * @param string          $search
    # * @param string|\Closure $replace
    # */
    def _searchAndReplace(self, search, replace) -> None:
        # if ($replace instanceof \Closure):
        #     callableReplace = \Closure::bind($replace, self, self::class)
        #     replace = callableReplace()

        regexStart = (
            r"(?P<start>class(?:Name)?\s*=\s*(?P<quotation>[\"'])((?!(?P=quotation)).)*)"
            if not self.isCssClassesOnly
            else r"(?P<start>\s*)"
        )
        # "(?<end>((?!\k<quotation>).)*\k<quotation>)"
        regexEnd = (
            r"(?P<end>((?!(?P=quotation)).)*(?P=quotation))"
            if not self.isCssClassesOnly
            else r"(?P<end>\s*)"
        )

        # TODO OK?
        #search = re.escape(search)
        currentSubstitute = 0

        # TODO
        while True:
            # if (strpos($search, '{regex_string}') !== false || strpos($search, '{regex_number}') !== false) {
            if "{regex_string}" in search or "{regex_number}" in search:
                currentSubstitute += 1
                # for regexName, regexValue in ['regex_string'=> '[a-zA-Z0-9]+', 'regex_number' => '[0-9]+']:
                for regexName, regexValue in {
                    'regex_string': r'[a-zA-Z0-9]+',
                    'regex_number': r'[0-9]+',
                    }.items():
                    regexMatchCount = len(re.findall(fr"{{{regexName}}}", search))
                    search = re.sub(
                        fr"{{{regexName}}}",
                        f"(?P<{regexName}_{currentSubstitute}>{regexValue})",
                        search,
                        count=1,
                    )

                    replace = re.sub(
                        fr"{{{regexName}}}",
                        f"{{{regexName}_{currentSubstitute}}}",
                        replace,
                        count=(1 if regexMatchCount > 1 else 0),
                    )
            break

        matches = re.search(
            fr"{regexStart}(?P<given>(?<![\-_.\w\d]){search}(?![\-_.\w\d])){regexEnd}",
            self.givenContent,
        )
        if not matches: return

        def evaluator(match):

            #print(match)
            _replace = re.sub(
                "{regex_(string|number)_(\d+)}",
                lambda m: match[f"regex_{m[1]}_{m[2]}"],
                replace,
            )

            if self.generateComponents and match["given"] not in self.components:
                self.components[match["given"]] = re.sub(
                    "{tailwindo\|([^}]+)}", "\1", replace
                )

            def fn(css_class):
                try:
                    idx = css_class.index(':')
                except ValueError:
                    idx = 0
                responsiveOrStatePrefix = css_class[:idx]
                if responsiveOrStatePrefix:
                    utilityName = css_class.replace(responsiveOrStatePrefix + ":", "")
                    return f"{responsiveOrStatePrefix}:{self.prefix}{utilityName}"
                elif css_class:
                    return f"{self.prefix}{css_class}"
                return css_class

            if self.prefix:
                arr = _replace.split()
                arr = list(map(fn, arr))
                # remove all nil items
                # arr = list(filter(lambda x: x, arr))  # array_filter(arr)
                return r' '.join(arr).strip()

            return _replace
        # unecessary loop??
        for match in matches.groups():
            result = re.sub(
                fr"(?P<given>(?<![\-_.\w\d]){search}(?![\-_.\w\d]))",
                evaluator,
                matches[0],
            )

            if matches[0] != result:
                count = len(re.findall(r"{tailwindo\|.*?}", result))
                if count and count > 1:
                    result = re.sub(r"{tailwindo\|.*?}", "", result, count - 1)

                self.givenContent = self.givenContent.replace(matches[0], result)
                self._addToLastSearches(search)
