#!/usr/bin/python3
"""
This function determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    This function determines if all the boxes can be opened
    """
    cajas_abiertas = set()
    cajas_abiertas.add(0)
    por_explorar = [0]
    while por_explorar:
        caja_actual = por_explorar.pop()
        for llave in boxes[caja_actual]:
            if llave < len(boxes) and llave not in cajas_abiertas:
                cajas_abiertas.add(llave)
                por_explorar.append(llave)
    return len(cajas_abiertas) == len(boxes)
