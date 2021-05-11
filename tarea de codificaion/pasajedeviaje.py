def costodepasajes():
  #definir variables y otros
  montoP=0
  #datos de entrada
  cantidadX=int(input("ingrese la cantidad de estudiantes:"))
  #proceso
  if cantidadX>=100:
    montoP=cantidadX*20
  elif cantidadX<100 and cantidadX>49:
    montoP=cantidadX*35
  elif cantidadX<50 and cantidadX>19:
    montoP=cantidadX*40
  elif cantidadX<20:
    montoP=cantidadX*70
  #datos de salida
  print("el monto a pagar es:",montoP)
costodepasajes()