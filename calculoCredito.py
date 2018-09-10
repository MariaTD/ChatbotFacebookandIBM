
def GetValorDeCuota(monto):
    
    """
    Retorna el valor actual de la cuota, según el 
    método francés en donde las cuotas son fijas.
                
    Formula = R = P [(i (1 + i)**n) / ((1 + i)**n – 1)]. 
    Donde: 
        C = renta (cuota)
        P = principal (préstamo adquirido)
        i = tasa de interés
        n = número de periodos
    """
    tasa=1.35
    tasa = tasa / 100.0
    #R12 corresponde a la couta con plazo de 12 meses
    cuotas=12
    if "$" in monto:
        monto=monto.replace("$","")

    if "," in monto:
        monto=monto.replace(",","")
    elif "." in monto:
        monto=monto.replace(".","")
        
    monto=float(monto)

    valor = monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) )
    cuotas=24
    valor2 = monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) )
    cuotas=36
    valor3 = monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) )
    R = [valor, valor2, valor3]
    Cuota=[]
    Meses=['12 Meses','24 Meses', '36 Meses']
    for r in range (0,3):
        Moneda=setMoneda(R[r])
        Cuota.append((Meses[r],Moneda))
    print (Cuota)
    mensaje = setMensaje(Cuota)
    return mensaje
    
    

def setMoneda(num, simbolo="$", n_decimales=2):
    #se redondea a los decimales idicados.
    num = round(num, n_decimales)
    #se divide el entero del decimal y obtenemos los string
    num, dec = str(num).split(".")
    #si el num tiene menos decimales que los que se quieren mostrar,
    #se completan los faltantes con ceros.
    dec += "0" * (n_decimales - len(dec))
    #se invierte el num, para facilitar la adicion de comas.
    num = num[::-1]
    #se crea una lista con las cifras de miles como elementos.
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    #se pasa la lista a string, uniendo sus elementos con comas.
    num = str.join(",", l)
    if not n_decimales:
        return "%s %s" % (simbolo, num)
        
    return "%s %s.%s" % (simbolo, num, dec)


def setMensaje(cuota):

    mensje = "Para el valor de credito que deseas te ofrecemos las siguientes opciones de pago dependiendo del tiempo al que desees diferirlo. A " + cuota[0][0] +", tu CMV seria de " + cuota[0][1] + ". Si deseas tomarlo a "+ cuota[1][0] +", tu CMV seria de " + cuota[1][1] + ". Si deseas tomarlo a "+ cuota[2][0] +"tu CMV seria de " + cuota[2][1] +". Espero te haya sido util la información. Te interesa aplicar para obtener el credito ?"
    return mensje




        



