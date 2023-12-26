from PyQt5.QtGui import QFont, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout, QLabel, \
    QLineEdit, QFormLayout, QGroupBox, QRadioButton, QTextBrowser, QSizePolicy, QButtonGroup, QFileDialog, QCheckBox


class Window3(QWidget):
    def __init__(self):
        super().__init__()
        self.init_artifactForecast_ui()

    def init_artifactForecast_ui(self):
        """
        该部分绘制伤圣遗物评分与预测 artifactForecast 的布局
        """
        font_chinese_SimSun16Bold = QFont("SimSun", 16)
        font_chinese_SimSun16Bold.setBold(True)
        GroupBox_style = "font-size: 21px; font-weight: bold; color: red; font-family: KaiTi;"

        """ 布局 """
        self.layout_V_all = QVBoxLayout()  # 全局的
        self.layout_H_artifactForecast_title = QHBoxLayout()  # 标题居中
        self.layout_H_artifactForecast_btn = QHBoxLayout()  # 按钮居中
        self.layout_V_artifactForecast_BtnText = QVBoxLayout()  # 按钮与输出框是竖直
        self.layout_H_artifactForecast_input = QHBoxLayout()  # 主体的输入框水平排列
        self.layout_V_originalArtifact_box = QVBoxLayout()  # 原圣遗物的竖直排列
        self.layout_V_currentArtifact_box = QVBoxLayout()  # 原圣遗物的竖直排列
        self.layout_V_ArtifactRate_box = QVBoxLayout()  # 原圣遗物的竖直排列
        self.layout_H_ArtifactRate_box = QHBoxLayout()  # 圣遗物自定义加权水平排列
        self.layout_H_entryData = QHBoxLayout()  # 输出词条数的文本框是水平排列
        self.layout_H_HitProbability = QHBoxLayout()  # 两个计算命中率的的文本框是水平排列

        """ 标题 """
        self.label_artifactForecast_title = QLabel("圣遗物评分与预测", self)
        self.label_artifactForecast_title.setFont(font_chinese_SimSun16Bold)
        self.label_artifactForecast_title.setStyleSheet("background-color:rgba(102, 204, 255, 0.6);")
        self.layout_H_artifactForecast_title.addStretch(1)
        self.layout_H_artifactForecast_title.addWidget(self.label_artifactForecast_title)
        self.layout_H_artifactForecast_title.addStretch(1)

        """ 原圣遗物"""
        self.originalArtifact_box = QGroupBox()
        self.originalArtifact_box_label = QLabel("原来的圣遗物")
        self.originalArtifact_box_label.setStyleSheet(GroupBox_style)
        self.layout_V_originalArtifact_box.addWidget(self.originalArtifact_box_label)
        self.originalArtifact_box_hlayout = QHBoxLayout()
        self.originalArtifact_box_vlayout1 = QVBoxLayout()
        self.originalArtifact_box_vlayout2 = QVBoxLayout()
        self.originalArtifact_box_hlayout11 = QHBoxLayout()
        self.originalArtifact_box_hlayout12 = QHBoxLayout()
        self.originalArtifact_box_hlayout13 = QHBoxLayout()
        self.originalArtifact_box_hlayout14 = QHBoxLayout()
        self.originalArtifact_box_hlayout15 = QHBoxLayout()
        self.originalArtifact_box_hlayout21 = QHBoxLayout()
        self.originalArtifact_box_hlayout22 = QHBoxLayout()
        self.originalArtifact_box_hlayout23 = QHBoxLayout()
        self.originalArtifact_box_hlayout24 = QHBoxLayout()
        self.originalArtifact_box_hlayout25 = QHBoxLayout()
        # 原圣遗物 左列
        self.originalArtifact_box_btn11 = QCheckBox("暴击率")
        self.originalArtifact_box_btn12 = QCheckBox("大生命")
        self.originalArtifact_box_btn13 = QCheckBox("大攻击")
        self.originalArtifact_box_btn14 = QCheckBox("大防御")
        self.originalArtifact_box_btn15 = QCheckBox("充能")
        self.originalArtifact_box_btn15.setFixedWidth(72)  # 72这个值是试出来的，不要改。
        self.input_original_CritRate = QLineEdit()
        self.input_original_BigHP = QLineEdit()
        self.input_original_BigATK = QLineEdit()
        self.input_original_BigDEF = QLineEdit()
        self.input_original_Charge = QLineEdit()
        self.input_original_CritRate.setFixedWidth(100)
        self.input_original_BigHP.setFixedWidth(100)
        self.input_original_BigATK.setFixedWidth(100)
        self.input_original_BigDEF.setFixedWidth(100)
        self.input_original_Charge.setFixedWidth(100)
        self.original_percent11 = QLabel("%")
        self.original_percent12 = QLabel("%")
        self.original_percent13 = QLabel("%")
        self.original_percent14 = QLabel("%")
        self.original_percent15 = QLabel("%")
        self.originalArtifact_box_hlayout11.addWidget(self.originalArtifact_box_btn11)
        self.originalArtifact_box_hlayout11.addWidget(self.input_original_CritRate)
        self.originalArtifact_box_hlayout11.addWidget(self.original_percent11)
        self.originalArtifact_box_hlayout12.addWidget(self.originalArtifact_box_btn12)
        self.originalArtifact_box_hlayout12.addWidget(self.input_original_BigHP)
        self.originalArtifact_box_hlayout12.addWidget(self.original_percent12)
        self.originalArtifact_box_hlayout13.addWidget(self.originalArtifact_box_btn13)
        self.originalArtifact_box_hlayout13.addWidget(self.input_original_BigATK)
        self.originalArtifact_box_hlayout13.addWidget(self.original_percent13)
        self.originalArtifact_box_hlayout14.addWidget(self.originalArtifact_box_btn14)
        self.originalArtifact_box_hlayout14.addWidget(self.input_original_BigDEF)
        self.originalArtifact_box_hlayout14.addWidget(self.original_percent14)
        self.originalArtifact_box_hlayout15.addWidget(self.originalArtifact_box_btn15)
        self.originalArtifact_box_hlayout15.addWidget(self.input_original_Charge)
        self.originalArtifact_box_hlayout15.addWidget(self.original_percent15)
        self.originalArtifact_box_vlayout1.addLayout(self.originalArtifact_box_hlayout11)
        self.originalArtifact_box_vlayout1.addLayout(self.originalArtifact_box_hlayout12)
        self.originalArtifact_box_vlayout1.addLayout(self.originalArtifact_box_hlayout13)
        self.originalArtifact_box_vlayout1.addLayout(self.originalArtifact_box_hlayout14)
        self.originalArtifact_box_vlayout1.addLayout(self.originalArtifact_box_hlayout15)
        # 原圣遗物 右列
        self.originalArtifact_box_btn21 = QCheckBox("暴伤")
        self.originalArtifact_box_btn22 = QCheckBox("小生命")
        self.originalArtifact_box_btn23 = QCheckBox("小攻击")
        self.originalArtifact_box_btn24 = QCheckBox("小防御")
        self.originalArtifact_box_btn25 = QCheckBox("精通")
        self.originalArtifact_box_btn21.setFixedWidth(72)
        self.input_original_CritDMG = QLineEdit()
        self.input_original_SmallHP = QLineEdit()
        self.input_original_SmallATK = QLineEdit()
        self.input_original_SmallDEF = QLineEdit()
        self.input_original_EM = QLineEdit()
        self.input_original_CritDMG.setFixedWidth(100)
        self.input_original_SmallHP.setFixedWidth(120)
        self.input_original_SmallATK.setFixedWidth(120)
        self.input_original_SmallDEF.setFixedWidth(120)
        self.input_original_EM.setFixedWidth(120)
        self.original_percent21 = QLabel("%")
        self.originalArtifact_box_hlayout21.addWidget(self.originalArtifact_box_btn21)
        self.originalArtifact_box_hlayout21.addWidget(self.input_original_CritDMG)
        self.originalArtifact_box_hlayout21.addWidget(self.original_percent21)
        self.originalArtifact_box_hlayout22.addWidget(self.originalArtifact_box_btn22)
        self.originalArtifact_box_hlayout22.addWidget(self.input_original_SmallHP)
        self.originalArtifact_box_hlayout23.addWidget(self.originalArtifact_box_btn23)
        self.originalArtifact_box_hlayout23.addWidget(self.input_original_SmallATK)
        self.originalArtifact_box_hlayout24.addWidget(self.originalArtifact_box_btn24)
        self.originalArtifact_box_hlayout24.addWidget(self.input_original_SmallDEF)
        self.originalArtifact_box_hlayout25.addWidget(self.originalArtifact_box_btn25)
        self.originalArtifact_box_hlayout25.addWidget(self.input_original_EM)
        self.originalArtifact_box_vlayout2.addLayout(self.originalArtifact_box_hlayout21)
        self.originalArtifact_box_vlayout2.addLayout(self.originalArtifact_box_hlayout22)
        self.originalArtifact_box_vlayout2.addLayout(self.originalArtifact_box_hlayout23)
        self.originalArtifact_box_vlayout2.addLayout(self.originalArtifact_box_hlayout24)
        self.originalArtifact_box_vlayout2.addLayout(self.originalArtifact_box_hlayout25)
        # 原圣遗物的布局
        self.originalArtifact_box_hlayout.addLayout(self.originalArtifact_box_vlayout1)
        self.originalArtifact_box_hlayout.addLayout(self.originalArtifact_box_vlayout2)
        self.layout_V_originalArtifact_box.addLayout(self.originalArtifact_box_hlayout)
        self.originalArtifact_box.setLayout(self.layout_V_originalArtifact_box)

        """ 现圣遗物"""
        self.currentArtifact_box = QGroupBox()
        self.currentArtifact_box_label = QLabel("现在的圣遗物")
        self.currentArtifact_box_label.setStyleSheet(GroupBox_style)
        self.layout_V_currentArtifact_box.addWidget(self.currentArtifact_box_label)
        self.currentArtifact_box_hlayout = QHBoxLayout()
        self.currentArtifact_box_vlayout1 = QVBoxLayout()
        self.currentArtifact_box_vlayout2 = QVBoxLayout()
        self.currentArtifact_box_hlayout11 = QHBoxLayout()
        self.currentArtifact_box_hlayout12 = QHBoxLayout()
        self.currentArtifact_box_hlayout13 = QHBoxLayout()
        self.currentArtifact_box_hlayout14 = QHBoxLayout()
        self.currentArtifact_box_hlayout15 = QHBoxLayout()
        self.currentArtifact_box_hlayout21 = QHBoxLayout()
        self.currentArtifact_box_hlayout22 = QHBoxLayout()
        self.currentArtifact_box_hlayout23 = QHBoxLayout()
        self.currentArtifact_box_hlayout24 = QHBoxLayout()
        self.currentArtifact_box_hlayout25 = QHBoxLayout()
        # 现圣遗物 左侧
        self.currentArtifact_box_btn11 = QCheckBox("暴击率")
        self.currentArtifact_box_btn12 = QCheckBox("大生命")
        self.currentArtifact_box_btn13 = QCheckBox("大攻击")
        self.currentArtifact_box_btn14 = QCheckBox("大防御")
        self.currentArtifact_box_btn15 = QCheckBox("充能")
        self.currentArtifact_box_btn15.setFixedWidth(72)  # 72这个值是试出来的，不要改。但是还是对齐不了
        self.input_current_CritRate = QLineEdit()
        self.input_current_BigHP = QLineEdit()
        self.input_current_BigATK = QLineEdit()
        self.input_current_BigDEF = QLineEdit()
        self.input_current_Charge = QLineEdit()
        self.input_current_CritRate.setFixedWidth(100)
        self.input_current_BigHP.setFixedWidth(100)
        self.input_current_BigATK.setFixedWidth(100)
        self.input_current_BigDEF.setFixedWidth(100)
        self.input_current_Charge.setFixedWidth(100)
        self.current_percent11 = QLabel("%")
        self.current_percent12 = QLabel("%")
        self.current_percent13 = QLabel("%")
        self.current_percent14 = QLabel("%")
        self.current_percent15 = QLabel("%")
        self.currentArtifact_box_hlayout11.addWidget(self.currentArtifact_box_btn11)
        self.currentArtifact_box_hlayout11.addWidget(self.input_current_CritRate)
        self.currentArtifact_box_hlayout11.addWidget(self.current_percent11)
        self.currentArtifact_box_hlayout12.addWidget(self.currentArtifact_box_btn12)
        self.currentArtifact_box_hlayout12.addWidget(self.input_current_BigHP)
        self.currentArtifact_box_hlayout12.addWidget(self.current_percent12)
        self.currentArtifact_box_hlayout13.addWidget(self.currentArtifact_box_btn13)
        self.currentArtifact_box_hlayout13.addWidget(self.input_current_BigATK)
        self.currentArtifact_box_hlayout13.addWidget(self.current_percent13)
        self.currentArtifact_box_hlayout14.addWidget(self.currentArtifact_box_btn14)
        self.currentArtifact_box_hlayout14.addWidget(self.input_current_BigDEF)
        self.currentArtifact_box_hlayout14.addWidget(self.current_percent14)
        self.currentArtifact_box_hlayout15.addWidget(self.currentArtifact_box_btn15)
        self.currentArtifact_box_hlayout15.addWidget(self.input_current_Charge)
        self.currentArtifact_box_hlayout15.addWidget(self.current_percent15)
        self.currentArtifact_box_vlayout1.addLayout(self.currentArtifact_box_hlayout11)
        self.currentArtifact_box_vlayout1.addLayout(self.currentArtifact_box_hlayout12)
        self.currentArtifact_box_vlayout1.addLayout(self.currentArtifact_box_hlayout13)
        self.currentArtifact_box_vlayout1.addLayout(self.currentArtifact_box_hlayout14)
        self.currentArtifact_box_vlayout1.addLayout(self.currentArtifact_box_hlayout15)
        # 现圣遗物 右侧
        self.currentArtifact_box_btn21 = QCheckBox("暴伤")
        self.currentArtifact_box_btn22 = QCheckBox("小生命")
        self.currentArtifact_box_btn23 = QCheckBox("小攻击")
        self.currentArtifact_box_btn24 = QCheckBox("小防御")
        self.currentArtifact_box_btn25 = QCheckBox("精通")
        self.currentArtifact_box_btn21.setFixedWidth(72)
        self.input_current_CritDMG = QLineEdit()
        self.input_current_SmallHP = QLineEdit()
        self.input_current_SmallATK = QLineEdit()
        self.input_current_SmallDEF = QLineEdit()
        self.input_current_EM = QLineEdit()
        self.input_current_CritDMG.setFixedWidth(100)
        self.input_current_SmallHP.setFixedWidth(120)
        self.input_current_SmallATK.setFixedWidth(120)
        self.input_current_SmallDEF.setFixedWidth(120)
        self.input_current_EM.setFixedWidth(120)
        self.current_percent21 = QLabel("%")
        self.currentArtifact_box_hlayout21.addWidget(self.currentArtifact_box_btn21)
        self.currentArtifact_box_hlayout21.addWidget(self.input_current_CritDMG)
        self.currentArtifact_box_hlayout21.addWidget(self.current_percent21)
        self.currentArtifact_box_hlayout22.addWidget(self.currentArtifact_box_btn22)
        self.currentArtifact_box_hlayout22.addWidget(self.input_current_SmallHP)
        self.currentArtifact_box_hlayout23.addWidget(self.currentArtifact_box_btn23)
        self.currentArtifact_box_hlayout23.addWidget(self.input_current_SmallATK)
        self.currentArtifact_box_hlayout24.addWidget(self.currentArtifact_box_btn24)
        self.currentArtifact_box_hlayout24.addWidget(self.input_current_SmallDEF)
        self.currentArtifact_box_hlayout25.addWidget(self.currentArtifact_box_btn25)
        self.currentArtifact_box_hlayout25.addWidget(self.input_current_EM)
        self.currentArtifact_box_vlayout2.addLayout(self.currentArtifact_box_hlayout21)
        self.currentArtifact_box_vlayout2.addLayout(self.currentArtifact_box_hlayout22)
        self.currentArtifact_box_vlayout2.addLayout(self.currentArtifact_box_hlayout23)
        self.currentArtifact_box_vlayout2.addLayout(self.currentArtifact_box_hlayout24)
        self.currentArtifact_box_vlayout2.addLayout(self.currentArtifact_box_hlayout25)
        # 现圣遗物的布局
        self.currentArtifact_box_hlayout.addLayout(self.currentArtifact_box_vlayout1)
        self.currentArtifact_box_hlayout.addLayout(self.currentArtifact_box_vlayout2)
        self.layout_V_currentArtifact_box.addLayout(self.currentArtifact_box_hlayout)
        self.currentArtifact_box.setLayout(self.layout_V_currentArtifact_box)

        """圣遗物自定义加权"""
        self.ArtifactRate_box = QGroupBox()
        self.ArtifactRate_box_label = QLabel("对圣遗物的自定义加权分数")
        self.ArtifactRate_box_label.setStyleSheet(GroupBox_style)
        self.layout_V_ArtifactRate_box.addWidget(self.ArtifactRate_box_label)
        self.ArtifactRate_formlayout1 = QFormLayout()  # 表单容器
        self.ArtifactRate_formlayout2 = QFormLayout()  # 表单容器
        self.inputRate_CritRate = QLineEdit()
        self.inputRate_BigHP = QLineEdit()
        self.inputRate_BigATK = QLineEdit()
        self.inputRate_BigDEF = QLineEdit()
        self.inputRate_Charge = QLineEdit()
        self.inputRate_CritDMG = QLineEdit()
        self.inputRate_SmallHP = QLineEdit()
        self.inputRate_SmallATK = QLineEdit()
        self.inputRate_SmallDEF = QLineEdit()
        self.inputRate_CritRate = QLineEdit()
        self.inputRate_EM = QLineEdit()
        self.inputRate_CritRate.setFixedWidth(50)
        self.inputRate_BigHP.setFixedWidth(50)
        self.inputRate_BigATK.setFixedWidth(50)
        self.inputRate_BigDEF.setFixedWidth(50)
        self.inputRate_Charge.setFixedWidth(50)
        self.inputRate_CritDMG.setFixedWidth(50)
        self.inputRate_SmallHP.setFixedWidth(50)
        self.inputRate_SmallATK.setFixedWidth(50)
        self.inputRate_SmallDEF.setFixedWidth(50)
        self.inputRate_EM.setFixedWidth(50)
        self.inputRate_CritRate.setText("100")
        self.inputRate_BigHP.setText("80")
        self.inputRate_BigATK.setText("80")
        self.inputRate_BigDEF.setText("80")
        self.inputRate_Charge.setText("75")
        self.inputRate_CritDMG.setText("100")
        self.inputRate_SmallHP.setText("50")
        self.inputRate_SmallATK.setText("50")
        self.inputRate_SmallDEF.setText("50")
        self.inputRate_EM.setText("75")
        self.ArtifactRate_formlayout1.addRow("暴击:", self.inputRate_CritRate)
        self.ArtifactRate_formlayout1.addRow("大生命:", self.inputRate_BigHP)
        self.ArtifactRate_formlayout1.addRow("大攻击:", self.inputRate_BigATK)
        self.ArtifactRate_formlayout1.addRow("大防御:", self.inputRate_BigDEF)
        self.ArtifactRate_formlayout1.addRow("充能:", self.inputRate_Charge)
        self.ArtifactRate_formlayout2.addRow("暴伤:", self.inputRate_CritDMG)
        self.ArtifactRate_formlayout2.addRow("小生命:", self.inputRate_SmallHP)
        self.ArtifactRate_formlayout2.addRow("小攻击:", self.inputRate_SmallATK)
        self.ArtifactRate_formlayout2.addRow("小防御:", self.inputRate_SmallDEF)
        self.ArtifactRate_formlayout2.addRow("精通:", self.inputRate_EM)

        self.layout_H_ArtifactRate_box.addLayout(self.ArtifactRate_formlayout1)
        self.layout_H_ArtifactRate_box.addLayout(self.ArtifactRate_formlayout2)
        self.layout_V_ArtifactRate_box.addLayout(self.layout_H_ArtifactRate_box)
        self.ArtifactRate_box.setLayout(self.layout_V_ArtifactRate_box)

        """赌不赌要得先看词条数啊"""
        # 原圣遗物现在是+几了？
        self.CurrentLevel1_box = QGroupBox("当前等级")
        self.CurrentLevel1_vlayout = QVBoxLayout()
        self.CurrentLevel1_btn0 = QRadioButton("+0")
        self.CurrentLevel1_btn4 = QRadioButton("+4")
        self.CurrentLevel1_btn8 = QRadioButton("+8")
        self.CurrentLevel1_btn12 = QRadioButton("+12")
        self.CurrentLevel1_btn16 = QRadioButton("+16")
        self.CurrentLevel1_btn20 = QRadioButton("+20")
        self.CurrentLevel1_btn20.setChecked(True)  # 默认20级
        self.CurrentLevel1_value = 20
        self.CurrentLevel1_vlayout.addWidget(self.CurrentLevel1_btn0)
        self.CurrentLevel1_vlayout.addWidget(self.CurrentLevel1_btn4)
        self.CurrentLevel1_vlayout.addWidget(self.CurrentLevel1_btn8)
        self.CurrentLevel1_vlayout.addWidget(self.CurrentLevel1_btn12)
        self.CurrentLevel1_vlayout.addWidget(self.CurrentLevel1_btn16)
        self.CurrentLevel1_vlayout.addWidget(self.CurrentLevel1_btn20)
        self.CurrentLevel1_box.setLayout(self.CurrentLevel1_vlayout)
        self.CurrentLevel1_btn0.clicked.connect(self.CurrentLevel1_button_click)
        self.CurrentLevel1_btn4.clicked.connect(self.CurrentLevel1_button_click)
        self.CurrentLevel1_btn8.clicked.connect(self.CurrentLevel1_button_click)
        self.CurrentLevel1_btn12.clicked.connect(self.CurrentLevel1_button_click)
        self.CurrentLevel1_btn16.clicked.connect(self.CurrentLevel1_button_click)
        self.CurrentLevel1_btn20.clicked.connect(self.CurrentLevel1_button_click)
        # 新圣遗物现在是+几了？
        self.CurrentLevel2_box = QGroupBox("当前等级")
        self.CurrentLevel2_vlayout = QVBoxLayout()
        self.CurrentLevel2_btn0 = QRadioButton("+0")
        self.CurrentLevel2_btn4 = QRadioButton("+4")
        self.CurrentLevel2_btn8 = QRadioButton("+8")
        self.CurrentLevel2_btn12 = QRadioButton("+12")
        self.CurrentLevel2_btn16 = QRadioButton("+16")
        self.CurrentLevel2_btn20 = QRadioButton("+20")
        self.CurrentLevel2_btn0.setChecked(True)  # 设置不激化默认选中
        self.CurrentLevel2_value = 0
        self.CurrentLevel2_vlayout.addWidget(self.CurrentLevel2_btn0)
        self.CurrentLevel2_vlayout.addWidget(self.CurrentLevel2_btn4)
        self.CurrentLevel2_vlayout.addWidget(self.CurrentLevel2_btn8)
        self.CurrentLevel2_vlayout.addWidget(self.CurrentLevel2_btn12)
        self.CurrentLevel2_vlayout.addWidget(self.CurrentLevel2_btn16)
        self.CurrentLevel2_vlayout.addWidget(self.CurrentLevel2_btn20)
        self.CurrentLevel2_box.setLayout(self.CurrentLevel2_vlayout)
        self.CurrentLevel2_btn0.clicked.connect(self.CurrentLevel2_button_click)
        self.CurrentLevel2_btn4.clicked.connect(self.CurrentLevel2_button_click)
        self.CurrentLevel2_btn8.clicked.connect(self.CurrentLevel2_button_click)
        self.CurrentLevel2_btn12.clicked.connect(self.CurrentLevel2_button_click)
        self.CurrentLevel2_btn16.clicked.connect(self.CurrentLevel2_button_click)
        self.CurrentLevel2_btn20.clicked.connect(self.CurrentLevel2_button_click)
        # 创建按钮
        self.cal_data_button = QPushButton("计算数据")
        self.cal_data_button.setStyleSheet("QPushButton {"
                                           "background-color:rgba(102, 204, 255, 0.8);"  # 设置按钮
                                           "border: none;"  # 移除按钮的边框
                                           "font-weight: bold;"   # 加粗
                                           "color: white;"  # 文本颜色
                                           "padding: 6px 12px;"  # 按钮内边距
                                           "text-align: center;"  # 文本居中对齐
                                           "text-decoration: none;"  # 移除按钮文本的装饰（如下划线）
                                           "display: inline-block;"  # 行内块级元素
                                           "font-size: 21px;"  # 字体大小
                                           "margin: 0px 0px;"  # 外边距
                                           "cursor: pointer;"  # 设置鼠标悬停在按钮上时的光标样式为指针
                                           "border-radius: 8px;"  # 设置按钮边框的圆角半径
                                           "}"
                                           )
        self.cal_data_button.clicked.connect(self.cal_artifactData)
        self.cal_data_button2 = QPushButton("赌赢OR赌输")
        self.cal_data_button2.setStyleSheet("QPushButton {"
                                            "background-color:rgba(57, 197, 187, 0.8);"  # 设置按钮
                                            "border: none;"  # 移除按钮的边框
                                            "font-weight: bold;"   # 加粗
                                            "color: white;"  # 文本颜色
                                            "padding: 6px 12px;"  # 按钮内边距
                                            "text-align: center;"  # 文本居中对齐
                                            "text-decoration: none;"  # 移除按钮文本的装饰（如下划线）
                                            "display: inline-block;"  # 行内块级元素
                                            "font-size: 21px;"  # 字体大小
                                            "margin: 0px 0px;"  # 外边距
                                            "cursor: pointer;"  # 设置鼠标悬停在按钮上时的光标样式为指针
                                            "border-radius: 8px;"  # 设置按钮边框的圆角半径
                                            "}"
                                            )
        self.cal_data_button2.clicked.connect(self.cal_artifactData2)
        # 创建赌不赌的输出框
        self.grindArtifact_text = QTextBrowser()
        self.grindArtifact_text.setText("这里会提供一些建议，关于你是否应该赌圣遗物。仅供参考，不代表真实事件😋\n"
                                        "如果两个圣遗物加起来大于或等于12级点右边的按钮，否则请点左边的")
        self.grindArtifact_text.setStyleSheet("color: gray;" "font-size: 16px;" "font-weight: bold;")  # 字体大小
        self.grindArtifact_text.setFixedSize(300, 130)
        # 词条计算的布局
        self.originalEntryData_text = QTextBrowser()
        self.originalEntryData_text.setText("点击“计算数据”后，这里会显示你的圣遗物词条数")
        self.originalEntryData_text.setStyleSheet("color: gray;" "font-size: 16px;")  # 字体大小
        self.originalEntryData_text.setFixedSize(280, 180)
        self.currentEntryData_text = QTextBrowser()
        self.currentEntryData_text.setText("点击“计算数据”后，这里会显示你的圣遗物词条数")
        self.currentEntryData_text.setStyleSheet("color: gray;" "font-size: 16px;")  # 字体大小
        self.currentEntryData_text.setFixedSize(280, 180)
        self.layout_H_artifactForecast_btn.addStretch(1)
        self.layout_H_artifactForecast_btn.addWidget(self.cal_data_button)
        self.layout_H_artifactForecast_btn.addWidget(self.cal_data_button2)
        self.layout_H_artifactForecast_btn.addStretch(1)
        self.layout_V_artifactForecast_BtnText.addLayout(self.layout_H_artifactForecast_btn)
        self.layout_V_artifactForecast_BtnText.addWidget(self.grindArtifact_text)

        """两个命中率的框"""
        self.originalHitProbability_text = QTextBrowser()
        self.originalHitProbability_text.setText("点击“计算数据”后，这里会显示对圣遗物的预测")
        self.originalHitProbability_text.setFixedSize(200, 64)
        self.currentHitProbability_text = QTextBrowser()
        self.currentHitProbability_text.setText("点击“计算数据”后，这里会显示对圣遗物的预测")
        self.currentHitProbability_text.setFixedSize(200, 64)
        self.layout_H_HitProbability.addStretch(5)
        self.layout_H_HitProbability.addWidget(self.originalHitProbability_text)
        self.layout_H_HitProbability.addStretch(11)
        self.layout_H_HitProbability.addWidget(self.currentHitProbability_text)
        self.layout_H_HitProbability.addStretch(20)

        """ 整体布局 """
        # 词条读入的布局
        self.layout_V_all.addLayout(self.layout_H_artifactForecast_title)

        self.layout_H_artifactForecast_input.addWidget(self.originalArtifact_box)
        self.layout_H_artifactForecast_input.addStretch(1)
        self.layout_H_artifactForecast_input.addWidget(self.currentArtifact_box)
        self.layout_H_artifactForecast_input.addStretch(1)
        self.layout_H_artifactForecast_input.addWidget(self.ArtifactRate_box)
        self.layout_H_artifactForecast_input.addStretch(1)
        # 词条计算的布局
        self.layout_H_entryData.addWidget(self.CurrentLevel1_box)
        self.layout_H_entryData.addWidget(self.originalEntryData_text)
        self.layout_H_entryData.addStretch(3)
        self.layout_H_entryData.addWidget(self.CurrentLevel2_box)
        self.layout_H_entryData.addWidget(self.currentEntryData_text)
        self.layout_H_entryData.addStretch(3)
        self.layout_H_entryData.addLayout(self.layout_V_artifactForecast_BtnText)
        self.layout_H_entryData.addStretch(2)
        # 整体的垂直布局
        self.layout_V_all.addLayout(self.layout_H_artifactForecast_input)
        self.layout_V_all.addLayout(self.layout_H_entryData)
        self.layout_V_all.addLayout(self.layout_H_HitProbability)

        # 整体布局
        self.layout_V_all.addStretch(1)
        self.setLayout(self.layout_V_all)

    def cal_artifactData(self):
        """
        用于读取数据并调用计算圣遗物数据\n
        注意此函数仅计算和预测词条，计算赌赢的概率在cal_artifactData2里。\n
        函数功能：读取UI中新旧圣遗物的数据。仅读取，不计算。计算调用cal_entryData计算词条数\n
        关联按钮：cal_data_button
        """
        """初始化"""
        self.originalEntryData_text.setStyleSheet("color: black;" "font-size: 18px;")  # 字体大小
        self.currentEntryData_text.setStyleSheet("color: black;" "font-size: 18px;")  # 字体大小
        self.original_CritRate_value = self.original_BigHP_value = self.original_BigATK_value = \
            self.original_BigDEF_value = self.original_Charge_value = self.original_CritDMG_value = \
            self.original_SmallHP_value = self.original_SmallATK_value = self.original_SmallDEF_value = \
            self.original_EM_value = 0
        self.current_CritRate_value = self.current_BigHP_value = self.current_BigATK_value = \
            self.current_BigDEF_value = self.current_Charge_value = self.current_CritDMG_value = \
            self.current_SmallHP_value = self.current_SmallATK_value = self.current_SmallDEF_value = \
            self.current_EM_value = 0

        """计算选中的框对应的属性"""
        if self.originalArtifact_box_btn11.isChecked():
            self.original_CritRate_value = float(self.input_original_CritRate.text())
        if self.originalArtifact_box_btn12.isChecked():
            self.original_BigHP_value = float(self.input_original_BigHP.text())
        if self.originalArtifact_box_btn13.isChecked():
            self.original_BigATK_value = float(self.input_original_BigATK.text())
        if self.originalArtifact_box_btn14.isChecked():
            self.original_BigDEF_value = float(self.input_original_BigDEF.text())
        if self.originalArtifact_box_btn15.isChecked():
            self.original_Charge_value = float(self.input_original_Charge.text())
        if self.originalArtifact_box_btn21.isChecked():
            self.original_CritDMG_value = float(self.input_original_CritDMG.text())
        if self.originalArtifact_box_btn22.isChecked():
            self.original_SmallHP_value = float(self.input_original_SmallHP.text())
        if self.originalArtifact_box_btn23.isChecked():
            self.original_SmallATK_value = float(self.input_original_SmallATK.text())
        if self.originalArtifact_box_btn24.isChecked():
            self.original_SmallDEF_value = float(self.input_original_SmallDEF.text())
        if self.originalArtifact_box_btn25.isChecked():
            self.original_EM_value = float(self.input_original_EM.text())

        if self.currentArtifact_box_btn11.isChecked():
            self.current_CritRate_value = float(self.input_current_CritRate.text())
        if self.currentArtifact_box_btn12.isChecked():
            self.current_BigHP_value = float(self.input_current_BigHP.text())
        if self.currentArtifact_box_btn13.isChecked():
            self.current_BigATK_value = float(self.input_current_BigATK.text())
        if self.currentArtifact_box_btn14.isChecked():
            self.current_BigDEF_value = float(self.input_current_BigDEF.text())
        if self.currentArtifact_box_btn15.isChecked():
            self.current_Charge_value = float(self.input_current_Charge.text())
        if self.currentArtifact_box_btn21.isChecked():
            self.current_CritDMG_value = float(self.input_current_CritDMG.text())
        if self.currentArtifact_box_btn22.isChecked():
            self.current_SmallHP_value = float(self.input_current_SmallHP.text())
        if self.currentArtifact_box_btn23.isChecked():
            self.current_SmallATK_value = float(self.input_current_SmallATK.text())
        if self.currentArtifact_box_btn24.isChecked():
            self.current_SmallDEF_value = float(self.input_current_SmallDEF.text())
        if self.currentArtifact_box_btn25.isChecked():
            self.current_EM_value = float(self.input_current_EM.text())

        """权值"""
        self.Rate_CritRate_value = float(self.inputRate_CritRate.text()) / 100
        self.Rate_BigHP_value = float(self.inputRate_BigHP.text()) / 100
        self.Rate_BigATK_value = float(self.inputRate_BigATK.text()) / 100
        self.Rate_BigDEF_value = float(self.inputRate_BigDEF.text()) / 100
        self.Rate_Charge_value = float(self.inputRate_Charge.text()) / 100
        self.Rate_CritDMG_value = float(self.inputRate_CritDMG.text()) / 100
        self.Rate_SmallHP_value = float(self.inputRate_SmallHP.text()) / 100
        self.Rate_SmallATK_value = float(self.inputRate_SmallATK.text()) / 100
        self.Rate_SmallDEF_value = float(self.inputRate_SmallDEF.text()) / 100
        self.Rate_EM_value = float(self.inputRate_EM.text()) / 100

        """ 存储变量 """
        original_values = [
            self.original_CritRate_value,
            self.original_BigHP_value,
            self.original_BigATK_value,
            self.original_BigDEF_value,
            self.original_Charge_value,
            self.original_CritDMG_value,
            self.original_SmallHP_value,
            self.original_SmallATK_value,
            self.original_SmallDEF_value,
            self.original_EM_value
        ]  # 原圣遗物值
        current_values = [
            self.current_CritRate_value,
            self.current_BigHP_value,
            self.current_BigATK_value,
            self.current_BigDEF_value,
            self.current_Charge_value,
            self.current_CritDMG_value,
            self.current_SmallHP_value,
            self.current_SmallATK_value,
            self.current_SmallDEF_value,
            self.current_EM_value
        ]  # 新圣遗物值
        """调用词条计算,赌圣遗物"""
        self.cal_entryData()
        self.artifactForecast1 = self.artifactForecast(self.CurrentLevel1_value, original_values, 1)
        self.artifactForecast2 = self.artifactForecast(self.CurrentLevel2_value, current_values, 2)
        self.originalHitProbability_text.setText(self.artifactForecast1)
        self.currentHitProbability_text.setText(self.artifactForecast2)

    def cal_artifactData2(self):
        """
        加上了赌圣遗物的功能
        cal_grindProbability计算赌赢的概率
        """
        self.cal_artifactData()
        self.CompareNumbers()
        self.cal_grindProbability()

    def cal_entryData(self):
        """
        [子函数]
          函数功能：计算词条数\n
          关联函数：cal_data_button
          参考资料：
               hp    HP      atk     ATK     def     DEF    Charge    EM     CR      CD
        1档 209.13  4.08%   13.62   4.08%   16.20   5.10%   4.53%   16.32   2.72%   5.44%
        2档 239.00  4.66%   15.56   4.66%   18.52   5.83%   5.18%   18.65   3.11%   6.22%
        3档 268.88  5.25%   17.51   5.25%   20.83   6.56%   5.83%   20.98   3.50%   6.99%
        4档 298.75  5.83%   19.45   5.83%   23.15   7.29%   6.48%   23.31   3.89%   7.77%
        AVG 253.94  4.95%   16.54   4.95%   19.68   6.19%   5.51%   19.81   3.30%   6.60%
        """
        self.original_entryData = self.original_SmallHP_value / 253.94 + self.original_BigHP_value / 4.95 + \
                                  self.original_SmallATK_value / 16.54 + self.original_BigATK_value / 4.95 + \
                                  self.original_SmallDEF_value / 19.68 + self.original_BigDEF_value / 6.19 + \
                                  self.original_Charge_value / 5.51 + self.original_EM_value / 19.81 + \
                                  self.original_CritRate_value / 3.30 + self.original_CritDMG_value / 6.60
        self.originalEntryData_text.setText("词条数为："+"{:.4f}".format(self.original_entryData))
        if self.originalArtifact_box_btn11.isChecked():
            self.originalEntryData_text.append("暴击词条数:"+"{:.3f}".format(self.original_CritRate_value / 3.30))
        if self.originalArtifact_box_btn12.isChecked():
            self.originalEntryData_text.append("大生命词条数:"+"{:.3f}".format(self.original_BigHP_value / 4.95))
        if self.originalArtifact_box_btn13.isChecked():
            self.originalEntryData_text.append("大攻击词条数:"+"{:.3f}".format(self.original_BigATK_value / 4.95))
        if self.originalArtifact_box_btn14.isChecked():
            self.originalEntryData_text.append("大防御词条数:"+"{:.3f}".format(self.original_BigDEF_value / 6.19))
        if self.originalArtifact_box_btn15.isChecked():
            self.originalEntryData_text.append("充能词条数:"+"{:.3f}".format(self.original_Charge_value / 5.51))
        if self.originalArtifact_box_btn21.isChecked():
            self.originalEntryData_text.append("暴击伤害词条数:"+"{:.3f}".format(self.original_CritDMG_value / 6.60))
        if self.originalArtifact_box_btn22.isChecked():
            self.originalEntryData_text.append("小生命词条数:"+"{:.3f}".format(self.original_SmallHP_value / 253.94))
        if self.originalArtifact_box_btn23.isChecked():
            self.originalEntryData_text.append("小攻击词条数:"+"{:.3f}".format(self.original_SmallATK_value / 16.54))
        if self.originalArtifact_box_btn24.isChecked():
            self.originalEntryData_text.append("小防御词条数:"+"{:.3f}".format(self.original_SmallDEF_value / 19.68))
        if self.originalArtifact_box_btn25.isChecked():
            self.originalEntryData_text.append("精通词条数:"+"{:.3f}".format(self.original_EM_value / 19.81))

        self.Rate_original_entryData = self.original_SmallHP_value / 253.94 * self.Rate_SmallHP_value + \
                                       self.original_BigHP_value / 4.95 * self.Rate_BigHP_value + \
                                       self.original_SmallATK_value / 16.54 * self.Rate_SmallATK_value + \
                                       self.original_BigATK_value / 4.95 * self.Rate_BigATK_value + \
                                       self.original_SmallDEF_value / 19.68 * self.Rate_SmallDEF_value + \
                                       self.original_BigDEF_value / 6.19 * self.Rate_BigDEF_value + \
                                       self.original_Charge_value / 5.51 * self.Rate_Charge_value + \
                                       self.original_EM_value / 19.81 * self.Rate_EM_value + \
                                       self.original_CritRate_value / 3.30 * self.Rate_CritRate_value + \
                                       self.original_CritDMG_value / 6.60 * self.Rate_CritDMG_value
        self.originalEntryData_text.append("\n加权后的词条数为："+"{:.4f}".format(self.Rate_original_entryData))
        if self.originalArtifact_box_btn11.isChecked():
            self.originalEntryData_text.append("暴击词条数:"+"{:.3f}".format(self.original_CritRate_value / 3.30 * self.Rate_CritRate_value))
        if self.originalArtifact_box_btn12.isChecked():
            self.originalEntryData_text.append("大生命词条数:"+"{:.3f}".format(self.original_BigHP_value / 4.95 * self.Rate_BigHP_value))
        if self.originalArtifact_box_btn13.isChecked():
            self.originalEntryData_text.append("大攻击词条数:"+"{:.3f}".format(self.original_BigATK_value / 4.95 * self.Rate_BigATK_value))
        if self.originalArtifact_box_btn14.isChecked():
            self.originalEntryData_text.append("大防御词条数:"+"{:.3f}".format(self.original_BigDEF_value / 6.19 * self.Rate_BigDEF_value))
        if self.originalArtifact_box_btn15.isChecked():
            self.originalEntryData_text.append("充能词条数:"+"{:.3f}".format(self.original_Charge_value / 5.51 * self.Rate_Charge_value))
        if self.originalArtifact_box_btn21.isChecked():
            self.originalEntryData_text.append("暴击伤害词条数:"+"{:.3f}".format(self.original_CritDMG_value / 6.60 * self.Rate_CritDMG_value))
        if self.originalArtifact_box_btn22.isChecked():
            self.originalEntryData_text.append("小生命词条数:"+"{:.3f}".format(self.original_SmallHP_value / 253.94 * self.Rate_SmallHP_value))
        if self.originalArtifact_box_btn23.isChecked():
            self.originalEntryData_text.append("小攻击词条数:"+"{:.3f}".format(self.original_SmallATK_value / 16.54 * self.Rate_SmallATK_value))
        if self.originalArtifact_box_btn24.isChecked():
            self.originalEntryData_text.append("小防御词条数:"+"{:.3f}".format(self.original_SmallDEF_value / 19.68 * self.Rate_SmallDEF_value))
        if self.originalArtifact_box_btn25.isChecked():
            self.originalEntryData_text.append("精通词条数:"+"{:.3f}".format(self.original_EM_value / 19.81 * self.Rate_EM_value))

        self.current_entryData = self.current_SmallHP_value / 253.94 + self.current_BigHP_value / 4.95 + \
                                 self.current_SmallATK_value / 16.54 + self.current_BigATK_value / 4.95 + \
                                 self.current_SmallDEF_value / 19.68 + self.current_BigDEF_value / 6.19 + \
                                 self.current_Charge_value / 5.51 + self.current_EM_value / 19.81 + \
                                 self.current_CritRate_value / 3.30 + self.current_CritDMG_value / 6.60
        self.currentEntryData_text.setText("词条数为：" + "{:.4f}".format(self.current_entryData))
        if self.currentArtifact_box_btn11.isChecked():
            self.currentEntryData_text.append("暴击词条数:" + "{:.3f}".format(self.current_CritRate_value / 3.30))
        if self.currentArtifact_box_btn12.isChecked():
            self.currentEntryData_text.append("大生命词条数:" + "{:.3f}".format(self.current_BigHP_value / 4.95))
        if self.currentArtifact_box_btn13.isChecked():
            self.currentEntryData_text.append("大攻击词条数:" + "{:.3f}".format(self.current_BigATK_value / 4.95))
        if self.currentArtifact_box_btn14.isChecked():
            self.currentEntryData_text.append("大防御词条数:" + "{:.3f}".format(self.current_BigDEF_value / 6.19))
        if self.currentArtifact_box_btn15.isChecked():
            self.currentEntryData_text.append("充能词条数:" + "{:.3f}".format(self.current_Charge_value / 5.51))
        if self.currentArtifact_box_btn21.isChecked():
            self.currentEntryData_text.append("暴击伤害词条数:" + "{:.3f}".format(self.current_CritDMG_value / 6.60))
        if self.currentArtifact_box_btn22.isChecked():
            self.currentEntryData_text.append("小生命词条数:" + "{:.3f}".format(self.current_SmallHP_value / 253.94))
        if self.currentArtifact_box_btn23.isChecked():
            self.currentEntryData_text.append("小攻击词条数:" + "{:.3f}".format(self.current_SmallATK_value / 16.54))
        if self.currentArtifact_box_btn24.isChecked():
            self.currentEntryData_text.append("小防御词条数:" + "{:.3f}".format(self.current_SmallDEF_value / 19.68))
        if self.currentArtifact_box_btn25.isChecked():
            self.currentEntryData_text.append("精通词条数:" + "{:.3f}".format(self.current_EM_value / 19.81))

        self.Rate_current_entryData = self.current_SmallHP_value / 253.94 * self.Rate_SmallHP_value + \
                                      self.current_BigHP_value / 4.95 * self.Rate_BigHP_value + \
                                      self.current_SmallATK_value / 16.54 * self.Rate_SmallATK_value + \
                                      self.current_BigATK_value / 4.95 * self.Rate_BigATK_value + \
                                      self.current_SmallDEF_value / 19.68 * self.Rate_SmallDEF_value + \
                                      self.current_BigDEF_value / 6.19 * self.Rate_BigDEF_value + \
                                      self.current_Charge_value / 5.51 * self.Rate_Charge_value + \
                                      self.current_EM_value / 19.81 * self.Rate_EM_value + \
                                      self.current_CritRate_value / 3.30 * self.Rate_CritRate_value + \
                                      self.current_CritDMG_value / 6.60 * self.Rate_CritDMG_value
        self.currentEntryData_text.append("\n加权后的词条数为："+"{:.4f}".format(self.Rate_current_entryData))
        if self.currentArtifact_box_btn11.isChecked():
            self.currentEntryData_text.append("暴击词条数:"+"{:.3f}".format(self.current_CritRate_value / 3.30 * self.Rate_CritRate_value))
        if self.currentArtifact_box_btn12.isChecked():
            self.currentEntryData_text.append("大生命词条数:"+"{:.3f}".format(self.current_BigHP_value / 4.95 * self.Rate_BigHP_value))
        if self.currentArtifact_box_btn13.isChecked():
            self.currentEntryData_text.append("大攻击词条数:"+"{:.3f}".format(self.current_BigATK_value / 4.95 * self.Rate_BigATK_value))
        if self.currentArtifact_box_btn14.isChecked():
            self.currentEntryData_text.append("大防御词条数:"+"{:.3f}".format(self.current_BigDEF_value / 6.19 * self.Rate_BigDEF_value))
        if self.currentArtifact_box_btn15.isChecked():
            self.currentEntryData_text.append("充能词条数:"+"{:.3f}".format(self.current_Charge_value / 5.51 * self.Rate_Charge_value))
        if self.currentArtifact_box_btn21.isChecked():
            self.currentEntryData_text.append("暴击伤害词条数:"+"{:.3f}".format(self.current_CritDMG_value / 6.60 * self.Rate_CritDMG_value))
        if self.currentArtifact_box_btn22.isChecked():
            self.currentEntryData_text.append("小生命词条数:"+"{:.3f}".format(self.current_SmallHP_value / 253.94 * self.Rate_SmallHP_value))
        if self.currentArtifact_box_btn23.isChecked():
            self.currentEntryData_text.append("小攻击词条数:"+"{:.3f}".format(self.current_SmallATK_value / 16.54 * self.Rate_SmallATK_value))
        if self.currentArtifact_box_btn24.isChecked():
            self.currentEntryData_text.append("小防御词条数:"+"{:.3f}".format(self.current_SmallDEF_value / 19.68 * self.Rate_SmallDEF_value))
        if self.currentArtifact_box_btn25.isChecked():
            self.currentEntryData_text.append("精通词条数:"+"{:.3f}".format(self.current_EM_value / 19.81 * self.Rate_EM_value))

    def cal_grindProbability(self):
        """
        [子函数]
          函数功能：计算赌赢的概率\n
          触发函数：按下cal_data_button后触发的cal_artifactData中调用cal_grindProbability
          关联函数：artifactForecast计算圣遗物能不能生出来
        """
        WinningProbability = "赌赢的概率是:"
        WinningProbability += str(self.WinningProbability)
        self.grindArtifact_text.setText(WinningProbability)

    def CurrentLevel1_button_click(self):
        """
        [点击按钮的关联函数]
          当点击原圣遗物等级选项后，记录其等级
          默认值self.CurrentLevel1_value = 20
        """
        button = self.sender()
        choice_text = button.text()
        if choice_text == "+0":
            self.CurrentLevel1_value = 0
        elif choice_text == "+4":
            self.CurrentLevel1_value = 4
        elif choice_text == "+8":
            self.CurrentLevel1_value = 8
        elif choice_text == "+12":
            self.CurrentLevel1_value = 12
        elif choice_text == "+16":
            self.CurrentLevel1_value = 16
        elif choice_text == "+20":
            self.CurrentLevel1_value = 20
        else:
            self.CurrentLevel1_value = False
        print(self.CurrentLevel1_value)

    def CurrentLevel2_button_click(self):
        """
        [点击按钮的关联函数]
          当点击新圣遗物等级选项后，记录其等级
          默认值 self.CurrentLevel2_value = 0
        """
        button = self.sender()
        choice_text = button.text()
        if choice_text == "+0":
            self.CurrentLevel2_value = 0
        elif choice_text == "+4":
            self.CurrentLevel2_value = 4
        elif choice_text == "+8":
            self.CurrentLevel2_value = 8
        elif choice_text == "+12":
            self.CurrentLevel2_value = 12
        elif choice_text == "+16":
            self.CurrentLevel2_value = 16
        elif choice_text == "+20":
            self.CurrentLevel2_value = 20
        else:
            self.CurrentLevel2_value = False
        print(self.CurrentLevel2_value)

    def artifactForecast(self, CurrentLevel, values, artifactType):
        """
        [子函数]
          用于计算某一等级圣遗物未来的强化可能性
        :param CurrentLevel: 当前等级
        :param values: 原圣遗物和新圣遗物的值的列表，用于在GetRateVariable_RateValues里判断哪些属性是输入的圣遗物中有的
        :param artifactType: 圣遗物是老(1)还是新(2)
        :return: Artifact_ForecastText 圣遗物强化提示语
        """
        """ Part 1 计算不歪率"""
        # 调用两个函数
        self.GetRateVariable_RateValues(values)
        RateMaxTupleLength = 0
        RateMaxTuple = []
        RateMaxTupleLength, RateMaxTuple = self.FindMaxRate()
        EnhanceTimes = 0  # 强化次数
        if 0 <= CurrentLevel < 4:
            EnhanceTimes = 5
        elif 4 <= CurrentLevel < 8:
            EnhanceTimes = 4
        elif 8 <= CurrentLevel < 12:
            EnhanceTimes = 3
        elif 12 <= CurrentLevel < 16:
            EnhanceTimes = 2
        elif 16 <= CurrentLevel < 20:
            EnhanceTimes = 1
        elif CurrentLevel == 20:
            EnhanceTimes = 0
        else:
            EnhanceTimes = False
        # todo 如果初始3，需要EnhanceTimes-=1 这个以后再做。并且要考虑初始3还要new一个新词条来预测词条。
        HitProbability = RateMaxTupleLength / 4  # 全命中所选最高得分词条的概率
        Artifact_ForecastText = ""
        if EnhanceTimes == 0:
            Artifact_ForecastText = "已经是最高等级了"
        elif EnhanceTimes:
            HitProbability = HitProbability**EnhanceTimes
            if HitProbability > 1:
                HitProbability = 1  # 如果选择了大于5个值，其实这应该是不存在的，但是还是给它转回1，不然概率超过100%真好玩
            Artifact_ForecastText = "全部命中的概率是" + "{:.2f}".format(HitProbability*100) + "%"
        else:
            Artifact_ForecastText = "有bug呜呜"
        """ Part 2 计算预测词条数 """
        if EnhanceTimes == 0:
            pass  # 已经是最高等级就算了
        elif EnhanceTimes:
            if artifactType == 1:
                NewRate_original_entryData = self.Rate_original_entryData
                NewRate_original_entryData += EnhanceTimes / 4 *  \
                                               ((self.original_SmallHP_value != 0) * self.Rate_SmallHP_value +
                                               (self.original_BigHP_value != 0) * self.Rate_BigHP_value +
                                               (self.original_SmallATK_value != 0) * self.Rate_SmallATK_value +
                                               (self.original_BigATK_value != 0) * self.Rate_BigATK_value +
                                               (self.original_SmallDEF_value != 0) * self.Rate_SmallDEF_value +
                                               (self.original_BigDEF_value != 0) * self.Rate_BigDEF_value +
                                               (self.original_Charge_value != 0) * self.Rate_Charge_value +
                                               (self.original_EM_value != 0) * self.Rate_EM_value +
                                               (self.original_CritRate_value != 0) * self.Rate_CritRate_value +
                                               (self.original_CritDMG_value != 0) * self.Rate_CritDMG_value)
                Artifact_ForecastText += "\n预估强化后的加权词条数为："+"{:.4f}".format(NewRate_original_entryData)
            if artifactType == 2:
                NewRate_current_entryData = self.Rate_current_entryData
                NewRate_current_entryData += EnhanceTimes / 4 * \
                                               ((self.current_SmallHP_value != 0) * self.Rate_SmallHP_value +
                                               (self.current_BigHP_value != 0) * self.Rate_BigHP_value +
                                               (self.current_SmallATK_value != 0) * self.Rate_SmallATK_value +
                                               (self.current_BigATK_value != 0) * self.Rate_BigATK_value +
                                               (self.current_SmallDEF_value != 0) * self.Rate_SmallDEF_value +
                                               (self.current_BigDEF_value != 0) * self.Rate_BigDEF_value +
                                               (self.current_Charge_value != 0) * self.Rate_Charge_value +
                                               (self.current_EM_value != 0) * self.Rate_EM_value +
                                               (self.current_CritRate_value != 0) * self.Rate_CritRate_value +
                                               (self.current_CritDMG_value != 0) * self.Rate_CritDMG_value)
                Artifact_ForecastText += "\n预估强化后的加权词条数为："+"{:.4f}".format(NewRate_current_entryData)
        else:
            Artifact_ForecastText += "有bug呜呜"
        """ Part 3 计算赌赢率 """
        if artifactType == 1:
            self.EnhanceSimulator(self.Rate_original_entryData, EnhanceTimes, artifactType)
        elif artifactType == 2:
            self.EnhanceSimulator(self.Rate_current_entryData, EnhanceTimes, artifactType)
        return Artifact_ForecastText

    def FindMaxRate(self):
        """
        [子函数]
          找到圣遗物自定义评分中100的值，认为你很重视这些属性
        """
        non_zero_values = sorted([(variable, value) for variable, value in zip(self.RateVariables, self.RateValues)
                                  if value == 1],
                                 key=lambda x: x[1], reverse=True)
        if not non_zero_values:
            return 0, None  # 没有值的情况
        else:
            # 使用列表推导式提取每个元组的第一个元素
            non_zero_list = [item[0] for item in non_zero_values]
            return len(non_zero_list), non_zero_list  # 有值的情况

    def GetRateVariable_RateValues(self, values):
        """
        [子函数]
          获取self.RateVariable和self.RateValue
        """
        self.RateVariables = []
        self.RateValues = []
        # Rate变量列表
        self.ALLRateVariables = ["self.Rate_CritRate_value", "self.Rate_BigHP_value", "self.Rate_BigATK_value",
                                 "self.Rate_BigDEF_value", "self.Rate_Charge_value", "self.Rate_CritDMG_value",
                                 "self.Rate_SmallHP_value", "self.Rate_SmallATK_value", "self.Rate_SmallDEF_value",
                                 "self.Rate_EM_value"]
        # Rate变量值
        self.ALLRateValues = [self.Rate_CritRate_value, self.Rate_BigHP_value, self.Rate_BigATK_value,
                              self.Rate_BigDEF_value, self.Rate_Charge_value, self.Rate_CritDMG_value,
                              self.Rate_SmallHP_value, self.Rate_SmallATK_value, self.Rate_SmallDEF_value,
                              self.Rate_EM_value]
        for value, RateVariable, RateValue in zip(values, self.ALLRateVariables, self.ALLRateValues):
            if value != 0:
                self.RateVariables.append(RateVariable)
                self.RateValues.append(RateValue)  # 使用getattr获取属性的值

    def EnhanceSimulator(self, entryData, EnhanceTimes, artifactType):
        """
        [子函数]
          模拟强化
        本质上还是每次强化是16个随机可能结果，用一个列表存放本次强化后的词条数。
        然后下一次强化时在这16个数的基础上再强化一次，相当于16×16。然后迭代下去。
        比如现在新出的胚子是初始四从零开始强化，最后这个列表应该是16*16*16*16*16=1048576个元素
               hp    HP      atk     ATK     def     DEF    Charge    EM     CR      CD
        1档 209.13  4.08%   13.62   4.08%   16.20   5.10%   4.53%   16.32   2.72%   5.44%
        2档 239.00  4.66%   15.56   4.66%   18.52   5.83%   5.18%   18.65   3.11%   6.22%
        3档 268.88  5.25%   17.51   5.25%   20.83   6.56%   5.83%   20.98   3.50%   6.99%
        4档 298.75  5.83%   19.45   5.83%   23.15   7.29%   6.48%   23.31   3.89%   7.77%
        AVG 253.94  4.95%   16.54   4.95%   19.68   6.19%   5.51%   19.81   3.30%   6.60%

        :param entryData: 当前加权词条数
        :param EnhanceTimes: 剩余强化次数
        :param artifactType: 圣遗物是老还是新(artifactType=1:老 artifactType=2:新)
        :return: 强化结果列表
        """
        """ 前置数据库 """
        # 获取加权词条表
        hp = [209.13, 239.00, 268.88, 298.75]
        HP = [4.08, 4.66, 5.25, 5.83]
        atk = [13.62, 15.56, 17.51, 19.45]
        ATK = [4.08, 4.66, 5.25, 5.83]
        def_val = [16.20, 18.52, 20.83, 23.15]
        DEF = [5.10, 5.83, 6.56, 7.29]
        charge = [4.53, 5.18, 5.83, 6.48]
        EM = [16.32, 18.65, 20.98, 23.31]
        CR = [2.72, 3.11, 3.50, 3.89]
        CD = [5.44, 6.22, 6.99, 7.77]
        hp_RateScore = [x * (self.Rate_SmallHP_value / 253.94) for x in hp]
        HP_RateScore = [x * (self.Rate_BigHP_value / 4.95) for x in HP]
        atk_RateScore = [x * (self.Rate_SmallATK_value / 16.54) for x in atk]
        ATK_RateScore = [x * (self.Rate_BigATK_value / 4.95) for x in ATK]
        def_RateScore = [x * (self.Rate_SmallDEF_value / 19.68) for x in def_val]
        DEF_RateScore = [x * (self.Rate_BigDEF_value / 6.19) for x in DEF]
        Charge_RateScore = [x * (self.Rate_Charge_value / 5.51) for x in charge]
        EM_RateScore = [x * (self.Rate_EM_value / 19.81) for x in EM]
        CR_RateScore = [x * (self.Rate_CritRate_value / 3.30) for x in CR]
        CD_RateScore = [x * (self.Rate_CritDMG_value / 6.60) for x in CD]
        # EnhanceList用于存放 当前圣遗物所拥有的的属性 所对应的 加权词条表
        EnhanceList = []
        if artifactType == 1:
            if self.original_SmallHP_value != 0:
                EnhanceList += hp_RateScore
            if self.original_BigHP_value != 0:
                EnhanceList += HP_RateScore
            if self.original_SmallATK_value != 0:
                EnhanceList += atk_RateScore
            if self.original_BigATK_value != 0:
                EnhanceList += ATK_RateScore
            if self.original_SmallDEF_value != 0:
                EnhanceList += def_RateScore
            if self.original_BigDEF_value != 0:
                EnhanceList += DEF_RateScore
            if self.original_Charge_value != 0:
                EnhanceList += Charge_RateScore
            if self.original_EM_value != 0:
                EnhanceList += EM_RateScore
            if self.original_CritRate_value != 0:
                EnhanceList += CR_RateScore
            if self.original_CritDMG_value != 0:
                EnhanceList += CD_RateScore
        elif artifactType == 2:
            if self.current_SmallHP_value != 0:
                EnhanceList += hp_RateScore
            if self.current_BigHP_value != 0:
                EnhanceList += HP_RateScore
            if self.current_SmallATK_value != 0:
                EnhanceList += atk_RateScore
            if self.current_BigATK_value != 0:
                EnhanceList += ATK_RateScore
            if self.current_SmallDEF_value != 0:
                EnhanceList += def_RateScore
            if self.current_BigDEF_value != 0:
                EnhanceList += DEF_RateScore
            if self.current_Charge_value != 0:
                EnhanceList += Charge_RateScore
            if self.current_EM_value != 0:
                EnhanceList += EM_RateScore
            if self.current_CritRate_value != 0:
                EnhanceList += CR_RateScore
            if self.current_CritDMG_value != 0:
                EnhanceList += CD_RateScore
        # 让EnhanceList的长度刚好为16，也就是四个属性
        if len(EnhanceList) < 16:
            EnhanceList += [0] * (16 - len(EnhanceList))
        elif len(EnhanceList) > 16:
            EnhanceList = EnhanceList[:16]
        # 将现有词条数转化为列表Current_entryData_list
        Current_entryData = entryData
        Current_entryData_list = [Current_entryData]

        for _ in range(EnhanceTimes):
            Current_entryData_list = [xelem + addelem for xelem in Current_entryData_list for addelem in EnhanceList]
        # print(str(artifactType) + "的 Current_entryData_list为:\n" + str(Current_entryData_list) + "\n长度" + str(len(Current_entryData_list)))

        # nmd终于把强化全概率结果的list搞出来了，现在把这两个寄品圣遗物组存起来
        if artifactType == 1:
            self.original_RubbishArtifact_list = Current_entryData_list
        elif artifactType == 2:
            self.current_RubbishArtifact_list = Current_entryData_list

    def CompareNumbers(self):
        """
        [子函数]
          传入参数：列表，列表
        比如现在新出的胚子是初始四从零开始强化，最后这个列表应该是16*16*16*16*16=1048576个元素。
        以前的胚子是+12级的，就是16*16=256种强化结果。
        然后比较1048576个结果和256种结果，得到超过的概率，1048576*256=268435456种情况中，现在的胚子比以前的强的概率。
        :return: 概率
        """
        winwinwincount = 0
        count = 0
        for original_value in self.original_RubbishArtifact_list:
            for current_value in self.current_RubbishArtifact_list:
                count += 1
                if current_value >= original_value:
                    # 如果现在的圣遗物的预测词条数大于原来的圣遗物，则认为成功
                    winwinwincount += 1
        self.WinningProbability = 0
        self.WinningProbability = winwinwincount/count  # 现在的圣遗物赢了的概率
