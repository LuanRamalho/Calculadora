#-*- coding:utf-8 -*-

class Calculadora():
    def adição():
        num = [0]*9999
        i = 1
        z = 0
        resultado = 0.00
        while(i>0):
            print("Digite 1 número qualquer: ")
            num[z] = float(input())
                        
            resultado = resultado + num[z]
            print("")
            print("Resultado: ",resultado)
            
            i = i + 1
            z = z + 1
            
            print("")
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            
            print("")
        
        print("Resultado: ",resultado)
        
        
    def subtração():
        num = [0]*9999
        i = 1
        z = 0
        resultado = 0.00
        while(i>0):
            print("Digite 1 número qualquer: ")
            num[z] = float(input())
                        
            resultado = resultado - num[z]
            print("")
            print("Resultado: ",resultado)
            
            i = i + 1
            z = z + 1
            
            print("")
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            
            print("")
        
        print("Resultado: ",resultado)   


    def multiplicação():
        num = [0]*9999
        i = 1
        z = 0
        resultado = 1.00
        while(i>0):
            print("Digite 1 número qualquer: ")
            num[z] = float(input())
                        
            resultado = resultado * num[z]
            print("")
            print("Resultado: ",resultado)
            
            i = i + 1
            z = z + 1
            
            print("")
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            
            print("")
        
        print("Resultado: ",resultado)     


    def divisão():
        divisor = [0]*9999
        dividendo = [0]*9999
        i = 1
        z = 0
        while(i>0):
            print("Digite o divisor: ")
            divisor[z] = float(input())
            print("Digite o dividendo: ")
            dividendo[z] = float(input())
                        
            resultado = divisor[z] / dividendo[z]
            print("")
            print("Resultado: ",resultado)
            
            i = i + 1
            z = z + 1
            
            print("")
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            
            print("")   
        
    def exponenciação():
        base = [0]*9999
        expo = [0]*9999
        i = 1
        z = 0
        while(i>0):
            print("Digite a base: ")
            base[z] = float(input())
            print("Digite o expoente: ")
            expo[z] = float(input())
                        
            resultado = base[z] ** expo[z]
            print("")
            print("Resultado: ",resultado)
            
            i = i + 1
            z = z + 1
            
            print("")
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            
            print("")

    def raiz_quadrada():
        num = [0]*9999
        i = 1
        z = 0
        while(i>0):
            print("Digite 1 número qualquer: ")
            num[z] = float(input())
                        
            resultado =  num[z] ** (1/2)
            print("")
            print("Resultado: ",resultado)
            
            i = i + 1
            z = z + 1
            
            print("")
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
            
            print("")
            
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
        
    def porcentagem():
        i = 1
        while(i>0):
            print("Digite o primeiro número qualquer")
            a = float(input())
            print("Digite o segundo número qualquer")
            b = float(input())
        
            porcentagem = a/b*100
            
            print("")
            
            print("Resultado: ",porcentagem,"%")
            
            print("")
            print("")
            
            i = i + 1
            print("Digite 1 para continuar ou 0 para sair")
            i = int (input())
        

c = Calculadora

print("")
print("")
print("Digite 1 para Adição")
print("Digite 2 para Subtração")
print("Digite 3 para Multiplicação")
print("Digite 4 para Divisão")
print("Digite 5 para Exponenciação")
print("Digite 6 para Raíz Quadrada")
print("Digite 7 para Fatorial")
print("Digite 8 para Porcentagem")

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
    c.fatorial()
elif (op==8):
    c.porcentagem()
    