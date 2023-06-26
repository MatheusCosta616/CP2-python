
import random
raten = random.randint(1,4)

if raten == 1:
    funcionario = "Pedro"
elif raten == 2:
    funcionario = "Henrique"
elif raten == 3:
    funcionario = "João"
else:
    funcionario = "Matheus"

print(f"Olá! Iremos dar inicio ao seu atendimento. \nVocê será atendido pelo {funcionario}!")

cep = str(input("Digite o seu CEP: "))
idade = int(input("Digite seu ano de nascimento: "))
nome = str(input("Digite o seu nome: "))
comprar = 0
if 2023 - idade < 18:
    print("Desculpe, não podemos vender bebidas alcoólicas para menores de idade.")
else:
    comp = "sim"
    bask = 0
    while comp == "sim":
        print("Nossos preços de vinho são:\nTinto:R$40,00\nBranco:R$70,00\nSuave:R$80,00\nSeco:R$100,00\nRose:R$120,00")
        compra = str.lower(input("Qual tipo você quer adicionar ao carrinho?\n"))
        if compra == "tinto":
            mult1 = int(input("Quantas garrafas você deseja?\n"))
            print(mult1, "Garrafas de tinto totalizando:", mult1 * 40)
            bask += mult1 * 40
            print("Valor da cesta:", bask)
        elif compra == "branco":
            mult2 = int(input("Quantas garrafas você deseja?"))
            print(mult2, "Garrafas de branco totalizando:", mult2 * 70)
            bask += mult2 * 70
            print("Valor da cesta:", bask)
        elif compra == "suave":
            mult3 = int(input("Quantas garrafas você deseja?"))
            print(mult3, "Garrafas de suave totalizando:", mult3 * 80)
            bask += mult3 * 80
            print("Valor da cesta:", bask)
        elif compra == "seco":
            mult4 = int(input("Quantas garrafas você deseja?"))
            print(mult4, "Garrafas de seco totalizando:", mult4 * 100)
            bask += mult4 * 100
            print("Valor da cesta:", bask)
        elif compra == "rose":
            mult5 = int(input("Quantas garrafas você deseja?"))
            print(mult5, "Garrafas de rose totalizando:", mult5 * 120)
            bask += mult5 * 120
            print("Valor da cesta:", bask)
        else:
            print("Opção inválida")
        keep = str.lower(input("Deseja continuar comprando?\nDigite 'Sim' caso queira continuar, caso queira terminar o atendimento digite 'Não'\n"))
        if keep == "sim":
            comp = "sim"
        else:
            comp = "não"

    print("O valor total da sua compra é:", bask)
    print(f"Você foi atendido pelo funcionario{funcionario}\nSr(a){nome} Obrigado Volte sempre")
    if bask >= 200:
        print("O frete é gratis")
    else:
        print("Você pagara frete, que custa 10,50 reais, totalizando", bask + 10.50)


