#mencari bilangan random

a = input("Masukan bilangan :")
b = input("Masukan bilangan :")
c = input("Masukan bilangan :")

if a > b > c :
	print("Bilangan Besar = %s" %a)
elif b > c:
	print("Bilangan Besar = %s" %b)
elif c > a:
	print("Bilangan Terbesar = %s" %c)
