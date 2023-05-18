lista = [1, 2, 3]
try:
    elemento = lista[3]
    print("El elemento es:", elemento)
except IndexError:
    print("Error: El índice está fuera de rango.")

# Error de indentation ya que en python las listas estan indexadas desde el 0