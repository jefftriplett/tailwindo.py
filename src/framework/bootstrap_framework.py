from collections import defaultdict

class BootstrapFramework:
    def __init__(self):
        self.last_searches = []
        self._hidden = 0
        self._media_options = {
            "xs": "sm",
            "sm": "sm",
            "md": "md",
            "lg": "lg",
            "xl": "xl",
            "print": "print",
        }
        self._spacings = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "4",
            "4": "6",
            "5": "12",
        }
        self._grid = {
            "1": "1/6",
            "2": "1/5",
            "3": "1/4",
            "4": "1/3",
            "5": "2/5",
            "6": "1/2",
            "7": "3/5",
            "8": "2/3",
            "9": "3/4",
            "10": "4/5",
            "11": "5/6",
            "12": "full",
        }
        self._colors = {
            "primary": "blue-600",
            "secondary": "gray-600",
            "success": "green-500",
            "danger": "red-600",
            "warning": "yellow-500",
            "info": "teal-500",
            "light": "gray-100",
            "dark": "gray-900",
            "white": "white",
            "muted": "gray-700",
        }

    @property
    def name(self) -> str:
        return "Bootstrap"

    @property
    def supported_version(self) -> list:
        """
         * latest versions of Bootstrap/Tailwind during the coding of this file.
        """
        return [
            "4.4.1",  # bootstrap
            "1.4.0",  # tailwind
        ]

    """
     * This is the default css classes to be added to your main css file for compatibility.
    """

    def default_css(self) -> dict:

        return {
            # https://getbootstrap.com/docs/4.4/content/reboot/
            "h1": "",
            # ...
            "fieldset": "",
            # https://getbootstrap.com/docs/4.4/content/typography/
            "del": "",
            # ..
            "a": "",
            "p": "",
        }

    def get(self):  #  -> Generator[]
        """
        .get all convertible items.
        """
        for component in [
            self.general(),
            self.grid(),
            self.borders(),
            self.media_object(),
            self.colors(),
            self.display(),
            self.sizing(),
            self.flex_elements(),
            self.spacing(),
            self.text(),
            self.floats(),
            self.positioning(),
            self.visibility(),
            self.alerts(),
            self.vertical_alignment(),
            self.badges(),
            self.breadcrumb(),
            self.buttons(),
            self.cards(),
            self.dropdowns(),
            self.forms(),
            self.input_groups(),
            self.list_groups(),
            self.modals(),
            self.navs(),
            self.pagination(),
        ]:
            yield component

    def general(self) -> dict:
        main_classes = {
            "container-fluid": "container max-w-full mx-auto sm:px-4",
            "container": "container mx-auto sm:px-4",
            #  """
            #  => function () {
            #  if (self.is_in_last_searches('jumbotron', 1)) {
            #      return 'container mx-auto max-w-2xl sm:px-4';
            #  }
            #  return 'container mx-auto sm:px-4';
            #  },
            #  """
            # http://getbootstrap.com/docs/4.0/utilities/embed/
            "embed-responsive": "",
            "embed-responsive-item": "",
            "embed-responsive-21by9": "",
            "embed-responsive-16by9": "",
            "embed-responsive-4by3": "",
            "embed-responsive-1by1": "",
            # http://getbootstrap.com/docs/4.0/utilities/image-replacement/
            "text-hide": "",
            # http://getbootstrap.com/docs/4.0/utilities/screenreaders/
            "sr-only": "sr-only",
            "sr-only-focusable": "focus:not-sr-only",
            # http://getbootstrap.com/docs/4.0/content/images/
            "img-fluid": "max-w-full h-auto",
            "img-thumbnail": "max-w-full h-auto border-1 border-gray-200 rounded p-1",
            # http://getbootstrap.com/docs/4.0/content/tables/
            "table": "w-full max-w-full mb-4 bg-transparent",
            "table-sm": "p-1",
            # 'table-bordered' => '',
            # 'table-striped' => '',
            "table-responsive": "block w-full overflow-auto scrolling-touch",
            "table-responsive-{regex_string}": "block w-full overflow-auto scrolling-touch",
            # http://getbootstrap.com/docs/4.0/content/figures/
            "figure": "inline-block mb-4",
            "figure-img": "mb-2 leading-none",
            "figure-caption": "text-gray-",
            "fade": "opacity-0",
            "show": "opacity-100 block",  # need to be checked
            "disabled": "opacity-75",
            # http://getbootstrap.com/docs/4.0/components/collapse/
            # 'collapse' => 'hidden',
            "collapsing": "relative h-0 overflow-hidden ",  # there should be a h-0
            # http://getbootstrap.com/docs/4.0/utilities/close-icon/
            "close": "absolute top-0 bottom-0 right-0 px-4 py-3",
            # http://getbootstrap.com/docs/4.0/components/jumbotron/
            "jumbotron": "py-8 px-4 md:py-16 md:px-8 mb-8 bg-gray-200 rounded",
            "jumbotron-fluid": "pr-0 pl-0 rounded-none",
        }

        # main_classes_each_screen = {
        #     'container-{screen}': 'container min-w-{screen} mx-auto sm:px-4',
        #     }

        # items = defaultdict(str)
        # for bt_class, tw_class in main_classes.items():
        #     items[bt_class] = tw_class

        # for bt_class, tw_class in main_classes_each_screen.items():
        #     for bt_media, tw_media in self._media_options.items():
        #         items[bt_class.replace('{screen}', bt_media)] = tw_class.replace('{screen}', tw_media)

        # return items
        return main_classes

    # TODO
    def grid(self) -> dict:
        items = {
            "row": "flex flex-wrap ",
            "col": "relative flex-grow max-w-full flex-1 px-4",
        }

        # col-(xs|sm|md|lg|xl) = (sm|md|lg|xl):flex-grow
        # ml-(xs|sm|md|lg|xl)-auto = (sm|md|lg|xl):mx-auto:ml-auto
        # mr-(xs|sm|md|lg|xl)-auto = (sm|md|lg|xl):mx-auto:mr-auto
        for bt_media, tw_media in self._media_options.items():
            items["col-" + bt_media] = (
                "relative " + tw_media + ":flex-grow " + tw_media + ":flex-1"
            )
            items["ml-" + bt_media + "-auto"] = tw_media + ":ml-auto"
            items["mr-" + bt_media + "-auto"] = tw_media + ":mr-auto"

            # col-bt_elem
            # col-(xs|sm|md|lg|xl)-bt_elem = (sm|md|lg|xl):w-tw_elem
            # offset-(xs|sm|md|lg|xl)-bt_elem = (sm|md|lg|xl):mx-auto
            for bt_elem, tw_elem in self._grid.items():
                if bt_media == "xs":
                    items["col-" + bt_elem] = "w-" + tw_elem
                items[
                    "col-" + bt_media + "-" + bt_elem
                ] = f"{tw_media}:w-{tw_elem} pr-4 pl-4"

                # might work :)
                items["offset-" + bt_media + "-" + bt_elem] = (
                    tw_media + ":mx-" + tw_elem
                )
        return items

    def media_object(self) -> dict:
        # http://getbootstrap.com/docs/4.0/layout/media-object/
        return {
            "media": "flex items-start",
            "media-body": "flex-1",
        }

    def borders(self) -> dict:
        items = defaultdict(str)

        side = {
            "top": "t",
            "right": "r",
            "bottom": "b",
            "left": "l",
        }
        for bt_side, tw_side in side.items():
            items[f"border-{bt_side}"] = f"border-{tw_side}"
            items[f"border-{bt_side}-0"] = f"border-{tw_side}-0"

        for bt_color, tw_color in self._colors.items():
            items[f"border-{bt_color}"] = f"border-{tw_color}"

        style = {
            "top": "t",
            "right": "r",
            "bottom": "b",
            "left": "l",
            "circle": "full",
            "pill": "full py-2 px-4",
            "0": "none",
        }
        for bt_style, tw_style in style.items():
            items["rounded-" + bt_style] = "rounded-" + tw_style

        return items

    def colors(self) -> dict:
        items = defaultdict(str)

        for bt_color, tw_color in self._colors.items():
            items[f"text-{bt_color}"] = f"text-{tw_color}"
            items[f"bg-{bt_color}"] = f"bg-{tw_color}"
            items[f"table-{bt_color}"] = f"bg-{tw_color}"
            # items[f'bg-gradient-{bt_color}'] = f'bg-{tw_color}';

        return items

    def display(self) -> dict:
        # .d-none
        # .d-{sm,md,lg,xl}-none
        items = defaultdict(str)

        elem = {
            "none": "hidden",
            "inline": "inline",
            "inline-block": "inline-block",
            "block": "block",
            "table": "table",
            "table-cell": "table-cell",
            "table-row": "table-row",
            "flex": "flex",
            "inline-flex": "inline-flex",
        }
        for bt_elem, tw_elem in elem.items():
            items[f"d-{bt_elem}"] = tw_elem

            for bt_media, tw_media in self._media_options.items():
                items[f"d-{bt_media}-{bt_elem}"] = f"{tw_media}:{tw_elem}"

        return items

    def flex_elements(self) -> dict:
        items = defaultdict(str)

        self._media_options[""] = ""

        for bt_media, tw_media in self._media_options.items():
            for key in ["row", "row-reverse", "column", "column-reverse"]:
                items["flex" + ("" if not bt_media else "-") + bt_media + "-" + key] = (
                    ("" if not tw_media else tw_media + ":")
                    + "flex-"
                    + key.replace("column", "col")
                )

            for key in ["grow-0", "grow-1", "shrink-0", "shrink-1"]:
                items["flex" + ("" if not bt_media else "-") + bt_media + "-" + key] = (
                    ("" if not tw_media else tw_media + ":")
                    + "flex-"
                    + key.replace("-1", "")
                )

            for key in ["start", "end", "center", "between", "around"]:
                items[
                    "justify-content"
                    + ("" if not bt_media else "-")
                    + bt_media
                    + "-"
                    + key
                ] = (("" if not tw_media else tw_media + ":") + "justify-" + key)

            for key in ["start", "end", "center", "stretch", "baseline"]:
                items[
                    "align-items" + ("" if not bt_media else "-") + bt_media + "-" + key
                ] = (("" if not tw_media else tw_media + ":") + "items-" + key)

            for key in ["start", "end", "center", "stretch", "baseline"]:
                items[
                    "align-content"
                    + ("" if not bt_media else "-")
                    + bt_media
                    + "-"
                    + key
                ] = (("" if not tw_media else tw_media + ":") + "content-" + key)

            for key in ["start", "end", "center", "stretch", "baseline"]:
                items[
                    "align-self" + ("" if not bt_media else "-") + bt_media + "-" + key
                ] = (("" if not tw_media else tw_media + ":") + "self-" + key)

            items["flex" + ("" if not bt_media else "-") + bt_media + "-wrap"] = (
                "" if not tw_media else tw_media + ":"
            ) + "flex-wrap"
            items[
                "flex" + ("" if not bt_media else "-") + bt_media + "-wrap-reverse"
            ] = ("" if not tw_media else tw_media + ":") + "flex-wrap-reverse"
            items["flex" + ("" if not bt_media else "-") + bt_media + "-nowrap"] = (
                "" if not tw_media else tw_media + ":"
            ) + "flex-no-wrap"

            items["flex" + ("" if not bt_media else "-") + bt_media + "-nowrap"] = (
                "" if not tw_media else tw_media + ":"
            ) + "flex-no-wrap"

            if bt_media != "":
                items["order-" + bt_media + "-{regex_number}"] = (
                    tw_media + ":order-{regex_number}"
                )
        del self._media_options[""] # a better way??
        return items

    def sizing(self):
        items = {
            "mw-100": "max-w-full",
            "mh-100": "max-h-full",
        }

        for bt_class, tw_class in [
            ("25", "1/4"),
            ("50", "1/2"),
            ("75", "3/4"),
            ("100", "full"),
        ]:
            items[f"w-{bt_class}"] = f"w-{tw_class}"

            # no percentages in TW for heights except for full
            if bt_class == "100":
                items[f"h-{bt_class}"] = f"h-{tw_class}"
        return items

    def spacing(self):
        items = defaultdict(str)
        spacing_properties = ["p", "m"]

        for prop in spacing_properties:
            for bt_spacing, tw_spacing in self._spacings.items():
                items[f"{prop}-{bt_spacing}"] = f"{prop}-{tw_spacing}"

        for prop in spacing_properties:
            for bt_media, tw_media in self._media_options.items():
                for bt_spacing, tw_spacing in self._spacings.items():
                    items[
                        f"{prop}-{bt_media}-{bt_spacing}"
                    ] = f"{tw_media}:{prop}-{tw_spacing}"
                    items[
                        f"{prop}{{regex_string}}-{bt_media}-{bt_spacing}"
                    ] = f"{tw_media}:{prop}{{regex_string}}-{tw_spacing}"

                items[
                    f"{prop}{{regex_string}}-{bt_media}-auto"
                ] = f"{tw_media}:{prop}{{regex_string}}-auto"

        return items

    def floats(self):
        items = defaultdict(str)

        for bt_media, tw_media in self._media_options.items():
            for alignment in ["left", "right", "none"]:
                items[f"float-{bt_media}-{alignment}"] = f"{tw_media}:float-{alignment}"

        return items

    def text(self):
        items = {
            "text-nowrap": "whitespace-no-wrap",
            "text-truncate": "truncate",
            "text-lowercase": "lowercase",
            "text-uppercase": "uppercase",
            "text-capitalize": "capitalize",
            "initialism": "",
            "lead": "text-xl font-light",
            "small": "text-xs",
            "mark": "",
            "display-1": "text-xl",
            "display-2": "text-2xl",
            "display-3": "text-3xl",
            "display-4": "text-4xl",
            "h-1": "mb-2 font-medium leading-tight text-4xl",
            "h-2": "mb-2 font-medium leading-tight text-3xl",
            "h-3": "mb-2 font-medium leading-tight text-2xl",
            "h-4": "mb-2 font-medium leading-tight text-xl",
            "h-5": "mb-2 font-medium leading-tight text-lg",
            "h-6": "mb-2 font-medium leading-tight text-base",
            "blockquote": "mb-6 text-lg",
            "blockquote-footer": "block text-gray-",
            "font-weight-bold": "font-bold",
            "font-weight-normal": "font-normal",
            "font-weight-300": "font-light",
            "font-italic": "italic",
        }

        self._media_options[""] = ""
        for alignment in ["left", "right", "center", "justify"]:
            for bt_media, tw_media in self._media_options.items():
                items[
                    "text" + ("" if not bt_media else f"-{bt_media}") + f"-{alignment}"
                ] = ("" if not tw_media else f"{tw_media}:") + f"text-{alignment}"
        del self._media_options[""] # a better way??
        return items

    def positioning(self):
        items = {
            "position-static": "static",
            "position-relative": "relative",
            "position-absolute": "absolute",
            "position-fixed": "fixed",
            "position-sticky": "",
            "fixed-top": "top-0",
            "fixed-bottom": "bottom-0",
        }

        return items

    def vertical_alignment(self):
        # same bt <> tw
        return defaultdict()

    def visibility(self):
        # same
        return defaultdict()

    def alerts(self):
        items = {
            "alert": "relative px-3 py-3 mb-4 border rounded",
            "alert-heading": "",  # color: inherit
            "alert-link": "font-bold no-underline text-current",
            "alert-dismissible": "",
        }

        colors = [
            ("primary", "bg-blue-200 border-blue-300 text-blue-800"),
            ("secondary", "bg-gray-300 border-gray-400 text-gray-800"),
            ("success", "bg-green-200 border-green-300 text-green-800"),
            ("danger", "bg-red-200 border-red-300 text-red-800"),
            ("warning", "bg-orange-200 border-orange-300 text-orange-800"),
            ("info", "bg-teal-200 border-teal-300 text-teal-800"),
            ("light", "bg-white text-gray-600"),
            ("dark", "bg-gray-400 border-gray-500 text-gray-900"),
        ]

        for bt_color, tw_color in colors:
            items[f"alert-{bt_color}"] = tw_color

        return items

    def badges(self):
        items = {
            "badge": "inline-block p-1 text-center font-semibold text-sm align-baseline leading-none rounded",
            "badge-pill": "rounded-full py-1 px-3",
        }

        colors = [
            ("primary", "bg-blue-500 text-white hover:bg-blue-600"),
            ("secondary", "bg-gray-600 text-white hover:bg-gray-700"),
            ("success", "bg-green-500 text-white hover:green-600"),
            ("danger", "bg-red-600 text-white hover:bg-red-700"),
            ("warning", "bg-orange-400 text-black hover:bg-orange-500"),
            ("info", "bg-teal-500 text-white hover:bg-teal-600"),
            ("light", "bg-gray-100 text-gray-800 hover:bg-gray-200"),
            ("dark", "bg-gray-900 text-white"),
        ]

        for bt_color, tw_color in colors:
            items[f"badge-{bt_color}"] = tw_color

        return items

    def breadcrumb(self):
        return {
            "breadcrumb": "flex flex-wrap list-reset pt-3 pb-3 py-4 px-4 mb-4 bg-gray-200 rounded",
            "breadcrumb-item": "inline-block px-2 py-2 text-gray-700",
        }

    # TODO
    def buttons(self):
        items = {
            "btn": "inline-block align-middle text-center select-none border font-normal whitespace-no-wrap rounded {tailwindo|py-1 px-3 leading-normal} no-underline",
            "btn-group": "relative inline-flex align-middle",
            "btn-group-vertical": "relative inline-flex align-middle flex-col items-start justify-center",
            "btn-toolbar": "flex flex-wrap justify-start",
            "btn-link": "font-normal text-blue-700 bg-transparent",
            "btn-block": "block w-full",
        }

        # for bt_media, tw_classes in [
        #     ('sm', '{tailwindo|py-1 px-2 leading-tight} text-xs '),
        #     ('lg', '{tailwindo|py-3 px-4 leading-tight} text-xl'),
        # ]:
        #     items[f'btn-{bt_media}'] = tw_classes
        #     items[f'btn-group-{bt_media}'] = tw_classes

        colors = [
            ("primary", "bg-blue-600 text-white hover:bg-blue-600"),
            ("secondary", "bg-gray-600 text-white hover:bg-gray-700"),
            ("success", "bg-green-500 text-white hover:bg-green-600"),
            ("danger", "bg-red-600 text-white hover:bg-red-700"),
            ("warning", "bg-orange-400 text-black hover:bg-orange-500"),
            ("info", "bg-teal-500 text-white hover:bg-teal-600"),
            ("light", "bg-gray-100 text-gray-800 hover:bg-gray-200"),
            ("dark", "bg-gray-900 text-white hover:bg-gray-900"),
        ]

        # def _replace(m):
        #     if m[1].find('bg-') != -1:
        #         color = m[1].replace('bg-', '')
        #         return f'text-{color} border-{color} hover:bg-{color} hover:text-white'
        #      else:
        #          return 'bg-white'
        #
        # for bt_color, tw_color in colors:
        #     items[f'btn-{bt_color}'] = tw_color # TODO XXX Below XXX
        #     items[f'btn-outline-{bt_color}'] = re.sub(
        #           r'(?P<!hover:)(text-[^\s]+|bg-[^\s]+)', 
        #           _replace, 
        #           tw_color
        #           )

        return items

    # ???  TODO?
    def is_in_last_searches(self, thing, idx):
        return

    def cards(self):
        return {
            "card-deck": "flex flex-row flex-wrap md:flex-no-wrap -mx-1",
            "card-group": "flex flex-col",
            "card": (
                "relative block md:flex w-full md:min-w-0 md:mx-4 flex-col flex-no-shrink flex-grow rounded break-words border bg-white border-1 border-gray-300"
                if self.is_in_last_searches("card-deck", None)
                else "relative flex flex-col min-w-0 rounded break-words border bg-white border-1 border-gray-300"
            ),
            "card-body": "flex-auto p-6",
            "card-title": "mb-3",
            "card-text": "mb-0",
            "card-subtitle": "-mt-2 mb-0",
            "card-link": "ml-6",
            "card-header": "py-3 px-6 mb-0 bg-gray-200 border-b-1 border-gray-300 text-gray-900",
            "card-footer": "py-3 px-6 bg-gray-200 border-t-1 border-gray-300",
            "card-header-tabs": "border-b-0 -ml-2 -mb-3",
            "card-header-pills": "-ml-3 -mr-3",
            "card-img-overlay": "absolute inset-y-0 inset-x-0 p-6",
            "card-img": "w-full rounded",
            "card-img-top": "w-full rounded rounded-t",
            "card-img-bottom": "w-full rounded rounded-b",
        }

    def dropdowns(self):
        return {
            "dropdown": "relative",
            "dropup": "relative",
            "dropdown-toggle": " inline-block w-0 h-0 ml-1 align border-b-0 border-t-1 border-r-1 border-l-1",
            "dropdown-menu": " absolute left-0 z-50 float-left hidden list-reset	 py-2 mt-1 text-base bg-white border border-gray-300 rounded",
            "dropdown-divider": "h-0 my-2 overflow-hidden border-t-1 border-gray-300",
            "dropdown-item": "block w-full py-1 px-6 font-normal text-gray-900 whitespace-no-wrap border-0",
            "dropdown-header": "block py-2 px-6 mb-0 text-sm text-gray-800 whitespace-no-wrap",
        }

    def forms(self):
        return {
            "form-group": "mb-4",
            "form-control": "block appearance-none w-full py-1 px-2 mb-1 text-base leading-normal bg-white text-gray-800 border border-gray-200 rounded",
            "form-control-lg": "py-2 px-4 text-lg leading-normal rounded",
            "form-control-sm": "py-1 px-2 text-sm leading-normal rounded",
            "form-control-file": "block appearance-none",
            "form-control-range": "block appearance-none",
            "form-inline": "flex items-center",
            "col-form-label": "pt-2 pb-2 mb-0 leading-normal",
            "col-form-label-lg": "pt-3 pb-3 mb-0 leading-normal",
            "col-form-label-sm": "pt-1 pb-1 mb-0 leading-normal",
            "col-form-legend": "pt-2 pb-2 mb-0 text-base",
            "col-form-plaintext": "pt-2 pb-2 mb-0 leading-normal bg-transparent border-transparent border-r-0 border-l-0 border-t border-b",
            "form-text": "block mt-1",
            "form-row": "flex flex-wrap -mr-1 -ml-1",
            "form-check": "relative block mb-2",
            "form-check-label": "text-gray-700 pl-6 mb-0",
            "form-check-input": "absolute mt-1 -ml-6",
            "form-check-inline": "inline-block mr-2",
            "valid-feedback": "hidden mt-1 text-sm text-green",
            "valid-tooltip": "absolute z-10 hidden w-4 font-normal leading-normal text-white rounded p-2 bg-green-700",
            "is-valid": "bg-green-700",
            "invalid-feedback": "hidden mt-1 text-sm text-red",
            "invalid-tooltip": "absolute z-10 hidden w-4 font-normal leading-normal text-white rounded p-2 bg-red-700",
            "is-invalid": "bg-red-700",
        }

    def input_groups(self):
        return {
            "input-group": "relative flex items-stretch w-full",
            "input-group-addon": "py-1 px-2 mb-1 text-base font-normal leading-normal text-gray-900 text-center bg-gray-300 border border-4 border-gray-100 rounded",
            "input-group-addon-lg": "py-2 px-3 mb-0 text-lg",
            "input-group-addon-sm": "py-3 px-4 mb-0 text-lg",
        }

    def list_groups(self):

        items = {
            "list-group": "flex flex-col pl-0 mb-0 border rounded border-gray-300",
            "list-group-item-action": "w-full",
            "list-group-item": "relative block py-3 px-6 -mb-px border border-r-0 border-l-0 border-gray-300 no-underline",
            "list-group-flush": "",
        }

        for bt_color, tw_color in self._colors.items():
            if bt_color == "dark":
                items[f"list-group-item-{bt_color}"] = "text-white bg-gray-700"
            elif bt_color == "light":
                items[f"list-group-item-{bt_color}"] = "text-black bg-gray-200"
            else:
                items[
                    f"list-group-item-{bt_color}"
                ] = f"bg-{tw_color}-200 text-{tw_color}-900"

        return items

    def modals(self):
        return defaultdict()

    def navs(self):
        items = {
            "nav": "flex flex-wrap list-none pl-0 mb-0",
            "nav-tabs": "border border-t-0 border-r-0 border-l-0 border-b-1 border-gray-200",
            "nav-pills": "",
            "nav-fill": "",
            "nav-justified": "",
        }

        items["nav-link"] = (
            "inline-block py-2 px-4 no-underline"
            + (
                " border border-b-0 mx-1 rounded rounded-t"
                if self.is_in_last_searches("nav-tabs", 5)
                else ""
            )
            + (
                " border border-blue bg-blue rounded text-white mx-1"
                if self.is_in_last_searches("nav-pills", 5)
                else ""
            )
        )

        items["nav-item"] = ""
        if self.is_in_last_searches("nav-tabs", 5):
            items["nav-item"] += "-mb-px"
        elif self.is_in_last_searches("nav-fill", 5):
            items["nav-item"] += " flex-auto text-center"
        elif self.is_in_last_searches("nav-justified", 5):
            items["nav-item"] += " flex-grow text-center"

        items[
            "navbar"
        ] = "relative flex flex-wrap items-center content-between py-3 px-4"
        items["navbar-brand"] = "inline-block pt-1 pb-1 mr-4 text-lg whitespace-nowrap"
        items["navbar-nav"] = "flex flex-wrap list-reset pl-0 mb-0"
        items["navbar-text"] = "inline-block pt-2 pb-2"
        items["navbar-dark"] = "text-white"
        items["navbar-light"] = "text-black"
        items["navbar-collapse"] = "flex-grow items-center"
        items["navbar-expand"] = "flex-no-wrap content-start"
        items["navbar-expand-{regex_string}"] = ""
        items[
            "navbar-toggler"
        ] = "py-1 px-2 text-md leading-normal bg-transparent border border-transparent rounded"

        # for now
        items["collapse"] = "hidden"
        items["navbar-toggler-icon"] = "px-5 py-1 border border-gray-600 rounded"

        return items

    def pagination(self) -> dict:
        return {
            "pagination": "flex list-reset pl-0 rounded",
            "pagination-lg": "text-xl",
            "pagination-sm": "text-sm",
            "page-link": "relative block py-2 px-3 -ml-px leading-normal text-blue bg-white border border-gray-200 no-underline hover:text-blue-800 hover:bg-gray-200",
            # 'page-link': 'relative block py-2 px-3 -ml-px leading-normal text-blue bg-white border border-gray-',
        }
