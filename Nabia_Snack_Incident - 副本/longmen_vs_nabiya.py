# longmen_vs_nabiya.py
# 请根据引导文档(README.md)的要求，完成下面的8个函数。

import random
import time

# --- 战斗设定 (这些是预设好的值，不需要修改哦) ---
NAGATO_MAX_HP = 120
NABIYA_MAX_HP = 100
NAGATO_ATTACK_DICE = 4
NAGATO_DEFEND_DICE = 3
NABIYA_ATTACK_DICE = 4
NABIYA_DEFEND_DICE = 3
SPECIAL_ATTACK_DAMAGE = 30
CRITICAL_HIT_THRESHOLD = 18


# 任务一：显示角色状态
def display_status(character_name, current_hp, max_hp):
    """打印格式: 【角色名】HP: 当前血量 / 最大血量"""
    # 在这里写你的代码，用print()函数

    print(f'{current_hp}/{max_hp}')

    pass


# 任务二：掷骰子
def roll_dice(num_dice):
    """用while循环，模拟掷N个骰子，返回总点数"""
    total_points = 0
    count = 0
    # 在这里写你的代码

    while(count < num_dice):
        count += 1
        total_points += random.randint(1,6)


    return total_points


# 任务三：选择长门的行动
def choose_nagato_action(nagato_hp, nabiya_hp):
    """用if/elif/else，根据血量返回 'attack', 'defend', 或 'special'"""
    
    # 在这里写你的代码

    if(nagato_hp < 30):
        return 'defend'
    elif(nabiya_hp < 20):
        return 'special'
    else:
        return 'attack'
    
    pass


# 任务四：计算攻击伤害
def calculate_attack_damage(num_dice):
    """调用 roll_dice() 函数来计算伤害"""
    # 在这里写你的代码
    return roll_dice(num_dice)
    pass


# 任务五：计算防御值
def calculate_defense_value(num_dice):
    """调用 roll_dice() 函数来计算防御值"""
    # 在这里写你的代码
    return roll_dice(num_dice)
    pass


# 任务六：检查是否暴击 (BIG SEVEN)
def check_critical_hit(base_damage):
    """如果伤害 >= 18，返回 True，否则返回 False"""
    # 在这里写你的代码
    if(base_damage >= 18):
        return True
    else:
        return False
    pass


# 任务七：娜比娅的AI行动
def nabiya_ai_action(nabiya_hp):
    """如果娜比娅HP <= 40，返回 'defend'，否则返回 'attack'"""
    # 在这里写你的代码
    if(nabiya_hp <= 40):
        return 'defend'
    else:
        return 'attack'
    pass

#进行攻击行为（包含破甲计算）
def action_attack(damage,enemy_hp,enemy_defense):
    true_damage = damage - enemy_defense
    if(true_damage > 0):
        
        return enemy_hp-true_damage
    else:
        print('未击穿敌人装甲')
        return enemy_hp


    
# 任务八：核心战斗循环
def main_battle_loop():
    """
    这是最重要的部分！请根据下面的注释步骤来完成。
    
    适当的编写输出来说明战斗发生了什么，比如：
    print("长门：「感受BIG SEVEN的威力吧！」")
    print("💥「BIG SEVEN」触发！伤害翻倍！")
    """
    # 1. 初始化长门和娜比娅的HP，以及双方的防御值
    nagato_hp = NAGATO_MAX_HP
    nabiya_hp = NABIYA_MAX_HP
    nagato_defense_bonus = 0
    nabiya_defense_bonus = 0
    turn = 1

    # 2. 编写 while 循环，在双方都存活时继续战斗
    # 注意，不需要你编写选择行动的代码，只需要编写行动后的逻辑即可
    

        # 3. --- 长门的回合 ---
        
        
        # 用 if/elif/else 处理不同行动
        
        #     ...
        
        # 4. 检查娜比娅是否被击败
        # if nabiya_hp <= 0:
        #     ...
        
        # time.sleep(1)

        # 5. --- 娜比娅的回合 ---
        # print("\n>>> 娜比娅的回合")
        # (和长门回合逻辑类似)
        
        # 6. 检查长门是否被击败
        # if nagato_hp <= 0:
        #     ...

        # turn = turn + 1
        # time.sleep(1)
    
    # 在这里写你的代码

    while(nagato_hp > 0 and nabiya_hp > 0):

        print(f"\n======== 回合 {turn} ========")
        display_status("长门", nagato_hp, NAGATO_MAX_HP)
        display_status("娜比娅", nabiya_hp, NABIYA_MAX_HP)

        # 3. --- 长门的回合 ---
        print("\n>>> 长门的回合")
        action = choose_nagato_action(nagato_hp, nabiya_hp)
        
        # 用 if/elif/else 处理不同行动
        if(action == 'attack'):
            base_damage = calculate_attack_damage(NAGATO_ATTACK_DICE)
            
            if(check_critical_hit(base_damage) == True):
                nabiya_hp = action_attack(base_damage*2,nabiya_hp,nabiya_defense_bonus)
                print(f'成功暴击,对nabiya造成{base_damage*2}的伤害')
            elif(check_critical_hit(base_damage) == False):
                nabiya_hp = action_attack(base_damage,nabiya_hp,nabiya_defense_bonus)
                print(f'造成{base_damage}的伤害')
            
        elif(action == 'defend'):
            nagato_defense_bonus = roll_dice(NABIYA_DEFEND_DICE)
            print(f'nagato使用了防御，防御值为{nagato_defense_bonus}')
        # else: # special
        else:
            whether_special = random.randint(0,1)==0
            if(whether_special):
                nabiya_hp = action_attack(30,nabiya_hp,nabiya_defense_bonus)
                print('special成功')
            else:
                print('special失败')
        nabiya_defense_bonus = 0
        
        # 4. 检查娜比娅是否被击败
        if nabiya_hp <= 0:
            print('nagato获胜')
        
        time.sleep(1)

        # 5. --- 娜比娅的回合 ---
        print("\n>>> 娜比娅的回合")
        # (和长门回合逻辑类似)
        nabiya_action = nabiya_ai_action(nabiya_hp)
        if(nabiya_action == 'attack'):
            base_damage = calculate_attack_damage(NABIYA_ATTACK_DICE)
            
            if(check_critical_hit(base_damage)):
                nagato_hp = action_attack(base_damage*2,nagato_hp,nagato_defense_bonus)
                print(f'成功暴击,对nagato造成{base_damage*2}的伤害')
            else:
                nagato_hp = action_attack(base_damage,nagato_hp,nagato_defense_bonus)
                print(f'造成{base_damage}的伤害')
        else:
            nabiya_defense_bonus = calculate_defense_value(NABIYA_DEFEND_DICE)
            print(f'nabiya使用了防御，防御值为{nabiya_defense_bonus}')
        # 6. 检查长门是否被击败
        if nagato_hp <= 0:
            print('nabiya获胜')
            break

        #     ...
        
        
        nagato_defense_bonus = 0

        turn = turn + 1
        time.sleep(1)
    
    pass
 
main_battle_loop()
