from pip._vendor.distlib.compat import raw_input
from sympy import *

def es_primo(numero):
    for i in range(2, numero):
        if(numero%i)==0:
            print("\nEl numero NO %s es primo" % numero)
        print("\nEl numero %s es primo" % numero)


def mcd(a, b):
    if (a == 0):
        return b
    return mcd(b % a, a)


def phi(n):
    result = 1
    for i in range(2, n):
        if (mcd(i, n) == 1):
            result += 1
    return result


def mod(a,b):
    return a % b


def bezout(a, b):

    if a < b:
        a, b = b, a

    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q, r = divmod(r1, r2)
        r1, r2 = r2, r
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2

    print(r1, s1, t1)


def inverso_modular(a, b):
    num = a**(phi(b)-1)
    return mod(num, b)


# Operaciones con polinomios
def polinomio_prod(p1, p2):
    sympy.init_printing()
    x, y = sympy.symbols('x,y')

    poly1 = sympy.Poly(p1)
    poly2 = sympy.Poly(p2)

    result= poly1 * poly2
    return result


def polinomio_div(p1, p2):
    # sympy.init_printing()
    # x, y = sympy.symbols('x,y')
    x = Symbol('x')

    c, r = div(p1,p2)
    return [c, r]




while True:
    # try:
        print("")
        print("1- Número primo");
        print("2- Identidad de Bézout");
        print("3- MCD");
        print("4- Fi de Euler");
        print("5- Entero mod entero")
        print("6- Inverso modular enteros")
        print("7- Producto de polinomios")
        print("8- Division de polinomios")
        print("")
        opcion = int(input("escoge opción, 0 para salir >>"))
        if opcion==0:
            break
        if opcion==1:
            print("")
            numero = int(input("inserta un numero, 0 para salir >> "))
            if numero==0:
                break
            es_primo(numero)
        if opcion==2:
            print("")
            a = int(input('Please enter the first number, "a":\n'))
            b = int(input('Please enter the second number, "b":\n'))
            bezout(a, b)
        if opcion==3:
            print("")
            a = int(input('Please enter the first number, "a":\n'))
            b = int(input('Please enter the second number, "b":\n'))
            print(mcd(a,b))
        if opcion==4:
            print("")
            n = int(input('Please enter the number, "n":\n'))
            print(phi(n))
        if opcion==5:
            print("")
            a = int(input('Please enter the first number, "a":\n'))
            b = int(input('Please enter the second number, "b":\n'))
            print(mod(a,b))
        if opcion==6:
            print("")
            a = int(input('Please enter the first number, "a":\n'))
            b = int(input('Please enter the second number, "b":\n'))
            print(inverso_modular(a, b))
        if opcion==7:
            print("")
            p1 = input("Primer Polinomio: ")
            p2 = input("Segundo Polinomio: ")
            print(polinomio_prod(p1, p2))
        if opcion==8:
            print("")
            p1 = input("Primer Polinomio: ")
            p2 = input("Segundo Polinomio: ")
            # p1 = "x**2 + 4"
            # p2 = "4*x + 1"
            c,r = polinomio_div(p1, p2)
            print("C =  ", c)
            print("R =  ", r)

    # except:
    #     print ("\nEl numero tiene que ser entero")