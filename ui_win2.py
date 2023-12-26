from PyQt5.QtGui import QFont, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout, QLabel, \
    QLineEdit, QFormLayout, QGroupBox, QRadioButton, QTextBrowser, QSizePolicy, QButtonGroup, QFileDialog, QCheckBox


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_abcd_ui()

    def init_abcd_ui(self):
        """
        摆烂
        """
        font_chinese_SimSun16Bold = QFont("SimSun", 16)
        font_chinese_SimSun16Bold.setBold(True)

        self.Vlayout = QVBoxLayout()
        self.title = QLabel("组队伤害，没做，催也没用，得打钱")
        self.title.setFont(font_chinese_SimSun16Bold)
        self.title.setStyleSheet("background-color:rgba(102, 204, 255, 0.6);")
        self.Vlayout.addWidget(self.title)
        self.Vlayout.addStretch(1)
        self.setLayout(self.Vlayout)
