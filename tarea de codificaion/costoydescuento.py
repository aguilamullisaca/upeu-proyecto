def costoydescuento():
  #definicion de variables
  montop=0
  #datos de entrada
  costoX=int(input("ingrese costo:"))
  #proceso
  if costoX>=200:
    montop=costoX*0.15
  elif costoX>=100 and costoX<200:
    montop=costoX*0.12
  elif costoX<100:
    montop=costoX*0.10
  #datos de salida
  print("el descuento es:",montop)
costoydescuento()