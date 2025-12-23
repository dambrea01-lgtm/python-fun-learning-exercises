# ============================================================
# 🕵️ MISION 404 – 🔵 INTERMEDIO: EL AGENTE TORPE
# ============================================================
# NIVEL: Intermedio 🕵️
# 🎯 OBJETIVO: Aprender a usar distintos tipos de comentarios en Python
# 📌 ENUNCIADO:
# 1. Ayudar al Agente 404 a enviar mensajes secretos.
# 2. Usar comentarios de una línea (#) para pistas rápidas.
# 3. Usar comentarios multilínea (''' ... ''' o """ ... """) para notas largas o historias.
# 4. Imprimir mensajes usando print() y practicar errores y correcciones.
# 5. Aprender escribiendo línea por línea y reforzando la documentación divertida.
# ============================================================

# ------------------------------------------------------------
# 1️⃣ PRESENTACIÓN DEL AGENTE
# ------------------------------------------------------------
                                # Nuestro héroe despistado
                                # Su guía experto

# ------------------------------------------------------------
# 2️⃣ PRIMEROS INTENTOS FALLIDOS
# ------------------------------------------------------------
 

# Primer intento usando # dentro del string
 
 

# Segundo intento usando comillas triples simples
 

# Tercer intento usando comillas triples dobles
 

# Cuarto intento usando estilo C


# ------------------------------------------------------------
# 3️⃣ EL AGENTE 404 APRENDE
# ------------------------------------------------------------
# Comentario de una línea
# Este es un comentario real que Python ignora


# Comentario multilínea con comillas triples simples
'''
Ahora {agente_torpe} prueba comentarios largos usando comillas triples simples.
Python lo interpreta como un string sin asignar, así que actúa como comentario.
Esto sirve para notas largas o historias divertidas dentro del código.
'''

# Comentario multilínea con comillas triples dobles
"""
{agente_torpe} también descubre que las comillas triples dobles funcionan igual.
Perfecto para historias, pistas secretas o explicaciones extensas.
Python ignora estas líneas durante la ejecución.
"""

# ------------------------------------------------------------
#  EXPLICACIÓN DE F-STRINGS
# ------------------------------------------------------------
# En Python, las f-strings nos permiten insertar valores de variables directamente dentro de un string.
# Estructura:
# 1. Se coloca una 'f' o 'F' antes de las comillas que delimitan el string.
# 2. Dentro del string, cualquier expresión o variable que pongamos dentro de llaves {} 
#    será reemplazada por su valor al ejecutar el código.
# 3. Son útiles para combinar texto y variables de forma clara y legible.

# Ejemplo dentro del contexto del agente:
# nombre_agente = "404"
# print(f"El {nombre_agente} ha enviado un mensaje secreto")
# Esto imprimirá: El 404 ha enviado un mensaje secreto

# También podemos usar expresiones dentro de {}:
# edad = 42
# print(f"El doble de {edad} es {edad * 2}")
# Esto imprimirá: El doble de 42 es 84

# Ventaja:
# Más legible que concatenar con + o convertir tipos manualmente.

# ------------------------------------------------------------
# 4️⃣ MENSAJE FINAL
# -----------------------------------------------------------



# ------------------------------------------------------------
# 5️⃣ EXPLICACIÓN FINAL
# ------------------------------------------------------------
# 1. # Comentarios de una línea: para notas rápidas y pistas.
# 2. ''' ... ''' o """ ... """ Comentarios multilínea: para historias largas, explicaciones o documentación.
# 3. Python ignora los comentarios durante la ejecución.
# 4. print() muestra mensajes y permite probar errores y aciertos.
# 5. Practicar línea por línea refuerza la comprensión de los comentarios.
# 6. Aprender con historias divertidas ayuda a recordar la sintaxis.
# 7. Los comentarios multilínea no se imprimen si no se asignan a una variable.
# 8. Las f-strings (f"{variable}") permiten insertar variables y expresiones directamente dentro de un string.

