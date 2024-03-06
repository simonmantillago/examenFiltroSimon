import modules.reusable as rs
from datetime import datetime
from tabulate import tabulate
import modules.corefiles as cf

def addPago(data):
    getEmpleado = rs.checkInput('str','Ingrese el id del empleado al que va a realizar le pago')
    if getEmpleado in data['empleados']:
        fecha=str(datetime.now().date())
        diasTrabajados = rs.checkInput('float','Ingrese la cantidad de dias trabajados')
        horasExtras = rs.checkInput('float','Ingrese la cantidad de horas extra trabajadas')
        sueldoBase = data['empleados'][getEmpleado]['salario']
        valorDia =(sueldoBase/30)
        descuentoxCafeteria = 0 
        siCafeteria = rs.yesORnot('El empleado tiene alguna cuenta sin pagar en la cafeteria?')
        if siCafeteria == True:
            descuentoxCafeteria = rs.checkInput('float','Ingrese la cantidad que debe en cafeteria')
        cuotaPrestamo = 0
        siCuota= rs.yesORnot('Se le cobra cuota por algun prestamo al empleado?')
        if siCuota == True:
            cuotaPrestamo = rs.checkInput('float','Ingrese la cuota por prestamos')
        meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
        isMes = True
        while isMes == True:
            mesPagado = rs.checkInput('str','Ingrese el mes que se esta pagando').upper()
            if mesPagado in meses:
                isMes = False
            else:
                isMes = True
                rs.showError('Mes no valido')
                
        fechaPago = fecha
        valorTotalHrasExtras = horasExtras * 5500
        totalAPagar = round((((valorDia*diasTrabajados)-descuentoxCafeteria)-cuotaPrestamo)+valorTotalHrasExtras,2)
        
        new_colilla = {
            'id': getEmpleado,
            'mesPagado' : mesPagado,
            'fechaPago' : fechaPago,
            'diasTrabajados': diasTrabajados,
            'sueldoBase' : sueldoBase, 
            'pagoHorasExtra' : valorTotalHrasExtras,
            'cuotaPrestamo' : cuotaPrestamo,
            'descuentoxCafeteria' : descuentoxCafeteria,
            'totalAPagar' : totalAPagar
        }
        data['colillas'].update({str(len(data['colillas'])).zfill(3) : new_colilla})
        cf.UpdateFile('nominas.json',data)
        rs.showSuccess('Pago realizado con exito')
    else:
        rs.showError('Empleado no se encuentra registrado')

def searchColilla(data):
    if len(data['colillas']):
        valor = input("Ingrese el id de la persona a buscar -> ").upper()
        rs.os.system('cls')
        for key,value in data['colillas'].items():
            if value['id'] == valor:
                print(f'NOMINAS REGISTRADAS DE {valor}')
                result= value
                id,mes,fecha,dias,base,horasExtra,prestamo,cafeteria,total = result.values()
                
                displayList = [['Id',id],['Mes',mes],['Fecha pago',fecha],['Dias Trabajados',dias],['Salario base',base],['Pago H.extra',horasExtra],['Cuota prestamo',prestamo],['Descuento Cafeteria',cafeteria],['Pago total',total]]
                print(tabulate(displayList,tablefmt="fancy_grid"))
                rs.os.system('pause')
                rs.os.system('cls')
                
            else:
                rs.showError(f'No hay colillas regitradas de ese empleado') 
    else: 
        rs.showError('No hay pagos registrados')
       
        
def nominasTotal(data):
    totalPagado = 0
    if len(data['colillas']):
        for key,value in data['colillas'].items():
            totalPagado += value['totalAPagar']
        print(f'El total pagado en nominas a empleados es {round(totalPagado,2)}')
        rs.os.system('pause')
        
    else: 
        rs.showError('No hay pagos registrados')