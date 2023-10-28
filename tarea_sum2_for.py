s= 0
m: int()
n:int()
n= int(input(f"Ingrese un número límite."))
if n > 0:
    m= n * 2
else:
   print(f"Ingrese un número válido")
for i in range(1,n+2): 
    s = s + 1
    m = m*s
else:
    for i in range(1,n+2):
     if i == n:
        break
    print("El resultado es:", m)