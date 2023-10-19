from typing import AnyStr
from urllib.parse import urljoin, quote

import requests

from settings import WEATHER_APP_URL, AREAS, Languages, Options


def get_link(area: str, url: str = WEATHER_APP_URL) -> AnyStr:
    return urljoin(
        base=url,
        url=quote(area)
    )


def format_get_params(*no_kw_params, **kw_params) -> str:
    """
    Format HTTP get params.
    Example: a, b, c; d="m" -> abc&d=m
    :param no_kw_params: params with no value
    :type no_kw_params:
    :param kw_params: params with values
    :type kw_params:
    :return: formatted params
    :rtype: str
    """
    params = dict.fromkeys(no_kw_params, None)
    params.update(kw_params)

    return "".join(
        [k for k, v in params.items() if v is None]
    ) + "&" + "&".join(
        [f"{k}={v}" for k, v in params.items() if v is not None]
    )


def get_weather(
    area: str,
    options: list[str],
    lang: Languages = Languages.RUSSIAN,
):
    params = format_get_params(*options, lang=lang.value)
    url = get_link(area=area)

    with requests.Session() as session:
        response: requests.Response = session.get(
            url=url,
            params=params
        )

        if response.status_code == 200:
            return response.text


if __name__ == "__main__":
    options_ = Options.default_options()

    [
        print(get_weather(area=area, options=options_))
        for area in AREAS
    ]
