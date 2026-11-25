ingreso_mensual = 10000
gasto_mensual = 9000

#if anidados y else if (elif)

if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en defisit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("ahora si estas bien")
    else:
        print("estas gastando demasiado")
    
elif ingreso_mensual >= 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual >= 500:
    print("estas bien en argentina")
elif ingreso_mensual >= 200:
    print("estas bien en venezuela")
else:
    print("sos pobre")
