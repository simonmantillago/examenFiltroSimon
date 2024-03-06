import modules.reusable as rs
import modules.corefiles as cf
def addInfo(data):
    addMore = True
    while addMore:
        id = rs.checkInput('str','Ingrese el id del usuario')
        nombre = rs.checkInput('str','Ingrese el nombre del usuario')
        apellido = rs.checkInput('str','Ingrese el apellido del usuario')
        direccion = rs.checkInput('str','Ingrese la direccion del usuario')
        ciudad = rs.checkInput('str','Ingrese la ciudad del usuario')
        longitud = rs.checkInput('float','Ingrese la longitud en la que se encuentra usuario')
        latitud = rs.checkInput('float','Ingrese la latitud en la que se encuentra usuario')
        email = rs.checkInput('str','Ingrese el email del usuario')
        edad = rs.checkInput('int','Ingrese la edad del usuario')
        ocupacion = rs.checkInput('str','Ingrese la ocupacion del usuario')
        
        new_user= {
            'id' : id,
            'nombres' : nombre,
            'apellidos': apellido,
            'ubicacion': {
                'direccion': direccion,
                'ciudad' : ciudad,
                'longitud': longitud,
                'latitud': latitud
            },
            'email' : email,
            'edad': edad,
            'ocupacion': ocupacion
        }
        
        data['users'].update({id : new_user})
        cf.addData('users.json',data)
        addMore = rs.yesORnot('Desea ingresar otro usuario?')