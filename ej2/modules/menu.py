import modules.reusable as rs
import modules.addUser as au
import modules.corefiles as cf
import sys
data_users = {}
    
def main_menu():
    def wrapper(func,*params):
        rs.os.system('cls')
        func(*params)
        main_menu()
    data = cf.readDataFile("users.json")
    global data_users 
    data_users = data
    rs.os.system('cls')
    print("""
======================
=    Info Usuarios   =
======================
1. Añadir usuario
2. Mostrar usuarios
3. Salir
""")
    op = input(":> ")
    
    if op == '1':
        wrapper(au.addInfo,data_users)
    elif op == '2':
        print(data_users)
        rs.os.system('pause')
    elif op == '3':
        sys.exit(rs.showSuccess('Vuelva pronto'))
    else:
        main_menu()
    
        