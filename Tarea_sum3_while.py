i= 2
suma= 1
s= 0
n= int(input(f"Ingrese un número."))
if n > 0:
    m = n * 2
while i < m:
     i = i + 2
     s = s + i 
     suma =  suma * s
     if i == m:
          print(f"La suma es:", suma)