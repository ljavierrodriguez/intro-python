# loops

# for,  while

nombres = ["Hugo", "Paco", "Luis"]

for x in range(0, len(nombres), 1): # start (optional), stop, step (optional)
    if x == 1: break
    print(nombres[x])

for nombre in nombres:
    print(nombre)

i = 0
while(i < len(nombres)):
    print(nombres[i])
    i = i + 1   
