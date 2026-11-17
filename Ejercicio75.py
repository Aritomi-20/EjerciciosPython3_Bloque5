def EscribirCentrado(texto):
    longitud = len(texto)
    espacios = 40 - (longitud//2)
    print(" " * espacios + texto)
    print(" " * espacios + "=" * longitud )

EscribirCentrado("Hola mundo")
EscribirCentrado("Python es genial")
EscribirCentrado("Programación")