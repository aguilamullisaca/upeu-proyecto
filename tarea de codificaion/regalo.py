def regalodefebrero():
  #definir variables y otros
  tarjeta="tarjeta"
  chocolate="chocolate"
  flores="flores"
  anillos="anillos"
  #datos de entrada
  costox=int(input("ingrese costo:"))
  #proceso
  if costox<=10:
    costox=tarjeta
  elif costox<=100 and costox>=11:
    costox=chocolate
  elif costox<=250 and costox>=101:
    costox=flores
  elif costox>=251:
    costox=anillos
  #datos de salida
  print("le alcanza para:",costox)
regalodefebrero()