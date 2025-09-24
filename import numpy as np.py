import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 1. Creación y Manipulación de Arrays
A = np.arange(1, 16).reshape(3, 5)
print("Matriz A (3x5):\n", A)

# 2. Operaciones Básicas
suma = np.sum(A)
media = np.mean(A)
producto = np.prod(A)
print("\nSuma de A:", suma)
print("Media de A:", media)
print("Producto de A:", producto)

# 3. Acceso y Slicing
seleccion = A[1, 1:3]
print("\nSegundo y tercer elemento de la segunda fila de A:", seleccion)

# 4. Indexación Booleana
B = A[A > 7]
print("\nElementos de A mayores que 7:\n", B)

# 5. Álgebra Lineal
C = np.random.rand(3, 3)
determinante = np.linalg.det(C)
inversa = np.linalg.inv(C)
print("\nMatriz C (3x3):\n", C)
print("\nDeterminante de C:", determinante)
print("Inversa de C:\n", inversa)

# 6. Estadísticas con NumPy
D = np.random.rand(100)
max_val = np.max(D)
min_val = np.min(D)
media_D = np.mean(D)
desviacion = np.std(D)
print("\nEstadísticas de D (100 números aleatorios):")
print("Máximo:", max_val)
print("Mínimo:", min_val)
print("Media:", media_D)
print("Desviación estándar:", desviacion)

# 7. Gráfico Básico (Seno y Coseno)
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label="Seno")
plt.plot(x, np.cos(x), label="Coseno")
plt.title("Seno y Coseno entre -2π y 2π")
plt.legend()
plt.grid()
plt.show()

# 8. Gráficos de Dispersión
plt.figure(figsize=(8, 5))
plt.scatter(range(len(D)), D)
plt.title("Gráfico de dispersión de D")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid()
plt.show()

# 9. Histogramas
plt.figure(figsize=(8, 5))
plt.hist(D, bins=20)
plt.title("Histograma de D")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()

# 10. Manipulación de Imágenes con Matplotlib
img = mpimg.imread('imagen.png')  # Cambia 'imagen.png' por la ruta de tu imagen
grayscale = np.mean(img, axis=2)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Imagen Original")

plt.subplot(1, 2, 2)
plt.imshow(grayscale, cmap='gray')
plt.title("Imagen en Escala de Grises")
plt.show()
