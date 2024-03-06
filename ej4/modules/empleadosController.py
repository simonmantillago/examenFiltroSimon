import modules.reusable as rs
import modules.corefiles as cf

def addInfo(data):
    addMore = True
    while addMore == True:
        id = rs.checkInput('str','Ingrese el id del empleado')
        if id in data['empleados']:
            rs.showError('Ese id ya se encuentra registrado')
            return
            
        nombre = rs.checkInput('str','Ingrese el nombre del empleado')
        cargo = rs.checkInput('str','Ingrese el cargo del empleado')
        salario = rs.checkInput('float','Ingrese el salario base del empleado')
        
            
                
        
        new_empleado= {
            'id' : id,
            'nombre' : nombre,
            'cargo' : cargo,
            'salario': salario
        }
        
        data['empleados'].update({id : new_empleado})
        cf.addData('nominas.json',data)
        addMore = rs.yesORnot('Desea ingresar otro empleado?')
        