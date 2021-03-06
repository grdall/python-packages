

from enum import Enum

class BashColor(Enum):
    # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal?rq=1
    NONE = ""
    GREY = "\x1b[1;30;40m"
    HEADER = "\x1b[95m"
    OKBLUE = "\x1b[94m"
    OKGREEN = "\x1b[92m"
    WARNING = "\x1b[93m"
    FAIL = "\x1b[91m"
    ERROR = "\x1b[91m"
    ENDC = "\x1b[0m"

    BOLD = "\x1b[1m"
    ITALIC = "\x1b[3m"
    URL = "\x1b[4m"
    BLINK = "\x1b[5m"
    BLINK2 = "\x1b[6m"
    SELECTED = "\x1b[7m"

    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    VIOLET = "\x1b[35m"
    TEAL = "\x1b[36m"
    WHITE = "\x1b[37m"

    BLACKBG = "\x1b[40m"
    REDBG = "\x1b[41m"
    GREENBG = "\x1b[42m"
    YELLOWBG = "\x1b[43m"
    BLUEBG = "\x1b[44m"
    VIOLETBG = "\x1b[45m"
    TEALBG = "\x1b[46m"
    WHITEBG = "\x1b[47m"
    GREYBG = "\x1b[100m"