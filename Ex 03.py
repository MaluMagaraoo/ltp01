# Programa para imprimir os primeiros 10 números da sequência de Fibonacci

fibonacci = [0, 1]

for i in range(2, 10):
    proximo_numero = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo_numero)

for numero in fibonacci:
    print(numero)