import re
from .bootstrap_framework import BootstrapFramework

# givencontent = ""
# iscssclassesonly = false
# changes = 0
# lastsearches = []
# generatecomponents = false
# components = []

# # @var \awssat\tailwindo\framework\framework */
# framework = none
# # @var string|null */
# prefix = none

# def __construct(str: content=None):


class Converter:
    def __init__(self, content=""):
        self.isCssClassesOnly = False
        self.changes = 0
        self.generateComponents = False

        # @var \Awssat\Tailwindo\Framework\Framework */
        self.framework = None
        # @var string|null */
        self.prefix = ""

        if content:
            self.setContent(content)

    def setContent(self, content: str):
        self.givenContent = content
        self.lastSearches = []
        self.components = []
        return self

    def setFramework(self, framework: str):
        framework = "BootstrapFramework"
        # 'Awssat\\Tailwindo\\Framework\\'.ucfirst($framework).'Framework';

        self.framework = BootstrapFramework()

        return self

    def getFramework(self):  # \Awssat\Tailwindo\Framework\Framework
        return self.framework

    #
    # * Is the given content a CSS content or HTML content.
    # */
    def classesOnly(self, value: bool):
        self.isCssClassesOnly = value
        return self

    #
    # * Is the given content a CSS content or HTML content.
    # */
    def setGenerateComponents(value: bool):
        self.generateComponents = value
        return self

    #
    # * The prefix option allows you to add a custom prefix to all of
    # Tailwind's generated utility classes. This can be really useful when
    # layering Tailwind on top of existing CSS where there might be naming
    # conflicts.
    # *
    # * @param string $prefix
    # *
    # * @return Converter
    #

    def setPrefix(self, prefix: str):
        prefix = prefix.strip()
        if not prefix:
            self.prefix = prefix

        return self

    # TODO
    def convert(self):
        # foreach (self.getFramework()->get() as $item)
        #   foreach ($item as $search => $replace)
        # item should return functions btstrp.grid() ...
        for item in self.getFramework().get():
            for search, replace in item.items():
                self.searchAndReplace(search, replace)

        return self

    def get(self, getComponents=False) -> str:
        # * Get the converted content.
        if getComponents:
            return self.getComponents()

        # regex replace TODO
        self.givenContent = re.sub(r"\{tailwindo\|([^\}]+)\}", "\1", self.givenContent)

        return self.givenContent

    def getComponents(self) -> str:
        result = ""
        if not self.generateComponents:
            return result

        # TODO
        for selector, classes in self.components:
            if selector == classes:
                continue

            # ???
            result += "".join([".", selector, "{\n\t@apply ", classes, ";\n}\n"])

        return result

    #
    # Get the number of committed changes.
    #
    def changes(self) -> int:
        return self.changes

    #
    # * search for a word in the last searches.
    # */
    def strpos(self):
        pass

    # @protected
    def isInLastSearches(self, searchFor: str, limit: int = 0) -> bool:
        for i, search in enumerate(self.lastSearches):
            # strpos?
            # if not self.strpos(search, searchFor):
            #    return True
            if searchFor in search:
                return True
            if i >= limit and limit > 0:
                return False
        return False

    def stripslashes(self, s: str) -> str:
        r = re.sub(r"\\(n|r)", "\n", s)
        r = re.sub(r"\\", "", r)
        return r

    # @protected
    def addToLastSearches(self, search):
        self.changes += 1

        # strip slashes?
        search = self.stripslashes(search)

        if self.isInLastSearches(search):
            return

        self.lastSearches = search

        if len(self.lastSearches) >= 50:
            # array_shift(self.lastSearches)
            self.lastSearches.pop(0)

    #
    # * Search the given content and replace.
    # *
    # * @param string          $search
    # * @param string|\Closure $replace
    # */
    # @protected
    def searchAndReplace(self, search, replace) -> None:
        # if ($replace instanceof \Closure) {
        #     $callableReplace = \Closure::bind($replace, self, self::class);
        #     $replace = $callableReplace();
        # }

        # "(?<start>class(?:Name)?\s*=\s*(?<quotation>[\"'])((?!\k<quotation>).)*)"
        regexStart = (
            "(?P<start>class(?:Name)?\s*=\s*(?P<quotation>[\"'])((?!(?P=quotation)).)*)"
            if not self.isCssClassesOnly
            else "(?P<start>\s*)"
        )
        # "(?<end>((?!\k<quotation>).)*\k<quotation>)"
        regexEnd = (
            "(?P<end>((?!(?P=quotation)).)*(?P=quotation))"
            if not self.isCssClassesOnly
            else "(?P<end>\s*)"
        )

        # TODO
        # search = preg_quote(search)

        currentSubstitute = 0

        # TODO
        while True:
            # if (strpos($search, '\{regex_string\}') !== false || strpos($search, '\{regex_number\}') !== false) {
            if "{regex_string}" in search or "{regex_number}" in search:
                currentSubstitute += 1
                # for regeName, regexValue in ['regex_string'=> '[a-zA-Z0-9]+', 'regex_number' => '[0-9]+']:
                for regeName, regexValue in [
                    ("{regex_string}", "[a-zA-Z0-9]+"),
                    ("{regex_number}", "[0-9]+"),
                ]:
                    #regexMatchCount = len(re.findall(fr"\\\\?\{{{regeName}\\\\?\}}", search))
                    search = re.sub(
                        fr"\\\\?\{{{regeName}\\\\?\}}",
                        f"(?<{regeName}_{currentSubstitute}>{regexValue})",
                        search,
                        count=1,
                    )
                    replace = re.sub(
                        fr"\\\\?\{{{regeName}\\\\?\}}",
                        f"{{{regeName}_{currentSubstitute}}}",
                        replace,
                        #count=(1 if regexMatchCount > 1 else 0),
                    )
                continue
            break

        # if (!preg_match_all('/'.$regexStart.'(?<given>(?<![\-_.\w\d])'.$search.'(?![\-_.\w\d]))'.$regexEnd.'/i', self.givenContent, $matches, PREG_SET_ORDER)) { return; }
        matches = re.findall(
            fr"{regexStart}(?P<given>(?<![\-_.\w\d]){search}(?![\-_.\w\d])){regexEnd}",
            self.givenContent,
        )
        print(matches)
        if not matches:
            return

        def evaluator(match):
            replace = re.sub(
                "\{regex_(string|number)_(\d+)\}",
                lambda m: m[f"regex_{m[1]}_{m[2]}"],
                replace,
            )
            if self.generateComponents and match["given"] not in self.components:
                self.components[match["given"]] = re.sub(
                    "\{tailwindo\|([^\}]+)\}", "\1", replace
                )

            def fn(css_class):
                responsiveOrStatePrefix = css_class[: css_class.index(":")]
                if responsiveOrStatePrefix:
                    utilityName = css_class.replace(responsiveOrStatePrefix + ":", "")
                    return f"{responsiveOrStatePrefix}:{self.prefix}{utilityName}"
                elif css_class:
                    return f"{self.prefix}{css_class}"
                return css_class

            if self.prefix:
                arr = replace.split()
                arr = map(fn, arr)
                # remove all nil items
                arr = list(lambda x: x, arr)  # array_filter(arr)

                return " ".join(arr).strip()

            return replace

        for match in matches:
            result = re.sub(
                fr"(?P<given>(?<![\-_.\w\d]){search}(?![\-_.\w\d]))",
                evaluator,
                match[0],
            )

            if match[0] != result:
                count = re.findall(r"\{tailwindo\|.*?\}", result)
                if count and count > 1:
                    result = re.sub(r"\{tailwindo\|.*?\}", "", result, count - 1)

                self.givenContent = self.givenContent.replace(match[0], result)
                self.addToLastSearches(search)
