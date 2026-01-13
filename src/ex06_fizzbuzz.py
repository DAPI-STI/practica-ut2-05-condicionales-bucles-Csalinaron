"""
Ejercicio 6 (un poco más complejo):
FizzBuzz.
"""

def fizzbuzz(n: int) -> list[str]:
    """
    Devuelve una lista con los valores de 1 a n, siguiendo estas reglas:

    - Si el número es múltiplo de 3: "Fizz"
    - Si es múltiplo de 5: "Buzz"
    - Si es múltiplo de 3 y 5: "FizzBuzz"
    - En otro caso: el número en texto (por ejemplo "7")

    Si n <= 0, devuelve lista vacía.
    """
    if n <= 0:
        return []
    
    resultado = []
    for i in range(1, n + 1):
        texto = ""
        if i % 3 == 0:
            texto += "Fizz"
        if i % 5 == 0:
            texto += "Buzz"
        if texto == "":
            texto = str(i)
        resultado.append(texto)
    return resultado
    raise NotImplementedError("Implementa fizzbuzz(n)")
