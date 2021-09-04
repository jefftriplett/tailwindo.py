import re
from collections import defaultdict

from .framework.bootstrap_framework import BootstrapFramework


class Converter:
    def __init__(
        self,
        content="",
        classes_only: bool = False,
        generate_components: bool = False,
        prefix="",
        framework="bootstrap",
    ):
        self.changes = 0
        self.is_css_classes_only = classes_only
        self.generate_components = generate_components
        self.prefix = prefix

        self.framework = self.set_framework(framework)

        if content:
            self.set_content(content)

    def set_content(self, content: str) -> "Converter":
        self.given_content = content
        self.last_searches = []
        self.components = defaultdict(str)
        return self

    def set_framework(self, framework: str):
        """
        sets framework, 
        Only checks for to bootstrap...
        """
        if framework.lower() == "bootstrap":
            self.framework = BootstrapFramework()

        return self.framework

    def classes_only(self, value: bool) -> "Converter":
        """Is the given content a CSS content or HTML content."""
        self.is_css_classes_only = value
        return self

    def set_prefix(self, prefix: str) -> "Converter":
        """
        The prefix option allows you to add a custom prefix to all of
        Tailwind's generated utility classes. This can be really useful when
        layering Tailwind on top of existing CSS where there might be naming
        conflicts.
        
        :param prefix:
        :return Converter
        """
        prefix = prefix.strip()
        if prefix:
            self.prefix = prefix

        return self

    def convert(self, get_components: bool = False) -> str:
        for item in self.framework.get():
            for search, replace in item.items():
                self._search_and_replace(search, replace)

        if get_components:
            return self.get_components()

        self.given_content = re.sub(r"{tailwindo\|([^}]+)}", "\1", self.given_content)

        return self.given_content

    def get_components(self) -> str:
        result = ""
        if not self.generate_components:
            return result

        for selector, classes in self.components.items():
            if selector == classes:
                continue

            # improve??
            result += "".join([".", selector, "{\n\t@apply ", classes, ";\n}\n"])

        return result

    def _is_in_last_searches(self, search_for: str, limit: int = 0) -> bool:
        """
        Search for a word in the last searches

        :param search_for:
        :param limit:
        :return: Boolean if search_for is in last_searches 
        """
        for i, search in enumerate(self.last_searches):
            if search_for in search:
                return True
            if i >= limit and limit > 0:
                return False
        return False

    @staticmethod
    def stripslashes(s: str) -> str:
        r = re.sub(r"\\(n|r)", "\n", s)
        r = re.sub(r"\\", "", r)
        return r

    def _add_to_last_searches(self, search: str) -> None:
        self.changes += 1

        search = self.stripslashes(search)

        if self._is_in_last_searches(search):
            return

        self.last_searches = search

        if len(self.last_searches) >= 50:
            # use deque.popleft() ?
            self.last_searches.pop(0)

    def _search_and_replace(self, search: str, replace: str) -> None:
        """
        Search the given content and replace
        :param search: 
        :param replace:
        """

        regex_start = (
            r"(?P<start>class(?:Name)?\s*=\s*(?P<quotation>[\"'])((?!(?P=quotation)).)*)"
            if not self.is_css_classes_only
            else r"(?P<start>\s*)"
        )
        regex_end = (
            r"(?P<end>((?!(?P=quotation)).)*(?P=quotation))"
            if not self.is_css_classes_only
            else r"(?P<end>\s*)"
        )

        current_substitute = 0

        # TODO
        while True:
            if "{regex_string}" in search or "{regex_number}" in search:
                current_substitute += 1
                for regex_name, regex_value in {
                    "regex_string": r"[a-zA-Z0-9]+",
                    "regex_number": r"[0-9]+",
                }.items():
                    regex_match_count = len(re.findall(fr"{{{regex_name}}}", search))
                    search = re.sub(
                        fr"{{{regex_name}}}",
                        f"(?P<{regex_name}_{current_substitute}>{regex_value})",
                        search,
                        count=1,
                    )

                    replace = re.sub(
                        fr"{{{regex_name}}}",
                        f"{{{regex_name}_{current_substitute}}}",
                        replace,
                        count=(1 if regex_match_count > 1 else 0),
                    )
            break

        pattern = re.compile(fr"{regex_start}(?P<given>(?<![\-_.\w\d]){search}(?![\-_.\w\d])){regex_end}")
        matches = pattern.search(self.given_content)
        if not matches:
            return

        def evaluator(match):
            _replace = re.sub(
                "{regex_(string|number)_(\d+)}",
                lambda m: match[f"regex_{m[1]}_{m[2]}"],
                replace,
            )

            if self.generate_components and match["given"] not in self.components:
                self.components[match["given"]] = re.sub(
                    r"{tailwindo\|([^}]+)}", "\1", replace
                )

            def fn(css_class):
                try:
                    idx = css_class.index(":")
                except ValueError:
                    idx = 0
                responsive_or_state_prefix = css_class[:idx]
                if responsive_or_state_prefix:
                    utility_name = css_class.replace(
                        responsive_or_state_prefix + ":", ""
                    )
                    return f"{responsive_or_state_prefix}:{self.prefix}{utility_name}"
                elif css_class:
                    return f"{self.prefix}{css_class}"
                return css_class

            if self.prefix:
                arr = _replace.split()
                arr = list(map(fn, arr))
                # remove all nil items
                # arr = list(filter(lambda x: x, arr))  # array_filter(arr)
                return r" ".join(arr).strip()

            return _replace

        # unecessary loop?
        # for match in matches.groups():
        result = re.sub(
            fr"(?P<given>(?<![\-_.\w\d]){search}(?![\-_.\w\d]))", evaluator, matches[0],
        )

        if matches[0] != result:
            count = len(re.findall(r"{tailwindo\|.*?}", result))
            if count and count > 1:
                result = re.sub(r"{tailwindo\|.*?}", "", result, count - 1)

            self.given_content = self.given_content.replace(matches[0], result)
            self._add_to_last_searches(search)
