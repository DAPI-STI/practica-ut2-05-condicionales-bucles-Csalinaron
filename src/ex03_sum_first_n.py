"""
Ejercicio 3:
Suma de los primeros n números.
"""

def sum_first_n(n: int) -> int:
    """
    Devuelve la suma 1 + 2 + ... + n.

    - Si n <= 0, devuelve 0.
    - Debe resolverse usando un bucle (for o while).
    """
    if n <= 0:
        return 0

    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

    raise NotImplementedError("Implementa sum_first_n(n)")
