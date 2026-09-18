balance = 50000
def menu():
    print("---------主菜单-----------")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    choice = int(input("请输入你的选择："))
    return choice

def query():
    print("你的余额为：", balance)

def deposit():
    global balance
    amount = float(input("请输入存款金额："))
    balance += amount
    print("存款后余额为：", balance)
    query()

def withdraw():
    global balance
    amount = float(input("请输入取款金额："))
    if amount > balance:
        print("余额不足")
    else:
        balance -= amount
        print("取款后余额为：", balance)
        query()

def exit():
    print("退出系统")

while True:
    choice = menu()
    if choice == 1:
        query()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        exit()
        break
    else:
        print("输入错误")
