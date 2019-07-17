# 1、自动贩卖机： 只接受1元、5元、10元的纸币或硬币，可以1块，5元，10元。最多不超过10块钱。
#  饮料只有橙汁、椰汁、矿泉水、早餐奶，售价分别是3.5，4，2，4.5
# 写一个函数用来表示贩卖机的功能： 用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零。

#输入钱币函数

def input_money():
    money_all=0
    while True:
        money=input("请输入1元、5元、10元价钱，退出请按q:")
        if money == '1'or money == '5' or money == '10':
            money_all+=eval(money)
        elif money == 'q':
            break
        else:
            print("你输入的金钱不符合条件，退给你。请你投入1元，5元，10元价钱")
    return money_all



#选择物品函数

def choose_food():
    money_food=0


    while True:
        food = input("1为橙汁，2为椰汁，3为矿泉水，4为早餐奶，q为退出")
        if food == '1':
            money_food+=3.5
            count_orange+=1
        elif food == '2':
            money_food+=4
            count_yezhi+=1
        elif food =='3':
            money_food+=2
            count_water+=1
        elif food == '4':
            money_food+=4.5
            count_milk+=1
        elif food =="q":
            break
        else:
            print("你选择的物品不正确，请选择正确的物品")
    return money_food


#计算结算的价格

pay = input_money()
buy = choose_food()


def count_money():
    global pay
    if pay ==buy:
        print(f"你投入{pay}元，购买物品需花费{buy},请接受你购买的物品")
    elif pay > buy:
        change = pay - buy
        print(f"你投入{pay}元，购买物品需花费{buy}元，找你零钱{change}元，请接受你购买的物品和所剩零钱")
    else:
        not_enough = buy - pay
        print(f"你投入{pay}元，购买物品需花费{buy}元，还需你投入{not_enough}元")
        putchoose=input("如需继续购买，请选择y，放弃购买，请选择n:")
        if putchoose == 'y':
            print(pay)
            pay1 = input_money()
            pay+=pay1
            print(pay)
            count_money()
        else:
            print(f"请接受你投入的{pay}元")




count_money()








# 2、定义一个函数，成绩作为参数传入。如果成绩小于60，则输出不及格。
# 如果成绩在60到80之间，则输出良好；如果成绩高于80分，
# 则输出优秀，如果成绩不在0-100之间，则输出 成绩输入错误。

# def score(score):
#     if 0<=score<=100:
#         if score < 60:
#             print(f"你当前分数{score},成绩不及格")
#         elif 60 <= score <= 80:
#             print(f"你当前分数{score}，成绩良好")
#         else:
#             print(f"你当前分数{score}，成绩优秀")
#     else:
#         print("成绩输入错误，请重新输入")
#
# score(1000)





