menu= """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite= 500
totalDp= ""
totalSq= ""
numero_saques= 0
LIMITE_SAQUES= 3
opcao= -1


while opcao!= 0:
    opcao= int(input(f"{menu}Digite o número da operação \n"))
    if opcao <= 3:
        if opcao== 1:
            print ("Deposito".center(50, "-"))
            deposito= float(input ("Qual valor será depositado?\n"))
            if deposito>0:
                saldo= saldo+deposito
                totalDp= (
    f"""{totalDp} 
    R${deposito:.2f}""")
                print(f"Deposito efetuado com sucesso\nSaldo: R${saldo:.2f}")
            else:
                print("Falha no deposito\nNúmero do deposito tem que ser maior que 0")    
            
        else:
            if opcao == 2:
                print("Sacar".center(50, "-"))
                print(f"Saldo: R${saldo:.2f}")
                print(f"Saques efetuados {numero_saques}")
                if numero_saques<LIMITE_SAQUES:
                    saque=float(input("Qual o valor que deseja sacar?\n"))
                    if saque>0:
                        if saque<=limite:
                            if saque<=saldo:
                                saldo=saldo-saque
                                totalSq= (
    f"""{totalSq} 
    R${saque:.2f}""")
                                print("Saque feito com sucesso")
                                numero_saques= numero_saques+1
                            else:
                                print("Falha no saque\nSaldo insuficiente")    
                        else:
                            print("Falha no saque\nO valor foi maior que o limite[500]")
                    else:
                        print("Falha no saque\nO valor do saque tem que ser maior que 0")       
                else:
                    print("Falha no saque\nNúmero de saques chegoua ao limite[3]")
            else:
                if opcao==3:
                    print("Extrato".center(50, "-"))
                    extrato= (f"""

Depositos:{totalDp}
Saques:{totalSq}
Saldo
    R${saldo:.2f}
""")
                    print(f"{extrato}")
                else:
                    print ("SAINDO...")
    else: 
        print("Número inválido") 
    
