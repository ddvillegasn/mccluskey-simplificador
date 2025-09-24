# mccluskey-simplificador
# 🧮 Simplificador de Funciones Booleanas - Método de McCluskey

Aplicación de escritorio desarrollada en **Python** con interfaz gráfica en **Tkinter**, que implementa el **Método de McCluskey** (o método de los implicantes primos) para la simplificación de funciones booleanas.

---

## 📌 ¿Qué hace?
- Simplifica expresiones booleanas dadas en forma de minterms.  
- Encuentra **implicantes primos esenciales**.  
- Minimiza el número de compuertas lógicas necesarias.  
- Genera una expresión booleana más corta y eficiente.  

---

## ⚙️ Funcionamiento
1. **Entrada**: El usuario ingresa números (minterms) separados por espacios.  
2. **Procesamiento**:
   - Convierte los minterms a binario.  
   - Agrupa términos por número de unos (1s).  
   - Combina términos que difieren en un solo bit.  
   - Encuentra los implicantes primos esenciales.  
3. **Salida**: Una expresión booleana simplificada usando variables A, B, C, D, etc.  

---

## 🖥 Ejemplo
**Entrada**:  
