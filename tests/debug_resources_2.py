
import sys
import os

# Ensure we use local package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import QFile, QDir, QIODevice
from PySide6.QtWidgets import QApplication
import qfluentwidgets

app = QApplication(sys.argv)

print("Listing resources under :/qss")
d = QDir(":/qss")
for entry in d.entryList():
    print(f" - {entry}")

print("\nListing resources under :/qss/qss")
d = QDir(":/qss/qss")
for entry in d.entryList():
    print(f" - {entry}")

print("\nListing resources under :/qss/qss/light")
d = QDir(":/qss/qss/light")
for entry in d.entryList():
    print(f" - {entry}")
