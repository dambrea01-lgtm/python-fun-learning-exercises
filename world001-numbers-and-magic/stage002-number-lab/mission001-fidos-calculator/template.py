# ============================================================
# 🐶🧮 MISION 001 – ⚪ BÁSICO: LA CALCULADORA DE FIDO
# ============================================================
# ⚠️ IMPORTANTE:
# Sustituye cada línea que dice "ESCRIBE AQUÍ" por tu propio código que puedes verlo en guide.py.
# No copies y pegues código de otros sitios: teclea tú mismo cada línea.
# Este ejercicio es para aprender escribiendo y practicando Python.
# ============================================================
# NIVEL: Básico 🦴
# 🎯 OBJETIVO: Aprender a usar números enteros y decimales, operadores aritméticos,
# división normal, floor division y módulo (%).
# 📌 ENUNCIADO:
# 1. Fido quiere repartir sus 17 huesos entre sus 3 amigos.
# 2. Calcula cuántos huesos le toca a cada amigo (/) y cuántos sobran (%).
# 3. Comprueba que división entera × divisor + resto = total de huesos.
# ============================================================

# ------------------------------------------------------------
# 1️⃣ DEFINIR VARIABLES
# ------------------------------------------------------------
# En Python, una variable se crea con: nombre_variable = valor
# No hace falta declarar tipo, Python lo infiere automáticamente.

# Número total de huesos que tiene Fido
# ESCRIBIR CÓDIGO AQUÍ    # int, enteros: números sin decimales

# Nota: en Python no se necesita ; al final de la línea, a diferencia de otros lenguajes

# Número de amigos con los que Fido compartirá sus huesos
# ESCRIBIR CÓDIGO AQUÍ

# ------------------------------------------------------------
# 2️⃣ REALIZAR CÁLCULOS
# ------------------------------------------------------------

# División normal (/) devuelve float, incluso si ambos operandos son enteros
# ESCRIBIR CÓDIGO AQUÍ   # 17 / 3 = 5.666...
# ESCRIBIR CÓDIGO AQUÍ

# Comentario extra: Python imprime el resultado automáticamente si usamos print()

# División entera (//) descarta los decimales y devuelve un int
# ESCRIBIR CÓDIGO AQUÍ  # 17 // 3 = 5


# Operador módulo (%) devuelve el resto de la división
# ESCRIBIR CÓDIGO AQUÍ  # 17 % 3 = 2
# ESCRIBIR CÓDIGO AQUÍ

# Verificación: floor_bones * friends + remainder_bones debería ser igual a total_bones
# ESCRIBIR CÓDIGO AQUÍ
# ESCRIBIR CÓDIGO AQUÍ
# Esto ayuda a entender cómo se relacionan floor division y módulo

# ------------------------------------------------------------
# 3️⃣ CONSEJOS DE PYTHON
# ------------------------------------------------------------
# - Las variables se escriben usando letras, números y guiones bajos (_), 
#   no pueden empezar con un número.
# - Nombres significativos ayudan a entender el código: total_bones, friends...
# - Python ignora todo lo que está después del símbolo # en la misma línea.
# - Los comentarios ayudan a documentar la lógica paso a paso.
# - Puedes mezclar int y float; Python convierte automáticamente cuando es necesario.

# ------------------------------------------------------------
# ✅ EXPLICACIÓN FINAL
# ------------------------------------------------------------
# 1. total_bones y friends almacenan la información básica del problema.
# 2. bones_per_friend calcula la división normal, mostrando decimales.
# 3. floor_bones calcula la división entera, útil cuando solo quieres números completos.
# 4. remainder_bones calcula los huesos sobrantes.
# 5. La verificación asegura que floor division y resto juntos suman el total.
# 6. print() permite mostrar resultados y combinarlos con texto.
# 7. Los comentarios paso a paso enseñan buenas prácticas mientras tecleas.