import string
import pytest


# se define la funcion check_char
def check_char(userin):

    # se define la lista de caracteres
    amay = string.ascii_uppercase
    azmay = list(amay)
    amin = string.ascii_lowercase
    azmin = list(amin)
    aztotal = azmay+azmin

    # los errores se llamaran utilizando asserts en el codigo

    # el primer assert corresponde al error del punto d
    # se comprueba que se trate de caracteres del alfabeto unicamente
    E3 = "Error 3: La entrada no corresponde a un caracter o string"
    assert userin.isalpha(), E3

    # el segundo assert corresponde al error del punto c
    # se comprueba si al menos un caracter esta fuera del rango a-Z
    # si un caracter esta fuera del rango, la variable rango toma el valor de 0
    rango = 1
    for k in userin:
        if k not in aztotal:
            rango = 0
    E2 = "Error 2: La entrada presenta caracteres fuera del rango A-Z"
    assert rango == 1, E2

    # el tercer y ultimo assert corresponde al error del punto b
    # se comprueba si la longitud del string es igual a 1
    assert len(userin) == 1, "Error 1: La entrada contiene más de un caracter"

    # si se pasan todas estas pruebas, la funcion retorna el valor de 0
    return 0


# se define la función caps_switch
def caps_switch(userin):

    # se llama la función check_char para comprobar entrada válida
    if check_char(userin) == 0:
        # se cambia de mayuscula a minuscula o vice versa
        userin2 = userin.swapcase()
    return userin2


# -------------------------------------------------------------------------------


# para probar check_char para todo el rango de a-Z
# se debe utilizar la parametrizacion
# primero se define la lista del alfabeto en minusculas y mayusculas
a = string.ascii_uppercase
ab = list(a)
b = string.ascii_lowercase
bz = list(b)
az = ab + bz

# se define una lista vacia que contiene los parametros por probar
param = []

# se crean tuplas con las entradas (caracteres a-z) y resultados (0)
for car in az:
    par = tuple((car, 0))
    # se añade cada tupla a la lista de parametros
    param.append(par)


# se define la parametrizacion
@pytest.mark.parametrize("test_input,expected", param)
# prueba de check_char para todos los casos de a-z
def test_check_char_1(test_input, expected):
    assert check_char(test_input) == expected


# para probar caps_switch para todo el rango de a-Z
# se debe utilizar la parametrizacion
# se utilizan las listas creadas en la parametrizacion anterior

# se define la lista vacia que contiene los parametros
param2 = []

# se crean las tuplas con la letra en mayuscula y
# minuscula y vice versa ((a,A),(A,a))
for a, b in zip(ab, bz):
    par = tuple((a, b))
    par2 = tuple((b, a))
    # se añaden los pares de tuplas a la lista
    param2.append(par)
    param2.append(par2)


# se define la parametrizacion
@pytest.mark.parametrize("test_input2,expected2", param2)
# prueba de caps_switch para todo el rango A-Z
def test_caps_switch(test_input2, expected2):
    assert caps_switch(test_input2) == expected2


# prueba check_char con mas de un caracter
def test_check_char_2():
    with pytest.raises(AssertionError):
        check_char("ITCR")


# prueba check_char con entrada fuera de rango
def test_check_char_3():
    with pytest.raises(AssertionError):
        check_char("Año")


# prueba check_char con otro tipo de dato
def test_check_char_4():
    with pytest.raises(AssertionError):
        check_char("42")
