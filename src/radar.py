# programa.py
# -*- coding: utf-8 -*-
"""
Radares de tramo — Esqueleto para alumnos
- Lectura de fichero YA resuelta (función leer_casos).
- main() itera sobre las líneas y llama a procesar_linea(linea).
- procesar_linea(linea) está VACÍA; los alumnos deben implementarla.
"""

from typing import List
import sys
from pathlib import Path


def leer_casos(ruta_fichero: str) -> List[str]:
    """
    Lee un fichero de texto con casos de prueba, devolviendo
    una lista de líneas (str) ya limpias, sin la línea de terminación "0 0 0".
    Ignora líneas en blanco y comentarios que empiecen por '#'.
    """
    ruta = Path(ruta_fichero)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el fichero: {ruta_fichero}")

    casos: List[str] = []
    with ruta.open(encoding="utf-8") as f:
        for raw in f:
            linea = raw.strip()
            if not linea or linea.startswith("#"):
                continue
            if linea == "0 0 0":
                break
            casos.append(linea)
    return casos


def procesar_linea(linea: str) -> str:
    """
    TODO: Implementar por el alumnado.

    Recibe:
        linea (str): cadena con tres enteros: distancia_m, vmax_kmh, tiempo_s,
                     separados por espacios.

    Debe devolver uno de los textos EXACTOS:
        - "OK"
        - "MULTA"
        - "PUNTOS"
        - "ERROR"

    Recomendación:
    1) Parsear ints; si hay problema o valores inválidos -> "ERROR".
    2) Calcular la velocidad media y compararla con los umbrales.
    3) Devolver el texto pedido.
    """
    # --- Implementación del alumnado aquí ---
	numero1 = sys.argv[1]
	numero2 = sys.argv[2]
	numero3 = sys.argv[3]
		if numero1 < 0 or numero2 < 0 or nuemro3 < 0:
			print ("ERROR")
		else:
			distancia_m = int(round(numero1 / 100))
			vmax_kmh = int(numero2)
			tiempo_s = int(numero3)

			tiempo_m = tiempo_s / 60
			tiempo_h = tiempo_m / 60
			vmedia = 

			if vmedia <= vmax_kmh:
				print ("OK")
			elif vmedia - 20%:
				print ("MULTA")
			else:
				print ("PUNTOS")




    raise NotImplementedError("Función aún no implementada por el alumnado.")

# a main se llama de la siguiente forma  main(sys.argv)
def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("Uso: python programa.py <ruta_entrada.txt>")
        sys.exit(1)

    ruta = argv[1]
    for linea in leer_casos(ruta):
        resultado = procesar_linea(linea)   # <- llamada a la función de los alumnos
        print(resultado)                     # <- impresión del resultado

