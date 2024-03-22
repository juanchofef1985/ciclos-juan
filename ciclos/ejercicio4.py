def generar_cuadrados(n):
     if 2 * n <= 30:
         cuadrados = [i ** 2 for i in range(1,31)]
         
         return cuadrados[:n] + cuadrados[-n:]
    else:
     raise valueError('n no debe ser mayor a 2*n')
        
resultado = generar_cuadrados(5)

print(resultado)