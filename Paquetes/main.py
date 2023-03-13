import my_paquete.aritmetica as a

def main():
    suma = a.sumar(4,5,5,6,4,1,2)
    resta = a.restar(25, 15)
    potecia = a.potencia(3, 3)

    print(f'La suma es: {suma}')
    print(f'La resta es: {resta}')
    print(f'La potencia es: {potecia}')

if __name__ == '__main__':
    main()