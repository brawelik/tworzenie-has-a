
import random

# pierwszy program: Generator haseł

losoweCyfryIZnaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

licznik = -1

for i in losoweCyfryIZnaki:
    licznik += 1

# print(licznik)

dlogoscHasla = 15
haslo = ""

for i in range(dlogoscHasla):
    haslo += losoweCyfryIZnaki[random.randint(0, licznik)]

print(haslo)