import modules.reusable as rs
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
   
    
        