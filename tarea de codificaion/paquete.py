def paquetedecompra():
  #definir variables y otros
  paqueteA="paquete A= television, un modular, tres pares de zapatos, cinco camisas y cinco pantalones"
  paqueteB="paquete B= una grabadora, cinco pares de zapatos, cinco camisas y cinco pantalones"
  paqueteC="paquete C= dos pares de zapatos, tres camisas y tres pantalones"
  paqueteD="paquete D= un par de zapatos, dos camisas y dos pantalones"
  #datos de entrada
  montoT=int(input("ingrese dinero recibido en diciembre:"))
  #proceso
  if montoT>=50000:
    montoT=paqueteA
  elif montoT>=20000 and montoT<50000:
    montoT=paqueteB
  elif montoT>=10000 and montoT<20000 :
    montoT=paqueteC
  elif montoT<10000:
    montoT=paqueteD
  #datos de salida
  print("le alcanza para el:",montoT)
paquetedecompra()