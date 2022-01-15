"""
Created by Mardonov Hoshim
on 14 december 2021 year
at 10:55 o'clock
"""
menu = ["osh", 'somsa', 'shashlik', 'tarvuz', 'non', 'suv', 'salat', 'qovun']
ovqat = input("Nima buyurtma berasiz\n>>>")
if ovqat.lower() not in menu:
    print("Afsus bizda bunday ovqat yoq")
else:
    print("Buyurtma qabul qilindi")

buyurtmalar = ['non', 'suv', 'olma', 'nok', 'tarvuz', 'qovun', 'shaftoli']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"{taom} menuda bor")
        else:
            print(f"Bizda {taom} yoq")
                
else:
    print("Ro'yxat bo'sh")

son = int(input("Juft son kiriting\n>>>"))
if son % 2 == 0:
    print("rahmat")
else:
    print("Juft son kiriting")




yosh = int(input("Yoshingiz nechchida?\n>>>"))
if yosh<4:
    narh=0
elif yosh<18:
    narh=10000
elif yosh<60:
    narh=20000
else:
    narh=0
    
if narh == 0:
    print("Sizga bepul!")
else:
    print(f"Sizga kirish narhi {narh} so'm!")



son1 = int(input("Birorta son kiriting\n>>>"))
son2 = int(input("Ikkinchi sonni kiriting\n>>>"))
if son1 > son2:
    print(f"{son1} katta ekan {son2} dan")
else:
    print(f"{son1} kichik ekan {son2} dan")

mevalar = ["olma", "o'rik", "anor", "Sabzi"]
for meva in mevalar:
    print(meva)
print("dastur tugadi")




































