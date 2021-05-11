def polizadeseguros():
  #definir variables y otros
  Tplan=0
  #datos de entrada
  Tplan=int(input("ingrese su tipo de plan:"))
  alcohol=input("ingiere alcohol:")
  lentes=input("utiliza lentes:")
  enfermedad=input("padece alguna enfermedad:")
  edad=int(input("es mayor de 40 años:"))
  #proceso
  if Tplan==1200 and alcohol=="si" and lentes=="si" and enfermedad=="deficiencia cardiaca" or "diabetes" and edad>=40:
    plan=Tplan+1200*0.10+1200*0.05+1200*0.05+1200*0.20
  elif Tplan==1200 and alcohol=="no" and lentes=="si" and enfermedad=="deficiencia cardiaca" or "diabetes" and edad>=40:
    plan=Tplan+1200*0.05+1200*0.05+1200*0.20
  elif Tplan==1200 and alcohol=="si" and lentes=="no" and enfermedad=="deficiencia cardiaca" or "diabetes" and edad>=40:
    plan=Tplan+alcohol+enfermedad+edad41
  elif Tplan==1200 and alcohol=="si" and lentes=="si" and enfermedad=="ninguna" and edad>=40:
    plan=Tplan+alcohol+lentes+edad41
  elif Tplan==1200 and alcohol=="si" and lentes=="si" and enfermedad=="deficiencia cardiaca" or "diabetes" and edad<=40:
    plan=Tplan+alcohol+lentes+enfermedad+edad39
  elif Tplan==950 and alcohol=="si" and lentes=="si" and enfermedad=="deficiencia cardiaca" or "diabetes" and edad<=40:
    plan=Tplan+alcohol+lentes+enfermedad+edad39
  #datos de salida
  print("la poliza le cuesta:",plan)
polizadeseguros()