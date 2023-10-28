s= 0
suma: int= 0
n:int()
n= int(input(f"Ingrese primer número."))
n2= int(input(f"Ingrese segundo número"))
for i in range(n,n2+2): 
    s = s + 1
    suma = suma + s
else:
    for i in range(n,n2+2):
     if i == n2:
        break
    print("El resultado es:", suma)