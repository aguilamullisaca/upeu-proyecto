def tipodevacuna():
  #definir variables y otros
  vacunaA="A"
  vacunaB="B"
  vacunaC="C" 
  #datos de entrada
  pedad=int(input("ingrese edad de la persona:"))
  genero=input("ingrese genero del paciente:")
  #proceso
  if pedad>=70:
    pedad=vacunaC
  elif pedad<=69 and pedad>=16 and genero=="mujer":
    genero=generoM
    pedad=vacunaB
  elif pedad<=69 and pedad>=16 and genero=="varon":
    pedad=vacunaA
  elif pedad<16:
    pedad=vacunaA
  #datos de salida
  print("recibe vacuna de tipo:",pedad)
tipodevacuna()