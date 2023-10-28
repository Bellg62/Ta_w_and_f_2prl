s= 0
suma= 0
rst = 0
n:int()
n= int(input(f"Ingrese un número límite."))
if n > 0:
    m= n * 2
for i in range(2,m+2): 
    s = s + 2
    suma = suma + s
    rst = rst * suma
else:
    for i in range(2,m+2):
     if i == m:
        break
    print("El resultado es:", suma)
    