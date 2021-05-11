def calificaciones():
  #definicion de variables y otros
  notaA="A"
  notaB="B"
  notaC="C"
  notaD="D"
  notaF="F"
  #datos de entrada
  notaX=int(input("ingrese la nota:"))
  #proceso
  if notaX>9 and notaX<11:
    notaX=notaA
  elif notaX>8 and notaX<10:
    notaX=notaB
  elif notaX>7 and notaX<9:
    notaX=notaC
  elif notaX>5 and notaX<8:
    notaX=notaD
  elif notaX>=0 and notaX<6:
    notaX=notaF
  #datos de salida
  print("su calificacion es:",notaX)
calificaciones()