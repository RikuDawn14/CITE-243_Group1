# steampunk_theme.py
# Steampunk-inspired dark theme with copper/brass accents

APP_STYLESHEET = """
/* Global Styles */
* {
    font-family: 'Segoe UI', Arial, sans-serif;
}

QWidget {
    background-color: #1a0a0a;
    color: #b87333;
}

QMainWindow {
    background-color: #0a0a0a;
}

/* Headers */
QFrame#HeaderBar {
    background-color: #2a1a1a;
    border-bottom: 2px solid #b08d57;
}

QLabel#HeaderTitle {
    color: #b08d57;
    font-size: 16px;
    font-weight: bold;
}

QLabel#HeaderSubtitle {
    color: #b87333;
    font-size: 12px;
}

/* Content Panel */
QFrame#ContentPanel {
    background-color: #1a0a0a;
    border: 2px solid #b08d57;
    border-radius: 5px;
}

/* Buttons */
QPushButton {
    background-color: #98002E;
    color: #b08d57;
    border: 2px solid #b08d57;
    border-radius: 5px;
    padding: 6px 12px;
    font-weight: bold;
    min-height: 25px;
}

QPushButton:hover {
    background-color: #b8003e;
    color: #d0a868;
}

QPushButton:pressed {
    background-color: #780024;
}

QPushButton:disabled {
    background-color: #4a4a4a;
    color: #7a7a7a;
    border-color: #5a5a5a;
}

/* List Widget */
QListWidget {
    background-color: #2a1a1a;
    border: 2px solid #b08d57;
    border-radius: 5px;
    color: #b87333;
    outline: none;
}

QListWidget::item {
    padding: 8px;
    border-bottom: 1px solid #3a2a2a;
}

QListWidget::item:selected {
    background-color: #98002E;
    color: #d0a868;
}

QListWidget::item:hover {
    background-color: #3a2a2a;
}

/* Group Boxes */
QGroupBox {
    border: 2px solid #b08d57;
    border-radius: 5px;
    margin-top: 10px;
    padding-top: 10px;
    font-weight: bold;
    color: #b08d57;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}

/* Line Edits and Spin Boxes */
QLineEdit, QSpinBox {
    background-color: #2a1a1a;
    border: 2px solid #b08d57;
    border-radius: 3px;
    padding: 5px;
    color: #b87333;
}

QLineEdit:focus, QSpinBox:focus {
    border-color: #d0a868;
}

QSpinBox::up-button, QSpinBox::down-button {
    background-color: #98002E;
    border: 1px solid #b08d57;
}

QSpinBox::up-button:hover, QSpinBox::down-button:hover {
    background-color: #b8003e;
}

/* Checkboxes */
QCheckBox {
    color: #b87333;
    spacing: 5px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 2px solid #b08d57;
    border-radius: 3px;
    background-color: #2a1a1a;
}

QCheckBox::indicator:checked {
    background-color: #98002E;
}

QCheckBox::indicator:hover {
    border-color: #d0a868;
}

/* Progress Bar */
QProgressBar {
    border: 2px solid #b08d57;
    border-radius: 5px;
    text-align: center;
    background-color: #1a0a0a;
    color: #b08d57;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: #98002E;
    border-radius: 3px;
}

/* Text Edit */
QTextEdit {
    background-color: #0a0a0a;
    border: 2px solid #b08d57;
    border-radius: 5px;
    color: #b87333;
    selection-background-color: #98002E;
}

/* Scrollbars */
QScrollBar:vertical {
    background-color: #1a0a0a;
    width: 14px;
    border: 1px solid #b08d57;
}

QScrollBar::handle:vertical {
    background-color: #98002E;
    border-radius: 3px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #b8003e;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #1a0a0a;
    height: 14px;
    border: 1px solid #b08d57;
}

QScrollBar::handle:horizontal {
    background-color: #98002E;
    border-radius: 3px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #b8003e;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

/* Tooltips */
QToolTip {
    background-color: #2a1a1a;
    color: #b87333;
    border: 2px solid #b08d57;
    padding: 5px;
    border-radius: 3px;
}

/* Labels */
QLabel {
    color: #b87333;
}

/* Splitter */
QSplitter::handle {
    background-color: #b08d57;
    width: 2px;
}

QSplitter::handle:hover {
    background-color: #d0a868;
}
"""
