user_win=int(0)
com_win=int(0)

while user_win<3 and com_win<3:
    user=input("가위,바위,보 중에 하나를 내주세요! ")

    import random as rd
    com_list=["가위","바위","보"]
    com=rd.choice(com_list)

    print("유저 : {}  vs 컴퓨터 : {}".format(user,com))

    if user=="가위" and com=="가위":
        print("무승부")
    elif user=="가위" and com=="바위":
        print("컴퓨터 승리")
        com_win=com_win+int(1)
    elif user=="가위" and com=="보":
        print("사용자 승리")
        user_win=user_win+int(1)
    elif user=="바위" and com=="가위":
        print("사용자 승리")
        user_win=user_win+int(1)
    elif user=="바위" and com=="바위":
        print("무승부")
    elif user=="바위" and com=="보":
        print("컴퓨터 승리")
        com_win=com_win+int(1)
    elif user=="보" and com=="가위":
        print("컴퓨터 승리")
        com_win=com_win+int(1)
    elif user=="보" and com=="바위":
        print("사용자 승리")
        user_win=user_win+int(1)
    elif user=="보" and com=="보":
        print("무승부")
    else:
        print("제대로 입력해주세요")

print("---------------------------")
print("유저 : {}  vs 컴퓨터 : {}".format(user_win,com_win))
print("---------------------------")
