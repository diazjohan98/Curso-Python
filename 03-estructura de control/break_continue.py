
c = 0

while c < 10:
    c += 1
    print(c)
    
    if c == 5:
        # print('termina el bucle')
        print('Salta a la siguiente iteracion')
        #break
        continue
    print('despues de continue')
else:
    print('Fin de while')