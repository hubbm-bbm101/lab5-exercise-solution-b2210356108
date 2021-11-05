import random
number = random.randint(1,100)
print("sayı 1 ile 100 arasındadır.")
tahmin = 0
while tahmin!= number:
    tahmin = int(input("tahmininiz:"))
    if tahmin>number:
        print("tahmininiz büyük")
    elif tahmin<number:
        print("tahmininiz küçük")

print("Bildiniz , sayı:" + str(number))
