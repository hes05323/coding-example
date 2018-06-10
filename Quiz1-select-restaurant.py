import random
korea=["비빔밥","불고기","떡갈비"]
china=["짜장면","짬뽕","탕수육"]
japan=["초밥","일본라멘","사시미"]

kategorie=input("한식, 중식, 일식 중 한가지를 고르세요!  ")

while kategorie!="한식" and kategorie!="중식" and kategorie!="일식":
    kategorie=input("제발 한식, 중식, 일식 중에서만 한가지를 고르세요!  ")

if kategorie=="한식":
    print(random.choice(korea))
if kategorie=="중식":
    print(random.choice(china))
if kategorie=="일식":
    print(random.choice(japan))
