a = 1
b = 10
print(a, b)
print(a + b)
print(a - b)
print ( a* b)
print ( a/ b)
print ( a% b)

tempo_gasto_viagem = int(input("Qual foi o tempo gasto na viagem? "))
velocidade_media = int(input("Qual foi a velocidade media da viagem? "))
distancia = tempo_gasto_viagem * velocidade_media
litros_usados = distancia / 12
print(f"Você usou {litros_usados} litros de gasolina")