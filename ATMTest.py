balance = 50000
while True:
    print("---------主菜单-----------")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    choice = int(input("请输入你的选择："))
    if choice == 1:
        print("你的余额为：", balance)
    elif choice == 2:
        deposit = float(input("请输入存款金额："))
        balance += deposit
        print("存款后余额为：", balance)
    elif choice == 3:
        withdraw = float(input("请输入取款金额："))
        if withdraw > balance:
            print("余额不足")
        else:
            balance -= withdraw
            print("取款后余额为：", balance)
    elif choice == 4:
        break
    else:
        print("输入错误")
