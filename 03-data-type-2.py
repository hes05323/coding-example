# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
print("list")
list_a=[1,2,3]
print(list_a)
print(type([1,2,3]))
# index는 0부터 시작합니다.
print(list_a[0])
print(list_a[1])
print(list_a[2])
# slice
print(list_a[0:2])
list_a.append(4)
print(list_a)
list_a.remove(2)
print(list_a)
list_a.clear()
print(list_a)

tuple (1, )
print("tuple")
tuple_a=(1,2,3)
print(tuple_a)
print(type((1,2,3)))
tuple_a.append(4)
# tuple은 append, clear 등은 적용이 안된다. 즉 더 가벼운 코드로서 가치가 있음.
# 아니면 프로그래머가 수정을 못하도록 할때도 사용하기도 함

dict (map) {}
key & value
dict_a={
    "apple":"a type of fruits",
    "pen":"a thing to write"
}
print(dict_a)
print(dict_a["apple"])
# edit value
dict_a["pen"]="something to write"
# print(dict_a["pen"])

# set set([])
set_a=set([1,2,3,3,3,2,2,2])
set_b=set([2,4,6])
print(set_a)
print(set_b)

# 집합 - 교집합, 합집합, 차집합, 여집합
# set은 중복을 자동으로 제거해준다

# 교집합
print(set_a & set_b)
# 합집합
print(set_a | set_b)
# 차집합
print(set_a - set_b)
