from mate import aritmetica, geometrica

def main():
    print('Suma:', aritmetica.add(5, 3))
    print('Resta:', aritmetica.subtract(5, 3))
    print('Multiplicación:', aritmetica.multiply(5, 3))
    print('División:', aritmetica.divide(5, 3))
    print('Módulo:', aritmetica.modulo(5, 3))
    print('Potencia:', aritmetica.power(5, 3))

    print('Área del círculo:', geometrica.circle_area(5))

if __name__ == "__main__":
    main()
