def damage_cal(AE, DB, CD, ER, DF, RT):
    """
    根据六大乘区的伤害计算，这里暂时仅作为测试。\n
    AE(基础伤害区+激化加成值)：(攻击区Attack × 倍率区Damage Multipiler + 激化区Elemental Reaction)\n
    DB(增伤区)：Damage Bonus\n
    CD(暴击区)：Critical Damage\n
    ER(增幅区)：Elemental Reaction\n
    DF(防御区)：Defense\n
    RT(抗性区)：Resistance\n
    """
    damage = AE*DB*CD*ER*DF*RT
    return damage


def AE_cal(atk=1304.1, talent=2.8325, em=500.6, catalyze_verify=1, damage_boost_increased=0):
    """
    Attack * Damage Multiplier + Elemental Reaction \n
    基础伤害区+激化加成值\n
    ☆ atk 指单一倍率角色的倍率所属属性(如可莉是atk，芙宁娜是hp)\n
    ☆ talent 如果是单一倍率，则按倍率算。如果是多个倍率，此处赋值1，让atk处先行计算完毕。\n
    ☆ em 元素精通\n
    ☆ catalyze_verify 是否激化\n
    ☆ damage_boost_increased 激化反应加成值(圣遗物套装)\n
    AE_cal = atk * talent + catalyze_damage
    """
    AD = atk * talent  # 基础伤害区
    if catalyze_verify:
        catalyze_damage = Cat_cal(em, damage_boost_increased)
        ADE = AD + catalyze_damage  # 如果激化，则算激化加成值
    else:
        ADE = AD  # 如果不激化，则基础伤害区不变
    return ADE  # 这里返回值使用的名称是ADE是为了体现激化加成是算入基础伤害区的


def DB_cal(elemental_increase=0, influence_increase=0, artifact_increase=0.466, skill_increase=0):
    """
    Damage Bonus 增伤区\n
    ☆ elemental_increase 元素/物理伤害加成\n
    ☆ influence_increase 对元素影响下的敌人伤害提高\n
    ☆ artifact_increase (圣遗物)造成伤害提高\n
    ☆ skill_increase 元素爆发/元素战技/普攻/重击伤害提高\n
    DB_cal = 1 + 4个increase之和
    """
    # 圣遗物的造成伤害提高是特指全技能的伤害提高，比如磐岩拾取结晶。如果仅单独提升某一技能则归为下一类skill_increase，比如乐团。
    # 这里元素爆发/元素战技/普攻/重击伤害的区分可利用其他参数来区分
    DB = 1 + elemental_increase + influence_increase + artifact_increase + skill_increase  # 加1是因为初始为100%
    return DB


def CD_cal(cr=0.458, cd=2.294, cr100=0):
    """
    Critical Damage 暴击区\n
    ☆ cr 暴击率\n
    ☆ cd 暴击伤害\n
    ☆ cr100 是否计算满暴击(0否1是,默认否)\n
    CD_cal = 1 + CRIT Rate * CRIT DMG
    """
    if cr100:  # 认为满暴
        CD = 1 + cd
    else:
        CD = 1 + cr * cd
    return CD


def ER_cal(em=0, elemental_magnification=1.5, increased_reaction_coefficient=0):
    """
    Elemental Reaction 增幅区\n
    ☆ elemental_magnification反应基础倍率(水火蒸发2.0 火水蒸发1.5 火冰融化2.0 冰火融化1.5)\n
    ☆ increased_reaction_coefficient反应系数提高(圣遗物套装)\n
    ER_cal = 反应基础倍率*(1+精通提升+反应系数提高)
    """
    ER = elemental_magnification * (1 + ((2.78 * em) / (em + 1400)) + increased_reaction_coefficient)
    return ER


def DF_cal(person_lever=90, hilichurl_level=90, reduce_defenses=0, ignore_defenses=0, increase_defenses=0):
    """
    Defense 防御区\n
    ☆ reduce defenses降低防御\n
    ☆ ignore defenses无视防御\n
    DF_cal = (人等+100)/[(人等+100)+(1-穿防)*(1-减防+增防)*(怪等+100)],即默认为190/[190+(1-穿防)*(1-减防)*190]
    """
    DF = (person_lever + 100) / ((person_lever + 100) +
                                 (1 - ignore_defenses) * (1 - reduce_defenses + increase_defenses) * (hilichurl_level + 100))
    return DF


def RT_cal(reduce_resistance=0, resistance=0.1):
    """
    Resistance 抗性区\n
    ☆ Reduce resistance降低敌人抗性\n
    RT_cal = f(resistance - reduce_resistance) (f函数见代码)
    """
    resistance -= reduce_resistance  # 原抗性减去减抗
    if resistance < 0:
        RT = 1 - (resistance / 2.0)
    elif 0 <= resistance <= 0.75:
        RT = 1 - resistance
    else:  # resistance > 0.75
        RT = 1.0 / (1 + 4 * resistance)
    return RT


def Cat_cal(em, damage_boost_increased, catalyze_type=2):
    """
    [子函数] catalyze_damage 激化加成伤害\n
    ☆ damage_boost_increased 激化反应加成值(圣遗物套装)
    ☆ catalyze_type 激化类型(0:Quicken原激化 1:Aggravate超激化 2:Spread蔓激化)
    暂时只写90级蔓激化的参考公式
    """
    type_coefficient = 1
    if catalyze_type == 1:
        type_coefficient = 1.15
    elif catalyze_type == 2:
        type_coefficient = 1.25
    cat_damage = 1446.853458 * type_coefficient * (1 + (5 * em) / (em + 1200) + damage_boost_increased)
    return cat_damage
