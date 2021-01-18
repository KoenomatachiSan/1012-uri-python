VALOR = input("Valor:").split(" ")

a, b, c = VALOR
PI = 3.14159

TRIANGULO = (float(a) * float(c))/2
CIRCULO = PI * (float(c)* float(c))
TRAPEZIO = float(c) *(float(a) + float(b)) / 2
QUADRADO = float(b) * float(b)
RETANGULO = float(a) * float(b)


print("TRIANGULO: %0.3f \n CIRCULO: %0.3f \n TRAPEZIO: %0.3f \n QUADRADO: %0.3f \n RETANGULO: %0.3f" % (TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO))