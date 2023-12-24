import sys
import dmg_cal
from openpyxl import Workbook, load_workbook

from PyQt5.QtGui import QFont, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout, QLabel, \
    QLineEdit, QFormLayout, QGroupBox, QRadioButton, QTextBrowser, QSizePolicy, QButtonGroup, QFileDialog, QCheckBox


def isFloat(s):
    try:
        float(s)
        return True
    except:
        return False


class Window1(QWidget):
    """
    窗口1\n
    包括伤害乘区计算\n
    """
    def __init__(self):
        """
        初始化damage的UI
        """
        super().__init__()
        self.init_damage_ui()

    def init_damage_ui(self):
        """
        该部分绘制伤害乘区的布局
        """
        font_chinese_SimSun12 = QFont("SimSun", 12)
        font_chinese_SimSun16Bold = QFont("SimSun", 16)
        font_chinese_SimSun16Bold.setBold(True)
        font_english_TNR12 = QFont("Times New Roman", 12)

        self.layout_V_all = QVBoxLayout()  # 整体的垂直布局

        self.layout_H_damage_title = QHBoxLayout()  # 伤害乘区标题的水平布局
        self.layout_H_damage = QHBoxLayout()  # 伤害乘区的水平布局
        self.layout_CBT_damage = QHBoxLayout()  # 激化乘区和按钮和伤害输出框(文字)的水平布局

        self.layout_AE_cal = QVBoxLayout()  # AE乘区的竖直排列
        self.layout_DB_cal = QVBoxLayout()  # DB乘区的竖直排列
        self.layout_CD_cal = QVBoxLayout()  # CD乘区的竖直排列
        self.layout_ER_cal = QVBoxLayout()  # ER乘区的竖直排列
        self.layout_DF_cal = QVBoxLayout()  # DF乘区的竖直排列
        self.layout_RT_cal = QVBoxLayout()  # RT乘区的竖直排列
        self.layout_btn_damagedata_cal = QHBoxLayout()  # 计算、存储、读取三个按钮水平排列
        self.layout_BT_cal = QVBoxLayout()  # btn和text的竖直排列
        self.layout_Cat_cal = QVBoxLayout()  # Cat_cal子乘区的竖直排列

        """ ----- 伤害乘区标题 ----- """
        self.label_damage_title = QLabel("伤害乘区计算")
        self.label_damage_title.setFont(font_chinese_SimSun16Bold)
        self.label_damage_title.setStyleSheet("background-color:rgba(102, 204, 255, 0.6);")
        self.layout_H_damage_title.addStretch(1)
        self.layout_H_damage_title.addWidget(self.label_damage_title)
        self.layout_H_damage_title.addStretch(1)

        """ ----- 六个伤害乘区 ----- """

        """ Part 1 AE乘区 """
        self.label_AE = QLabel("AE")
        self.label_AE.setFont(font_english_TNR12)
        self.AE_formlayout = QFormLayout()  # 表单容器
        """攻击力"""
        self.input_atk = QLineEdit()  # 攻击力输入框
        self.input_atk.setPlaceholderText("atk")  # 设置提示语
        self.input_atk.setText("2000")  # 设置默认值
        """天赋倍率"""
        self.input_talent = QLineEdit()  # 天赋倍率输入框
        self.input_talent.setPlaceholderText("talent")
        self.input_talent.setText("300")  # 设置默认值
        self.input_talent_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_talent_withpercent.addWidget(self.input_talent)
        self.input_talent_withpercent.addWidget(self.percent_label)
        """基础伤害加成(加算)"""
        self.input_added_basedamage = QLineEdit()  # 基础伤害加成(加算)输入框
        self.input_added_basedamage.setPlaceholderText("加算")  # 设置提示语
        self.input_added_basedamage.setText("0")  # 设置默认值
        """基础伤害加成(乘算)"""
        self.input_multiply_basedamage = QLineEdit()  # 基础伤害加成(乘算)输入框
        self.input_multiply_basedamage.setPlaceholderText("乘算")  # 设置提示语
        self.input_multiply_basedamage.setText("0")  # 设置默认值
        self.input_multiply_basedamage_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_multiply_basedamage_withpercent.addWidget(self.input_multiply_basedamage)
        self.input_multiply_basedamage_withpercent.addWidget(self.percent_label)
        """设置窗口格式"""
        self.AE_formlayout.addRow("攻击力:", self.input_atk)
        self.AE_formlayout.addRow("倍率:", self.input_talent_withpercent)
        self.AE_formlayout.addRow("基础伤害加成:", self.input_added_basedamage)
        self.AE_formlayout.addRow("基础伤害加成:", self.input_multiply_basedamage_withpercent)
        self.layout_AE_cal.addWidget(self.label_AE)
        self.layout_AE_cal.addLayout(self.AE_formlayout)
        self.layout_AE_cal.addStretch(1)

        """ Part 2 DB乘区 """
        self.label_DB = QLabel("DB")
        self.label_DB.setFont(font_english_TNR12)
        self.DB_formlayout = QFormLayout()  # 表单容器
        """增伤"""
        self.input_db = QLineEdit()  # 增伤输入框
        self.input_db.setPlaceholderText("DB%")
        self.input_db.setText("46.6")  # 设置默认值
        self.input_db_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_db_withpercent.addWidget(self.input_db)
        self.input_db_withpercent.addWidget(self.percent_label)
        """设置窗口格式"""
        self.DB_formlayout.addRow("增伤:", self.input_db_withpercent)
        self.layout_DB_cal.addWidget(self.label_DB)
        self.layout_DB_cal.addLayout(self.DB_formlayout)
        self.layout_DB_cal.addStretch(1)

        """ Part 3 CD乘区 """
        self.label_CD = QLabel("CD")
        self.label_CD.setFont(font_english_TNR12)
        self.CD_formlayout = QFormLayout()  # 表单容器
        """暴击率"""
        self.input_cr = QLineEdit()  # 暴击率输入框
        self.input_cr.setPlaceholderText("CR")
        self.input_cr.setText("80")  # 设置默认值
        self.input_cr_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_cr_withpercent.addWidget(self.input_cr)
        self.input_cr_withpercent.addWidget(self.percent_label)
        """暴击伤害"""
        self.input_cd = QLineEdit()  # 暴击伤害输入框
        self.input_cd.setPlaceholderText("CD")
        self.input_cd.setText("180")  # 设置默认值
        self.input_cd_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_cd_withpercent.addWidget(self.input_cd)
        self.input_cd_withpercent.addWidget(self.percent_label)
        """设置窗口格式"""
        self.CD_formlayout.addRow("暴击率:", self.input_cr_withpercent)
        self.CD_formlayout.addRow("暴伤:", self.input_cd_withpercent)
        self.layout_CD_cal.addWidget(self.label_CD)
        self.layout_CD_cal.addLayout(self.CD_formlayout)
        self.layout_CD_cal.addStretch(1)

        """ Part 4 ER乘区 """
        self.label_ER = QLabel("ER")
        self.label_ER.setFont(font_english_TNR12)
        self.ER_formlayout = QFormLayout()
        """4种反应"""
        self.elemental_box = QGroupBox("反应过程")
        # elemental_vlayout = QVBoxLayout()  # 四个反应水平排放放不下，真狗屎，放一列又太丑。。
        self.elemental_vlayout = QVBoxLayout()
        self.elemental_hlayout1 = QHBoxLayout()
        self.elemental_hlayout2 = QHBoxLayout()
        self.elemental_box_btn1 = QRadioButton("水火蒸发")  # 2
        self.elemental_box_btn2 = QRadioButton("火水蒸发")  # 1.5
        self.elemental_box_btn3 = QRadioButton("火冰融化")  # 2
        self.elemental_box_btn4 = QRadioButton("冰火融化")  # 1.5
        # todo 我靠忘了纯色队
        self.elemental_box_btn1.setChecked(True)  # 设置水火蒸发默认选中并为参数设置默认值
        self.elementalchoice_value = 1
        self.elemental_magnification = 2
        # 连接四个按钮的信号和槽elemental_button_click
        self.elemental_box_btn1.clicked.connect(self.elemental_button_click)
        self.elemental_box_btn2.clicked.connect(self.elemental_button_click)
        self.elemental_box_btn3.clicked.connect(self.elemental_button_click)
        self.elemental_box_btn4.clicked.connect(self.elemental_button_click)
        self.elemental_hlayout1.addWidget(self.elemental_box_btn1)
        self.elemental_hlayout1.addWidget(self.elemental_box_btn2)
        self.elemental_hlayout2.addWidget(self.elemental_box_btn3)
        self.elemental_hlayout2.addWidget(self.elemental_box_btn4)
        self.elemental_vlayout.addLayout(self.elemental_hlayout1)
        self.elemental_vlayout.addLayout(self.elemental_hlayout2)
        self.elemental_box.setLayout(self.elemental_vlayout)
        """精通"""
        self.input_em = QLineEdit()  # 精通输入框
        self.input_em.setText("0")  # 设置默认值
        """反应系数提高"""
        self.input_IRC = QLineEdit()  # 反应系数提高输入框
        self.input_IRC.setText("0")  # 设置默认值
        self.input_IRC_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_IRC_withpercent.addWidget(self.input_IRC)
        self.input_IRC_withpercent.addWidget(self.percent_label)
        """设置窗口格式"""
        self.ER_formlayout.addRow("精通:", self.input_em)
        self.ER_formlayout.addRow("反应系数提高:", self.input_IRC_withpercent)
        self.layout_ER_cal.addWidget(self.label_ER)
        self.layout_ER_cal.addWidget(self.elemental_box)
        self.layout_ER_cal.addLayout(self.ER_formlayout)
        self.layout_ER_cal.addStretch(1)

        """ Part 5 DF乘区 """
        self.label_DF = QLabel("DF")
        self.label_DF.setFont(font_english_TNR12)
        self.DF_formlayout = QFormLayout()  # 表单容器
        """人物等级"""
        self.input_person_lever = QLineEdit()  # 角色等级输入框
        self.input_person_lever.setText("90")  # 设置默认值
        """魔物等级"""
        self.input_hilichurl_level = QLineEdit()  # 魔物等级输入框
        self.input_hilichurl_level.setText("100")  # 设置默认值
        """减防"""
        self.input_reduce_defenses = QLineEdit()  # 减防输入框
        self.input_reduce_defenses.setPlaceholderText("降低敌人防御")
        self.input_reduce_defenses.setText("0")  # 设置默认值
        self.input_reduce_defenses_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_reduce_defenses_withpercent.addWidget(self.input_reduce_defenses)
        self.input_reduce_defenses_withpercent.addWidget(self.percent_label)
        """穿防"""
        self.input_ignore_defenses = QLineEdit()  # 穿防输入框
        self.input_ignore_defenses.setPlaceholderText("无视敌人防御")
        self.input_ignore_defenses.setText("0")  # 设置默认值
        self.input_ignore_defenses_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_ignore_defenses_withpercent.addWidget(self.input_ignore_defenses)
        self.input_ignore_defenses_withpercent.addWidget(self.percent_label)
        """增防"""
        self.input_increase_defenses = QLineEdit()  # 增防输入框
        self.input_increase_defenses.setPlaceholderText("常见于魔物塔")
        self.input_increase_defenses.setText("0")  # 设置默认值
        """设置窗口格式"""
        self.DF_formlayout.addRow("人物等级:", self.input_person_lever)
        self.DF_formlayout.addRow("魔物等级:", self.input_hilichurl_level)
        self.DF_formlayout.addRow("减防:", self.input_reduce_defenses_withpercent)
        self.DF_formlayout.addRow("穿防:", self.input_ignore_defenses_withpercent)
        self.DF_formlayout.addRow("增防:", self.input_increase_defenses)
        self.layout_DF_cal.addWidget(self.label_DF)
        self.layout_DF_cal.addLayout(self.DF_formlayout)
        self.layout_DF_cal.addStretch(1)

        """ Part 6 RT乘区 """
        self.label_RT = QLabel("RT")
        self.label_RT.setFont(font_english_TNR12)
        self.RT_formlayout = QFormLayout()  # 表单容器
        """抗性"""
        self.input_resistance = QLineEdit()  # 抗性输入框
        self.input_resistance.setText("10")  # 设置默认值
        self.input_resistance_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_resistance_withpercent.addWidget(self.input_resistance)
        self.input_resistance_withpercent.addWidget(self.percent_label)
        """减抗"""
        self.input_reduce_resistance = QLineEdit()  # 减抗输入框
        self.input_reduce_resistance.setPlaceholderText("RT%")
        self.input_reduce_resistance.setText("0")  # 设置默认值
        self.input_reduce_resistance_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_reduce_resistance_withpercent.addWidget(self.input_reduce_resistance)
        self.input_reduce_resistance_withpercent.addWidget(self.percent_label)
        """设置窗口格式"""
        self.RT_formlayout.addRow("抗性:", self.input_resistance_withpercent)
        self.RT_formlayout.addRow("减抗:", self.input_reduce_resistance_withpercent)
        self.layout_RT_cal.addWidget(self.label_RT)
        self.layout_RT_cal.addLayout(self.RT_formlayout)
        self.layout_RT_cal.addStretch(1)

        """ 将伤害部分添加到水平布局器 """
        self.layout_H_damage.addLayout(self.layout_AE_cal)
        self.layout_H_damage.addLayout(self.layout_DB_cal)
        self.layout_H_damage.addLayout(self.layout_CD_cal)
        self.layout_H_damage.addLayout(self.layout_ER_cal)
        self.layout_H_damage.addLayout(self.layout_DF_cal)
        self.layout_H_damage.addLayout(self.layout_RT_cal)

        self.layout_V_all.addLayout(self.layout_H_damage_title)
        self.layout_V_all.addLayout(self.layout_H_damage)  # 将水平的六个伤害乘区添加到整体的垂直排列

        """ SubPart 1 Cat_cal乘区 """
        self.label_Cat_cal = QLabel("激化加成")
        self.label_Cat_cal.setFont(font_chinese_SimSun12)
        self.Cat_cal_formlayout = QFormLayout()  # 表单容器
        """是否激化"""
        self.catalyzeIf_box = QGroupBox("是否激化")
        self.catalyzeIf_hlayout = QHBoxLayout()
        self.catalyzeIf_box_btn1 = QRadioButton("激化")
        self.catalyzeIf_box_btn2 = QRadioButton("不激化")
        self.catalyzeIf_box_btn2.setChecked(True)  # 设置不激化默认选中
        self.catalyzeIf_value = 0
        # 连接两个按钮的信号和槽catalyzeIf_button_click
        self.catalyzeIf_box_btn1.clicked.connect(self.catalyzeIf_button_click)
        self.catalyzeIf_box_btn2.clicked.connect(self.catalyzeIf_button_click)
        self.catalyzeIf_hlayout.addWidget(self.catalyzeIf_box_btn1)
        self.catalyzeIf_hlayout.addWidget(self.catalyzeIf_box_btn2)
        self.catalyzeIf_box.setLayout(self.catalyzeIf_hlayout)
        """激化类型"""
        self.catalyzeType_box = QGroupBox("激化类型")
        self.catalyzeType_hlayout = QHBoxLayout()
        self.catalyzeType_box_btn1 = QRadioButton("原激化")
        self.catalyzeType_box_btn2 = QRadioButton("超激化")
        self.catalyzeType_box_btn3 = QRadioButton("蔓激化")
        self.catalyzeType_box_btn3.setChecked(True)  # 设置蔓激化默认选中
        self.catalyzeType_value = 2
        # 连接三个按钮的信号和槽catalyzeType_button_click
        self.catalyzeType_box_btn1.clicked.connect(self.catalyzeType_button_click)
        self.catalyzeType_box_btn2.clicked.connect(self.catalyzeType_button_click)
        self.catalyzeType_box_btn3.clicked.connect(self.catalyzeType_button_click)
        self.catalyzeType_hlayout.addWidget(self.catalyzeType_box_btn1)
        self.catalyzeType_hlayout.addWidget(self.catalyzeType_box_btn2)
        self.catalyzeType_hlayout.addWidget(self.catalyzeType_box_btn3)
        self.catalyzeType_box.setLayout(self.catalyzeType_hlayout)
        """激化反应加成值"""
        self.input_DCI = QLineEdit()  # damage_catalyze_increased激化反应加成值输入框
        self.input_DCI.setText("0")  # 设置默认值
        self.input_DCI_withpercent = QHBoxLayout()
        self.percent_label = QLabel("%")
        self.input_DCI_withpercent.addWidget(self.input_DCI)
        self.input_DCI_withpercent.addWidget(self.percent_label)
        """设置窗口格式"""
        self.Cat_cal_formlayout.addRow("激化反应加成值:", self.input_DCI_withpercent)
        self.layout_Cat_cal.addWidget(self.label_Cat_cal)
        self.layout_Cat_cal.addWidget(self.catalyzeIf_box)
        self.layout_Cat_cal.addWidget(self.catalyzeType_box)
        self.layout_Cat_cal.addLayout(self.Cat_cal_formlayout)

        """ Part Added 按钮 """
        # 第七大乘区，按钮乘区。蒸馍，你不服气
        self.button_cal_damage_data = QPushButton("计算数据")
        self.button_cal_damage_data.setStyleSheet("QPushButton {"
                                                  "background-color:rgba(170, 102, 128, 0.7);"  # 设置按钮
                                                  "border: none;"  # 移除按钮的边框
                                                  "font-weight: bold;"   # 加粗
                                                  "color: white;"  # 文本颜色
                                                  "padding: 6px 12px;"  # 按钮内边距
                                                  "text-align: center;"  # 文本居中对齐
                                                  "text-decoration: none;"  # 移除按钮文本的装饰（如下划线）
                                                  "display: inline-block;"  # 行内块级元素
                                                  "font-size: 16px;"  # 字体大小
                                                  "margin: 2px 1px;"  # 外边距
                                                  "cursor: pointer;"  # 设置鼠标悬停在按钮上时的光标样式为指针
                                                  "border-radius: 8px;"  # 设置按钮边框的圆角半径
                                                  "}"
                                                  )
        self.button_cal_damage_data.clicked.connect(self.cal_damage_data)
        self.button_store_data = QPushButton("存储数据")
        self.button_store_data.setStyleSheet("QPushButton {"
                                             "background-color:rgba(102, 204, 255, 0.8);"  # 设置按钮颜色
                                             "border: none;"  # 移除按钮的边框
                                             "font-weight: bold;"   # 加粗
                                             "color: white;"  # 文本颜色
                                             "padding: 6px 12px;"  # 按钮内边距
                                             "text-align: center;"  # 文本居中对齐
                                             "text-decoration: none;"  # 移除按钮文本的装饰（如下划线）
                                             "display: inline-block;"  # 行内块级元素
                                             "font-size: 16px;"  # 字体大小
                                             "margin: 2px 1px;"  # 外边距
                                             "cursor: pointer;"  # 设置鼠标悬停在按钮上时的光标样式为指针
                                             "border-radius: 8px;"  # 设置按钮边框的圆角半径
                                             "}"
                                             )
        self.button_store_data.clicked.connect(self.store_data)
        self.button_read_data = QPushButton("读取数据")
        self.button_read_data.setStyleSheet("QPushButton {"
                                            "background-color:rgba(57, 197, 187, 0.8);"  # 设置按钮颜色
                                            "border: none;"  # 移除按钮的边框
                                            "font-weight: bold;"   # 加粗
                                            "color: white;"  # 文本颜色
                                            "padding: 6px 12px;"  # 按钮内边距
                                            "text-align: center;"  # 文本居中对齐
                                            "text-decoration: none;"  # 移除按钮文本的装饰（如下划线）
                                            "display: inline-block;"  # 行内块级元素
                                            "font-size: 16px;"  # 字体大小
                                            "margin: 2px 1px;"  # 外边距
                                            "cursor: pointer;"  # 设置鼠标悬停在按钮上时的光标样式为指针
                                            "border-radius: 8px;"  # 设置按钮边框的圆角半径
                                            "}"
                                            )
        self.button_read_data.clicked.connect(self.read_data)
        """设置三个数据处理的按钮格式"""
        self.layout_btn_damagedata_cal.addWidget(self.button_cal_damage_data)
        self.layout_btn_damagedata_cal.addWidget(self.button_store_data)
        self.layout_btn_damagedata_cal.addWidget(self.button_read_data)

        """ Part Added 输出显示(数值) """
        # 第八大乘区，显示屏乘区。显示计算结果的窗口。
        self.show_text_damage = QTextBrowser()
        self.show_text_damage.setText("点击上方的按钮能够实现：\n1.计算数据:根据界面上的数据计算\n2.存储数据:"
                                      "存储当前界面上的数据到本地\n3.读取数据:读取本地数据并更改当前界面内的数值\n"
                                      "！！！存储数据前请务必先计算数据一次，不然会闪退！！！")
        self.show_text_damage.setStyleSheet("color: gray;" "font-size: 16px;")  # 字体大小
        self.show_text_damage.setFixedSize(310, 150)

        """ 添加按钮与伤害输出窗口(文字版) B:Button T:Text """
        self.layout_BT_cal.addLayout(self.layout_btn_damagedata_cal)
        self.layout_BT_cal.addWidget(self.show_text_damage)

        """ 设置激化与按钮与伤害输出框(文字)的格式 """
        self.layout_CBT_damage.addLayout(self.layout_Cat_cal)
        self.layout_CBT_damage.addLayout(self.layout_BT_cal)
        self.layout_CBT_damage.addStretch(1)
        self.layout_V_all.addLayout(self.layout_CBT_damage)

        """ ----- 设置整体剩下的垂直布局 ----- """
        self.layout_V_all.addStretch(1)
        self.setLayout(self.layout_V_all)

    def cal_damage_data(self):
        """
        计算伤害
        """
        """ 获取数据 """
        self.atk_value = self.input_atk.text()
        self.talent_value = self.input_talent.text()
        self.added_basedamage_value = self.input_added_basedamage.text()
        self.multiply_basedamage_value = self.input_multiply_basedamage.text()

        self.DCI_value = self.input_DCI.text()

        self.db_value = self.input_db.text()

        self.cr_value = self.input_cr.text()
        self.cd_value = self.input_cd.text()

        self.em_value = self.input_em.text()
        # self.elementalchoice_value已经在函数on_elemental_buttongroup_clicked取值了
        self.IRC_value = self.input_IRC.text()

        self.person_lever_value = self.input_person_lever.text()
        self.hilichurl_level_value = self.input_hilichurl_level.text()
        self.reduce_defenses_value = self.input_reduce_defenses.text()
        self.ignore_defenses_value = self.input_ignore_defenses.text()
        self.increase_defenses_value = self.input_increase_defenses.text()

        self.resistance_value = self.input_resistance.text()
        self.reduce_resistance_value = self.input_reduce_resistance.text()

        """ 判断是不是都是int/float类型 """
        if (isFloat(self.atk_value) and isFloat(self.talent_value) and isFloat(self.added_basedamage_value) and isFloat(self.multiply_basedamage_value)
                and isFloat(self.db_value)
                and isFloat(self.cr_value) and isFloat(self.cd_value)
                and isFloat(self.em_value) and isFloat(self.IRC_value)
                and isFloat(self.person_lever_value) and isFloat(self.hilichurl_level_value) and isFloat(self.reduce_defenses_value) and isFloat(self.ignore_defenses_value) and isFloat(self.increase_defenses_value)
                and isFloat(self.resistance_value) and isFloat(self.reduce_resistance_value)):
            # 抽象的if
            self.atk_value = float(self.atk_value)
            self.talent_value = float(self.talent_value) / 100
            self.added_basedamage_value = float(self.added_basedamage_value)
            self.multiply_basedamage_value = float(self.multiply_basedamage_value) / 100

            self.DCI_value = float(self.DCI_value) / 100

            self.db_value = float(self.db_value) / 100

            self.cr_value = float(self.cr_value) / 100
            self.cd_value = float(self.cd_value) / 100

            self.em_value = float(self.em_value)
            # self.elementalchoice_value=1,2,3,4代表水火2火水1.5火冰2冰火1.5
            self.IRC_value = float(self.IRC_value) / 100

            self.person_lever_value = float(self.person_lever_value)
            self.hilichurl_level_value = float(self.hilichurl_level_value)
            self.reduce_defenses_value = float(self.reduce_defenses_value) / 100
            self.ignore_defenses_value = float(self.ignore_defenses_value) / 100
            self.increase_defenses_value = float(self.increase_defenses_value)

            self.resistance_value = float(self.resistance_value) / 100
            self.reduce_resistance_value = float(self.reduce_resistance_value) / 100

            self.damage_expectation = dmg_cal.damagecal_detailedly(atk=self.atk_value, talent=self.talent_value, em=self.em_value,
                                                                   catalyze_verify=self.catalyzeIf_value,
                                                                   damage_catalyze_increased=self.DCI_value,
                                                                   catalyze_type=self.catalyzeType_value,
                                                                   added_basedamage=self.added_basedamage_value,
                                                                   multiply_basedamage=self.multiply_basedamage_value,
                                                                   db_increase=self.db_value,
                                                                   cr=self.cr_value, cd=self.cd_value, cr100=0,
                                                                   elemental_magnification=self.elemental_magnification,
                                                                   increased_reaction_coefficient=self.IRC_value,
                                                                   person_lever=self.person_lever_value,
                                                                   hilichurl_level=self.hilichurl_level_value,
                                                                   reduce_defenses=self.reduce_defenses_value,
                                                                   ignore_defenses=self.ignore_defenses_value,
                                                                   increase_defenses=self.increase_defenses_value,
                                                                   reduce_resistance=self.reduce_resistance_value,
                                                                   resistance=self.resistance_value
                                                                   )
            self.damage_nuclearbomb = dmg_cal.damagecal_detailedly(atk=self.atk_value, talent=self.talent_value, em=self.em_value,
                                                                   catalyze_verify=self.catalyzeIf_value,
                                                                   damage_catalyze_increased=self.DCI_value,
                                                                   catalyze_type=self.catalyzeType_value,
                                                                   added_basedamage=self.added_basedamage_value,
                                                                   multiply_basedamage=self.multiply_basedamage_value,
                                                                   db_increase=self.db_value,
                                                                   cr=self.cr_value, cd=self.cd_value, cr100=1,
                                                                   elemental_magnification=self.elemental_magnification,
                                                                   increased_reaction_coefficient=self.IRC_value,
                                                                   person_lever=self.person_lever_value,
                                                                   hilichurl_level=self.hilichurl_level_value,
                                                                   reduce_defenses=self.reduce_defenses_value,
                                                                   ignore_defenses=self.ignore_defenses_value,
                                                                   increase_defenses=self.increase_defenses_value,
                                                                   reduce_resistance=self.reduce_resistance_value,
                                                                   resistance=self.resistance_value
                                                                   )
            self.show_text_damage.setStyleSheet("color: rgba(238, 0, 0, 1);"
                                                "font-size: 21px;"  # 字体大小
                                                "font-weight: bold;")   # 加粗
            self.show_text_damage.setText(f'期望伤害:{self.damage_expectation}')  # todo 未来考虑再做个append的窗口作为对比
            self.show_text_damage.append(f'暴击伤害:{self.damage_nuclearbomb}')
        else:
            """说明输入有误"""
            self.show_text_damage.setStyleSheet("color: rgba(238, 0, 0, 1);"
                                                "font-size: 21px;"  # 字体大小
                                                "font-weight: bold;")   # 加粗
            self.show_text_damage.setText("WARNING！有笨蛋输入的不是数字")

    def store_data(self):
        """
        存储数据到本地Excel
        """
        # 弹出文件对话框，获取用户选择的文件名
        file_name, _ = QFileDialog.getSaveFileName(self, "数据存储", "主人请修改文件名喵(ฅ≧へ≦)ฅ～.xlsx", "Excel Files (*.xlsx);;All Files (*)")

        if file_name:
            workbook = Workbook()  # 创建一个Excel工作簿
            sheet = workbook.active  # 选择默认的工作表

            # 将提示语写入第一列
            sheet.cell(row=1, column=1, value="攻击力")
            sheet.cell(row=2, column=1, value="天赋倍率")
            sheet.cell(row=3, column=1, value="精通")
            sheet.cell(row=4, column=1, value="是否激化(1激0不激)")
            sheet.cell(row=5, column=1, value="激化反应加成值")
            sheet.cell(row=6, column=1, value="激化反应类型")
            sheet.cell(row=7, column=1, value="基础伤害加成(加算)")
            sheet.cell(row=8, column=1, value="基础伤害加成(乘算)")
            sheet.cell(row=9, column=1, value="所有的增伤的求和结果")
            sheet.cell(row=10, column=1, value="暴击率")
            sheet.cell(row=11, column=1, value="暴击伤害")
            sheet.cell(row=12, column=1, value="反应基础倍率+类型")
            sheet.cell(row=13, column=1, value="反应系数提高")
            sheet.cell(row=14, column=1, value="角色等级")
            sheet.cell(row=15, column=1, value="魔物等级")
            sheet.cell(row=16, column=1, value="降低防御")
            sheet.cell(row=17, column=1, value="无视防御")
            sheet.cell(row=18, column=1, value="增防")
            sheet.cell(row=19, column=1, value="降低敌人抗性")
            sheet.cell(row=20, column=1, value="敌人抗性")

            # 将数据写入Excel文件的第二列
            sheet.cell(row=1, column=2, value=self.atk_value)
            sheet.cell(row=2, column=2, value=self.talent_value)
            sheet.cell(row=3, column=2, value=self.em_value)
            sheet.cell(row=4, column=2, value=self.catalyzeIf_value)
            sheet.cell(row=5, column=2, value=self.DCI_value)
            sheet.cell(row=6, column=2, value=self.catalyzeType_value)
            sheet.cell(row=7, column=2, value=self.added_basedamage_value)
            sheet.cell(row=8, column=2, value=self.multiply_basedamage_value)
            sheet.cell(row=9, column=2, value=self.db_value)
            sheet.cell(row=10, column=2, value=self.cr_value)
            sheet.cell(row=11, column=2, value=self.cd_value)
            sheet.cell(row=12, column=2, value=self.elemental_magnification)
            sheet.cell(row=12, column=3, value=self.elementalchoice_value)  # 这里记录增幅选择对象
            sheet.cell(row=13, column=2, value=self.IRC_value)
            sheet.cell(row=14, column=2, value=self.person_lever_value)
            sheet.cell(row=15, column=2, value=self.hilichurl_level_value)
            sheet.cell(row=16, column=2, value=self.reduce_defenses_value)
            sheet.cell(row=17, column=2, value=self.ignore_defenses_value)
            sheet.cell(row=18, column=2, value=self.increase_defenses_value)
            sheet.cell(row=19, column=2, value=self.reduce_resistance_value)
            sheet.cell(row=20, column=2, value=self.resistance_value)

            # 写入伤害计算
            sheet.cell(row=1, column=4, value="期望伤害")
            sheet.cell(row=2, column=4, value="暴击伤害")
            sheet.cell(row=1, column=5, value=self.damage_expectation)
            sheet.cell(row=2, column=5, value=self.damage_nuclearbomb)
            # 保存Excel文件
            workbook.save(file_name)
            print(f"Data saved to {file_name}")  # 提示保存成功

    def read_data(self):
        """
        从本地Excel数据进行读入
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "数据读取", "主人请选择你之前保存过的Excel文件喵(ฅ≧へ≦)ฅ～", "Excel Files (*.xlsx);;All Files (*)")

        if file_name:
            # 使用openpyxl库读取Excel文件中的数据
            workbook = load_workbook(file_name)
            sheet = workbook.active
            atk_value = sheet.cell(row=1, column=2).value
            talent_value = sheet.cell(row=2, column=2).value
            em_value = sheet.cell(row=3, column=2).value
            catalyzeIf_value = sheet.cell(row=4, column=2).value  # 是否激化
            DCI_value = sheet.cell(row=5, column=2).value
            catalyzeType_value = sheet.cell(row=6, column=2).value  # 激化类型
            added_basedamage_value = sheet.cell(row=7, column=2).value
            multiply_basedamage_value = sheet.cell(row=8, column=2).value
            db_value = sheet.cell(row=9, column=2).value
            cr_value = sheet.cell(row=10, column=2).value
            cd_value = sheet.cell(row=11, column=2).value
            elemental_magnification = sheet.cell(row=12, column=2).value  # 该变量无需使用
            elementalchoice_value = sheet.cell(row=12, column=3).value  # 增幅类型
            IRC_value = sheet.cell(row=13, column=2).value
            person_lever_value = sheet.cell(row=14, column=2).value
            hilichurl_level_value = sheet.cell(row=15, column=2).value
            reduce_defenses_value = sheet.cell(row=16, column=2).value
            ignore_defenses_value = sheet.cell(row=17, column=2).value
            increase_defenses_value = sheet.cell(row=18, column=2).value
            reduce_resistance_value = sheet.cell(row=19, column=2).value
            resistance_value = sheet.cell(row=20, column=2).value

            # 将数据设置到self.input_atk文本框中
            self.input_atk.setText(str(atk_value))
            self.input_talent.setText(str(talent_value * 100))
            self.input_added_basedamage.setText(str(added_basedamage_value))
            self.input_multiply_basedamage.setText(str(multiply_basedamage_value * 100))
            self.input_DCI.setText(str(DCI_value * 100))
            self.input_db.setText(str(db_value * 100))
            self.input_cr.setText(str(cr_value * 100))
            self.input_cd.setText(str(cd_value * 100))
            self.input_em.setText(str(em_value))
            self.input_IRC.setText(str(IRC_value * 100))
            self.input_person_lever.setText(str(person_lever_value))
            self.input_hilichurl_level.setText(str(hilichurl_level_value))
            self.input_reduce_defenses.setText(str(reduce_defenses_value * 100))
            self.input_ignore_defenses.setText(str(ignore_defenses_value * 100))
            self.input_increase_defenses.setText(str(increase_defenses_value))
            self.input_resistance.setText(str(resistance_value * 100))
            self.input_reduce_resistance.setText(str(reduce_resistance_value * 100))

            # 更改按钮的选择
            if int(catalyzeIf_value) == 1:
                self.catalyzeIf_box_btn1.setChecked(True)
                self.catalyzeIf_value = 1
            elif int(catalyzeIf_value) == 0:
                self.catalyzeIf_box_btn2.setChecked(True)
                self.catalyzeIf_value = 0
            if int(catalyzeType_value) == 0:
                self.catalyzeType_box_btn1.setChecked(True)
                self.catalyzeType_value = 0
            elif int(catalyzeType_value) == 1:
                self.catalyzeType_box_btn1.setChecked(True)
                self.catalyzeType_value = 1
            elif int(catalyzeType_value) == 2:
                self.catalyzeType_box_btn1.setChecked(True)
                self.catalyzeType_value = 2
            if int(elementalchoice_value) == 1:
                self.elemental_box_btn1.setChecked(True)
                self.elementalchoice_value = 1
                self.elemental_magnification = 2
            elif int(elementalchoice_value) == 2:
                self.elemental_box_btn2.setChecked(True)
                self.elementalchoice_value = 2
                self.elemental_magnification = 1.5
            elif int(elementalchoice_value) == 3:
                self.elemental_box_btn3.setChecked(True)
                self.elementalchoice_value = 3
                self.elemental_magnification = 1.5
            elif int(elementalchoice_value) == 4:
                self.elemental_box_btn4.setChecked(True)
                self.elementalchoice_value = 4
                self.elemental_magnification = 2

    def elemental_button_click(self):
        """
        四种反应对应的按钮\n
        self.elementalchoice_value=1,2,3,4代表水火2火水1.5火冰2冰火1.5\n
        self.elemental_magnification代表加反应基础倍率的值
        """
        button = self.sender()
        choice_text = button.text()
        if choice_text == "水火蒸发":
            self.elementalchoice_value = 1
            self.elemental_magnification = 2
        elif choice_text == "火水蒸发":
            self.elementalchoice_value = 2
            self.elemental_magnification = 1.5
        elif choice_text == "火冰融化":
            self.elementalchoice_value = 3
            self.elemental_magnification = 1.5
        elif choice_text == "冰火融化":
            self.elementalchoice_value = 4
            self.elemental_magnification = 2
        else:
            self.elementalchoice_value = False
            self.elemental_magnification = 1
        print(self.elementalchoice_value)

    def catalyzeIf_button_click(self):
        """
        是否激化\n
        self.catalyzeIf_value=1,0代表激化/不激化
        """
        button = self.sender()
        choice_text = button.text()
        if choice_text == "激化":
            self.catalyzeIf_value = 1
        elif choice_text == "不激化":
            self.catalyzeIf_value = 0
        else:
            self.catalyzeIf_value = False
        print(self.catalyzeIf_value)

    def catalyzeType_button_click(self):
        """
        激化类型\n
        self.catalyzeType_value = (0:Quicken原激化 1:Aggravate超激化 2:Spread蔓激化)
        """
        button = self.sender()
        choice_text = button.text()
        if choice_text == "原激化":
            self.catalyzeType_value = 0
        elif choice_text == "超激化":
            self.catalyzeType_value = 1
        elif choice_text == "蔓激化":
            self.catalyzeType_value = 2
        else:
            self.catalyzeType_value = False
        print(self.catalyzeType_value)


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
        # 创建赌不赌的输出框
        self.grindArtifact_text = QTextBrowser()
        self.grindArtifact_text.setText("这里会提供一些建议，关于你是否应该赌圣遗物。仅供参考，不代表真实事件😋")
        self.grindArtifact_text.setStyleSheet("color: gray;" "font-size: 21px;")  # 字体大小
        self.grindArtifact_text.setFixedSize(280, 130)
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
        self.layout_H_artifactForecast_btn.addStretch(1)
        self.layout_V_artifactForecast_BtnText.addLayout(self.layout_H_artifactForecast_btn)
        self.layout_V_artifactForecast_BtnText.addWidget(self.grindArtifact_text)

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

        # 整体布局
        self.layout_V_all.addStretch(1)
        self.setLayout(self.layout_V_all)

    def cal_artifactData(self):
        """
        用于读取数据并调用计算圣遗物数据\n
        函数功能：读取UI中新旧圣遗物的数据。仅读取，不计算。计算调用cal_entryData计算词条数，cal_grindProbability计算赌赢的概率\n
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

        """调用词条计算,赌圣遗物"""
        self.cal_entryData()
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
          todo 函数功能：计算赌赢的概率\n
          关联函数：cal_data_button
        """
        self.grindArtifact_text.setText("你干嘛")

    def CurrentLevel1_button_click(self):
        """
        todo 当点击原圣遗物等级选项后，记录其等级
        """
        self.CurrentLevel1_value = 20

    def CurrentLevel2_button_click(self):
        """
        todo 当点击新圣遗物等级选项后，记录其等级
        """
        self.CurrentLevel2_value = 0

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

        container = QHBoxLayout()  # 1. 创建整体的垂直布局器

        widget = QWidget()  # 2. 创建一个要显示具体内容的子Widget
        widget.setLayout(self.stacked_layout)  # 设置为之前定义的抽屉布局
        widget.setStyleSheet("background-color:rgba(253, 230, 224, 0.2);")

        # 3. 创建2个按钮，用来点击进行切换抽屉布局器中的widget
        btn_widget = QWidget()
        btn_layout = QVBoxLayout()
        btn_press1 = QPushButton("主页面")
        btn_press2 = QPushButton("功能2")
        btn_press3 = QPushButton("功能3")
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
