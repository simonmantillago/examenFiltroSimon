import modules.corefiles as cf
import modules.menu as menu


pagos= {
   "empleados" : {},
   'colillas' : {}
}
def main():  
   cf.checkFile('nominas.json',pagos)
   menu.main_menu()
    

if __name__ == "__main__":
    main()