from enum import Enum

WEATHER_APP_URL = "https://wttr.in/"

AREAS = [
    "London",
    "SVO",  # ICAO Шереметьево
    "Череповец",
]


class Options:
    metric: str = "m"
    today: str = "0"
    extra_one_day: str = "1"
    extra_two_days: str = "2"
    narrow_version: str = "n"
    silent_version: str = "q"
    no_color: str = "T"

    @classmethod
    def default_options(cls) -> list[str]:
        return [
            cls.metric,
            cls.narrow_version,
            cls.silent_version,
            cls.no_color,
        ]


class Languages(Enum):
    RUSSIAN = "ru"
    ENGLISH = "en"
    FRENCH = "fr"
