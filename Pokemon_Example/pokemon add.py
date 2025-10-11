from pokemon import *

#ThunderPokemon类
class ThunderPokemon(Pokemon):
    type  = "Thunder"

    def type_effectiveness(self, opponent: Pokemon):
        # 针对敌方 Pokemon 的类型，调整效果倍率
        effectiveness = 1.0
        opponent_type = opponent.type

        if opponent_type == "Water":
            effectiveness = 2.0
        elif opponent_type == "Glass":
            effectiveness = 0.5
        return effectiveness
    
    def thunder_attribute(self):
        #当成功躲闪时，可以立即使用一次技能

