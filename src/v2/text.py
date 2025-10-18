import os
from enum import Enum

class Color(Enum):
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    ORANGE = "\033[38;5;166m"

class Modifier(Enum):
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    RESET = "\033[0m"

def modifyText(modifier, text):
    return f"{modifier.value}{text}{Modifier.RESET.value}"

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")