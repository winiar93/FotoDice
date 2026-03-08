import random
from enum import Enum


class Format(Enum):
    SERIES_3 = "Series of 3"
    SINGLE_SHOT = "Single Shot"
    STORY_5 = "Story (5 photos)"

class Orientation(Enum):
    VERTICAL = "Vertical"
    HORIZONTAL = "Horizontal"
    SQUARE = "Square"


class Color(Enum):
    CYANOTYPE = "Cyanotype"
    COLOR = "Color"
    BLACK_WHITE = "Black & white"
    SEPIA = "Sepia"


class Subject(Enum):
    GEOMETRY = "Geometry"
    SHADOW = "Shadow"
    REFLECTION = "Reflection"
    MOTION = "Motion"
    NEGATIVE_SPACE = "Negative space"
    FRAMING = "Framing"
    MINIMALISM = "Minimalism"
    ANY = "Any"


class TimeOfDay(Enum):
    ANY = "Any"
    GOLDEN_HOUR = "Golden hour"
    BLUE_HOUR = "Blue hour"
    NIGHT = "Night"
    HIGH_NOON = "High Noon"
    SUNRISE = "Sunrise"
    LATE_AFTERNOON = "Late Afternoon"
