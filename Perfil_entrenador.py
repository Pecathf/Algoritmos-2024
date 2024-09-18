print ("Soy el profesor Oak")
genero = input("¿Eres chico o chica? ").lower()
if genero== "chico":
    print ("Entendido amigo, bienvenido ")
    edad= input("¿Cuantos años tienes? ")
    if int(edad)<18:
        print("Bueno tendremos cuidado contigo peque")
    elif int(edad)>18:
        print ("Entonces estas listo para la aventura ")
    else:
        print ("ingresa algo valido")
        
    region= input("Cuentame, de que region eres: kanto, johto, kalos o guatire ").lower()
    if region== 'kanto':
        print ("Excelente")
        iniciales= input("Que tipo de pokemon buscas: fuego,agua,planta ").lower()
        if iniciales== "fuego":
            print("Tu inicial es Charmander")
        elif iniciales== "agua":
            print("Tu inicial es Squirtle")
        elif iniciales== "planta":
            print ("Tu inicial es Bulbasaur")
        else:
            print ("Tienes que escoger algo valido 'genio'")
    elif region== "johto":
        print ("Interesante")
        inicialesj= input("Que tipo de pokemon buscas: fuego,agua,planta ").lower()
        if inicialesj== 'fuego':
            print ("Haz elegido a Cyndaquil")
        elif inicialesj== "agua":
            print ("haz elegido a Totodile")
        elif inicialesj== "planta":
            print ("Haz elegido a chikorita")
        else:
            print ("Se que debo ser para toda la familia pero provoca insultarte")
    elif region== "kalos":
        print ("Una de las regiones más populares, increible")
        inicialK= input("Que tipo de pokemon buscas: fuego,agua,planta ").lower()
        if inicialK== "fuego":
            print ("Por tu eleccion tienes a Fennekin")
        elif inicialK== 'agua':
            print ("Por tu eleccion tienes a Froakie")
        elif inicialK== "planta":
            print ("Por tu eleccion tienes a Chespin")
        else:
            print ("Me estas haciendo preguntarme muchas cosas y no estas respondiendo nada")
    elif region== "guatire":
        print ("La ubicacion que elegiste no tiene pokemones... Y mucho menos una aventura para tí ")
    else:
        print ("3 opciones y aun así elegiste no decir ninguna que increible")
elif genero== "chica":
    print ("Bienvenida a la aventura ")
    edad= input("¿Cuantos años tienes? ")
    if int(edad)<18:
        print("Entendible, te protegeremos ")
    elif int (edad)>18:
        print ("La edad perfecta para tu travesia")
    else:
        print ("Ingresa algo logico la proxima")
    region= input("Cuentame, de que region eres: kanto, johto, kalos o guatire ").lower()
    if region== 'kanto':
        print ("Excelente")
        iniciales= input("Que tipo de pokemon buscas: fuego,agua,planta ").lower()
        if iniciales== "fuego":
            print("Tu inicial es Charmander")
        elif iniciales== "agua":
            print("Tu inicial es Squirtle")
        elif iniciales== "planta":
            print ("Tu inicial es Bulbasaur")
        else:
            print ("Tienes que escoger algo valido 'genia'")
    elif region== "johto":
            print ("Interesante")
            inicialesj= input("Que tipo de pokemon buscas: fuego,agua,planta ").lower()
            if inicialesj== 'fuego':
                print ("Haz elegido a Cyndaquil")
            elif inicialesj== "agua":
                 print ("haz elegido a Totodile")
            elif inicialesj== "planta":
                print ("Haz elegido a chikorita")
            else:
                print ("Se que debo ser para toda la familia pero provoca insultarte")
    elif region== "kalos":
        print ("Una de las regiones más populares, increible")
        inicialK= input("Que tipo de pokemon buscas: fuego,agua,planta ").lower()
        if inicialK== "fuego":
            print ("Por tu eleccion tienes a Fennekin")
        elif inicialK== 'agua':
            print ("Por tu eleccion tienes a Froakie")
        elif inicialK== "planta":
            print ("Por tu eleccion tienes a Chespin")
        else:
                print ("Me estas haciendo preguntarme muchas cosas y no estas respondiendo nada")
    elif region== "guatire":
        print ("La ubicacion que elegiste no tiene pokemones... Y no es una aventura para todo el mundo ")
    else:
            print ("3 opciones y aun así elegiste no decir ninguna que increible")
