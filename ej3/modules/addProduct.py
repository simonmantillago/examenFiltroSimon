import modules.reusable as rs
import modules.corefiles as cf

def addInfo(data):
    addMore = True
    while addMore:
        id = rs.checkInput('str','Ingrese el id del producto')
        nombre = rs.checkInput('str','Ingrese el nombre del producto')
        valorUnitario = rs.checkInput('float','Ingrese el valor unitario del producto')
        stockMin = rs.checkInput('int','Ingrese la cantidad minima de stock')
        stockMax = rs.checkInput('int','Ingrese la cantidad maxima de stock')
            
                
        
        new_product= {
            'id' : id,
            'nombre' : nombre,
            'valorUnitario' : valorUnitario,
            'stockMin': stockMin,
            'stockMax': stockMax
        }
        
        data['products'].update({id : new_product})
        cf.addData('products.json',data)
        addMore = rs.yesORnot('Desea ingresar otro producto?')