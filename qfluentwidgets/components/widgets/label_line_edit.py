# coding: utf-8
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from ...common.style_sheet import FluentStyleSheet, addStyleSheet
from .line_edit import LineEdit


class LabelLineEdit(LineEdit):
    """ Label line edit with prefix and suffix """

    def __init__(self, parent=None, prefix: str = None, suffix: str = None):
        super().__init__(parent)
        self.prefixLabel = QLabel(self)
        self.suffixLabel = QLabel(self)

        self.prefixLabel.setObjectName("PrefixLabel")
        self.suffixLabel.setObjectName("SuffixLabel")

        # Fix background color not showing
        self.prefixLabel.setAttribute(Qt.WA_StyledBackground)
        self.suffixLabel.setAttribute(Qt.WA_StyledBackground)

        self.prefixLabel.hide()
        self.suffixLabel.hide()

        # Apply style sheet
        addStyleSheet(self, FluentStyleSheet.LABEL_LINE_EDIT, register=True)
        addStyleSheet(self.prefixLabel, FluentStyleSheet.LABEL_LINE_EDIT, register=True)
        addStyleSheet(self.suffixLabel, FluentStyleSheet.LABEL_LINE_EDIT, register=True)

        # Add prefix to the left
        self.hBoxLayout.insertWidget(0, self.prefixLabel, 0, Qt.AlignLeft)
        self.hBoxLayout.insertStretch(1, 1)

        # Add suffix to the right
        self.hBoxLayout.addWidget(self.suffixLabel, 0, Qt.AlignRight)

        if prefix:
            self.setPrefix(prefix)
        if suffix:
            self.setSuffix(suffix)

    def setLabel(self, text: str):
        self.setPrefix(text)

    def setPrefix(self, text: str):
        self.prefixLabel.setText(text)
        self.prefixLabel.show()
        self.prefixLabel.adjustSize()
        self._adjustTextMargins()

    def setSuffix(self, text: str):
        self.suffixLabel.setText(text)
        self.suffixLabel.show()
        self.suffixLabel.adjustSize()
        self._adjustTextMargins()

    def _adjustTextMargins(self):
        """ Adjust text margins """
        # Copy LineEdit._adjustTextMargins logic
        left = len(self.leftButtons) * 30
        right = len(self.rightButtons) * 30 + 28 * self.isClearButtonEnabled()

        # Add label width
        if not self.prefixLabel.isHidden():
            left += self.prefixLabel.width() + 8

        if not self.suffixLabel.isHidden():
            right += self.suffixLabel.width() + 8

        m = self.textMargins()
        self.setTextMargins(left, m.top(), right, m.bottom())

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._adjustTextMargins()
