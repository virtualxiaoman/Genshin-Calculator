import damage_calculator as dc


def damagecal_detailedly(atk=1304.1, talent=2.8325, em=500.6, catalyze_verify=1, damage_catalyze_increased: float = 0,
                         catalyze_type=2, added_basedamage: float = 0, multiply_basedamage: float = 0,
                         db_increase=0,
                         cr=0.458, cd=2.294, cr100=0,
                         elemental_magnification=1.5, increased_reaction_coefficient=0,
                         person_lever=90, hilichurl_level=90, reduce_defenses=0, ignore_defenses=0, increase_defenses=0,
                         reduce_resistance=0, resistance=0.1
                         ):
    """
    计算逻辑：伤害 =
                       攻击力 * (天赋倍率 * (1+基础伤害加成的乘算) ) + 基础伤害加成的加算 +   【激化加成值-可选,不能和增幅冲突】
                    * ( 1 + 各种增伤 )
                    * ( 1 + 暴击率*暴击伤害)
                    * ( 反应基础倍率 * (1 + 精通提升 + 反应系数提高) )   【精通提升=(2.78 * em) / (em + 1400)】
                    * (人等+100)/[ (人等+100)+(1-穿防)*(1-减防+增防)*(怪等+100) ]   【即默认为190/[190+(1-穿防)*(1-减防)*190】
                    * f( 魔物抗性 - 减抗 )   【f(x)=1-(x/2.0)[if x<0], =1-x[if 0≤x≤0.75], =1.0/(1+4*x)[if x>0.75]】
    :param atk: 指单一倍率角色的倍率所属属性(如可莉是atk，芙宁娜是hp)
    :param talent: 如果是单一倍率，则按倍率算。如果是多个倍率，此处赋值1，让atk处先行计算完毕。
    :param em: 元素精通
    :param catalyze_verify: 是否激化
    :param damage_catalyze_increased: 激化反应加成值(圣遗物套装)
    :param catalyze_type: 激化反应类型(0:Quicken原激化 1:Aggravate超激化 2:Spread蔓激化)
    :param added_basedamage: 基础伤害加成(加算)，如申鹤
    :param multiply_basedamage: 基础伤害加成(乘算)，如辰砂之纺锤
    :param db_increase: 所有的增伤的求和结果，包含：
        elemental_increase: 元素/物理伤害加成
        influence_increase: 对元素影响下的敌人伤害提高
        artifact_increase: (圣遗物)造成伤害提高
        skill_increase: 元素爆发/元素战技/普攻/重击伤害提高
    :param cr: 暴击率
    :param cd: 暴击伤害
    :param cr100: 是否计算满暴击(0否1是,默认否)
    :param elemental_magnification: 反应基础倍率(水火蒸发2.0 火水蒸发1.5 火冰融化2.0 冰火融化1.5)
    :param increased_reaction_coefficient: 反应系数提高(圣遗物套装)
    :param person_lever: 角色等级
    :param hilichurl_level: 魔物等级(不知道怎么翻译所以用的丘丘人)
    :param reduce_defenses: 降低防御
    :param ignore_defenses: 无视防御
    :param increase_defenses: 增防(少见，一般见于原魔塔)
    :param reduce_resistance: 降低敌人抗性
    :param resistance: 敌人抗性(默认为10%)
    :return:从0开始的伤害计算
    """
    AE = dc.AE_cal(atk, talent, em, catalyze_verify, damage_catalyze_increased, catalyze_type, added_basedamage,
                   multiply_basedamage)
    DB = dc.DB_cal(db_increase, 0, 0, 0)
    CD = dc.CD_cal(cr, cd, cr100)
    ER = dc.ER_cal(em, elemental_magnification, increased_reaction_coefficient)
    DF = dc.DF_cal(person_lever, hilichurl_level, reduce_defenses, ignore_defenses, increase_defenses)
    RT = dc.RT_cal(reduce_resistance, resistance)
    if catalyze_verify:  # 激化不能增幅
        damage = AE*DB*CD*DF*RT
    else:
        damage = AE*DB*CD*ER*DF*RT
    return damage


def damagecal_informally():

    pass
