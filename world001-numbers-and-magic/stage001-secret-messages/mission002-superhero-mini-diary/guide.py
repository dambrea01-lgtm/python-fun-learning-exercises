# ============================================================
# 🦸‍♂️🦸‍♀️ EJERCICIO 2 – 🔵 INTERMEDIO: MINI DIARIO DEL SUPERHÉROE
# ============================================================
# NIVEL: Intermedio 🏹
# 🎯 OBJETIVO: Usar comentarios de varias líneas para explicar un mini programa.
# 📌 ENUNCIADO:
# 1. Crear variables: nombre, superpoder, enemigo.
# 2. Escribir un comentario multilínea """ ... """ explicando la misión del día.
# 3. Imprimir un mensaje divertido: "Hoy {nombre} luchó contra {enemigo} usando {superpoder}".
# ============================================================

# ------------------------------------------------------------
# 1️⃣ DEFINIR VARIABLES DEL SUPERHÉROE
# ------------------------------------------------------------
# Creamos variables para almacenar información sobre nuestro superhéroe.
nombre = "Capitán Risas"       # Nombre del superhéroe 😆
superpoder = "risa infinita"   # Superpoder loco 😂
enemigo = "Dr. Aburrimiento"   # Enemigo temible 😱

# ------------------------------------------------------------
# 2️⃣ COMENTARIO MULTILÍNEA: LA MISIÓN DEL DÍA
# ------------------------------------------------------------
# Usamos triple comillas """ ... """ para escribir un comentario de varias líneas.
# Esto permite contar historias o explicar programas largos.
"""
Hoy, Capitán Risas despertó muy temprano 🌞.
Su misión del día era salvar a la ciudad de Dr. Aburrimiento 😈.
Con su superpoder de risa infinita 😂, debía hacer reír a todos los ciudadanos tristes 😭.
A lo largo del día, se enfrentó a bromas, acertijos y pastelazos 🍰, pero nunca perdió la calma.
Al final del día, la ciudad estaba feliz y el enemigo huyó llorando de risa 😆.
"""

# ------------------------------------------------------------
# 3️⃣ IMPRIMIR MENSAJE DIVERTIDO
# ------------------------------------------------------------
# Usamos print() para mostrar el resultado en pantalla.
# Podemos combinar texto, variables y emojis para hacerlo más entretenido.
# En Python:
# - Para unir texto y variables dentro de print(), se recomienda usar comas (,) en lugar de +.
# - Las comas insertan automáticamente un espacio entre los elementos.
# - Esto evita errores de tipo (por ejemplo, intentar sumar str + int)
# - Sobre emojis: algunas consolas no los muestran directamente. En ese caso:
#   1. Puedes usar el código Unicode del emoji, por ejemplo:
#      ✨ -> "\u2728"
#   2. O reemplazarlos por texto como "[Risa]" o "[Superhéroe]" si la consola no soporta UTF-8.
print("Hoy", nombre, "luchó contra", enemigo, "usando", superpoder, "[Risa] \u2728")

# ------------------------------------------------------------
# ✅ EXPLICACIÓN
# ------------------------------------------------------------
# 1. Las variables 'nombre', 'superpoder' y 'enemigo' guardan información clave de nuestro superhéroe.
# 2. Los comentarios multilínea """ ... """ sirven para contar historias o explicar programas complejos.
# 3. print() muestra un mensaje combinando texto y las variables.
# 4. Las comas en print() insertan espacios automáticamente, evitando errores de concatenación.
# 5. Los emojis agregan diversión y ayudan a recordar la historia.
# 6. Este ejercicio enseña cómo documentar tu código de forma creativa y entretenida.
# 7. Si la consola no soporta emojis, se pueden usar códigos Unicode o texto alternativo.
