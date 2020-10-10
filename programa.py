n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
soma = 0
result = 0
if n1 <= n2:
    print("o primeiro valor digitado tem que ser maior que o segundo valor digitado")
else:
    maior=n1+1
    menor=n2
    for i in range(maior):
        if maior > menor:
            maior= maior -1
            soma= soma + maior
            print(maior, end=(" + "))
            result = soma
        else:
            print("Fim do programa")
print(f'O resultado é: {result}')
