import sys
from src.actividad1 import actividad_1

def main(options):
    if options[1] == "act_1":
        actividad_1()
        
    else:
        print("Comando no reconocido.")
        print("Uso: python main.py act_1")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Por favor, indique una opción. Ejemplo: python main.py act_1")
