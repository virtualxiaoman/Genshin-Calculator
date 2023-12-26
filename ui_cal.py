import sys
import dmg_cal
from openpyxl import Workbook, load_workbook

from PyQt5.QtGui import QFont, QDoubleValidator, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout, QLabel, \
    QLineEdit, QFormLayout, QGroupBox, QRadioButton, QTextBrowser, QSizePolicy, QButtonGroup, QFileDialog, QCheckBox

from ui_win1 import Window1
from ui_win2 import Window2
from ui_win3 import Window3


# todo 做完后记得删除print相关代码


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = None  # 使用self将变量绑定到类的实例上，能进行跨函数调用。不用self就是局部变量了。
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        """ 创建堆叠布局(抽屉布局) """
        self.stacked_layout = QStackedLayout()
        # 创建单独的Widget
        win1 = Window1()
        win2 = Window2()
        win3 = Window3()
        # 将创建的2个Widget添加到抽屉布局器中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)
        self.stacked_layout.addWidget(win3)

    def init_ui(self):
        """ 初始界面 """
        self.resize(1400, 800)  # 设置MyWindow的宽高
        self.setWindowTitle("原神伤害计算器")
        self.setWindowIcon(QIcon('Nahida.ico'))

        container = QHBoxLayout()  # 1. 创建整体的垂直布局器

        widget = QWidget()  # 2. 创建一个要显示具体内容的子Widget
        widget.setLayout(self.stacked_layout)  # 设置为之前定义的抽屉布局
        widget.setStyleSheet("background-color:rgba(253, 230, 224, 0.2);")

        # 3. 创建2个按钮，用来点击进行切换抽屉布局器中的widget
        btn_widget = QWidget()
        btn_layout = QVBoxLayout()
        btn_press1 = QPushButton("伤害")
        btn_press2 = QPushButton("组队")
        btn_press3 = QPushButton("圣遗物")
        btn_press1.setFixedSize(55, 30)
        btn_press2.setFixedSize(55, 30)
        btn_press3.setFixedSize(55, 30)
        # 给按钮添加事件（即点击后要调用的函数）
        btn_press1.clicked.connect(self.btn_press1_clicked)  # 为什么函数不加括号，因为绑定的是函数本身，而不是返回值。
        btn_press2.clicked.connect(self.btn_press2_clicked)
        btn_press3.clicked.connect(self.btn_press3_clicked)
        btn_layout.addWidget(btn_press1)
        btn_layout.addWidget(btn_press2)
        btn_layout.addWidget(btn_press3)
        btn_layout.addStretch(1)
        btn_widget.setLayout(btn_layout)

        # 4. 将widget与btn添加到布局器中
        container.addWidget(btn_widget)
        container.addWidget(widget)

        # 5. 设置当前要显示的Widget，从而能够显示这个布局器中的控件
        self.setLayout(container)

    def btn_press1_clicked(self):
        """ 切换界面1 """
        # setCurrentIndex 是 QStackedLayout 类的一个方法，用于设置抽屉布局器的当前索引值，即可切换显示哪个Widget
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        """ 切换界面2 """
        self.stacked_layout.setCurrentIndex(1)

    def btn_press3_clicked(self):
        """ 切换界面3 """
        self.stacked_layout.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
