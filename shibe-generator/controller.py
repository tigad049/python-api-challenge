"""
controller.py
by David Tigas
Python code to make API connections.
"""

import requests as re
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
)

url = "http://shibe.online/api/shibes"
response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")