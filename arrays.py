nombres = ["Hugo", "Paco", "Luis"]

imprimir = lambda item: item.upper()

nombres_mapeados = list(map(imprimir, nombres))

print(nombres_mapeados)

obtener_luis = lambda item: item == "Luis"

nombres_filtrados = list(filter(obtener_luis, nombres))

print(nombres_filtrados)