from typing import Dict
from collections import defaultdict

### XXX TEMP XXX

class BootstrapFramework:
    def __init__(self):
        self.lastSearches = []
        self.__hidden = 0
        self.__mediaOptions = {
            "xs": "sm",
            "sm": "sm",
            "md": "md",
            "lg": "lg",
            "xl": "xl",
            "print": "print",
        }
        self.__spacings = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "4",
            "4": "6",
            "5": "12",
        }
        self.__grid = {
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
        self.__colors = {
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


    def framework_name(self) -> str:
        return "Bootstrap"

    def supportedVersion(self) -> list:
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

    def defaultCSS(self) -> Dict:

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

    #
    # .get all convertible items.
    #
    def get(self):  # ?\Generator
        for component in [
            self.general(),
            self.grid(),
            self.borders(),
            self.mediaObject(),
            self.colors(),
            self.display(),
            self.sizing(),
            self.flexElements(),
            self.spacing(),
            self.text(),
            self.floats(),
            self.positioning(),
            self.visibility(),
            self.alerts(),
            self.verticalAlignment(),
            self.badges(),
            self.breadcrumb(),
            self.buttons(),
            self.cards(),
            self.dropdowns(),
            self.forms(),
            self.inputGroups(),
            self.listGroups(),
            self.modals(),
            self.navs(),
            self.pagination(),
        ]:
            yield component

    def general(self) -> Dict:
        mainClasses = {
            "container-fluid": "container max-w-full mx-auto sm:px-4",
            "container": "container mx-auto sm:px-4",
            #  """
            #  => function () {
            #  if (self.isInLastSearches('jumbotron', 1)) {
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

        # mainClassesEachScreen = {
        #     'container-{screen}': 'container min-w-{screen} mx-auto sm:px-4',
        #     }

        # items = []
        # for (mainClasses as btClass => twClass) {
        #     items[btClass] = twClass;
        # }

        # for (mainClassesEachScreen as btClass => twClass) {
        #     for (self.mediaOptions as btMedia => twMedia) {
        #         items[btClass.replace('{screen}', btMedia)] = twClass.replace('{screen}', twMedia)
        #     }
        # }

        # return items
        return mainClasses

    # TODO
    def grid(self) -> Dict:
        items = {
            "row": "flex flex-wrap ",
            "col": "relative flex-grow max-w-full flex-1 px-4",
        }

        # col-(xs|sm|md|lg|xl) = (sm|md|lg|xl):flex-grow
        # ml-(xs|sm|md|lg|xl)-auto = (sm|md|lg|xl):mx-auto:ml-auto
        # mr-(xs|sm|md|lg|xl)-auto = (sm|md|lg|xl):mx-auto:mr-auto
        for btMedia, twMedia in self.__mediaOptions.items():
            items["col-" + btMedia] = (
                "relative " + twMedia + ":flex-grow " + twMedia + ":flex-1"
            )
            items["ml-" + btMedia + "-auto"] = twMedia + ":ml-auto"
            items["mr-" + btMedia + "-auto"] = twMedia + ":mr-auto"

            # col-btElem
            # col-(xs|sm|md|lg|xl)-btElem = (sm|md|lg|xl):w-twElem
            # offset-(xs|sm|md|lg|xl)-btElem = (sm|md|lg|xl):mx-auto
            for btElem, twElem in self.__grid.items():
                if btMedia == "xs":
                    items["col-" + btElem] = "w-" + twElem
                items[
                    "col-" + btMedia + "-" + btElem
                ] = f"{twMedia}:w-{twElem} pr-4 pl-4"

                # might work :)
                items["offset-" + btMedia + "-" + btElem] = twMedia + ":mx-" + twElem
        return items

    def mediaObject(self) -> Dict:
        # http://getbootstrap.com/docs/4.0/layout/media-object/
        return {
            "media": "flex items-start",
            "media-body": "flex-1",
        }

    def borders(self) -> Dict:
        items = defaultdict(str)

        side = {
            "top": "t",
            "right": "r",
            "bottom": "b",
            "left": "l",
        }
        for btSide, twSide in side.items():
            items[f"border-{btSide}"] = f"border-{twSide}"
            items[f"border-{btSide}-0"] = f"border-{twSide}-0"

        for btColor, twColor in self.__colors.items():
            items[f"border-{btColor}"] = f"border-{twColor}"

        style = {
            "top": "t",
            "right": "r",
            "bottom": "b",
            "left": "l",
            "circle": "full",
            "pill": "full py-2 px-4",
            "0": "none",
        }
        for btStyle, twStyle in style.items():
            items["rounded-" + btStyle] = "rounded-" + twStyle

        return items

    def colors(self) -> Dict:
        items = defaultdict(str)

        for btColor, twColor in self.__colors.items():
            items[f"text-{btColor}"] = f"text-{twColor}"
            items[f"bg-{btColor}"] = f"bg-{twColor}"
            items[f"table-{btColor}"] = f"bg-{twColor}"
            # items['bg-gradient-'.btColor] = 'bg-'.twColor;

        return items

    def display(self) -> Dict:
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
        for btElem, twElem in elem.items():
            items[f"d-{btElem}"] = twElem

            for btMedia, twMedia in self.__mediaOptions.items():
                items[f"d-{btMedia}-{btElem}"] = f"{twMedia}:{twElem}"

        return items

    # TODO
    def flexElements(self) -> Dict:
        items = defaultdict(str)

        self.__mediaOptions[""] = ""
        for btMedia, twMedia in self.__mediaOptions.items():
            for key in ['row', 'row-reverse', 'column', 'column-reverse']:
                items['flex'+('' if not btMedia else '-')+btMedia+'-'+key] = ('' if not twMedia else twMedia+':')+'flex-'+key.replace('column', 'col')

            for key in ['grow-0', 'grow-1', 'shrink-0', 'shrink-1']:
                items['flex'+('' if not btMedia else '-')+btMedia+'-'+key] = ('' if not twMedia else twMedia+':')+'flex-'+key.replace('-1', '')

            for key in ['start', 'end', 'center', 'between', 'around']:
                items['justify-content'+('' if not btMedia else '-')+btMedia+'-'+key] = ('' if not twMedia else twMedia+':')+'justify-'+key;

            for key in ['start', 'end', 'center', 'stretch', 'baseline']:
                items['align-items'+('' if not btMedia else '-')+btMedia+'-'+key] = ('' if not twMedia else twMedia+':')+'items-'+key;

            for key in ['start', 'end', 'center', 'stretch', 'baseline']:
                items['align-content'+('' if not btMedia else '-')+btMedia+'-'+key] = ('' if not twMedia else twMedia+':')+'content-'+key;

            for key in ['start', 'end', 'center', 'stretch', 'baseline']:
                items['align-self'+('' if not btMedia else '-')+btMedia+'-'+key] = ('' if not twMedia else twMedia+':')+'self-'+key;

            items['flex'+('' if not btMedia else '-')+btMedia+'-wrap'] = ('' if not twMedia else twMedia+':')+'flex-wrap';
            items['flex'+('' if not btMedia else '-')+btMedia+'-wrap-reverse'] = ('' if not twMedia else twMedia+':')+'flex-wrap-reverse';
            items['flex'+('' if not btMedia else '-')+btMedia+'-nowrap'] = ('' if not twMedia else twMedia+':')+'flex-no-wrap';

            items['flex'+('' if not btMedia else '-')+btMedia+'-nowrap'] = ('' if not twMedia else twMedia+':')+'flex-no-wrap';

            if btMedia != '':
                items['order-'+btMedia+'-{regex_number}'] = twMedia+':order-{regex_number}'

        return items

    def sizing(self):
        items = {
            "mw-100": "max-w-full",
            "mh-100": "max-h-full",
        }

        for btClass, twClass in [
            ("25", "1/4"),
            ("50", "1/2"),
            ("75", "3/4"),
            ("100", "full"),
        ]:
            items[f"w-{btClass}"] = f"w-{twClass}"

            # no percentages in TW for heights except for full
            if btClass == 100:
                items[f"h-{btClass}"] = f"h-{twClass}"
        return items

    def spacing(self):
        items = defaultdict(str)
        spacingProperties = ['p', 'm']

        for prop in spacingProperties:
            for btSpacing, twSpacing in self.__spacings.items():
                items[f"{prop}-{btSpacing}"] = f'{prop}-{twSpacing}'

        for prop in spacingProperties:
            for btMedia, twMedia in self.__mediaOptions.items():
                for btSpacing, twSpacing in self.__spacings.items():
                    items[f'{property}-{btMedia}-{btSpacing}'] = f'{twMedia}:{property}-{twSpacing}'
                    items[f'{prop}{{regex_string}}-{btMedia}-{btSpacing}'] = f'{twMedia}:{prop}{{regex_string}}-{twSpacing}'

                items[f'{prop}{{regex_string}}-{btMedia}-auto'] = f'{twMedia}:{property}{{regex_string}}-auto'

        return items

    def floats(self):
        items = defaultdict(str)

        for btMedia, twMedia in self.__mediaOptions.items():
            for alignment in ["left", "right", "none"]:
                items[f"float-{btMedia}-{alignment}"] = f"{twMedia}:float-{alignment}"

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

        self.__mediaOptions[""] = ""
        for alignment in ["left", "right", "center", "justify"]:
            for btMedia, twMedia in self.__mediaOptions.items():
                items[
                    "text" + ("" if not btMedia else f"-{btMedia}") + f"-{alignment}"
                ] = ("" if not twMedia else f"{twMedia}:") + f"text-{alignment}"
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

    def verticalAlignment(self):
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

        for btColor, twColor in colors:
            items[f"alert-{btColor}"] = twColor

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

        for btColor, twColor in colors:
            items[f"badge-{btColor}"] = twColor

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

        # for ([
        #     'sm' => '{tailwindo|py-1 px-2 leading-tight} text-xs ',
        #     'lg' => '{tailwindo|py-3 px-4 leading-tight} text-xl',
        # ] as btMedia => twClasses) {
        #     items['btn-'.btMedia] = twClasses;
        #     items['btn-group-'.btMedia] = twClasses;
        # }

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

        # for btColor, twColor in colors:
        #     items[f'btn-{btColor}'] = twColor # TODO XXX Below XXX
        #     items[f'btn-outline-{btColor}'] = preg_replace_callback('/(?<!hover:)(text-[^\s]+|bg-[^\s]+)/i', function (m) {
        #         if (strpos(m[1], 'bg-') !== false) {
        #             color = m[1].replace('bg-', '')

        #             return 'text-'.color.' border-'.color.' hover:bg-'.color.' hover:text-white';
        #         } else {
        #             return 'bg-white';
        #         }
        #     }, twColor);
        # }

        return items

    # ???  TODO?
    def isInLastSearches(self, thing, idx):
        return

    def cards(self):
        return {
            "card-deck": "flex flex-row flex-wrap md:flex-no-wrap -mx-1",
            "card-group": "flex flex-col",
            "card": (
                "relative block md:flex w-full md:min-w-0 md:mx-4 flex-col flex-no-shrink flex-grow rounded break-words border bg-white border-1 border-gray-300"
                if self.isInLastSearches("card-deck", None)
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

    def inputGroups(self):
        return {
            "input-group": "relative flex items-stretch w-full",
            "input-group-addon": "py-1 px-2 mb-1 text-base font-normal leading-normal text-gray-900 text-center bg-gray-300 border border-4 border-gray-100 rounded",
            "input-group-addon-lg": "py-2 px-3 mb-0 text-lg",
            "input-group-addon-sm": "py-3 px-4 mb-0 text-lg",
        }

    def listGroups(self):

        items = {
            "list-group": "flex flex-col pl-0 mb-0 border rounded border-gray-300",
            "list-group-item-action": "w-fill",
            "list-group-item": "relative block py-3 px-6 -mb-px border border-r-0 border-l-0 border-gray-300 no-underline",
            "list-group-flush": "",
        }

        # TODO
        for btColor, twColor in self.__colors.items():
            if btColor == "dark":
                items[f"list-group-item-{btColor}"] = "text-white bg-gray-700"
            elif btColor == "light":
                items[f"list-group-item-{btColor}"] = "text-black bg-gray-200"
            else:
                items[
                    f"list-group-item-{btColor}"
                ] = f"bg-{twColor}-200 text-{twColor}-900"

        return items

    def modals(self):
        # TODO
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
                if self.isInLastSearches("nav-tabs", 5)
                else ""
            )
            + (
                " border border-blue bg-blue rounded text-white mx-1"
                if self.isInLastSearches("nav-pills", 5)
                else ""
            )
        )

        items["nav-item"] = ""
        if self.isInLastSearches("nav-tabs", 5):
            items["nav-item"] += "-mb-px"
        elif self.isInLastSearches("nav-fill", 5):
            items["nav-item"] += " flex-auto text-center"
        elif self.isInLastSearches("nav-justified", 5):
            items["nav-item"] += " flex-grow text-center"

        items[
            "navbar"
        ] = "relative flex flex-wrap items-center content-between py-3 px-4"
        items["navbar-brand"] = "inline-block pt-1 pb-1 mr-4 text-lg whitespace-no-wrap"
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
