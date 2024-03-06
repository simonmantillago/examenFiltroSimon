import modules.reusable as rs
import modules.addProduct as au
import modules.corefiles as cf
import sys
data_products = {}
    
def main_menu():
    def wrapper(func,*params):
        rs.os.system('cls')
        func(*params)
        main_menu()
    data = cf.readDataFile("products.json")
    global data_products 
    data_products = data
    rs.os.system('cls')
    print("""
======================
=   TIENDA VIVERES   =
======================
1. Añadir producto
2. Mostrar productos
3. Salir
""")
    op = input(":> ")
    
    if op == '1':
        wrapper(au.addInfo,data_products)
    elif op == '2':
        print(data_products)
        rs.os.system('pause')
        main_menu()
    elif op == '3':
        sys.exit(rs.showSuccess('Vuelva pronto'))
    else:
        main_menu()
    
        