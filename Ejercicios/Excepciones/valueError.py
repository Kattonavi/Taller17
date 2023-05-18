edad = "veinte"
try:
    edad_numerica = int(edad)
    print("La edad numérica es:", edad_numerica)
except ValueError:
    print("Error: No se puede convertir la cadena de texto a un entero.")

# Error de value ya que se esta pidiendo un numero y no texto