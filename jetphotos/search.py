#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Search(object):
    def aircraft(prefix: str):
        response = requests.get(f"https://www.jetphotos.com/photo/keyword/{prefix}")
        soup = BeautifulSoup(response.content, "html.parser")
        div = soup.find("div", class_="result__section result__section--photo-wrapper")
        img = div.find("img")
        src = img["src"]
        return src.replace("//", "https://")
