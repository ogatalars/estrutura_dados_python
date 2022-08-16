a = "casaco"
print(a)

maiscula = a.upper() 
print(maiscula)

minuscula = maiscula.lower() 
print(minuscula)

capital = a.capitalize()
print(capital)

metade_palavra = a[0:4]
print(metade_palavra)

ultimas_letras = a[3:]
print(ultimas_letras)

b = a.replace("aco", "inha")
print(a)

c = a.replace("c", "a")
print(c)

c.find("s" )
c.find("a")
# retorna a primeira letra

e = " c a s a c o "
print(len(e))

f = e.strip() 
print(f)
print(len(f))

n1 = 14
n2 = 16
print(f"dividinhdo {n1} por {n2} é {n1/n2}")