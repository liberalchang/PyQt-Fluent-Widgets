
import sys
import os

print("Step 1: Start")
try:
    from PySide6.QtCore import Qt
    print("Step 2: QtCore imported")
except Exception as e:
    print(f"Error importing QtCore: {e}")

try:
    from PySide6.QtWidgets import QApplication, QWidget
    print("Step 3: QtWidgets imported")
except Exception as e:
    print(f"Error importing QtWidgets: {e}")

print("Step 4: Attempting to import QtWebEngineWidgets...")
try:
    from PySide6.QtWebEngineWidgets import QWebEngineView
    print("Step 5: QtWebEngineWidgets imported SUCCESS")
except ImportError as e:
    print(f"Step 5: QtWebEngineWidgets import FAILED (ImportError): {e}")
except Exception as e:
    print(f"Step 5: QtWebEngineWidgets import FAILED (Exception): {e}")

print("Step 6: Creating QApplication...")
try:
    app = QApplication(sys.argv)
    print("Step 7: QApplication created")
except Exception as e:
    print(f"Error creating QApplication: {e}")

print("Step 8: Creating QWebEngineView...")
try:
    view = QWebEngineView()
    print("Step 9: QWebEngineView created")
except Exception as e:
    print(f"Error creating QWebEngineView: {e}")

print("Step 10: Finished")
