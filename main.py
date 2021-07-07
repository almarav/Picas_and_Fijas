import juego as juego

def iniciar_juego():
  # generación del código, por ejemplo (1, 2, 3, 4)
  codigo = juego.generate_number()

  # iniciamos interaccion con el usuario*
  print( "Bienvenidos al juego" )
  print( "Tienes que adivinar un número de 4 cifras distintas.")
  print()

  intentos = 0
  propuesta = input("¿Que código propones?: ")
  aciertos = 0
  coincidencias = 0
  while True:
      if len(propuesta) != 4:
          print("El número debe contener 4 digitos")
          propuesta = input("¿Que código propones?: ")
          continue
      
      intentos = intentos + 1
      
      aciertos, coincidencias = juego.picas_o_fijas(codigo, propuesta)
      
      print ("Tu propuesta (", propuesta, ") tiene", aciertos, "fijas y ", coincidencias, "picas.")
      if aciertos == 4:
        break
      
      propuesta = input("¿Que código propones?: ")

  print("Ganaste, tu número de intentos fue: {}".format(intentos))


if __name__ == '__main__':
  iniciar_juego()