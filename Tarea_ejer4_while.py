i= 1
suma= 0
s= 0
mult = 0
n= int(input(f"Ingrese un número."))
while i < n:
     i = i + 1
     s = s + i 
     mult= s * s * s
     suma =  suma + mult
     if i == n:
          print(f"La suma es:", suma)