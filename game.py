counts = 3

while counts > 0:
    temp = input("猜一下数字：")
    guess = int(temp)

    if guess == 8:
        print("猜对了！")
        print("牛逼！")
        break
    else:
        if guess < 8:
          print("数字小了")
        else:
          print("数字大了")
    counts = counts - 1
    
      
print("游戏结束，不玩了！")
