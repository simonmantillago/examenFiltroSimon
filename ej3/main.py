import modules.corefiles as cf
import modules.menu as menu
infoUser= {
   "users" : {}
}
def main():  
   cf.checkFile('users.json',infoUser)
   menu.main_menu()
    

if __name__ == "__main__":
    main()