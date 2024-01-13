import numpy as np
import damage_calculator as dc
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter


fontsimsun12 = FontProperties(fname="input/simsun.ttc", size=12)  # 设置中文字体

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
天赋1：依据队伍em最高角色的0.25em，提高领域内场上角色精通
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
        ax.scatter(self.x, self.y_quarter_on_quarter)  # x-->精通, y-->环比
        ax.set_xlabel('精通', fontproperties=fontsimsun12)
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
        self.y_DB = dc.DB_cal(artifact_increase=self.Nahida_DB_ForQ1)  # 增伤
        # y坐标轴--->伤害
        self.y_base = self.y_AE[0] * self.y_CD[0] * self.y_DB[0]
        self.y_actual = self.y_AE * self.y_CD * self.y_DB
        self.y_compare_initial = self.y_actual / self.y_base
        self.y_quarter_on_quarter = np.array([(self.y_actual[1] - self.y_actual[0]) / self.y_actual[0]] +
                                             [(self.y_actual[i + 1] - self.y_actual[i]) / self.y_actual[i]
                                              for i in range(len(self.x) - 1)])

def draw_Nahida_em_Q1(set_xylim1=False, set_xylim2=False):
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

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
                                              Nahida_CRITIncrease_forQ1=0.662, Nahida_DBIncrease_forQ1=0.24,
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
                                              Nahida_CRITIncrease_forQ1=0, Nahida_DBIncrease_forQ1=0.96, ax=axs[1, 2])
    axs[1, 2].set_title('精五流浪乐章精通收益曲线(精通)', fontproperties=fontsimsun12)
    if set_xylim1:
        axs[1, 2].set_xlim(600, 1000)
        axs[1, 2].set_ylim(0.0006, 0.0020)
    if set_xylim2:
        axs[1, 2].set_xlim(1000, 1200)
        axs[1, 2].set_ylim(0.0004, 0.0006)
    plt.show()

draw_Nahida_em_Q1()
draw_Nahida_em_Q1(set_xylim1=True)  # 结论1：1000精通前，武器白值、双暴、元素伤害加成越高，精通提升的环比越低
draw_Nahida_em_Q1(set_xylim2=True)  # 结论2：1000精通后，武器白值越高(此时与双暴、元素伤害加成无关)，精通提升的环比越低


# Part2 双暴
# 实战精通肯定大于1000，天赋2吃满，是0.8增伤，0.24暴击率
# 因此这里Nahida_em_ForQ1=1000，Nahida_CRIT_ForQ1 = x轴, Nahida_DB_ForQ1=0.466
