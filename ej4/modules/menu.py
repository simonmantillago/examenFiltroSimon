import modules.reusable as rs
import modules.empleadosController as ec
import modules.corefiles as cf
import modules.pagosController as pc
import sys
data_nominas = {}
    
def main_menu():
    def wrapper(func,*params):
        rs.os.system('cls')
        func(*params)
        main_menu()
    data = cf.readDataFile("nominas.json")
    global data_nominas 
    data_nominas = data
    rs.os.system('cls')
    print("""
==========================
=   Calculadora Nomina   =
==========================
1. Añadir empleado
2. Pagar nomina
3. Consultar colilla de pago
4. Total pagado por concepto de nomina
5. Salir
""")
    op = input(":> ")
    
    if op == '1':
        wrapper(ec.addInfo,data_nominas)
    elif op == '2':
        wrapper(pc.addPago,data_nominas)
    elif op == '3':
        wrapper(pc.searchColilla,data_nominas)
    elif op == '4':
        wrapper(pc.nominasTotal,data_nominas)
    elif op == '5':
        sys.exit("\033[92m{}\033[00m" .format('Vuelva pronto'))
    else:
        main_menu()
    
        