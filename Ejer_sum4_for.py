s= 0
suma: int= 0
n:int()
n= int(input(f"Ingrese un número límite."))
for i in range(1,n+2): 
    s = s + 1
    cub = s * s * s
    suma = suma + cub
else:
    for i in range(1,n+2):
     if i == n:
        break
    print("El resultado es:", suma)