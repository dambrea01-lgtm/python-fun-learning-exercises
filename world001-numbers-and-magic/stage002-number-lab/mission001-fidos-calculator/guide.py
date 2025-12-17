# ============================================================
# 🐶🧮 MISION 001 – ⚪ BÁSICO: LA CALCULADORA DE FIDO
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
total_bones = 17 # int, enteros: números sin decimales

# Nota: en Python no se necesita ; al final de la línea, a diferencia de otros lenguajes

# Número de amigos con los que Fido compartirá sus huesos
friends = 3

# ------------------------------------------------------------
# 2️⃣ REALIZAR CÁLCULOS
# ------------------------------------------------------------

# División normal (/) devuelve float, incluso si ambos operandos son enteros
bones_per_friends = total_bones / friends # 17 / 3 = 5.666...
print("Huesos por amigo (división normal):", bones_per_friends)
# Comentario extra: Python imprime el resultado automáticamente si usamos print()

# División entera (//) descarta los decimales y devuelve un int
floor_bones = total_bones // friends # 17 // 3 = 5


# Operador módulo (%) devuelve el resto de la división
remainder_bones = total_bones % friends # 17 % 3 = 2
print("Huesos sobrantes:", remainder_bones)

# Verificación: floor_bones * friends + remainder_bones debería ser igual a total_bones
check_total = floor_bones * friends + remainder_bones
print("Verificación (floor_bones * friends + remainder_bones):", check_total)
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
