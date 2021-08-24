def main():
    #escribe tu código abajo de esta línea
 viejo=350
 nuevo=1000
 compranueva=int(input("Dame la cantidad de juegos nuevos: "))
 compravieja=int(input("Dame la cantidad de juegos usados: "))
 totpagar= ((compravieja*viejo)+(compranueva*nuevo))
 print("El total de la compra es:",totpagar)




if __name__ == '__main__':
    main()
