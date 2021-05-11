def bonoantiguedad():
  #definir variables
  bonoA=100
  #datos de entrada
  añosX=int(input("ingrese su antiguedad:"))
  #proceso
  if añosX==1:
    montoB=bonoA
  elif añosX==2:
    montoB=bonoA*2
  elif añosX==3:
    montoB=bonoA*4
  elif añosX==4:
    montoB=bonoA*7
  elif añosX>=5:
    montoB=bonoA*10
  #datos de salida
  print("su bono por su antiguedad es:",montoB)
bonoantiguedad()