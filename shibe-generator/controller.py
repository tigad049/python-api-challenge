"""
controller.py
by David Tigas
Python code to make API connections.
"""

import requests as re
import json
import shutil
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
)

url = "http://shibe.online/api/shibes?urls=false"

def get_image() -> str:
    """Gets an image ID and URL from shibe.online.

    Returns:
        image_id: The image ID used in shibe.online's CDN.

        image_url = The URL on shibe.online's CDN.
    """
    response = re.get(url)
    
    if response.ok:
        data = json.loads(response.text)
        image_id = data[0]
        image_url = f"https://cdn.shibe.online/shibes/{image_id}.jpg"
        image_response = re.get(image_url, stream = True)

        if image_response.ok:
            return image_id, image_url

        else:
            print(f"There was an error accessing the image: {response.status_code}")

    else:
        print(f"There was an error accessing the API: {response.status_code}")

def download_image(image_id, image_url):
    """Downloads an image from shibe.online.

    Arguments:
        image_id: The image ID used in shibe.online's CDN.

        image_url = The URL on shibe.online's CDN.
    """
    image_response = re.get(image_url, stream = True)
    if image_response.ok:
        with open(f"cache/{image_id}.jpg",'wb') as f:
            shutil.copyfileobj(image_response.raw, f)
        print(f"Image donwloaded: {image_id}.jpg")
    else:
        print(f"There was an error accessing the image: {response.status_code}")

def get_vbox(image_id) -> QVBoxLayout:
    """Returns a vbox layout with an image from shibe.online.

    Arguments:
        image_id: The image ID used in shibe.online's CDN.

    Returns:
        image_layout: A vbox layout with an image from shibe.online.
    """
    image_layout = QVBoxLayout()
    folder = "cache/"
    filepath = f"{folder}{image_id}.jpg"
    print(filepath)
    image = QPixmap(filepath)

    image_layout.addWidget(image)
    return image_layout