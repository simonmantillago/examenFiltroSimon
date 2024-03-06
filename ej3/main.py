"""Elabore un programa en Python que permita registrar los productos de una
Tienda de viveres. La información se debe almacenar en un archivo JSON. La
Información de los productos es la siguiente (20ptos):

id
nombre
valorUnitario
stockmin
stockmax
valorUnitario"""

import modules.corefiles as cf
import modules.menu as menu
infoProducts= {
   "products" : {}
}
def main():  
   cf.checkFile('products.json',infoProducts)
   menu.main_menu()
    

if __name__ == "__main__":
    main()