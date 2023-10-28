i= 1
suma= 1
s= 0
n= int(input(f"Ingrese un número."))
while i < n:
     i = i + 1
     s = s + i 
     suma =  suma * s
     if i == n:
          print(f"La suma es:", suma)