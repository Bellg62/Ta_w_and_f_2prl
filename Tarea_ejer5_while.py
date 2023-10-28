suma= 0
s= 0
n= int(input(f"Ingrese primer número."))
n2 = int(input(f"Ingrese segundo número."))
while n < n2:
     n = n + 1
     s = s + n 
     suma =  suma + s
     if n == n2:
          print(f"La suma es:", suma)