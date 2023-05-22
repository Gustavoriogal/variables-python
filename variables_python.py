git Estructuras de control en Python
Indentación (sangría) en python

Esta es una de las principales señas de identidad de Python y es fuente de una gran parte de los errores que se producen. En Python, las líneas de código que están dentro de un mismo

deben estar agrupadas, teniendo el mismo número de espacios a la izquierda de cada línea, al igual que sucedería en la vida real. A modo de ejemplo:

    Carrefour
        Carnicería
            Cerdo
            Pollo
        Pescadería
    Lidl
        Frutería
            Peras
            Manzanas
    …

Este siguiente caso no sería correcto, y en Python generaría un error (o el funcionamiento no sería el esperado):

    Lidl
        Frutería
            Peras
        Manzanas

Lógicamente, Manzanas no puede estar al mismo nivel que Frutería.

En Python, se recomienda usar siempre bloques de cuatro espacios, aunque si se usan otro número de espacios, también funcionaría. También se pueden usar tabuladores, aunque se recomienda no usarlos.

 
if en Python

En todo programa que se precie, llega el momento en el que se llega a una bifuración y que en función de una determinada condición, hay que realizar una serie de cosas u otra.

Esto se hace con el comando if (condición principal), con los opcionales elif (condiciones adicionales, se pueden poner tantas como se quiera) y else (si no se ha cumplido ninguna de las anteriores, sólo se puede poner una vez y al final).

A modo de ejemplo:

>>> Alonso_Position=1
>>> if (Alonso_Position==1):
>>>     print("Espectacular Alonso, se ha hecho justicia a pesar del coche")
>>>     print("Ya queda menos para ganar el mundal")
>>> elif (Alonso_Position>1):
>>>     print("Gran carrera de Alonso, lástima que el coche no esté a la altura")
>>> else:
>>>     print("No ha podido terminar la carrera por una avería mecánica")

Como se ve, las líneas que están dentro de cada if o elif, tienen el mismo número de espacios a la izquierda.
Condiciones en Python

Las condiciones que se suelen usar con más frecuencia son:

     a == b –> Indica si a es igual a b
    a < b
    a > b
    not –> NO: niega la condición que le sigue.
    and –> Y: junta dos condiciones que tienen que cumplirse las dos
    or –> O: junta dos condiciones y tienen que cumplirse alguna de las dos.
