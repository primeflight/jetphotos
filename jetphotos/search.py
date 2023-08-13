#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Search(object):
    def aircraft(prefix: str) -> list:
        response = requests.get(f"https://www.jetphotos.com/photo/keyword/{prefix}")
        soup = BeautifulSoup(response.content, "html.parser")

        image_links = []

        divs = soup.find_all("div", class_="result__section--photo-wrapper")

        for div in divs:
            img = div.find("img")
            src = img["src"].replace("//", "https://")
            image_links.append(src)

        return image_links
