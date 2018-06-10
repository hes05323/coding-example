# 입력하는 ver.

name=input("이름: ")
age=input("나이: ")
sex=input("성별: ")

class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

people=People(name,age,sex)

rank=input("직급: ")
class Officer(People):
    def __init__(self,rank):
        self.rank=rank

officer=Officer(rank)

print("-----------------")
print("이름: ", people.name)
print("나이: ", people.age)
print("성별: ",people.sex)
print("직급: ",officer.rank)
print("-----------------")




# 상속클래스 출력 비교 Ver.
class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def print_show(self):
        print("이름: ",self.name)
        print("나이: ",self.age)
        print("성별: ",self.sex)

people1=People("홍길동","30살","남성")
people2=People("김건호","50살","남성")
people3=People("이혜림","33살","여성")
people4=People("이경미","47살","여성")
people5=People("정희태","42살","남성")
people6=People("김지훈","29살","남성")
people7=People("이승재","31살","남성")
people8=People("박유미","35살","여성")

class Officer(People):
    def __init__(self,name,age,sex,rank):
        self.name=name
        self.age=age
        self.sex=sex
        self.rank=rank
    def print_show(self):
        print("이름: ",self.name)
        print("나이: ",self.age)
        print("성별: ",self.sex)
        print("직급: ",self.rank)

people5=Officer("정희태","42살","남성","부장")
people6=Officer("김지훈","29살","남성","사원")
people7=Officer("이승재","31살","남성","대리")
people8=Officer("박유미","35살","여성","과장")

people5.print_show()
print("--------------")
people1.print_show()
