import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout, QLabel,\
                            QLineEdit, QFormLayout, QGroupBox, QRadioButton


class Window1(QWidget):
    """
    窗口1\n
    包括伤害乘区计算\n
    """
    def __init__(self):
        super().__init__()
        self.init_damage_ui()

    def init_damage_ui(self):
        """
        该部分绘制伤害乘区的布局
        """
        font_chinese_SimSun12 = QFont("SimSun", 12)
        font_english_TNR12 = QFont("Times New Roman", 12)

        self.layout_V_all = QVBoxLayout()  # 整体的垂直布局

        self.layout_H_damage = QHBoxLayout()  # 伤害乘区的水平布局

        self.layout_AE_cal = QVBoxLayout()  # AE乘区的竖直排列
        self.layout_DB_cal = QVBoxLayout()  # DB乘区的竖直排列
        self.layout_CD_cal = QVBoxLayout()  # CD乘区的竖直排列
        self.layout_ER_cal = QVBoxLayout()  # ER乘区的竖直排列
        self.layout_DF_cal = QVBoxLayout()  # DF乘区的竖直排列
        self.layout_RT_cal = QVBoxLayout()  # RT乘区的竖直排列

        """ ----- 伤害乘区标题 ----- """
        self.label_damage_title = QLabel("伤害乘区计算")
        self.label_damage_title.setFont(font_chinese_SimSun12)
        self.layout_V_all.addWidget(self.label_damage_title)
        self.label_damage_title.setStyleSheet("background-color:rgba(102, 204, 255, 0.3);")

        """ ----- 六个伤害乘区 ----- """
        """ Part 1 AE乘区 """
        self.label_AE = QLabel("AE")
        self.label_AE.setFont(font_english_TNR12)
        self.AE_formlayout = QFormLayout()  # 表单容器
        self.input_atk = QLineEdit()  # 攻击力输入框
        self.input_atk.setPlaceholderText("atk")
        self.input_talent = QLineEdit()  # 天赋倍率输入框
        self.input_talent.setPlaceholderText("talent")
        self.AE_formlayout.addRow("攻击力:", self.input_atk)
        self.AE_formlayout.addRow("倍率:", self.input_talent)
        self.layout_AE_cal.addWidget(self.label_AE)
        self.layout_AE_cal.addLayout(self.AE_formlayout)
        self.layout_AE_cal.addStretch(1)
        """ Part 2 DB乘区 """
        self.label_DB = QLabel("DB")
        self.DB_formlayout = QFormLayout()  # 表单容器
        self.input_db = QLineEdit()  # 增伤输入框
        self.input_db.setPlaceholderText("DB%")
        self.DB_formlayout.addRow("增伤:", self.input_db)
        self.layout_DB_cal.addWidget(self.label_DB)
        self.layout_DB_cal.addLayout(self.DB_formlayout)
        self.layout_DB_cal.addStretch(1)
        """ Part 3 CD乘区 """
        self.label_CD = QLabel("CD")
        self.CD_formlayout = QFormLayout()  # 表单容器
        self.input_cr = QLineEdit()  # 暴击率输入框
        self.input_cr.setPlaceholderText("CR")
        self.input_cd = QLineEdit()  # 暴击伤害输入框
        self.input_cd.setPlaceholderText("CD")
        self.CD_formlayout.addRow("暴击率:", self.input_cr)
        self.CD_formlayout.addRow("暴伤:", self.input_cd)
        self.layout_CD_cal.addWidget(self.label_CD)
        self.layout_CD_cal.addLayout(self.CD_formlayout)
        self.layout_CD_cal.addStretch(1)
        """ Part 4 ER乘区 """
        self.label_ER = QLabel("ER")
        self.ER_formlayout = QFormLayout()
        self.elemental_box = QGroupBox("反应过程")
        # elemental_vlayout = QVBoxLayout()  # 四个反应水平排放放不下，真狗屎，放一列又太丑。。
        self.elemental_vlayout = QVBoxLayout()
        self.elemental_hlayout1 = QHBoxLayout()
        self.elemental_hlayout2 = QHBoxLayout()
        self.btn1 = QRadioButton("水火蒸发")  # 2
        self.btn2 = QRadioButton("火水蒸发")  # 1.5
        self.btn3 = QRadioButton("火冰融化")  # 2
        self.btn4 = QRadioButton("冰火融化")  # 1.5
        self.elemental_hlayout1.addWidget(self.btn1)
        self.elemental_hlayout1.addWidget(self.btn2)
        self. elemental_hlayout2.addWidget(self.btn3)
        self.elemental_hlayout2.addWidget(self.btn4)
        self.elemental_vlayout.addLayout(self.elemental_hlayout1)
        self.elemental_vlayout.addLayout(self.elemental_hlayout2)
        self.elemental_box.setLayout(self.elemental_vlayout)
        self.input_IRC = QLineEdit()  # 反应系数提高输入框
        self.ER_formlayout.addRow("反应系数提高:", self.input_IRC)
        self.layout_ER_cal.addWidget(self.label_ER)
        self.layout_ER_cal.addWidget(self.elemental_box)
        self.layout_ER_cal.addLayout(self.ER_formlayout)
        self.layout_ER_cal.addStretch(1)
        """ Part 5 DF乘区 """
        self.label_DF = QLabel("DF")
        self.DF_formlayout = QFormLayout()  # 表单容器
        self.input_reduce_defenses = QLineEdit()  # 减防输入框
        self.input_reduce_defenses.setPlaceholderText("降低敌人防御")
        self.input_ignore_defenses = QLineEdit()  # 穿防输入框
        self.input_ignore_defenses.setPlaceholderText("无视敌人防御")
        self.DF_formlayout.addRow("减防:", self.input_reduce_defenses)
        self.DF_formlayout.addRow("穿防:", self.input_ignore_defenses)
        self.layout_DF_cal.addWidget(self.label_DF)
        self.layout_DF_cal.addLayout(self.DF_formlayout)
        self.layout_DF_cal.addStretch(1)
        """ Part 6 RT乘区 """
        self.label_RT = QLabel("RT")
        self.RT_formlayout = QFormLayout()  # 表单容器
        self.input_reduce_resistance = QLineEdit()  # 减抗输入框
        self.input_reduce_resistance.setPlaceholderText("RT%")
        self.RT_formlayout.addRow("增伤:", self.input_reduce_resistance)
        self.layout_RT_cal.addWidget(self.label_RT)
        self.layout_RT_cal.addLayout(self.RT_formlayout)
        self.layout_RT_cal.addStretch(1)
        """ Part Added 按钮 """
        # 第七大乘区，按钮乘区。蒸馍，你不服气
        self.button_read_damage_data = QPushButton("读取数据")
        self.button_read_damage_data.clicked.connect(self.read_damage_data)
        """ 将伤害部分添加到水平布局器 """
        self.layout_H_damage.addLayout(self.layout_AE_cal)
        self.layout_H_damage.addLayout(self.layout_DB_cal)
        self.layout_H_damage.addLayout(self.layout_CD_cal)
        self.layout_H_damage.addLayout(self.layout_ER_cal)
        self.layout_H_damage.addLayout(self.layout_DF_cal)
        self.layout_H_damage.addLayout(self.layout_RT_cal)
        self.layout_H_damage.addWidget(self.button_read_damage_data)

        self.layout_V_all.addLayout(self.layout_H_damage)  # 将水平的六个伤害乘区添加到整体的垂直排列

        self.layout_V_all.addStretch(1)
        self.setLayout(self.layout_V_all)

    def read_damage_data(self):
        """ 读取输入框数据并存储到其他变量 """
        atk_value = self.input_atk.text()
        talent_value = self.input_talent.text()

        # 这里你可以将数据存储到其他变量，例如类的属性
        self.input_atk = atk_value
        self.input_talent = talent_value

        if self.input_atk == 1 and self.input_talent == 2:
            print("abcde")
        else:
            print("ABCDE")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("这是功能2", self)
        self.setStyleSheet("background-color:lightgreen;")


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
        # 将创建的2个Widget添加到抽屉布局器中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        """ 初始界面 """
        self.resize(1200, 800)  # 设置MyWindow的宽高

        container = QHBoxLayout()  # 1. 创建整体的垂直布局器

        widget = QWidget()  # 2. 创建一个要显示具体内容的子Widget
        widget.setLayout(self.stacked_layout)  # 设置为之前定义的抽屉布局
        widget.setStyleSheet("background-color:rgba(253, 230, 224, 0.2);")

        # 3. 创建2个按钮，用来点击进行切换抽屉布局器中的widget
        btn_widget = QWidget()
        btn_layout = QVBoxLayout()
        btn_press1 = QPushButton("主页面")
        btn_press2 = QPushButton("功能2")
        btn_press1.setFixedSize(55, 30)
        btn_press2.setFixedSize(55, 30)
        # 给按钮添加事件（即点击后要调用的函数）
        btn_press1.clicked.connect(self.btn_press1_clicked)  # 为什么函数不加括号，因为绑定的是函数本身，而不是返回值。
        btn_press2.clicked.connect(self.btn_press2_clicked)
        btn_layout.addWidget(btn_press1)
        btn_layout.addWidget(btn_press2)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
