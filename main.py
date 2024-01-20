import os
import numpy as np
import damage_calculator as dc
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter
from sympy import *


# 代码注释中如有与攻略文档冲突的，请以文档为准

fontsimsun12 = FontProperties(fname="input/simsun.ttc", size=12)  # 设置中文字体
fontsimsun20 = FontProperties(fname="input/simsun.ttc", size=20)  # 设置中文字体

# 测试用参数
"""
# 基础面板
atk = 2001.1  # 总攻击力
talent = 0.5904  # 技能倍率
em = 0  # 元素精通
cr = 1  # 暴击率。如果设为1则表示计算的是暴击的了伤害
cd = 1.7048  # 暴击伤害
# AE 基础伤害
catalyze_verify = False  # 不激化
damage_boost_increased = 0  # 圣遗物中的激化伤害提升提高为0
# DB 增伤
elemental_increase = 1.074  # 元素/物理伤害加成：突破0.288 + 火伤杯0.466 + 精一四风满层0.32
influence_increase = 0  # 对元素影响下的敌人伤害提高：渡火35%
artifact_increase = 0.30  # (圣遗物)造成伤害提高：0.15 + 0.075*n (n为10s内释放E的次数,n<=3),这里算扔2个蹦蹦
skill_increase = 0  # 元素爆发/元素战技/普攻/重击伤害提高：1/2的几率金花50%
# ER 增幅
elemental_magnification = 1.5  # 火水蒸发1.5
increased_reaction_coefficient = 0.15  # 反应系数提高：四魔女给蒸发增伤15%
# DF 防御
person_lever = 90  # 角色等级
hilichurl_level = 87  # 魔物等级
reduce_defenses = 0  # 减防
ignore_defenses = 0  # 无视防御
increase_defenses = 0  # 怪物自身增防
# RT 抗性
reduce_resistance = 0  # 减抗
resistance = 0.1  # 默认魔物抗性
"""

"""
AE = dc.AE_cal()
DB = dc.DB_cal()
CD = dc.CD_cal()
ER = dc.ER_cal()
DF = dc.DF_cal()
RT = dc.RT_cal()

damage = dc.damage_cal(AE, DB, CD, ER, DF, RT)

print("基础伤害区+激化加成值：{:.3f}".format(AE))
print("增伤区：{:.2f}%".format(DB * 100))
print("双暴区：{:.2f}%".format(CD * 100))
print("增幅区：{:.2f}".format(ER))
print("防御区：{:.2f}".format(DF))
print("抗性区：{:.2f}".format(RT))

print("☆☆☆ 伤害 ☆☆☆ ：{:.3f}".format(damage))
"""

"""纳西妲"""
"""
倍率：
A10: 2.376atk
E10: 1.8576atk+3.7152em
E13: 2.193atk+4.386em
Q10: 火1/火2伤害提升0.2678 / 0.4018  雷1/雷2间隔降低0.45s / 0.67s  水1/水2持续延长6.02s / 9.03s
Q13: 火1/火2伤害提升0.3162 / 0.4743  雷1/雷2间隔降低0.53s / 0.79s  水1/水2持续延长7.11s / 10.66s

基础: 298.97atk
突破:  115.2em
天赋1：依据队伍em最高角色的0.25em，提高领域内场上角色精通至多250
天赋2：基于em-200,E增伤0.001，暴击率0.0003。至多0.8增伤，0.24暴击率

命座：
C1: Q额外计入火雷水角色各一名
C2: 燃烧绽放超绽放烈绽放双暴20-100。原激化超激化蔓激化8s内防御力降低30%
C3: E+3
C4: E下敌人数量1,2,3,4时纳西妲em+100/120/140/160
C5: Q+3
C6: Q后纳西妲a/z命中E下的敌人，释放灭净三业·业障除(2atk+4em)，视为E伤害，0.2s至多一次，至多持续10s，6次后移除。

武器：
千夜：atk542 em265   每个元素相同为装备者+32/40/48/56/64em，每个元素不同为装备者+0.1/0.14/0.18/0.22/0.26元素伤害  为队伍角色em+40/42/44/46/48
神乐: atk608 cd0.662  E后E伤害+0.12/0.15/0.18/0.21/0.24(至多16s至多3层)，3层时+0.12/0.15/0.18/0.21/0.24全元素伤害加成
祭礼: atk454 em221   E造成伤害40/50/60/70/80%概率重置E，每30/26/22/19/16s至多1次
流浪乐章: atk510 cd0.551 宣叙调atk+60/75/90/105/120%  咏叹调全元素伤害+48/60/72/84/96%  间奏曲em+240/300/360/420/480
"""

"""1.精通、双暴、伤害加成收益曲线"""
# Part1 精通
# 谈精通收益曲线，必须先确定其他可变变量，由于纳西妲的天赋2，使得精通和暴击率&增伤挂钩，因此只有当明确暴击率&增伤后，才能谈论精通的曲线
# 假设固定草伤杯，圣遗物前四件都是6词条双暴，最后一件是带4词条双暴，圣遗物双暴为(5*2+50 + 6*4*6.6+62.2+4*6.6) = 307%
# 记纳西妲的精通为Nahida_em_ForQ1，双暴为Nahida_CRIT_ForQ1 = Nahida_cr_ForQ1 + Nahida_cd_ForQ1，增伤为Nahida_DB_ForQ1
# 按照我们上面的假设，Nahida_CRIT_ForQ1 = 3.07, Nahida_DB_ForQ1=0.466
# 问题转化为，对于某个精通值Nahida_em_ForQ1，计算更新后的Nahida_CRIT_ForQ1与Nahida_DB_ForQ1，并为 Nahida_cr_ForQ1和Nahida_cd_ForQ1自动配平
# 然后以最初的精通为标准，计算其比值
# (不考虑圣遗物套装附加的元素伤害值)
class Nahida_em_Q1:
    def __init__(self, Nahida_atkIncrease_forQ1, Nahida_emIncrease_ForQ1, Nahida_CRITIncrease_forQ1, Nahida_DBIncrease_forQ1, ax):
        self.Nahida_atk_forQ1 = 298.97  # 基础攻击力
        self.Nahida_atk_forQ1 += Nahida_atkIncrease_forQ1 + 310.8  # 武器和羽毛
        self.Nahida_em_ForQ1 = 115.2 + Nahida_emIncrease_ForQ1 + 186.5  # 带精通沙
        self.Nahida_CRIT_ForQ1_init = 3.07 + Nahida_CRITIncrease_forQ1
        self.Nahida_DB_ForQ1_init = 0.466 + Nahida_DBIncrease_forQ1
        self.draw_em_Q1(ax)

    def draw_em_Q1(self, ax):
        """绘制精通收益曲线"""
        self.x = np.arange(self.Nahida_em_ForQ1, 1200, 1)
        self.calx_em_Q1()
        self.caly_em_Q1()
        ax.scatter(self.x[1:], self.y_quarter_on_quarter)  # x-->精通, y-->环比
        ax.set_xlabel('纳西妲当前总精通值', fontproperties=fontsimsun12)
        ax.set_ylabel('环比', fontproperties=fontsimsun12)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x:.3%}'))  # 使用匿名函数设置y轴的百分比格式

    def calx_em_Q1(self):
        """
        依据传入的精通x,Nahida_CRIT_ForQ1_init, Nahida_DB_ForQ1_init
        计算Nahida_base_forQ1, Nahida_CRIT_ForQ1, Nahida_DB_ForQ1
        """
        self.Nahida_base_forQ1 = 2.193 * self.Nahida_atk_forQ1 + 4.386 * self.x  # 因为dc里没写双倍率，因此这里先算出来，然后天赋设为1即可
        # 基于em-200,E增伤0.001，暴击率0.0003。至多0.8增伤，0.24暴击率
        self.Nahida_CRIT_ForQ1 = np.full_like(self.x, fill_value=self.Nahida_CRIT_ForQ1_init)  # 基础双暴
        self.Nahida_DB_ForQ1 = np.full_like(self.x, fill_value=self.Nahida_DB_ForQ1_init)  # 草伤
        self.Nahida_CRIT_ForQ1 += [0.0003 * 2 * (x1 - 200) if x1 < 1000 else 0.48 for x1 in self.x]  # 双暴
        self.Nahida_DB_ForQ1 += [0.001 * (x1 - 200) if x1 < 1000 else 0.8 for x1 in self.x]  # 增伤

    def caly_em_Q1(self):
        """依据传入的x,基础乘区值,双暴值,增伤值得到y值"""
        self.y_AE = dc.AE_cal(atk=self.Nahida_base_forQ1, talent=1, em=self.x, catalyze_verify=1, catalyze_type=2)
        # 暴击率>100%时，剩余的全部分配给暴伤
        # 暴击率<=100%时，双暴按1:2分配，而1%暴击率词条相当于2%暴伤词条，所以暴击占1/4，暴伤占1/2
        self.y_CD = np.where(self.Nahida_CRIT_ForQ1 / 4 > 1,
                             dc.CD_cal(cr=1, cd=self.Nahida_CRIT_ForQ1 - 2),
                             dc.CD_cal(cr=self.Nahida_CRIT_ForQ1 / 4, cd=self.Nahida_CRIT_ForQ1 / 2))
        self.y_DB = dc.DB_cal(artifact_increase=self.Nahida_DB_ForQ1)  # 增伤(选择artifact_increase是为了覆盖DB_cal里的init值)
        # y坐标轴--->伤害环比
        self.y_base = self.y_AE[0] * self.y_CD[0] * self.y_DB[0]
        self.y_actual = self.y_AE * self.y_CD * self.y_DB
        self.y_compare_initial = self.y_actual / self.y_base
        self.y_quarter_on_quarter = np.array([(self.y_actual[i + 1] - self.y_actual[i]) / self.y_actual[i]
                                              for i in range(len(self.x) - 1)])
        # 因为第一个点没有环比，就去除了
        # print(self.y_AE[-20:])
        # print(self.y_CD[-20:])
        # print(self.y_DB[-20:])
        # print(self.y_actual[-20:])
        # print(self.y_quarter_on_quarter[-20:])

def draw_Nahida_em_Q1(title, set_xylim1=False, set_xylim2=False):
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    plt.subplots_adjust(top=0.905, bottom=0.1, left=0.09, right=0.955, hspace=0.355, wspace=0.275)

    Nahida_em_Q1_AThousandFloatingDreams = Nahida_em_Q1(Nahida_atkIncrease_forQ1=542, Nahida_emIncrease_ForQ1=265,
                                                        Nahida_CRITIncrease_forQ1=0, Nahida_DBIncrease_forQ1=0.2,
                                                        ax=axs[0, 0])
    axs[0, 0].set_title('精一千夜精通收益曲线(2层增伤)', fontproperties=fontsimsun12)
    if set_xylim1:
        axs[0, 0].set_xlim(600, 1000)
        axs[0, 0].set_ylim(0.0006, 0.0020)
    if set_xylim2:
        axs[0, 0].set_xlim(1000, 1200)
        axs[0, 0].set_ylim(0.0004, 0.0006)

    Nahida_em_Q1_KagurasVerity = Nahida_em_Q1(Nahida_atkIncrease_forQ1=608, Nahida_emIncrease_ForQ1=0,
                                              Nahida_CRITIncrease_forQ1=0.662, Nahida_DBIncrease_forQ1=0.48,
                                              ax=axs[0, 1])
    axs[0, 1].set_title('精一神乐精通收益曲线(满层增伤)', fontproperties=fontsimsun12)
    if set_xylim1:
        axs[0, 1].set_xlim(600, 1000)
        axs[0, 1].set_ylim(0.0006, 0.0020)
    if set_xylim2:
        axs[0, 1].set_xlim(1000, 1200)
        axs[0, 1].set_ylim(0.0004, 0.0006)
    # axs[0, 2].axis('off')  # Turn off the axes to leave it blank

    Nahida_em_Q1_TEMP = Nahida_em_Q1(Nahida_atkIncrease_forQ1=542, Nahida_emIncrease_ForQ1=80.04,
                                     Nahida_CRITIncrease_forQ1=0.882, Nahida_DBIncrease_forQ1=0.2,
                                     ax=axs[0, 2])
    axs[0, 2].set_title('对比组(若水法器)精通收益曲线', fontproperties=fontsimsun12)
    if set_xylim1:
        axs[0, 2].set_xlim(600, 1000)
        axs[0, 2].set_ylim(0.0006, 0.0020)
    if set_xylim2:
        axs[0, 2].set_xlim(1000, 1200)
        axs[0, 2].set_ylim(0.0004, 0.0006)

    Nahida_em_Q1_SacrificialFragments = Nahida_em_Q1(Nahida_atkIncrease_forQ1=454, Nahida_emIncrease_ForQ1=221,
                                                     Nahida_CRITIncrease_forQ1=0, Nahida_DBIncrease_forQ1=0,
                                                     ax=axs[1, 0])
    axs[1, 0].set_title('祭礼精通收益曲线', fontproperties=fontsimsun12)
    if set_xylim1:
        axs[1, 0].set_xlim(600, 1000)
        axs[1, 0].set_ylim(0.0006, 0.0020)
    if set_xylim2:
        axs[1, 0].set_xlim(1000, 1200)
        axs[1, 0].set_ylim(0.0004, 0.0006)

    Nahida_em_Q1_TheWidsith_DB = Nahida_em_Q1(Nahida_atkIncrease_forQ1=510, Nahida_emIncrease_ForQ1=0,
                                              Nahida_CRITIncrease_forQ1=0.551, Nahida_DBIncrease_forQ1=0.96,
                                              ax=axs[1, 1])
    axs[1, 1].set_title('精五流浪乐章精通收益曲线(增伤)', fontproperties=fontsimsun12)
    if set_xylim1:
        axs[1, 1].set_xlim(600, 1000)
        axs[1, 1].set_ylim(0.0006, 0.0020)
    if set_xylim2:
        axs[1, 1].set_xlim(1000, 1200)
        axs[1, 1].set_ylim(0.0004, 0.0006)

    Nahida_em_Q1_TheWidsith_EM = Nahida_em_Q1(Nahida_atkIncrease_forQ1=510, Nahida_emIncrease_ForQ1=480,
                                              Nahida_CRITIncrease_forQ1=0.551, Nahida_DBIncrease_forQ1=0,
                                              ax=axs[1, 2])
    axs[1, 2].set_title('精五流浪乐章精通收益曲线(精通)', fontproperties=fontsimsun12)
    if set_xylim1:
        axs[1, 2].set_xlim(600, 1000)
        axs[1, 2].set_ylim(0.0006, 0.0020)
    if set_xylim2:
        axs[1, 2].set_xlim(1000, 1200)
        axs[1, 2].set_ylim(0.0004, 0.0006)
    fig.suptitle('初始精通沙+突破精通+武器精通，每1精通对伤害的提升值', fontproperties=fontsimsun20)
    os.makedirs('output/纳西妲攻略图片/Q1/', exist_ok=True)
    plt.savefig(f'output/纳西妲攻略图片/Q1/{title}.png')
    # plt.show()

draw_Nahida_em_Q1(title="纳西妲精通收益曲线(全图)")
draw_Nahida_em_Q1(set_xylim1=True, title="纳西妲精通收益曲线(600-1000)")
draw_Nahida_em_Q1(set_xylim2=True, title="纳西妲精通收益曲线(1000-1200)")


# Part2 双暴
# 实战精通肯定大于1000，天赋2吃满，是0.24暴击率
# 因此这里Nahida_em_ForQ1=1000，Nahida_CRIT_ForQ1 = x轴, Nahida_DB_ForQ1=0.466
# 由于双暴乘区不需要考虑基础区和增伤区，因此直接开算就行
# 也就是在纳西妲在装备此武器时的初始双暴下，计算圣遗物副词条双暴的环比

class Nahida_CRIT_Q1:
    def __init__(self, Nahida_CRITIncrease_forQ1, ax):
        self.Nahida_CRIT_ForQ1 = 0.622+0.24*2 + Nahida_CRITIncrease_forQ1  # 暴伤头+天赋
        self.draw_CRIT_Q1(ax)

    def draw_CRIT_Q1(self, ax):
        """绘制双暴收益曲线"""
        self.x = np.arange(0, 28, 1)
        self.Nahida_CRIT_ForQ1 = np.array(self.Nahida_CRIT_ForQ1 + self.x*0.066)
        self.caly_CRIT_Q1()
        ax.scatter(self.x[1:], self.y_quarter_on_quarter)  # x-->双暴词条数, y-->环比
        ax.set_xlabel('圣遗物双暴词条数', fontproperties=fontsimsun12)
        ax.set_ylabel('环比', fontproperties=fontsimsun12)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x:.3%}'))  # 使用匿名函数设置y轴的百分比格式

    def caly_CRIT_Q1(self):
        """依据传入的双暴值得到y值"""
        # 暴击率>100%时，剩余的全部分配给暴伤
        # 暴击率<=100%时，双暴按1:2分配，而1%暴击率词条相当于2%暴伤词条，所以暴击占1/4，暴伤占1/2
        self.y_CD = np.where(self.Nahida_CRIT_ForQ1 / 4 > 1,
                             dc.CD_cal(cr=1, cd=self.Nahida_CRIT_ForQ1 - 2),
                             dc.CD_cal(cr=self.Nahida_CRIT_ForQ1 / 4, cd=self.Nahida_CRIT_ForQ1 / 2))
        # y坐标轴--->伤害环比
        self.y_base = self.y_CD[0]
        print(self.y_CD)
        self.y_actual = self.y_CD
        self.y_compare_initial = self.y_actual / self.y_base
        self.y_quarter_on_quarter = np.array([(self.y_actual[i + 1] - self.y_actual[i]) / self.y_actual[i]
                                              for i in range(len(self.x) - 1)])

def draw_Nahida_CRTI_Q1():
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    plt.subplots_adjust(top=0.905, bottom=0.09, left=0.085, right=0.955, hspace=0.315, wspace=0.27)

    Nahida_CRIT_Q1_0 = Nahida_CRIT_Q1(Nahida_CRITIncrease_forQ1=0, ax=axs[0, 0])
    axs[0, 0].set_title('武器0双暴分(千夜)', fontproperties=fontsimsun12)
    Nahida_CRIT_Q1_0551 = Nahida_CRIT_Q1(Nahida_CRITIncrease_forQ1=0.442, ax=axs[0, 1])
    axs[0, 1].set_title('武器44.2%双暴分(金流)', fontproperties=fontsimsun12)
    Nahida_CRIT_Q1_0551 = Nahida_CRIT_Q1(Nahida_CRITIncrease_forQ1=0.551, ax=axs[0, 2])
    axs[0, 2].set_title('武器55.1%双暴分(流浪乐章)', fontproperties=fontsimsun12)
    Nahida_CRIT_Q1_0662 = Nahida_CRIT_Q1(Nahida_CRITIncrease_forQ1=0.662, ax=axs[1, 0])
    axs[1, 0].set_title('武器66.2%双暴分(四风、神乐)', fontproperties=fontsimsun12)
    Nahida_CRIT_Q1_0882 = Nahida_CRIT_Q1(Nahida_CRITIncrease_forQ1=0.882, ax=axs[1, 1])
    axs[1, 1].set_title('武器88.2%双暴分(万世)', fontproperties=fontsimsun12)
    axs[1, 2].axis('off')  # Turn off the axes to leave it blank
    fig.suptitle('初始24%天赋暴击率+爆伤头+武器双暴，每1词条双暴对伤害的提升值', fontproperties=fontsimsun20)
    os.makedirs('output/纳西妲攻略图片/Q1/', exist_ok=True)
    plt.savefig('output/纳西妲攻略图片/Q1/纳西妲双暴曲线.png')
    # plt.show()

draw_Nahida_CRTI_Q1()


# Part3 增伤
# 依旧让精通大于1000，天赋2吃满，是0.8增伤。双暴按之前假定的28双暴词条(虽然对此问没啥用)
# 因此这里Nahida_em_ForQ1=1000，Nahida_CRIT_ForQ1 = 3.07, Nahida_DB_ForQ1=x轴
# 也就是在纳西妲在草伤杯下，计算草伤的环比
# 因为草伤没有特别普世的增加方式，用词条数或者直接每次+1%都不太符合使用逻辑，因此这里依据合适的坐标尺度，选择的是5%
class Nahida_DB_Q1:
    def __init__(self, Nahida_DBIncrease_forQ1, ax):
        self.Nahida_DB_ForQ1 = 0.466 + Nahida_DBIncrease_forQ1  # 草伤杯+额外提供的草伤
        self.draw_DB_Q1(ax)

    def draw_DB_Q1(self, ax):
        """绘制草伤收益曲线"""
        self.x = np.arange(self.Nahida_DB_ForQ1, 4, 0.05)  # 草伤
        self.caly_DB_Q1()
        ax.scatter(self.x[1:], self.y_quarter_on_quarter)  # x-->草伤, y-->环比
        ax.set_xlabel('当前草伤值', fontproperties=fontsimsun12)
        ax.set_ylabel('环比', fontproperties=fontsimsun12)
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x:.0%}'))  # 使用匿名函数设置x轴的百分比格式
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x:.2%}'))  # 使用匿名函数设置y轴的百分比格式

    def caly_DB_Q1(self):
        """依据传入的草伤值得到y值"""
        self.y_DB = dc.DB_cal(artifact_increase=self.x)  # 增伤
        # y坐标轴--->伤害环比
        self.y_base = self.y_DB[0]
        print(self.y_DB)
        self.y_actual = self.y_DB
        self.y_compare_initial = self.y_actual / self.y_base
        self.y_quarter_on_quarter = np.array([(self.y_actual[i + 1] - self.y_actual[i]) / self.y_actual[i]
                                              for i in range(len(self.x) - 1)])

def draw_Nahida_DB_Q1():
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    plt.subplots_adjust(top=0.905, bottom=0.1, left=0.09, right=0.965, hspace=0.325, wspace=0.275)

    Nahida_DB_Q1_0 = Nahida_DB_Q1(Nahida_DBIncrease_forQ1=0, ax=axs[0, 0])
    axs[0, 0].set_title('0%草伤(祭礼)', fontproperties=fontsimsun12)
    Nahida_DB_Q1_15 = Nahida_DB_Q1(Nahida_DBIncrease_forQ1=0.15, ax=axs[0, 1])
    axs[0, 1].set_title('15%草伤(深林2)', fontproperties=fontsimsun12)
    Nahida_DB_Q1_20 = Nahida_DB_Q1(Nahida_DBIncrease_forQ1=0.2, ax=axs[0, 2])
    axs[0, 2].set_title('20%草伤(剧团2，精一千夜2层)', fontproperties=fontsimsun12)
    Nahida_DB_Q1_48 = Nahida_DB_Q1(Nahida_DBIncrease_forQ1=0.48, ax=axs[1, 0])
    axs[1, 0].set_title('48%草伤(精一神乐3层)', fontproperties=fontsimsun12)
    Nahida_DB_Q1_96 = Nahida_DB_Q1(Nahida_DBIncrease_forQ1=0.96, ax=axs[1, 1])
    axs[1, 1].set_title('96%草伤(精五流浪乐章增伤)', fontproperties=fontsimsun12)
    axs[1, 2].axis('off')  # Turn off the axes to leave it blank
    fig.suptitle('初始草伤杯46.6%草伤，每5%草伤对伤害的提升值', fontproperties=fontsimsun20)
    os.makedirs('output/纳西妲攻略图片/Q1/', exist_ok=True)
    plt.savefig('output/纳西妲攻略图片/Q1/纳西妲草伤曲线.png')
    # plt.show()

draw_Nahida_DB_Q1()


"""2.攻击力到底有多少作用？"""
# 纳西妲298.97atk，羽毛310.8   武器白值：千夜：atk542  神乐: atk608  祭礼: atk454  流浪乐章: atk510
# 1词条ATK4.95% atk16.54
# 与攻击力相关的是E13: 2.193atk+4.386em，以及基础乘区也和攻击力挂钩。
# 这里我们考虑将攻击力和精通对比一下，来判断攻击力的作用的大小
# 如果和Q1里算精通一样的话，会出现问题，讨论精通的时候直接当做圣遗物副词条里没有攻击力
# 而在此时，纳西妲不可能不要精通，因此此时的攻击力环比应该是在某一精通值下，如果不这样的话就是三维图了。
class Nahida_atk_Q2:
    def __init__(self, Nahida_em_Q2, Nahida_Weapon_whiteATK_Q2, ax):
        self.Nahida_whiteATK_Q2 = 298.97 + Nahida_Weapon_whiteATK_Q2
        self.Nahida_em_Q2 = Nahida_em_Q2
        self.draw_atk_Q2(ax)

    def draw_atk_Q2(self, ax):
        """绘制精通收益曲线"""
        self.x = np.arange(0, 10, 1)  # 攻击力词条数
        self.Nahida_atk_forQ2 = self.Nahida_whiteATK_Q2 * (1 + 0.0495*self.x) + 310.8
        self.calx_atk_Q2()
        self.caly_atk_Q2()
        ax.scatter(self.x[1:], self.y_quarter_on_quarter)  # x-->攻击力词条数, y-->环比
        ax.set_xlabel('圣遗物副词条的攻击力词条数', fontproperties=fontsimsun12)
        ax.set_ylabel('环比', fontproperties=fontsimsun12)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x:.3%}'))  # 使用匿名函数设置y轴的百分比格式

    def calx_atk_Q2(self):
        """依据传入的精通和攻击力计算Nahida_base_forQ1"""
        self.Nahida_base_forQ2 = 2.193 * self.Nahida_atk_forQ2 + 4.386 * self.Nahida_em_Q2  # 因为dc里没写双倍率，因此这里先算出来，然后天赋设为1即可

    def caly_atk_Q2(self):
        """依据传入的x,基础乘区值,双暴值,增伤值得到y值"""
        self.y_AE = dc.AE_cal(atk=self.Nahida_base_forQ2, talent=1, em=self.Nahida_em_Q2, catalyze_verify=1, catalyze_type=2)
        # y坐标轴--->伤害环比
        self.y_base = self.y_AE[0]
        self.y_actual = self.y_AE
        self.y_compare_initial = self.y_actual / self.y_base
        self.y_quarter_on_quarter = np.array([(self.y_actual[i + 1] - self.y_actual[i]) / self.y_actual[i]
                                              for i in range(len(self.x) - 1)])

def draw_Nahida_atk_Q2(Nahida_em_Q2=1000):
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    plt.subplots_adjust(top=0.905, bottom=0.1, left=0.09, right=0.965, hspace=0.325, wspace=0.275)
    Nahida_atk_Q2_454 = Nahida_atk_Q2(Nahida_em_Q2=Nahida_em_Q2, Nahida_Weapon_whiteATK_Q2=454, ax=axs[0, 0])
    axs[0, 0].set_title('454白值(祭礼)', fontproperties=fontsimsun12)
    Nahida_DB_Q1_510 = Nahida_atk_Q2(Nahida_em_Q2=Nahida_em_Q2, Nahida_Weapon_whiteATK_Q2=510, ax=axs[0, 1])
    axs[0, 1].set_title('510白值(流浪乐章)', fontproperties=fontsimsun12)
    Nahida_DB_Q1_545 = Nahida_atk_Q2(Nahida_em_Q2=Nahida_em_Q2, Nahida_Weapon_whiteATK_Q2=545, ax=axs[1, 0])
    axs[1, 0].set_title('545白值(千夜、万世)', fontproperties=fontsimsun12)
    Nahida_DB_Q1_608 = Nahida_atk_Q2(Nahida_em_Q2=Nahida_em_Q2, Nahida_Weapon_whiteATK_Q2=608, ax=axs[1, 1])
    axs[1, 1].set_title('608白值(神乐)', fontproperties=fontsimsun12)
    fig.suptitle(f'在{Nahida_em_Q2}精通下，不同武器白值，圣遗物每1词条大攻击对伤害的提升值', fontproperties=fontsimsun20)
    os.makedirs('output/纳西妲攻略图片/Q2/', exist_ok=True)
    plt.savefig(f'output/纳西妲攻略图片/Q2/纳西妲攻击力曲线-{Nahida_em_Q2}精通.png')
    # plt.show()

draw_Nahida_atk_Q2(Nahida_em_Q2=800)
draw_Nahida_atk_Q2(Nahida_em_Q2=1000)
draw_Nahida_atk_Q2(Nahida_em_Q2=1200)
draw_Nahida_atk_Q2(Nahida_em_Q2=1400)


"""3.深林4还是饰金4还是剧团4还是2+2？"""
# 这些圣遗物是什么？其实就是单纯的数值
# Deepwood Memories 深林4 15%草伤30%减抗(但减抗可以用辅助带草四)
# Gilded Dreams 饰金4 80EM 每名同类ATK+14%,不同类EM+50
# Golden Troupe 剧团4 20+25%E+(25%E在开大后稳定吃不到,除非切人的麻烦操作)
# 2+2 以前是2草2精通，现在出了剧团比深林高，那就2剧团2精通
# 因此因为深林比剧团弱5%，这里就不考虑了
# 在谈论圣遗物的时候到底应该谈论什么？如果我有一套圣遗物，词条不变，换成另一个套装的圣遗物会怎样？
# 因此，圣遗物应该是基于现有面板下的讨论。也就是这个圣遗物能带给我多少收益，其实还是一个比率。
# 按照之前的结论，千精并全叠双暴。因此这里面板还是采用1000精通，298.97 + 542 + 310.8 = 1151.77攻击力(840.97白字)，
# 28词条双暴(5 * 2 + 50 + 28 * 6.6 + 62.2 + 24 * 2) = 355.0%，相当于88.75%-177.5%双暴
# 增伤草伤杯46.6+千夜两层(0.1/0.14/0.18/0.22/0.26)*2
# and暂时先只写千夜的
Nahida_ATK_Q3 = 1151.77
Nahida_ATKW_Q3 = 840.97  # 840.97白字
Nahida_CR_Q3 = 0.8875
Nahida_CD_Q3 = 1.775
Nahida_DB1_Q3 = 0.466 + 0.2 + 0.8 + 0.4018  # 精一千夜2层+天赋2+Q火1层
Nahida_DB5_Q3 = 0.466 + 0.52 + 0.8 + 0.4018  # 精五千夜2层+天赋2+Q火1层
# 精一千夜2层
damage_NoArtifact = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                    dc.DB_cal(artifact_increase=Nahida_DB1_Q3)
damage_Deepwood_Memories = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                           dc.DB_cal(artifact_increase=Nahida_DB1_Q3+0.15)
damage_Gilded_Dreams = dc.AE_cal(atk=Nahida_ATK_Q3 + 0.28*Nahida_ATKW_Q3, em=1000+130) * \
                       dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * dc.DB_cal(artifact_increase=Nahida_DB1_Q3)
damage_Golden_Troupe = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                       dc.DB_cal(artifact_increase=Nahida_DB1_Q3+0.45)
damage_2and2_Golden = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000+80) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                       dc.DB_cal(artifact_increase=Nahida_DB1_Q3+0.2)
damage_2and2_Deepwood = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000+80) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                       dc.DB_cal(artifact_increase=Nahida_DB1_Q3+0.15)
# 67808.57314868286 71355.293970324 74766.98635538477 78448.73561360624 73904.87024352727 72700.34468378533
print(damage_NoArtifact, damage_Deepwood_Memories, damage_Gilded_Dreams, damage_Golden_Troupe, damage_2and2_Golden, damage_2and2_Deepwood)
# 1.0 1.052304902712881 1.102618487362126 1.1569147081386428 1.0899045181422289 1.0721409005963944
print(damage_NoArtifact/damage_NoArtifact, damage_Deepwood_Memories/damage_NoArtifact,
      damage_Gilded_Dreams/damage_NoArtifact, damage_Golden_Troupe/damage_NoArtifact,
      damage_2and2_Golden/damage_NoArtifact, damage_2and2_Deepwood/damage_NoArtifact)

# 精五千夜2层
damage_NoArtifact = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                    dc.DB_cal(artifact_increase=Nahida_DB5_Q3)
damage_Deepwood_Memories = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                           dc.DB_cal(artifact_increase=Nahida_DB5_Q3+0.15)
damage_Gilded_Dreams = dc.AE_cal(atk=Nahida_ATK_Q3 + 0.28*Nahida_ATKW_Q3, em=1000+130) * \
                       dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * dc.DB_cal(artifact_increase=Nahida_DB5_Q3)
damage_Golden_Troupe = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                       dc.DB_cal(artifact_increase=Nahida_DB5_Q3+0.45)
damage_2and2_Golden = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000+80) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                       dc.DB_cal(artifact_increase=Nahida_DB5_Q3+0.2)
damage_2and2_Deepwood = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000+80) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3) * \
                       dc.DB_cal(artifact_increase=Nahida_DB5_Q3+0.15)
# 75374.91090151727 78921.6317231584 83109.77024328601 86015.07336644067 81613.83382587579 80409.30826613383
print(damage_NoArtifact, damage_Deepwood_Memories, damage_Gilded_Dreams, damage_Golden_Troupe, damage_2and2_Golden, damage_2and2_Deepwood)
# 1.0 1.0470543948804818 1.102618487362126 1.1411631846414456 1.082771877933098 1.066791420439546
print(damage_NoArtifact/damage_NoArtifact, damage_Deepwood_Memories/damage_NoArtifact,
      damage_Gilded_Dreams/damage_NoArtifact, damage_Golden_Troupe/damage_NoArtifact,
      damage_2and2_Golden/damage_NoArtifact, damage_2and2_Deepwood/damage_NoArtifact)

# 精五千夜，赌狗赌到增伤，带剧团4和饰金的区别
damage_Gilded_Dreams = dc.AE_cal(atk=Nahida_ATK_Q3 + 0.28*Nahida_ATKW_Q3, em=1000+130) * \
                       dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3+0.551) * dc.DB_cal(artifact_increase=Nahida_DB5_Q3+0.96)
damage_Golden_Troupe = dc.AE_cal(atk=Nahida_ATK_Q3, em=1000) * dc.CD_cal(cr=Nahida_CR_Q3, cd=Nahida_CD_Q3+0.551) * \
                       dc.DB_cal(artifact_increase=Nahida_DB5_Q3+0.96+0.45)
print(damage_Gilded_Dreams, damage_Golden_Troupe, damage_Golden_Troupe / damage_Gilded_Dreams)


"""4.纳西妲自身在42词条下的极限面板"""
# 前面一直讨论28词条双暴，这里则仔细讨论比较好的42词条圣遗物应该如何分配这42个词条。
# 设精通，双暴词条数分别为a,b，则b=42-a
a = symbols('a', real=True)
em = 1048.7 + 19.81 * a
talent = 2 * 1151.77 + 4 * em
cat_add = 1446.853458 * 1.25 * (5 * em) / (em + 1200)
AE = talent + cat_add
DB = 3.3178
CD = 1 + ((1.702 + 0.066 * (42 - a)) ** 2) / 8
DF = 190/330
RT = 0.9
# damage_a = AE * CD
damage_a = AE * DB * CD * DF * RT
damage_a = expand(damage_a)
print("damage", damage_a)
print("damage", expand(damage_a))
fa_a = damage_a.diff(a)  # 对a求偏导数
print("fa", fa_a)
print("fa", expand(fa_a))
minimization_points = solve(fa_a, a)  # 求解方程
print(minimization_points)
expr1 = damage_a
expr2 = fa_a


def draw_expr(expr, title, filename):
    fig = plt.figure()
    # 将 SymPy 表达式转换为可在 matplotlib 中使用的函数
    expr_func = lambdify(a, expr, 'numpy')
    # 生成数据点
    a_values = np.linspace(0, 42, 1000)
    # 计算表达式的值
    expr_values = expr_func(a_values)
    plt.plot(a_values, expr_values)
    plt.xlabel('a')
    plt.ylabel('Expression Value')
    plt.title(f'Expression:{title}')
    plt.grid(True)
    os.makedirs('output/纳西妲攻略图片/Q4/', exist_ok=True)
    plt.savefig(f'output/纳西妲攻略图片/Q4/纳西妲{filename}函数图像.png')


draw_expr(expr1, r'$\text{DMG}$', "伤害[0,42]")
draw_expr(expr2, r'$\frac{\partial DMG}{\partial a}$', "伤害偏导[0,42]")

# 满命42词条业障除激化伤害
damage_42expectation1 = dc.AE_cal(atk=1151.77*2+1048.7*4, talent=1, em=1048.7) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0)
damage_42expectation2 = dc.AE_cal(atk=1151.77*2+1048.7*4, talent=1, em=1048.7) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0.3)
print(damage_42expectation1, damage_42expectation2)
# 满命42词条13E激化伤害
damage_42expectation1 = dc.AE_cal(atk=1151.77*2.193+1048.7*4.386, talent=1, em=1048.7) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0)
damage_42expectation2 = dc.AE_cal(atk=1151.77*2.193+1048.7*4.386, talent=1, em=1048.7) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0.3)
print(damage_42expectation1, damage_42expectation2)
# 满命42词条业障除不激化伤害
damage_42expectation1 = dc.AE_cal(atk=1151.77*2+1048.7*4, talent=1, em=1048.7, catalyze_verify=0) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0)
damage_42expectation2 = dc.AE_cal(atk=1151.77*2+1048.7*4, talent=1, em=1048.7, catalyze_verify=0) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0.3)
print(damage_42expectation1, damage_42expectation2)
# 满命42词条13E不激化伤害
damage_42expectation1 = dc.AE_cal(atk=1151.77*2.193+1048.7*4.386, talent=1, em=1048.7, catalyze_verify=0) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0)
damage_42expectation2 = dc.AE_cal(atk=1151.77*2.193+1048.7*4.386, talent=1, em=1048.7, catalyze_verify=0) * dc.DB_cal(artifact_increase=2.3178) * \
                       dc.CD_cal(cr=1, cd=2.474) * dc.DF_cal(hilichurl_level=100,reduce_defenses=0.3) * \
                       dc.RT_cal(reduce_resistance=0.3)
print(damage_42expectation1, damage_42expectation2)

# 满命42词条业障除激化提升曲线ATK:EM:DB:CR约是:1:1.5:2:3
def draw_42_Q4(atk_Q4=1151.77, em_Q4=1048.7, DB_Q4=2.3178, cr_Q4=1, cd_Q4=2.474):
    x_values = np.arange(0, 11, 1)
    y_values_atk = dc.AE_cal(atk=(x_values*0.0495*840.97+atk_Q4)*2+em_Q4*4, talent=1, em=em_Q4) * \
                   dc.DB_cal(artifact_increase=DB_Q4) * \
                   dc.CD_cal(cr=cr_Q4, cd=cd_Q4) * \
                   dc.DF_cal(hilichurl_level=100, reduce_defenses=0.3) * \
                   dc.RT_cal(reduce_resistance=0.3)
    y_qoq_atk = np.array([(y_values_atk[i + 1] - y_values_atk[i]) / y_values_atk[i] for i in range(len(x_values) - 1)])
    y_values_em = dc.AE_cal(atk=atk_Q4*2+(x_values*19.81+em_Q4)*4, talent=1, em=x_values*19.81+em_Q4) * \
                  dc.DB_cal(artifact_increase=DB_Q4) * \
                  dc.CD_cal(cr=cr_Q4, cd=cd_Q4) * \
                  dc.DF_cal(hilichurl_level=100, reduce_defenses=0.3) * \
                  dc.RT_cal(reduce_resistance=0.3)
    y_qoq_em = np.array([(y_values_em[i + 1] - y_values_em[i]) / y_values_em[i] for i in range(len(x_values) - 1)])
    y_values_db = dc.AE_cal(atk=atk_Q4*2+em_Q4*4, talent=1, em=em_Q4) * \
                  dc.DB_cal(artifact_increase=x_values*0.05+DB_Q4) * \
                  dc.CD_cal(cr=cr_Q4, cd=cd_Q4) * \
                  dc.DF_cal(hilichurl_level=100, reduce_defenses=0.3) * \
                  dc.RT_cal(reduce_resistance=0.3)
    y_qoq_db = np.array([(y_values_db[i + 1] - y_values_db[i]) / y_values_db[i] for i in range(len(x_values) - 1)])
    y_values_cd = dc.AE_cal(atk=atk_Q4*2+em_Q4*4, talent=1, em=em_Q4) * \
                  dc.DB_cal(artifact_increase=DB_Q4) * \
                  dc.CD_cal(cr=cr_Q4, cd=x_values*0.066+cd_Q4) * \
                  dc.DF_cal(hilichurl_level=100, reduce_defenses=0.3) * \
                  dc.RT_cal(reduce_resistance=0.3)
    y_qoq_cd = np.array([(y_values_cd[i + 1] - y_values_cd[i]) / y_values_cd[i] for i in range(len(x_values) - 1)])
    print(y_qoq_atk[0], y_qoq_em[0], y_qoq_db[0], y_qoq_cd[0])
    # 1.0 1.457916539288927 2.266996789831144 2.8578881327226138
    print(y_qoq_atk[0]/y_qoq_atk[0], y_qoq_em[0]/y_qoq_atk[0], y_qoq_db[0]/y_qoq_atk[0], y_qoq_cd[0]/y_qoq_atk[0])
    # 伤害
    fig = plt.figure(figsize=(9, 7))
    plt.subplots_adjust(top=0.920, bottom=0.125, left=0.125, right=0.940, hspace=0.2, wspace=0.2)
    plt.plot(x_values, y_values_atk, color='#66CCFF', label='4.95%ATK')
    plt.plot(x_values, y_values_em, color='#F4606C', label='19.81EM')
    plt.plot(x_values, y_values_db, color='#AA6680', label='5%DB')
    plt.plot(x_values, y_values_cd, color='#39C5BB', label='6.6%CIRT DMG')
    plt.xlabel('圣遗物新加词条数', fontproperties=fontsimsun12)
    plt.ylabel('伤害', fontproperties=fontsimsun12)
    plt.title('在此42词条基础上新加副词条', fontproperties=fontsimsun12)
    plt.grid(True)
    plt.legend()
    os.makedirs('output/纳西妲攻略图片/Q4/', exist_ok=True)
    plt.savefig(f'output/纳西妲攻略图片/Q4/满命42词条业障除激化伤害曲线.png')
    # 环比
    fig = plt.figure(figsize=(9, 7))
    plt.subplots_adjust(top=0.920, bottom=0.125, left=0.125, right=0.940, hspace=0.2, wspace=0.2)
    plt.plot(x_values[1:], y_qoq_atk, color='#66CCFF', label='4.95%ATK')
    plt.plot(x_values[1:], y_qoq_em, color='#F4606C', label='19.81EM')
    plt.plot(x_values[1:], y_qoq_db, color='#AA6680', label='5%DB')
    plt.plot(x_values[1:], y_qoq_cd, color='#39C5BB', label='6.6%CIRT DMG')
    plt.xlabel('圣遗物新加词条数', fontproperties=fontsimsun12)
    plt.ylabel('环比', fontproperties=fontsimsun12)
    ax = plt.gca()  # 获取当前轴对象
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x:.3%}'))  # 使用匿名函数设置y轴的百分比格式
    plt.title('在此42词条基础上新加副词条', fontproperties=fontsimsun12)
    plt.grid(True)
    plt.legend()
    os.makedirs('output/纳西妲攻略图片/Q4/', exist_ok=True)
    plt.savefig(f'output/纳西妲攻略图片/Q4/满命42词条业障除激化提升曲线.png')

draw_42_Q4()



