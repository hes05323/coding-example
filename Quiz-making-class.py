class School_class:
    school_name="광운대학교"
    address="노원구"

    def __init__(self,name,established_year):
        self.name=name
        self.established_year=established_year

school_class1=School_class("축구부","1996")
school_class2=School_class("농구부","1993")
school_class3=School_class("여명","1888")

print(school_class1.name)
print(school_class1.address)
print(school_class1.school_name)
print(school_class1.established_year)
print(school_class3.name)
print(school_class3.established_year)
print(school_class2.name)
print(school_class2.established_year)
