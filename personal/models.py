import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from math import floor
from flask import Flask, render_template, request, flash
from .forms import ContactForm
from flask_mail import Message, Mail
from . import mail


bp = Blueprint('models', __name__)

estado = None
contador = 0
personaActual = None
maxMotos = 2
actualMotos = maxMotos

#region Listas

informacion = {
    0: ["8:00-8:30", "Free", contador],
    1: ["8:30-9:00", "Free", contador],
    2: ["9:00-9:30", "Free", contador],
    3: ["9:00-10:00", "Free", contador],
    4: ["10:00-10:30", "Free", contador],
    5: ["10:30-11:00", "Free", contador],
    6: ["11:30-11:30", "Free", contador],
    7: ["11:30-12:00", "Free", contador],
    8: ["12:00-12:30", "Free", contador],
    9: ["12:30-13:00", "Free", contador],
    10: ["13:00-13:30", "Free", contador],
    11: ["13:30-14:00", "Free", contador],
    12: ["14:00-14:30", "Free", contador],
    13: ["14:30-15:00", "Free", contador],
    14: ["15:00-15:30", "Free", contador],
    15: ["15:30-16:00", "Free", contador],
    16: ["16:00-16:30", "Free", contador],
    17: ["16:30-17:00", "Free", contador],
    18: ["17:00-17:30", "Free", contador],
    19: ["17:30-18:00", "Free", contador],
    20: ["18:30-19:00", "Free", contador],
    21: ["19:00-19:30", "Free", contador],
    22: ["19:30-20:00", "Free", contador]
}


personas = {
    "persona1": {
        0: ["Free"],
        1: ["Free"],
        2: ["Free"],
        3: ["Free"],
        4: ["Free"],
        5: ["Free"],
        6: ["Free"],
        7: ["Free"],
        8: ["Free"],
        9: ["Free"],
        10: ["Free"],
        11: ["Free"],
        12: ["Free"],
        13: ["Free"],
        14: ["Free"],
        15: ["Free"],
        16: ["Free"],
        17: ["Free"],
        18: ["Free"],
        19: ["Free"],
        20: ["Free"],
        21: ["Free"],
        22: ["Free"]
    },
    "persona2": {
        0: ["Free"],
        1: ["Free"],
        2: ["Free"],
        3: ["Free"],
        4: ["Free"],
        5: ["Free"],
        6: ["Free"],
        7: ["Free"],
        8: ["Free"],
        9: ["Free"],
        10: ["Free"],
        11: ["Free"],
        12: ["Free"],
        13: ["Free"],
        14: ["Free"],
        15: ["Free"],
        16: ["Free"],
        17: ["Free"],
        18: ["Free"],
        19: ["Free"],
        20: ["Free"],
        21: ["Free"],
        22: ["Free"]
    },
    "persona3": {
        0: ["Free"],
        1: ["Free"],
        2: ["Free"],
        3: ["Free"],
        4: ["Free"],
        5: ["Free"],
        6: ["Free"],
        7: ["Free"],
        8: ["Free"],
        9: ["Free"],
        10: ["Free"],
        11: ["Free"],
        12: ["Free"],
        13: ["Free"],
        14: ["Free"],
        15: ["Free"],
        16: ["Free"],
        17: ["Free"],
        18: ["Free"],
        19: ["Free"],
        20: ["Free"],
        21: ["Free"],
        22: ["Free"]
    }
}

#endregion

#region Problema1
def addMoto(key):
    if informacion[key][2]<maxMotos:
        contador =  informacion[key][2] + 1
        informacion[key][2] = contador

def delMoto(key):
    if informacion[key][2]>0:
        contador =  informacion[key][2] - 1
        informacion[key][2] = contador

@bp.route('/problema1/<string:nombre>/', methods=['POST'])
def selectPerson(nombre):
    personaActual = nombre

    return render_template('problema1.html', informacion=informacion, personas=personas, personaActual=personaActual)


def assignSlot(estado):
    if estado == None:
        estado = "Free"
    ocupacion = estado
    return ocupacion


@bp.route('/problema1/<string:personaActual>/take/<int:hora>/', methods=['POST'])
def take(personaActual, hora):
    estado = "Selected"
    personas[personaActual][hora][0] = assignSlot(estado)
    addMoto(hora)

    return redirect(url_for('models.index'))


@bp.route('/problema1/<string:personaActual>/drop/<int:hora>/', methods=['POST'])
def drop(personaActual, hora):
    estado = "Free"
    personas[personaActual][hora][0] = assignSlot(estado)
    delMoto(hora)
    
    return redirect(url_for('models.index'))


@bp.route('/problema1/')
def index():
    return render_template('problema1.html', informacion=informacion, personas=personas, personaActual=personaActual)

#endregion


#region 3 amigos con 1 cleta

def checkFloat(number):
    try:
        number = float(number)
        return number
    except:
        flash("Por favor ingrese un valor numérico")
        return render_template('problema2.html')




@bp.route('/problema2/', methods=['POST'])
def calculo():
    if request.method == "POST":
        iteraciones = request.form['iteracion']

    iteraciones = checkFloat(iteraciones)
    distancia = 300 #en kilometros
    bikeSpeed = 60  # en kilometros por hora
    personSpeed = 15 # en kilometros por hora
    persona1 = 0
    persona2 = 0
    persona3 = 0
    totalTime = 0.000
    deltaTime = 1/3600 # corresponde a 1 minuto, puede ser cualquiera, dado que es los espacios de integracion que se usaran solamente.
    count = 0 # personas que han llegado
    persona2Reversa = False
    persona3InBike = False
    # forma = input("""
    # Eliga una de las dos formas: 
    #     1 : Llega a persona y vuelve a buscar al segundo que estaba caminando.
    #     2 : Si elige forma 2 debe elegir el numero de iteraciones, siento 1 el minimo y 1800 el maximo (ideal 180).
    # >   """)
    forma = "2"

    if forma == "1":

        # Forma 1 
        while(count < 3):
            if persona1>=distancia:
                count = 1
                persona2Reversa = True
            else:
                persona1 += bikeSpeed*deltaTime

            if persona2Reversa:
                persona2 -= bikeSpeed*deltaTime
            else :
                persona2 += bikeSpeed*deltaTime


            if persona2<=persona3:
                persona3InBike = True
                perona2Reversa = False

            if persona3InBike:
                persona3 += bikeSpeed*deltaTime
                if persona3>=distancia:
                    count += 2
            else :
                persona3 += personSpeed*deltaTime

            totalTime += deltaTime

        else:
            pass
            # print(f"Llegaron los 3 en un tiempo: {totalTime}")

    if forma == "2":
        try:
            distanciaIterada = distancia/iteraciones
        except:
            flash("Por favor ingrese un valor numérico")
            return render_template('problema2.html')

        numIteracion = 1
        persona1NotArrive = True
        persona2NotArrive = True
        persona3NotArrive = True
        llevandoPersona3 = False
        # Forma 2

        # Aca empiezo el ciclo
        while(count < 3):
            # Llevando persona 1
            if llevandoPersona3==False:

                if persona1 >= distanciaIterada*numIteracion:
                    llevandoPersona3 = True

                persona1 += bikeSpeed*deltaTime
                persona2 += bikeSpeed*deltaTime
                persona3 += personSpeed*deltaTime

            # Llevando persona 3
            elif llevandoPersona3:

                if persona2<=persona3:
                    persona3InBike = True
                if persona3 >= persona1:
                    llevandoPersona3 = False
                    numIteracion += 1
                    persona3InBike = False


                if persona3InBike:
                    persona2 += bikeSpeed*deltaTime
                    persona3 += bikeSpeed*deltaTime
                else:
                    persona2 -= bikeSpeed*deltaTime
                    persona3 += personSpeed*deltaTime
                
                persona1 += personSpeed*deltaTime


            #Se cuenta tiempo transcurrido
            totalTime += deltaTime
            # Cuenta si llegaron las personas
            if persona1>=distancia and persona1NotArrive :
                count += 1
                persona1NotArrive = False


            if persona2>=distancia and persona2NotArrive :
                count += 1
                persona2NotArrive = False


            if persona3>=distancia and persona3NotArrive :
                count += 1
                persona3NotArrive = False

        else:
            return render_template('resultado2.html', resultado=totalTime)


@bp.route('/problema2/')
def problema2():
    return render_template('problema2.html')
#endregion

#region Heraldo

def heraldo():
    niveles=[6,7,8,9,10,11,12]
    hp = []
    dmg = []
    eye = []
    for i,nivel in enumerate(niveles):
        hp.append(7125 + ((nivel-6)*((7125)/6)))
        dmg.append(855 + ((nivel-6)*((1710-855)/6)))
        eye.append((7125 + ((nivel-6)*((7125)/6)))*0.15)
        
    return niveles, hp, dmg, eye

@bp.route('/problema3')
def problema3():
    lvls, hp, dmg, eye = heraldo()
    return render_template('problema3.html', lvls=lvls, hp=hp, dmg=dmg, eye=eye)


#endregion


#region Multiplicacion

@bp.route('/problema4', methods=['POST'])
def multiplicador():
    """
    We multiply depending on the entered parameters in the function,
    being integers or float needed.
    """
    
    if request.method == "POST":
        numero_1 = request.form['numero1']
        numero_2 = request.form['numero2']
    
    if type(numero_1)==str or type(numero_2)==str: 
        try:
            numero_1 = int(numero_1)
            error = None
        except:
            try:
                numero_1 = float(numero_1)
                error = None
            except:
                error = "Ingrese valores validos"                
                return render_template('problema4.html', error=error)

    if type(numero_1)==str or type(numero_2)==str: 
        try:
            numero_2 = int(numero_2)
            error = None
        except:
            try:
                numero_2 = float(numero_2)
                error = None
            except:
                error = "Ingrese valores validos"
                return render_template('problema4.html', error=error)




    bothIntCondition = type(numero_1)==int and type(numero_2)==int
    bothFloatCondition = type(numero_1)==float and type(numero_2)==float
    oneFloatCondition = ((type(numero_1)==float or type(numero_1)==int) and
                      (type(numero_2)==float or type(numero_2)==int))
    result = 0
    decimalResult = 0
    

    if bothIntCondition:
        aux = True #Variable used to know in what condition did we enter
        for i in range(numero_1):
            result += numero_2 
            
    elif bothFloatCondition:
        aux = True
        #Variables for number 1
        float_numero_1 = str(numero_1)
        numbers_1 = float_numero_1.split(".")
        decimals_1 = len(numbers_1[1])
        noDec1 = int(numbers_1[0] + numbers_1[1])
        #Variables for number 2
        float_numero_2 = str(numero_2)
        numbers_2 = float_numero_2.split(".")
        decimals_2 = len(numbers_2[1])
        noDec2 = int(numbers_2[0] + numbers_2[1])

        #Now we use an if statement to do the shorter loop and save resources
        if decimals_1>decimals_2:
            #First we calculate the result of the multiplication
            #  of the second number by the floor of the first number.
            for i in range(floor(numero_1)):
                result += numero_2 
            
            #We considerate the zeros in the decimal value
            # of the first number after the '.' and before the fist number
            #  by adding a x10 to the second number

            #We calculate the addition decimal value
            for i in range(noDec2):
                decimalResult += int(numbers_1[1])
            
            #We transform decimalResult to the real value we need
            decimalResultStr = str(decimalResult)
            decimalResultLen = len(str(decimalResult))
            vecesCorrerPunto = decimals_1 + decimals_2
            puntoToRight = decimalResultLen-vecesCorrerPunto
                        
            if puntoToRight==0:
                decimalResultStr = "0." + decimalResultStr
            elif puntoToRight>0:
                decimalResultStr = decimalResultStr[0:puntoToRight]+"."+decimalResultStr[puntoToRight:]

            while(vecesCorrerPunto > len(decimalResultStr)):
                decimalResultStr = "0" + decimalResultStr
            
            decimalResult = float(decimalResultStr)
            result += decimalResult
            
        else:
            #First we calculate the result of the multiplication
            #  of the second number by the floor of the first number.
            for i in range(floor(numero_2)):
                result += numero_1
            
            #We considerate the zeros in the decimal value
            # of the first number after the '.' and before the fist number
            #  by adding a x10 to the second number

            #We calculate the addition decimal value
            for i in range(noDec1):
                decimalResult += int(numbers_2[1])
            
            #We transform decimalResult to the real value we need
            decimalResultStr = str(decimalResult)
            decimalResultLen = len(str(decimalResult))
            vecesCorrerPunto = decimals_1 + decimals_2
            puntoToRight = decimalResultLen-vecesCorrerPunto
                        
            if puntoToRight==0:
                decimalResultStr = "0." + decimalResultStr
            elif puntoToRight>0:
                decimalResultStr = decimalResultStr[0:puntoToRight]+"."+decimalResultStr[puntoToRight:]

            while(vecesCorrerPunto > len(decimalResultStr)):
                decimalResultStr = "0" + decimalResultStr
            
            decimalResult = float(decimalResultStr)
            result += decimalResult

    elif oneFloatCondition:
        aux = True
        if type(numero_1)==int:
            for i in range(numero_1):
                result += numero_2 
        else:
            for i in range(numero_2):
                result += numero_1

    else:
        error = "Error desconocido"
        return render_template('problema4.html', error=error)


    return render_template('resultado4.html', resultado=result)


@bp.route('/problema4')
def problema4():
    try:
        error
    except NameError:
        error = None
    return render_template('problema4.html', error=error)
#endregion



#region Contact

@bp.route('/contact', methods=['GET', 'POST'])
def contact():

    form = ContactForm(request.form)
 
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)

        else:
            msg = Message(form.subject.data, sender=os.environ.get("SEND_USERNAME"), recipients=[os.environ.get("RECEIVE_USERNAME")])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            flash('Mensaje enviado exitosamente.')
            return render_template('index.html', form=form)
    
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

#endregion