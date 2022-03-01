import random
import os
def main(arg1):
    inp = arg1;
    inp = inp.lower()
    #respuestas 
    if inp == "hola":
        print('hola ')
    elif inp =='sos gay?': print('Nop =)')
    elif inp == "dime un numero random": print(random.randint(1,5))
    elif inp =='que': print('so')
    elif inp =='nazi': print('depende')
    elif inp=='cambiame el color a verde': os.system('color a')
    else:
        dev = input('respuesta:')
        print(f"Comando python:\n elif inp =='{inp}': print('{dev}')")

while True:
    arg1 = input('Comando:')
    main(arg1)