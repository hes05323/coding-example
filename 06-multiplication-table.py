# num_a=input("몇 단을 출력 하시겠습니까? ")
#
# while int(num_a)>9 or int(num_a)<2:
#     print("2~9단까지만 입력해주십시오")
#     num_a=input("몇 단을 출력 하시겠습니끄아악??? ")
#
# num_b=1
#
# while num_b<10:
#     num_c=int(num_a)*int(num_b)
#     print(num_a, "*", num_b, "=", int(num_c))
#     num_b=int(num_b)+1




## 구구단 만들기 선생님Ver.
# dan=int(input("몇 단을 출력 하시겠습니까?"))
# if dan>1 and dan<10:
#     for num in range(1,10):
#         print("{} * {} = {}".format(dan, num, dan*num))
# else:
#     print("2에서 9사이의 숫자를 넣어주세요")


num_a=int(input("몇 단을 출력 하시겠습니까? "))

while num_a>9 or num_a<2:
    print("2~9단까지만 입력해주십시오")
    num_a=int(input("몇 단을 출력 하시겠습니끄아악??? "))

for num_b in range(1,10):
    print("{} * {} = {}".format(num_a,num_b,num_a*num_b))
