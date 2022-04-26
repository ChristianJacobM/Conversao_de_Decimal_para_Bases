while True: 
    print("------------------------------------")
    n = int(input("Digite um número: "))
    print("------------------------------------")
    print("[1]-Binário")
    print("[2]-Octal")
    print("[3]-Hexadecimal")
    print("[x]-Sair")
    print("------------------------------------")

    pergunta_num = str(input("Digite a opção que deseja converter: "))
    if pergunta_num == "x" or pergunta_num == "X":
        break
    elif pergunta_num == "1" or pergunta_num == "2" or pergunta_num == "3":
        if pergunta_num == "1":
            rio = str(bin(n))
            print("------------------------------------")
            print("Seu valor em Binário é:", rio)
        elif pergunta_num == "2":
            cta = str(oct(n))
            print("------------------------------------")
            print("Seu valor em Octal é:", cta)

        elif pergunta_num == "3":
            exa = str(hex(n))
            print("------------------------------------")
            print("Seu valor em Hexadecimal é:", exa)

    else:
        print("Opção invalida!")