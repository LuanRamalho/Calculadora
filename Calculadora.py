#-*- coding:utf-8 -*-

class Calculadora():
    def adição():
        i = 1
        while(i>0):
            print("Digite um número qualquer: ")
            num1 = float(input())
            print("Digite 1 número qualquer: ")
            num2 = float(input())
                        
            resultado =  num1 + num2
            print("")
            print("Resultado: ",resultado)

            print("")

            i = i + 1
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            print("")
        
        print("Resultado: ",resultado)
        
        
    def subtração():
        i = 1
        while (i > 0):
            print("Digite um número qualquer: ")
            num1 = float(input())
            print("Digite outro número qualquer: ")
            num2 = float(input())

            resultado = num1 - num2
            print("")
            print("Resultado: ", resultado)

            print("")

            i = i + 1
            print("Digite 1 para continuar ou 0 para sair")
            i = int(input())
            print("")

        print("Resultado: ", resultado)


    def multiplicação():
        i = 1
        while (i > 0):
            print("Digite um número qualquer: ")
            num1 = float(input())
            print("Digite outro número qualquer: ")
            num2 = float(input())

            resultado = num1 * num2
            print("")
            print("Resultado: ", resultado)

            print("")

            i = i + 1
            print("Digite 1 para continuar ou 0 para sair")
            i = int(input())
            print("")

        print("Resultado: ", resultado)


    def divisão():
        i = 1
        while (i > 0):
            print("Digite um número qualquer: ")
            num1 = float(input())
            print("Digite outro número qualquer: ")
            num2 = float(input())

            resultado = num1 / num2
            print("")
            print("Resultado: ", resultado)

            print("")

            i = i + 1
            print("Digite 1 para continuar ou 0 para sair")
            i = int(input())
            print("")

        print("Resultado: ", resultado)
        
    def exponenciação():
        i = 1
        while(i>0):
            print("Digite a base: ")
            base = float(input())
            print("Digite o expoente: ")
            expo = float(input())
                        
            resultado = base ** expo
            print("")
            print("Resultado: ",resultado)

            print("")

            i = i + 1
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            print("")

        print("Resultado: ", resultado)

    def raiz_quadrada():
        i = 1
        while(i>0):
            print("Digite 1 número qualquer: ")
            num = float(input())
            resultado =  num ** (1/2)
            print("")
            print("Resultado: ",resultado)

            print("")

            i = i + 1
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            
            print("")

        print("Resultado: ", resultado)

    def raiz_cúbica():
        i = 1
        while (i > 0):
            print("Digite 1 número qualquer: ")
            num = float(input())
            resultado = num ** (1/3)
            print("")
            print("Resultado: ", resultado)

            print("")

            i = i + 1

            print("Digite 1 para continuar ou 0 para sair")
            i = int(input())

            print("")

        print("Resultado: ", resultado)
            
    def fatorial():
        resultado = 1
         
        print("Digite um número inteiro: ")
        i = int (input())
        
        i = i
        while(i>0):
            resultado = resultado * i
            i = i - 1
        
        print("")
        print("")
        print("Fatorial: ",resultado)
        
    def porcentagem_1():
        i = 1
        while(i>0):
            print("Digite o primeiro número qualquer")
            a = float(input())
            print("Digite o segundo número qualquer")
            b = float(input())
        
            porcentagem = a/b*100
            
            print("")
            
            print("Resultado: %.2f" % porcentagem,"%")
            
            print("")
            print("")

            i = i + 1

            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())

        print("Resultado: %.2f" % porcentagem, "%")

    def porcentagem_2():
        i = 1
        while (i > 0):
            num = float(input("Digite um número qualquer: "))
            P = float(input("Digite o valor Acréscimo/Descrécimo percentual: "))
            R = num + (num * P) / 100

            print("")
            print("Resultado: %.0f" % R)

            print("")
            print("")
            print("Digite 1 para continuar ou 0 para sair: ")
            i = int(input())

        print("Resultado: %.0f" % R)

    def porcentagem_3():
        i = 1
        while (i > 0):
            num = float(input("Digite um número: "))
            P = float(input("Digite um valor percentual: "))
            R = (num * P) / 100

            print("")
            print("Resultado: %.0f" % R)

            print("")
            print("")
            print("Digite 1 para continuar ou 0 para sair: ")
            i = int(input())

        print("Resultado: %.0f" % R)

c = Calculadora

print("")
print("")
print("Digite 1 para Adição")
print("Digite 2 para Subtração")
print("Digite 3 para Multiplicação")
print("Digite 4 para Divisão")
print("Digite 5 para Exponenciação")
print("Digite 6 para Raíz Quadrada")
print("Digite 7 para Raiz Cúbica")
print("Digite 8 para Fatorial")
print("Digite 9 para Porcentagem 1")
print("Digite 10 para Porcentagem 2")
print("Digite 11 para Porcentagem 3")

op = int(input())
if (op==1):
    c.adição()  
elif (op==2):
    c.subtração()
elif (op==3):
    c.multiplicação()      
elif (op==4):
    c.divisão()      
elif (op==5):
    c.exponenciação()   
elif (op==6):
    c.raiz_quadrada()
elif (op==7):
    c.raiz_cúbica()
elif (op==8):
    c.fatorial()
elif (op==9):
    c.porcentagem_1()
elif (op==10):
    c.porcentagem_2()
elif (op==11):
    c.porcentagem_3()

input()
