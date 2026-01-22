# coding:utf-8
from enum import Enum
from typing import Union
import json

from PySide6.QtXml import QDomDocument
from PySide6.QtCore import QRectF, Qt, QFile, QObject, QRect
from PySide6.QtGui import QIcon, QIconEngine, QColor, QPixmap, QImage, QPainter, QFontDatabase, QFont, QAction, QPainterPath
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QApplication

from .config import isDarkTheme, Theme
from .overload import singledispatchmethod


class FluentIconEngine(QIconEngine):
    """ Fluent icon engine """

    def __init__(self, icon, reverse=False):
        """
        Parameters
        ----------
        icon: QICon | Icon | FluentIconBase
            the icon to be drawn

        reverse: bool
            whether to reverse the theme of icon
        """
        super().__init__()
        self.icon = icon
        self.isThemeReversed = reverse

    def paint(self, painter, rect, mode, state):
        painter.save()

        if mode == QIcon.Disabled:
            painter.setOpacity(0.5)
        elif mode == QIcon.Selected:
            painter.setOpacity(0.7)

        # change icon color according to the theme
        icon = self.icon

        if not self.isThemeReversed:
            theme = Theme.AUTO
        else:
            theme = Theme.LIGHT if isDarkTheme() else Theme.DARK

        if isinstance(self.icon, Icon):
            icon = self.icon.fluentIcon.icon(theme)
        elif isinstance(self.icon, FluentIconBase):
            icon = self.icon.icon(theme)

        if rect.x() == 19:
            rect = rect.adjusted(-1, 0, 0, 0)

        icon.paint(painter, rect, Qt.AlignCenter, QIcon.Normal, state)
        painter.restore()

    def clone(self) -> QIconEngine:
        return FluentIconEngine(self.icon, self.isThemeReversed)

    def pixmap(self, size, mode, state):
        image = QImage(size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        pixmap = QPixmap.fromImage(image, Qt.NoFormatConversion)

        painter = QPainter(pixmap)
        rect = QRect(0, 0, size.width(), size.height())
        self.paint(painter, rect, mode, state)
        return pixmap


class SvgIconEngine(QIconEngine):
    """ Svg icon engine """

    def __init__(self, svg: str):
        super().__init__()
        self.svg = svg

    def paint(self, painter, rect, mode, state):
        drawSvgIcon(self.svg.encode(), painter, rect)

    def clone(self) -> QIconEngine:
        return SvgIconEngine(self.svg)

    def pixmap(self, size, mode, state):
        image = QImage(size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        pixmap = QPixmap.fromImage(image, Qt.NoFormatConversion)

        painter = QPainter(pixmap)
        rect = QRect(0, 0, size.width(), size.height())
        self.paint(painter, rect, mode, state)
        return pixmap


class FontIconEngine(QIconEngine):
    """ Font icon engine """

    def __init__(self, fontFamily: str, char: str, color, isBold):
        super().__init__()
        self.color = color
        self.char = char
        self.fontFamily = fontFamily
        self.isBold = isBold

    def paint(self, painter, rect, mode, state):
        font = QFont(self.fontFamily)
        font.setBold(self.isBold)
        font.setPixelSize(round(rect.height()))
        painter.setFont(font)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self.color)
        painter.setRenderHints(
            QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing)

        path = QPainterPath()
        path.addText(rect.x(), rect.y() + rect.height(), font, self.char)
        painter.drawPath(path)


    def clone(self) -> QIconEngine:
        return FontIconEngine(self.fontFamily, self.char, self.color, self.isBold)

    def pixmap(self, size, mode, state):
        image = QImage(size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        pixmap = QPixmap.fromImage(image, Qt.NoFormatConversion)

        painter = QPainter(pixmap)
        rect = QRect(0, 0, size.width(), size.height())
        self.paint(painter, rect, mode, state)
        return pixmap


def getIconColor(theme=Theme.AUTO, reverse=False):
    """ get the color of icon based on theme """
    if not reverse:
        lc, dc = "black", "white"
    else:
        lc, dc = "white", "black"

    if theme == Theme.AUTO:
        color = dc if isDarkTheme() else lc
    else:
        color = dc if theme == Theme.DARK else lc

    return color


def drawSvgIcon(icon, painter, rect):
    """ draw svg icon

    Parameters
    ----------
    icon: str | bytes | QByteArray
        the path or code of svg icon

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon
    """
    renderer = QSvgRenderer(icon)
    renderer.render(painter, QRectF(rect))


def writeSvg(iconPath: str, indexes=None, **attributes):
    """ write svg with specified attributes

    Parameters
    ----------
    iconPath: str
        svg icon path

    indexes: List[int]
        the path to be filled

    **attributes:
        the attributes of path

    Returns
    -------
    svg: str
        svg code
    """
    if not iconPath.lower().endswith('.svg'):
        return ""

    f = QFile(iconPath)
    f.open(QFile.ReadOnly)

    dom = QDomDocument()
    dom.setContent(f.readAll())

    f.close()

    # change the color of each path
    pathNodes = dom.elementsByTagName('path')
    indexes = range(pathNodes.length()) if not indexes else indexes
    for i in indexes:
        element = pathNodes.at(i).toElement()

        for k, v in attributes.items():
            element.setAttribute(k, v)

    return dom.toString()


def drawIcon(icon, painter, rect, state=QIcon.Off, **attributes):
    """ draw icon

    Parameters
    ----------
    icon: str | QIcon | FluentIconBaseBase
        the icon to be drawn

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon

    **attribute:
        the attribute of svg icon
    """
    if isinstance(icon, FluentIconBase):
        icon.render(painter, rect, **attributes)
    elif isinstance(icon, Icon):
        icon.fluentIcon.render(painter, rect, **attributes)
    else:
        icon = QIcon(icon)
        icon.paint(painter, QRectF(rect).toRect(), Qt.AlignCenter, state=state)


class FluentIconBase:
    """ Fluent icon base class """

    def path(self, theme=Theme.AUTO) -> str:
        """ get the path of icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`
        """
        raise NotImplementedError

    def icon(self, theme=Theme.AUTO, color: QColor = None) -> QIcon:
        """ create a fluent icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `qconfig.theme`

        color: QColor | Qt.GlobalColor | str
            icon color, only applicable to svg icon
        """
        path = self.path(theme)

        if not (path.endswith('.svg') and color):
            return QIcon(self.path(theme))

        color = QColor(color).name()
        return QIcon(SvgIconEngine(writeSvg(path, fill=color)))

    def colored(self, lightColor: QColor, darkColor: QColor) -> "ColoredFluentIcon":
        """ create a colored fluent icon

        Parameters
        ----------
        lightColor: str | QColor | Qt.GlobalColor
            icon color in light mode

        darkColor: str | QColor | Qt.GlobalColor
            icon color in dark mode
        """
        return ColoredFluentIcon(self, lightColor, darkColor)

    def qicon(self, reverse=False) -> QIcon:
        """ convert to QIcon, the theme of icon will be updated synchronously with app

        Parameters
        ----------
        reverse: bool
            whether to reverse the theme of icon
        """
        return QIcon(FluentIconEngine(self, reverse))

    def render(self, painter, rect, theme=Theme.AUTO, indexes=None, **attributes):
        """ draw svg icon

        Parameters
        ----------
        painter: QPainter
            painter

        rect: QRect | QRectF
            the rect to render icon

        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`

        indexes: List[int]
            the svg path to be modified

        **attributes:
            the attributes of modified path
        """
        icon = self.path(theme)

        if icon.endswith('.svg'):
            if attributes:
                icon = writeSvg(icon, indexes, **attributes).encode()

            drawSvgIcon(icon, painter, rect)
        else:
            icon = QIcon(icon)
            rect = QRectF(rect).toRect()
            painter.drawPixmap(rect, icon.pixmap(QRectF(rect).toRect().size()))


class FluentFontIconBase(FluentIconBase):
    """ Fluent font icon base class """

    _isFontLoaded = False
    fontId = None
    fontFamily = None
    _iconNames = {}

    def __init__(self, char: str):
        super().__init__()
        self.char = char
        self.lightColor = QColor(0, 0, 0)
        self.darkColor = QColor(255, 255, 255)
        self.isBold = False
        self.loadFont()

    @classmethod
    def fromName(cls, name: str):
        icon = cls("")
        icon.char = cls._iconNames.get(name, "")
        return icon

    def bold(self):
        self.isBold = True
        return self

    def icon(self, theme=Theme.AUTO, color: QColor = None) -> QIcon:
        if not color:
            color = self._getIconColor(theme)

        return QIcon(FontIconEngine(self.fontFamily, self.char, color, self.isBold))

    def colored(self, lightColor, darkColor):
        self.lightColor = QColor(lightColor)
        self.darkColor = QColor(darkColor)
        return self

    def render(self, painter: QPainter, rect, theme=Theme.AUTO, indexes=None, **attributes):
        color = self._getIconColor(theme)

        if "fill" in attributes:
            color = QColor(attributes["fill"])

        font = QFont(self.fontFamily)
        font.setBold(self.isBold)
        font.setPixelSize(round(rect.height()))
        painter.setFont(font)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(color)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing)

        path = QPainterPath()
        path.addText(rect.x(), rect.y() + rect.height(), font, self.char)
        painter.drawPath(path)

    def iconNameMapPath(self) -> str:
        return None

    def loadFont(self):
        """ Load icon font """
        cls = self.__class__
        if cls._isFontLoaded or not QApplication.instance():
            return

        file = QFile(self.path())
        if not file.open(QFile.ReadOnly):
            raise FileNotFoundError(f"Cannot open font file: {self.path()}")

        data = file.readAll()
        file.close()

        cls.fontId = QFontDatabase.addApplicationFontFromData(data)
        cls.fontFamily = QFontDatabase.applicationFontFamilies(cls.fontId)[0]

        if self.iconNameMapPath():
            self.loadIconNames()

    def loadIconNames(self):
        """ Load icon name map """
        cls = self.__class__
        cls._iconNames.clear()

        file = QFile(self.iconNameMapPath())
        if not file.open(QFile.ReadOnly):
            raise FileNotFoundError(f"Cannot open font file: {self.iconNameMapPath()}")

        cls._iconNames = json.loads(str(file.readAll(), encoding='utf-8'))
        file.close()

    def _getIconColor(self, theme):
        if theme == Theme.AUTO:
            color = self.darkColor if isDarkTheme() else self.lightColor
        else:
            color = self.darkColor if theme == Theme.DARK else self.lightColor

        return color


class ColoredFluentIcon(FluentIconBase):
    """ Colored fluent icon """

    def __init__(self, icon: FluentIconBase, lightColor, darkColor):
        """
        Parameters
        ----------
        icon: FluentIconBase
            the icon to be colored

        lightColor: str | QColor | Qt.GlobalColor
            icon color in light mode

        darkColor: str | QColor | Qt.GlobalColor
            icon color in dark mode
        """
        super().__init__()
        self.fluentIcon = icon
        self.lightColor = QColor(lightColor)
        self.darkColor = QColor(darkColor)

    def path(self, theme=Theme.AUTO) -> str:
        return self.fluentIcon.path(theme)

    def render(self, painter, rect, theme=Theme.AUTO, indexes=None, **attributes):
        icon = self.path(theme)

        if not icon.endswith('.svg'):
            return self.fluentIcon.render(painter, rect, theme, indexes, attributes)

        if theme == Theme.AUTO:
            color = self.darkColor if isDarkTheme() else self.lightColor
        else:
            color = self.darkColor if theme == Theme.DARK else self.lightColor

        attributes.update(fill=color.name())
        icon = writeSvg(icon, indexes, **attributes).encode()
        drawSvgIcon(icon, painter, rect)



class FluentIcon(FluentIconBase, Enum):
    """ Fluent icon """

    UP = "Up"
    ADD = "Add"
    BUS = "Bus"
    CAR = "Car"
    CUT = "Cut"
    IOT = "IOT"
    PIN = "Pin"
    TAG = "Tag"
    VPN = "VPN"
    CAFE = "Cafe"
    CHAT = "Chat"
    COPY = "Copy"
    CODE = "Code"
    DOWN = "Down"
    EDIT = "Edit"
    FLAG = "Flag"
    FONT = "Font"
    GAME = "Game"
    HELP = "Help"
    HIDE = "Hide"
    HOME = "Home"
    INFO = "Info"
    LEAF = "Leaf"
    LINK = "Link"
    MAIL = "Mail"
    MENU = "Menu"
    MUTE = "Mute"
    MORE = "More"
    MOVE = "Move"
    PLAY = "Play"
    SAVE = "Save"
    SEND = "Send"
    SYNC = "Sync"
    UNIT = "Unit"
    VIEW = "View"
    WIFI = "Wifi"
    ZOOM = "Zoom"
    ALBUM = "Album"
    BRUSH = "Brush"
    BROOM = "Broom"
    CLOSE = "Close"
    CLOUD = "Cloud"
    EMBED = "Embed"
    GLOBE = "Globe"
    HEART = "Heart"
    LABEL = "Label"
    MEDIA = "Media"
    MOVIE = "Movie"
    MUSIC = "Music"
    ROBOT = "Robot"
    PAUSE = "Pause"
    PASTE = "Paste"
    PHOTO = "Photo"
    PHONE = "Phone"
    PRINT = "Print"
    SHARE = "Share"
    TILES = "Tiles"
    UNPIN = "Unpin"
    VIDEO = "Video"
    TRAIN = "Train"
    ADD_TO  ="AddTo"
    ACCEPT = "Accept"
    CAMERA = "Camera"
    CANCEL = "Cancel"
    DELETE = "Delete"
    FOLDER = "Folder"
    FILTER = "Filter"
    MARKET = "Market"
    SCROLL = "Scroll"
    LAYOUT = "Layout"
    GITHUB = "GitHub"
    UPDATE = "Update"
    REMOVE = "Remove"
    RETURN = "Return"
    PEOPLE = "People"
    QRCODE = "QRCode"
    RINGER = "Ringer"
    ROTATE = "Rotate"
    SEARCH = "Search"
    VOLUME = "Volume"
    FRIGID  = "Frigid"
    SAVE_AS = "SaveAs"
    ZOOM_IN = "ZoomIn"
    CONNECT  ="Connect"
    HISTORY = "History"
    SETTING = "Setting"
    PALETTE = "Palette"
    MESSAGE = "Message"
    FIT_PAGE = "FitPage"
    ZOOM_OUT = "ZoomOut"
    AIRPLANE = "Airplane"
    ASTERISK = "Asterisk"
    CALORIES = "Calories"
    CALENDAR = "Calendar"
    FEEDBACK = "Feedback"
    LIBRARY = "BookShelf"
    MINIMIZE = "Minimize"
    CHECKBOX = "CheckBox"
    DOCUMENT = "Document"
    LANGUAGE = "Language"
    DOWNLOAD = "Download"
    QUESTION = "Question"
    SPEAKERS = "Speakers"
    DATE_TIME = "DateTime"
    FONT_SIZE = "FontSize"
    HOME_FILL = "HomeFill"
    PAGE_LEFT = "PageLeft"
    SAVE_COPY = "SaveCopy"
    SEND_FILL = "SendFill"
    SKIP_BACK = "SkipBack"
    SPEED_OFF = "SpeedOff"
    ALIGNMENT = "Alignment"
    BLUETOOTH = "Bluetooth"
    COMPLETED = "Completed"
    CONSTRACT = "Constract"
    HEADPHONE = "Headphone"
    MEGAPHONE = "Megaphone"
    PROJECTOR = "Projector"
    EDUCATION = "Education"
    LEFT_ARROW = "LeftArrow"
    ERASE_TOOL = "EraseTool"
    PAGE_RIGHT = "PageRight"
    PLAY_SOLID = "PlaySolid"
    BOOK_SHELF = "BookShelf"
    HIGHTLIGHT = "Highlight"
    FOLDER_ADD = "FolderAdd"
    PAUSE_BOLD = "PauseBold"
    PENCIL_INK = "PencilInk"
    PIE_SINGLE = "PieSingle"
    QUICK_NOTE = "QuickNote"
    SPEED_HIGH = "SpeedHigh"
    STOP_WATCH = "StopWatch"
    ZIP_FOLDER = "ZipFolder"
    BASKETBALL = "Basketball"
    BRIGHTNESS = "Brightness"
    DICTIONARY = "Dictionary"
    MICROPHONE = "Microphone"
    ARROW_DOWN = "ChevronDown"
    FULL_SCREEN = "FullScreen"
    MIX_VOLUMES = "MixVolumes"
    REMOVE_FROM = "RemoveFrom"
    RIGHT_ARROW = "RightArrow"
    QUIET_HOURS  ="QuietHours"
    FINGERPRINT = "Fingerprint"
    APPLICATION = "Application"
    CERTIFICATE = "Certificate"
    TRANSPARENT = "Transparent"
    IMAGE_EXPORT = "ImageExport"
    SPEED_MEDIUM = "SpeedMedium"
    LIBRARY_FILL = "LibraryFill"
    MUSIC_FOLDER = "MusicFolder"
    POWER_BUTTON = "PowerButton"
    SKIP_FORWARD = "SkipForward"
    CARE_UP_SOLID = "CareUpSolid"
    ACCEPT_MEDIUM = "AcceptMedium"
    CANCEL_MEDIUM = "CancelMedium"
    CHEVRON_RIGHT = "ChevronRight"
    CLIPPING_TOOL = "ClippingTool"
    SEARCH_MIRROR = "SearchMirror"
    SHOPPING_CART = "ShoppingCart"
    FONT_INCREASE = "FontIncrease"
    BACK_TO_WINDOW = "BackToWindow"
    COMMAND_PROMPT = "CommandPrompt"
    CLOUD_DOWNLOAD = "CloudDownload"
    DICTIONARY_ADD = "DictionaryAdd"
    CARE_DOWN_SOLID = "CareDownSolid"
    CARE_LEFT_SOLID = "CareLeftSolid"
    CLEAR_SELECTION = "ClearSelection"
    DEVELOPER_TOOLS = "DeveloperTools"
    BACKGROUND_FILL = "BackgroundColor"
    CARE_RIGHT_SOLID = "CareRightSolid"
    CHEVRON_DOWN_MED = "ChevronDownMed"
    CHEVRON_RIGHT_MED = "ChevronRightMed"
    EMOJI_TAB_SYMBOLS = "EmojiTabSymbols"
    EXPRESSIVE_INPUT_ENTRY = "ExpressiveInputEntry"

    def path(self, theme=Theme.AUTO):
        return f':/icon/images/icons/{self.value}_{getIconColor(theme)}.svg'


class Icon(QIcon):

    def __init__(self, fluentIcon: FluentIcon):
        super().__init__(fluentIcon.path())
        self.fluentIcon = fluentIcon


def toQIcon(icon: Union[QIcon, FluentIconBase, str]) -> QIcon:
    """ convet `icon` to `QIcon` """
    if isinstance(icon, str):
        return QIcon(icon)

    if isinstance(icon, FluentIconBase):
        return icon.icon()

    return icon


class Action(QAction):
    """ Fluent action

    Constructors
    ------------
    * Action(`parent`: QWidget = None, `**kwargs`)
    * Action(`text`: str, `parent`: QWidget = None, `**kwargs`)
    * Action(`icon`: QIcon | FluentIconBase, `parent`: QWidget = None, `**kwargs`)
    """

    @singledispatchmethod
    def __init__(self, parent: QObject = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.fluentIcon = None

    @__init__.register
    def _(self, text: str, parent: QObject = None, **kwargs):
        super().__init__(text, parent, **kwargs)
        self.fluentIcon = None

    @__init__.register
    def _(self, icon: QIcon, text: str, parent: QObject = None, **kwargs):
        super().__init__(icon, text, parent, **kwargs)
        self.fluentIcon = None

    @__init__.register
    def _(self, icon: FluentIconBase, text: str, parent: QObject = None, **kwargs):
        super().__init__(icon.icon(), text, parent, **kwargs)
        self.fluentIcon = icon

    def icon(self) -> QIcon:
        if self.fluentIcon:
            return Icon(self.fluentIcon)

        return super().icon()

    def setIcon(self, icon: Union[FluentIconBase, QIcon]):
        if isinstance(icon, FluentIconBase):
            self.fluentIcon = icon
            icon = icon.icon()

        super().setIcon(icon)


class AntDesignIcon(FluentIconBase, Enum):
    """ Ant Design icon """

    BATCHFOLDING = "Batchfolding"
    CI = "CI"
    CI_CIRCLE_FILL = "CI-circle-fill"
    CODESANDBOX = "CodeSandbox"
    CODESANDBOX_CIRCLE_F = "CodeSandbox-circle-f"
    CODESANDBOX_SQUARE_F = "CodeSandbox-square-f"
    CONSOLE_SQL = "Console-SQL"
    DOLLAR = "Dollar"
    DOLLAR_CIRCLE_FILL = "Dollar-circle-fill"
    EURO = "EURO"
    EURO_CIRCLE_FILL = "EURO-circle-fill"
    FIELD_BINARY = "Field-Binary"
    FIELD_STRING = "Field-String"
    FIELD_NUMBER = "Field-number"
    FIELD_TIME = "Field-time"
    FUNCTION = "Function"
    GIF = "GIF"
    GITLAB = "Gitlab"
    GITLAB_FILL = "Gitlab-fill"
    HTML = "HTML"
    HTML_FILL = "HTML-fill"
    IE = "IE"
    IE_CIRCLE_FILL = "IE-circle-fill"
    IE_SQUARE_FILL = "IE-square-fill"
    IMPORT = "Import"
    PARTITION = "Partition"
    POUND = "Pound"
    POUND_CIRCLE_FILL = "Pound-circle-fill"
    QQ = "QQ"
    QQ_CIRCLE_FILL = "QQ-circle-fill"
    QQ_SQUARE_FILL = "QQ-square-fill"
    REPORT = "Report"
    STOREDPROCEDURE = "Storedprocedure"
    USB = "USB"
    USB_FILL = "USB-fill"
    VIEW = "View"
    YUAN = "YUAN"
    YUAN_CIRCLE_FILL = "YUAN-circle-fill"
    YOUTUBE = "Youtube"
    YOUTUBE_FILL = "Youtube-fill"
    ACCOUNTBOOK = "accountbook"
    ACCOUNTBOOK_FILL = "accountbook-fill"
    ADDTEAM = "addteam"
    ADDUSER = "adduser"
    AIM = "aim"
    ALERT = "alert"
    ALERT_FILL = "alert-fill"
    ALIBABA = "alibaba"
    ALIGN_CENTER = "align-center"
    ALIGN_LEFT = "align-left"
    ALIGN_RIGHT = "align-right"
    ALIPAY = "alipay"
    ALIPAY_CIRCLE_FILL = "alipay-circle-fill"
    ALIPAY_SQUARE_FILL = "alipay-square-fill"
    ALIWANGWANG = "aliwangwang"
    ALIWANGWANG_FILL = "aliwangwang-fill"
    AMAZON = "amazon"
    AMAZON_CIRCLE_FILL = "amazon-circle-fill"
    AMAZON_SQUARE_FILL = "amazon-square-fill"
    ANDROID = "android"
    ANDROID_FILL = "android-fill"
    ANT_CLOUD = "ant-cloud"
    ANTDESIGN = "antdesign"
    APARTMENT = "apartment"
    API = "api"
    API_FILL = "api-fill"
    APPLE = "apple"
    APPLE_FILL = "apple-fill"
    APPSTORE = "appstore"
    APPSTORE_FILL = "appstore-fill"
    APPSTOREADD = "appstoreadd"
    AREACHART = "areachart"
    ARRAWSALT = "arrawsalt"
    ARROWDOWN = "arrowdown"
    ARROWLEFT = "arrowleft"
    ARROWRIGHT = "arrowright"
    ARROWUP = "arrowup"
    ATTACHMENT = "attachment"
    AUDIO = "audio"
    AUDIO_FILL = "audio-fill"
    AUDIOSTATIC = "audiostatic"
    AUDIT = "audit"
    BACKWARD = "backward"
    BANK = "bank"
    BANK_FILL = "bank-fill"
    BARCHART = "barchart"
    BARCODE = "barcode"
    BATCHFOLDING_FILL = "batchfolding-fill"
    BEHANCE = "behance"
    BEHANCE_CIRCLE_FILL = "behance-circle-fill"
    BEHANCE_SQUARE_FILL = "behance-square-fill"
    BELL = "bell"
    BELL_FILL = "bell-fill"
    BG_COLORS = "bg-colors"
    BLOCK = "block"
    BOLD = "bold"
    BOOK = "book"
    BOOK_FILL = "book-fill"
    BORDER = "border"
    BORDER_BOTTOM = "border-bottom"
    BORDER_HORIZONTAL = "border-horizontal"
    BORDER_INNER = "border-inner"
    BORDER_LEFT = "border-left"
    BORDER_OUTER = "border-outer"
    BORDER_RIGHT = "border-right"
    BORDER_TOP = "border-top"
    BORDER_VERTICLE = "border-verticle"
    BOXPLOT = "boxplot"
    BOXPLOT_FILL = "boxplot-fill"
    BRANCHES = "branches"
    BUG = "bug"
    BUG_FILL = "bug-fill"
    BUILD = "build"
    BUILD_FILL = "build-fill"
    BULB = "bulb"
    BULB_FILL = "bulb-fill"
    CALCULATOR = "calculator"
    CALCULATOR_FILL = "calculator-fill"
    CALENDAR = "calendar"
    CALENDAR_CHECK = "calendar-check"
    CALENDAR_CHECK_FILL = "calendar-check-fill"
    CALENDAR_FILL = "calendar-fill"
    CAMERA = "camera"
    CAMERA_FILL = "camera-fill"
    CAR = "car"
    CAR_FILL = "car-fill"
    CARET_DOWN = "caret-down"
    CARET_LEFT = "caret-left"
    CARET_RIGHT = "caret-right"
    CARET_UP = "caret-up"
    CARRYOUT = "carryout"
    CARRYOUT_FILL = "carryout-fill"
    CHECK = "check"
    CHECK_CIRCLE = "check-circle"
    CHECK_CIRCLE_FILL = "check-circle-fill"
    CHECK_SQUARE = "check-square"
    CHECK_SQUARE_FILL = "check-square-fill"
    CHROME = "chrome"
    CHROME_FILL = "chrome-fill"
    CLEAR = "clear"
    CLOSE = "close"
    CLOSE_CIRCLE = "close-circle"
    CLOSE_CIRCLE_FILL = "close-circle-fill"
    CLOSE_SQUARE = "close-square"
    CLOSE_SQUARE_FILL = "close-square-fill"
    CLOUD = "cloud"
    CLOUD_DOWNLOAD = "cloud-download"
    CLOUD_FILL = "cloud-fill"
    CLOUD_SERVER = "cloud-server"
    CLOUD_SYNC = "cloud-sync"
    CLOUD_UPLOAD = "cloud-upload"
    CLUSTER = "cluster"
    CODE = "code"
    CODELIBRARY = "codelibrary"
    CODELIBRARY_FILL = "codelibrary-fill"
    CODEPEN = "codepen"
    CODEPEN_CIRCLE_FILL = "codepen-circle-fill"
    CODEPEN_SQUARE_FILL = "codepen-square-fill"
    COLLAPSE = "collapse"
    COLUM_HEIGHT = "colum-height"
    COLUMN_WIDTH = "column-width"
    COMMENT = "comment"
    COMPASS = "compass"
    COMPASS_FILL = "compass-fill"
    COMPRESS = "compress"
    CONTACTS = "contacts"
    CONTACTS_FILL = "contacts-fill"
    CONTAINER = "container"
    CONTAINER_FILL = "container-fill"
    CONTROL = "control"
    CONTROL_FILL = "control-fill"
    COPYRIGHT = "copyright"
    COPYRIGHT_CIRCLE_FIL = "copyright-circle-fil"
    CREDITCARD = "creditcard"
    CREDITCARD_FILL = "creditcard-fill"
    CROWN = "crown"
    CROWN_FILL = "crown-fill"
    CUSTOMERSERVICE = "customerservice"
    CUSTOMERSERVICE_FILL = "customerservice-fill"
    DASH = "dash"
    DASHBOARD = "dashboard"
    DASHBOARD_FILL = "dashboard-fill"
    DATABASE = "database"
    DATABASE_FILL = "database-fill"
    DELETE = "delete"
    DELETE_FILL = "delete-fill"
    DELETECOLUMN = "deletecolumn"
    DELETEROW = "deleterow"
    DELETETEAM = "deleteteam"
    DELETEUSER = "deleteuser"
    DEPLOYMENTUNIT = "deploymentunit"
    DESKTOP = "desktop"
    DETAIL = "detail"
    DETAIL_FILL = "detail-fill"
    DIFF = "diff"
    DIFF_FILL = "diff-fill"
    DINGTALK = "dingtalk"
    DINGTALK_CIRCLE_FILL = "dingtalk-circle-fill"
    DINGTALK_SQUARE_FILL = "dingtalk-square-fill"
    DISCONNECT = "disconnect"
    DOUBLELEFT = "doubleleft"
    DOUBLERIGHT = "doubleright"
    DOWN = "down"
    DOWN_CIRCLE = "down-circle"
    DOWN_CIRCLE_FILL = "down-circle-fill"
    DOWN_SQUARE = "down-square"
    DOWN_SQUARE_FILL = "down-square-fill"
    DOWNLOAD = "download"
    DRAG = "drag"
    DRIBBBLE = "dribbble"
    DRIBBBLE_CIRCLE_FILL = "dribbble-circle-fill"
    DRIBBBLE_SQUARE_FILL = "dribbble-square-fill"
    DROPBOX = "dropbox"
    DROPBOX_CIRCLE_FILL = "dropbox-circle-fill"
    DROPBOX_SQUARE_FILL = "dropbox-square-fill"
    EARTH = "earth"
    EDIT = "edit"
    EDIT_FILL = "edit-fill"
    EDIT_SQUARE = "edit-square"
    ELLIPSIS = "ellipsis"
    ENTER = "enter"
    ERROR = "error"
    ERROR_FILL = "error-fill"
    EXCLAIMINATION = "exclaimination"
    EXPAND = "expand"
    EXPEND = "expend"
    EXPERIMENT = "experiment"
    EXPERIMENT_FILL = "experiment-fill"
    EXPORT = "export"
    EYE = "eye"
    EYE_CLOSE = "eye-close"
    EYE_FILL = "eye-fill"
    EYECLOSE_FILL = "eyeclose-fill"
    FACEBOOK = "facebook"
    FACEBOOK_FILL = "facebook-fill"
    FALL = "fall"
    FAST_BACKWARD = "fast-backward"
    FAST_FORWARD = "fast-forward"
    FILE = "file"
    FILE_GIF = "file-GIF"
    FILE_ADD = "file-add"
    FILE_ADD_FILL = "file-add-fill"
    FILE_COPY = "file-copy"
    FILE_COPY_FILL = "file-copy-fill"
    FILE_EXCEL = "file-excel"
    FILE_EXCEL_FILL = "file-excel-fill"
    FILE_EXCEPTION = "file-exception"
    FILE_EXCLAMATION = "file-exclamation"
    FILE_EXCLAMATION_FIL = "file-exclamation-fil"
    FILE_FILL = "file-fill"
    FILE_IMAGE = "file-image"
    FILE_IMAGE_FILL = "file-image-fill"
    FILE_MARKDOWN = "file-markdown"
    FILE_MARKDOWN_FILL = "file-markdown-fill"
    FILE_PDF = "file-pdf"
    FILE_PDF_FILL = "file-pdf-fill"
    FILE_PPT = "file-ppt"
    FILE_PPT_FILL = "file-ppt-fill"
    FILE_TEXT = "file-text"
    FILE_TEXT_FILL = "file-text-fill"
    FILE_UNKNOWN = "file-unknown"
    FILE_UNKNOWN_FILL = "file-unknown-fill"
    FILE_WORD = "file-word"
    FILE_WORD_FILL = "file-word-fill"
    FILE_ZIP = "file-zip"
    FILE_ZIP_FILL = "file-zip-fill"
    FILEDONE = "filedone"
    FILEPROTECT = "fileprotect"
    FILESEARCH = "filesearch"
    FILESYNC = "filesync"
    FILTER = "filter"
    FILTER_FILL = "filter-fill"
    FIRE = "fire"
    FIRE_FILL = "fire-fill"
    FLAG = "flag"
    FLAG_FILL = "flag-fill"
    FOLDER = "folder"
    FOLDER_ADD = "folder-add"
    FOLDER_ADD_FILL = "folder-add-fill"
    FOLDER_FILL = "folder-fill"
    FOLDER_OPEN = "folder-open"
    FOLDER_OPEN_FILL = "folder-open-fill"
    FOLDER_VIEW = "folder-view"
    FONT_COLORS = "font-colors"
    FONT_SIZE = "font-size"
    FORK = "fork"
    FORMATPAINTER = "formatpainter"
    FORMATPAINTER_FILL = "formatpainter-fill"
    FORWARD = "forward"
    FROWN = "frown"
    FROWN_FILL = "frown-fill"
    FULLSCREEN = "fullscreen"
    FULLSCREEN_EXIT = "fullscreen-exit"
    FUND = "fund"
    FUND_FILL = "fund-fill"
    FUNNELPLOT = "funnelplot"
    FUNNELPLOT_FILL = "funnelplot-fill"
    GATEWAY = "gateway"
    GIFT = "gift"
    GIFT_FILL = "gift-fill"
    GITHUB_FILL = "github-fill"
    GOLD = "gold"
    GOLDEN_FILL = "golden-fill"
    GOOGLE = "google"
    GOOGLE_CIRCLE_FILL = "google-circle-fill"
    GOOGLE_SQUARE_FILL = "google-square-fill"
    GOOGLEPLUS = "googleplus"
    GOOGLEPLUS_CIRCLE_F = "googleplus-circle-f"
    GOOGLEPLUS_SQUARE_F = "googleplus-square-f"
    GROUP = "group"
    HEART = "heart"
    HEART_FILL = "heart-fill"
    HEATMAP = "heatmap"
    HIGHLIGHT = "highlight"
    HIGHLIGHT_FILL = "highlight-fill"
    HOME = "home"
    HOME_FILL = "home-fill"
    HOURGLASS = "hourglass"
    HOURGLASS_FILL = "hourglass-fill"
    ICON_TEST = "icon-test"
    IDCARD = "idcard"
    IDCARD_FILL = "idcard-fill"
    IMAGE = "image"
    IMAGE_FILL = "image-fill"
    INDENT = "indent"
    INDEX = "index"
    INFO_CIRCLE = "info-circle"
    INFO_CIRCLE_FILL = "info-circle-fill"
    INFOMATION = "infomation"
    INSERTROWABOVE = "insertrowabove"
    INSERTROWBELOW = "insertrowbelow"
    INSERTROWLEFT = "insertrowleft"
    INSERTROWRIGHT = "insertrowright"
    INSTAGRAM = "instagram"
    INSTAGRAM_FILL = "instagram-fill"
    INSURANCE = "insurance"
    INSURANCE_FILL = "insurance-fill"
    INTERATION = "interation"
    INTERATION_FILL = "interation-fill"
    ISSUESCLOSE = "issuesclose"
    ITALIC = "italic"
    KEY = "key"
    LAPTOP = "laptop"
    LAYOUT = "layout"
    LAYOUT_FILL = "layout-fill"
    LEFT = "left"
    LEFT_CIRCLE = "left-circle"
    LEFT_CIRCLE_FILL = "left-circle-fill"
    LEFT_SQUARE = "left-square"
    LEFT_SQUARE_FILL = "left-square-fill"
    LIKE = "like"
    LIKE_FILL = "like-fill"
    LINE = "line"
    LINE_HEIGHT = "line-height"
    LINECHART = "linechart"
    LINK = "link"
    LINKEDIN = "linkedin"
    LINKEDIN_FILL = "linkedin-fill"
    LOCATION = "location"
    LOCATION_FILL = "location-fill"
    LOCK = "lock"
    LOCK_FILL = "lock-fill"
    LOGIN = "login"
    LOGOUT = "logout"
    MAIL = "mail"
    MAIL_FILL = "mail-fill"
    MAN = "man"
    MEDICINEBOX = "medicinebox"
    MEDICINEBOX_FILL = "medicinebox-fill"
    MEDIUM = "medium"
    MEDIUM_CIRCLE_FILL = "medium-circle-fill"
    MEDIUM_SQUARE_FILL = "medium-square-fill"
    MEH = "meh"
    MEH_FILL = "meh-fill"
    MENU = "menu"
    MERGE_CELLS = "merge-cells"
    MESSAGE = "message"
    MESSAGE_FILL = "message-fill"
    MINUS = "minus"
    MINUS_CIRCLE = "minus-circle"
    MINUS_CIRCLE_FILL = "minus-circle-fill"
    MINUS_SQUARE = "minus-square"
    MINUS_SQUARE_FILL = "minus-square-fill"
    MOBILE = "mobile"
    MOBILE_FILL = "mobile-fill"
    MONEYCOLLECT = "moneycollect"
    MONEYCOLLECT_FILL = "moneycollect-fill"
    MONITOR = "monitor"
    MR = "mr"
    NOTIFICATION = "notification"
    NOTIFICATION_FILL = "notification-fill"
    NUMBER = "number"
    ORDEREDLIST = "orderedlist"
    OUTDENT = "outdent"
    PAUSE = "pause"
    PERCENTAGE = "percentage"
    PHONE = "phone"
    PHONE_FILL = "phone-fill"
    PIC_CENTER = "pic-center"
    PIC_LEFT = "pic-left"
    PIC_RIGHT = "pic-right"
    PIECHART = "piechart"
    PIECHART_CIRCLE_FIL = "piechart-circle-fil"
    PLAY_CIRCLE = "play-circle"
    PLAY_CIRCLE_FILL = "play-circle-fill"
    PLAY_SQUARE = "play-square"
    PLAY_SQUARE_FILL = "play-square-fill"
    PLUS = "plus"
    PLUS_CIRCLE = "plus-circle"
    PLUS_CIRCLE_FILL = "plus-circle-fill"
    PLUS_SQUARE = "plus-square"
    PLUS_SQUARE_FILL = "plus-square-fill"
    POINTMAP = "pointmap"
    POWEROFF = "poweroff"
    POWEROFF_CIRCLE_FILL = "poweroff-circle-fill"
    PRINTER = "printer"
    PRINTER_FILL = "printer-fill"
    PROJECT = "project"
    PROJECT_FILL = "project-fill"
    PROPERTYSAFETY = "propertysafety"
    PROPERTYSAFETY_FILL = "propertysafety-fill"
    PUSHPIN = "pushpin"
    PUSHPIN_FILL = "pushpin-fill"
    QRCODE = "qrcode"
    QUESTION = "question"
    QUESTION_CIRCLE = "question-circle"
    QUESTION_CIRCLE_FILL = "question-circle-fill"
    RADARCHART = "radarchart"
    RADIUS_BOTTOMLEFT = "radius-bottomleft"
    RADIUS_BOTTOMRIGHT = "radius-bottomright"
    RADIUS_SETTING = "radius-setting"
    RADIUS_UPLEFT = "radius-upleft"
    RADIUS_UPRIGHT = "radius-upright"
    READ = "read"
    READ_FILL = "read-fill"
    RECONCILIATION = "reconciliation"
    RECONCILIATION_FILL = "reconciliation-fill"
    REDDIT = "reddit"
    REDDIT_CIRCLE_FILL = "reddit-circle-fill"
    REDDIT_SQUARE_FILL = "reddit-square-fill"
    REDENVELOPE = "redenvelope"
    REDENVELOPE_FILL = "redenvelope-fill"
    REDO = "redo"
    RELOAD = "reload"
    RELOADTIME = "reloadtime"
    REST = "rest"
    REST_FILL = "rest-fill"
    RETWEET = "retweet"
    RIGHT = "right"
    RIGHT_CIRCLE = "right-circle"
    RIGHT_CIRCLE_FILL = "right-circle-fill"
    RIGHT_SQUARE = "right-square"
    RIGHT_SQUARE_FILL = "right-square-fill"
    RISE = "rise"
    ROBOT = "robot"
    ROBOT_FILL = "robot-fill"
    ROCKET = "rocket"
    ROCKET_FILL = "rocket-fill"
    ROLLBACK = "rollback"
    ROTATE_LEFT = "rotate-left"
    ROTATE_RIGHT = "rotate-right"
    SAFETYCERTIFICATE = "safetycertificate"
    SAFETYCERTIFICATE_F = "safetycertificate-f"
    SAVE = "save"
    SAVE_FILL = "save-fill"
    SCAN = "scan"
    SCISSOR = "scissor"
    SEARCH = "search"
    SECURITYSCAN = "securityscan"
    SECURITYSCAN_FILL = "securityscan-fill"
    SELECT = "select"
    SEND = "send"
    SETTING = "setting"
    SETTING_FILL = "setting-fill"
    SEVER = "sever"
    SEVER_FILL = "sever-fill"
    SHAKE = "shake"
    SHARE = "share"
    SHOP = "shop"
    SHOP_FILL = "shop-fill"
    SHOPPING = "shopping"
    SHOPPING_FILL = "shopping-fill"
    SHORTCUT = "shortcut"
    SHORTCUT_FILL = "shortcut-fill"
    SHRINK = "shrink"
    SIGNAL_FILL = "signal-fill"
    SISTERNODE = "sisternode"
    SKETCH = "sketch"
    SKETCH_CIRCLE_FILL = "sketch-circle-fill"
    SKETCH_SQUARE_FILL = "sketch-square-fill"
    SKIN = "skin"
    SKIN_FILL = "skin-fill"
    SKYPE = "skype"
    SKYPE_FILL = "skype-fill"
    SLACK = "slack"
    SLACK_CIRCLE_FILL = "slack-circle-fill"
    SLACK_SQUARE_FILL = "slack-square-fill"
    SLIDERS = "sliders"
    SLIDERS_FILL = "sliders-fill"
    SMALL_DASH = "small-dash"
    SMILE = "smile"
    SMILE_FILL = "smile-fill"
    SNIPPETS = "snippets"
    SNIPPETS_FILL = "snippets-fill"
    SOLIT_CELLS = "solit-cells"
    SOLUTION = "solution"
    SORT_ASCENDING = "sort-ascending"
    SORT_DESCENDING = "sort-descending"
    SOUND = "sound"
    SOUND_FILL = "sound-fill"
    STAR = "star"
    STAR_FILL = "star-fill"
    STAR1 = "star1"
    STEP_BACKWARD = "step-backward"
    STEP_FORWARD = "step-forward"
    STOCK = "stock"
    STOP = "stop"
    STOP_FILL = "stop-fill"
    STRIKETHROUGH = "strikethrough"
    SUBNODE = "subnode"
    SWAP = "swap"
    SWAP_LEFT = "swap-left"
    SWAP_RIGHT = "swap-right"
    SWITCHUSER = "switchuser"
    SYNC = "sync"
    TABLE = "table"
    TABLE1 = "table1"
    TABLET = "tablet"
    TABLET_FILL = "tablet-fill"
    TAG = "tag"
    TAG_FILL = "tag-fill"
    TAGS = "tags"
    TAGS_FILL = "tags-fill"
    TAOBAO = "taobao"
    TAOBAO_CIRCLE_FILL = "taobao-circle-fill"
    TAOBAO_SQUARE_FILL = "taobao-square-fill"
    TEAM = "team"
    THUNDERBOLT = "thunderbolt"
    THUNDERBOLT_FILL = "thunderbolt-fill"
    TIME_CIRCLE = "time-circle"
    TIME_CIRCLE_FILL = "time-circle-fill"
    TIMEOUT = "timeout"
    TOTOP = "totop"
    TRADEMARK = "trademark"
    TRADEMARK_CIRCLE_FIL = "trademark-circle-fil"
    TRANSACTION = "transaction"
    TRANSLATE = "translate"
    TROPHY = "trophy"
    TROPHY_FILL = "trophy-fill"
    TWITTER = "twitter"
    TWITTER_CIRCLE_FILL = "twitter-circle-fill"
    TWITTER_SQUARE_FILL = "twitter-square-fill"
    UNDERLINE = "underline"
    UNDO = "undo"
    UNGROUP = "ungroup"
    UNLIKE = "unlike"
    UNLIKE_FILL = "unlike-fill"
    UNLOCK = "unlock"
    UNLOCK_FILL = "unlock-fill"
    UNORDEREDLIST = "unorderedlist"
    UP = "up"
    UP_CIRCLE = "up-circle"
    UP_CIRCLE_FILL = "up-circle-fill"
    UP_SQUARE = "up-square"
    UP_SQUARE_FILL = "up-square-fill"
    UPLOAD = "upload"
    USER = "user"
    VERIFIED = "verified"
    VERTICAL_ALIGN_BOTTO = "vertical-align-botto"
    VERTICAL_ALIGN_MIDDL = "vertical-align-middl"
    VERTICAL_ALIGN_TOP = "vertical-align-top"
    VERTICALLEFT = "verticalleft"
    VERTICALRIGHT = "verticalright"
    VIDEO = "video"
    VIDEO_FILL = "video-fill"
    VIDEOCAMERAADD = "videocameraadd"
    WALLET = "wallet"
    WALLET_FILL = "wallet-fill"
    WARNING_CIRCLE = "warning-circle"
    WARNING_CIRCLE_FILL = "warning-circle-fill"
    WECHAT_FILL = "wechat-fill"
    WEIBO = "weibo"
    WEIBO_CIRCLE_FILL = "weibo-circle-fill"
    WEIBO_SQUARE_FILL = "weibo-square-fill"
    WHATSAPP = "whatsapp"
    WIFI = "wifi"
    WINDOWS = "windows"
    WINDOWS_FILL = "windows-fill"
    WOMAN = "woman"
    WRENCH = "wrench"
    WRENCH_FILL = "wrench-fill"
    YAHOO = "yahoo"
    YAHOO_FILL = "yahoo-fill"
    YUQUE = "yuque"
    YUQUE_FILL = "yuque-fill"
    ZHIHU = "zhihu"
    ZHIHU_CIRCLE_FILL = "zhihu-circle-fill"
    ZHIHU_SQUARE_FILL = "zhihu-square-fill"
    ZOOMIN = "zoomin"
    ZOOMOUT = "zoomout"

    def path(self, theme=Theme.AUTO):
        return f':/icon/images/antdesign/{self.value}_{getIconColor(theme)}.svg'
