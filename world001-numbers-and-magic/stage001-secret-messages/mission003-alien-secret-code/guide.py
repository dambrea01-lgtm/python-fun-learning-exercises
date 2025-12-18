# ============================================================
# 👽👾 MISION 003 – 🔴 AVANZADO: CÓDIGO SECRETO DEL ALIENÍGENA
# ============================================================
# NIVEL: Avanzado 🔥
# 🎯 OBJETIVO: Aprender a usar distintos tipos de comentarios en Python
# 📌 ENUNCIADO:
# 1. Crear variables para los alienígenas, el planeta y la contraseña secreta.
# 2. Usar comentarios de una línea (#) para pistas rápidas.
# 3. Usar comentarios multilínea (""" ... """) para historias o notas largas.
# 4. Imprimir mensajes usando variables y combinar texto con print().
# 5. Jugar con "códigos secretos" en los comentarios para la narrativa.
# 6. Aprender escribiendo línea por línea, reforzando la documentación y la lógica.
# ============================================================

# ------------------------------------------------------------
# 1️⃣ DEFINIR VARIABLES
# ------------------------------------------------------------
# Alienígenas protagonistas
alien1 = "Zog"          # Primer alienígena 👾
alien2 = "Blip"         # Segundo alienígena 👽

# Planeta de origen
planet = "Zeta-5"      # Planeta secreto 🪐

# Contraseña secreta (solo para jugar con comentarios)
password_part1 = 7       # Primer número de la contraseña
password_part2 = 3       # Segundo número de la contraseña

# ------------------------------------------------------------
# 2️⃣ CÓDIGO SECRETO EN COMENTARIOS DE UNA LÍNEA
# ------------------------------------------------------------
# Los alienígenas dejan pistas en comentarios de una línea:
# Recuerda que los comentarios de una línea usamos # 
# Python ignora las líneas comentadas.

# Primer número de la contraseña
# 7
# Segundo número de la contraseña
# 3

# ------------------------------------------------------------
# 3️⃣ HISTORIA MULTILÍNEA CON TRIPLE COMILLAS
# ------------------------------------------------------------
# Podemos usar """ ... """ para narrar la historia completa.
# Aunque Python lo interpreta como una cadena, si no se asigna a una variable, actúa como comentario.
"""
Zog y Blip planeaban invadir la Tierra sin ser detectados.
Cada mensaje secreto era escrito en comentarios de código.
Su misión: confundir a los humanos mientras enviaban códigos cifrados.
El héroe Fido, el perro cósmico, interceptaba los mensajes con risas.
Cada línea de comentario era un jeroglífico galáctico que solo los aliens entendían.
"""

# ------------------------------------------------------------
# 4️⃣ EXPLICAR F-STRING (FORMATTED STRING)
# ------------------------------------------------------------
# Las f-strings permiten incrustar variables directamente en una cadena de texto.
# La letra 'f' antes de las comillas indica que la cadena puede formatearse.
# Todo lo que pongas entre llaves {} será reemplazado por el valor de la variable.
# Ejemplo:
# nombre = "Zog"
# print(f"Hola {nombre}")  -> Esto imprimirá: Hola Zog
# Ventaja: más legible que concatenar con + o convertir tipos manualmente.

# ------------------------------------------------------------
# 5️⃣ IMPRIMIR MENSAJE DIVERTIDO
# ------------------------------------------------------------
# Ahora mostramos un mensaje usando print() y nuestras variables
# Observa cómo podemos combinar texto y variables con una f-string
mensaje = f"Los alienígenas {alien1} y {alien2} enviaron un mensaje secreto desde {planet}."
print(mensaje)

# Mensaje literal adicional
print("Recuerda: las pistas están en los comentarios de código 👾✨")

# ------------------------------------------------------------
# 6️⃣ EXPLICACIÓN FINAL
# ------------------------------------------------------------
# 1. # Comentarios de una línea: para notas rápidas y pistas.
# 2. """ ... """ Comentarios multilínea: para historias largas, explicaciones o documentación.
# 3. Python ignora los comentarios durante la ejecución.
# 4. Variables almacenan información que se puede mostrar o combinar.
# 5. f-strings permiten incrustar variables directamente dentro de cadenas de texto usando {}.
# 6. print() muestra el mensaje en pantalla.
# 7. Este ejercicio enseña a usar múltiples tipos de comentarios dentro de una temática divertida.
# 8. Aprender escribiendo línea por línea refuerza la comprensión y la memoria.
# 9. Los códigos secretos en comentarios son un ejemplo creativo de cómo documentar programas complejos.
