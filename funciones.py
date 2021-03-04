import string


#se define la funcion check_char
def check_char(userin):

    #se define la lista de caracteres
    amay=string.ascii_uppercase
    azmay=list(amay)
    amin=string.ascii_lowercase
    azmin=list(amin)
    aztotal=azmay+azmin

    #los errores se llamaran utilizando asserts en el codigo
    
    #el primer assert corresponde al error del punto d
    #se comprueba que se trate de caracteres del alfabeto unicamente
    assert userin.isalpha(), "Error 3: La entrada no corresponde a un caracter o string"

    #el segundo assert corresponde al error del punto c
    #se comprueba si al menos un caracter esta fuera del rango a-Z
    #si un caracter esta fuera del rango, la variable rango toma el valor de 0
    rango=1
    for k in userin:
        if k not in aztotal:
            rango=0
    assert rango == 1, "Error 2: La entrada presenta al menos un caracter fuera del rango A-Z"

    #el tercer y ultimo assert corresponde al error del punto b
    #se comprueba si la longitud del string es igual a 1
    assert len(userin) == 1, "Error 1: La entrada contiene más de un caracter"

    #si se pasan todas estas pruebas, la funcion retorna el valor de 0
    return 0





#se define la función caps_switch
def caps_switch (userin):
    
    #se llama la función check_char para comprobar entrada válida
    if check_char (userin) == 0:
        #se cambia de mayuscula a minuscula o vice versa
        userin2 = userin.swapcase()
    return userin2



userin=input("Entrada: ")
print(caps_switch(userin))


