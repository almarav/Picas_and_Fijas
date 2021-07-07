import random


def generate_number():
  """
    Generar un número aleatorio de 4 digitos, donde no se repitan los digitos

    Parameters
    ----------
    void

    Returns
    ---------
    Tuple 
      Tupla de longitud 4, donde no se repita ningún digito, deben ser string los dígitos
  """
  
  digitos = ('0','1','2','3','4','5','6','7','8','9')

  codigo = []
  
  for i in range(4):
    num_elegido = random.choice(digitos)
    while num_elegido in codigo:
      num_elegido = random.choice(digitos)
    codigo.append(num_elegido)
  
  #print (codigo)

  return (codigo)



def picas_o_fijas(codigo, propuesta):
  """
    Dado un código y una propuesta, determinar mediante el juego de picas y fijas, 
    Si hay coincidencias o aciertos.
    - Un acierto es cuando un digito de la propuesta se encuentra en la misma posición.
    - Una coincidencia es cuando un digito se encuentra en el código, pero NO en la misma posición

    Parameters
    ----------
    codigo : tuple
    propuesta : string

    Returns
    ---------
    aciertos, coincidencias : int
  """
 
  aciertos = 0
  coincidencias = 0
  
  for i in range(len(propuesta)):
    if propuesta[i] == codigo[i]:
      aciertos = aciertos + 1
    elif propuesta[i] in codigo:
      coincidencias = coincidencias + 1

  return aciertos, coincidencias

