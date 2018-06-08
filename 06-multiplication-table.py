num_a=input("몇 단을 출력 하시겠습니까? ")

while int(num_a)>9:
    print("1~9단까지만 입력해주십시오")
    num_a=input("몇 단을 출력 하시겠습니끄아악??? ")

num_b=1

while num_b<10:
    num_c=int(num_a)*int(num_b)
    print(num_a, "*", num_b, "=", int(num_c))
    num_b=int(num_b)+1
