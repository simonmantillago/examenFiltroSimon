import modules.reusable as rs



def main_menu():
    rs.os.system('cls')
    print("""
======================
=   Casa de cambio   =
======================
""")
    valPesos = rs.checkInput('float','Ingrese el valor en pesos que desea convertir')
    rs.os.system('cls')
    again = True
    while again:
        print("""
    Ingrese la moneda a la que desea convertir
    1. YEN
    2. DOLAR
    3. EURO
    4. SALIR 
            """)
        op = input(':> ')
        if op  == '1':
            valYen = valPesos/26.30
            print(f'{valPesos} equivale a {round(valYen,2)} yenes')
            rs.os.system('pause')
            rs.os.system('cls')
            again = rs.yesORnot('Desea realizar el cambio a otra moneda?')
        elif op  == '2':
            valDolar = valPesos/3944
            print(f'{valPesos} equivale a {round(valDolar,2)} dolares')
            rs.os.system('pause')
            rs.os.system('cls')
            again = rs.yesORnot('Desea realizar el cambio a otra moneda?')
        elif op  == '3':
            valEuro = valPesos/4279
            print(f'{valPesos} equivale a {round(valEuro,2)} euros')
            rs.os.system('pause')
            rs.os.system('cls')
            again = rs.yesORnot('Desea realizar el cambio a otra moneda?')
        elif op  == '4':
            main_menu()
    main_menu()
            
        