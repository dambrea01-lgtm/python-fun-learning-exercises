# ➡️ Stage 001 – Secret Messages 🔐

| [↩️ Volver al inicio del proyecto](../../README.md) | [↩️ Volver al World 001](../world001.md) |
| :-------------------------------------------------: | :--------------------------------------: |

## Teoria breve de este Stage:

<p>En este stage nos convertimos en agentes secretos del código 🕵️‍♂️💻. Aprenderemos a dejar <strong>mensajes secretos</strong> dentro de nuestro Python usando comentarios, para que otros (y tú mismo) puedan entender lo que está pasando sin que el intérprete lo ejecute.</p>

<p>Las claves del mensaje secreto son:</p>

<ul>
  <li><strong># Comentarios de una línea:</strong> empiezan con <code>#</code> y Python los ignora. Puedes ponerlos al inicio de una línea o al final de tu instrucción. 📝</li>
  <li><strong>Triple comillas:</strong> <code>''' ... '''</code> o <code>""" ... """</code> sirven para comentarios multilínea, perfectos para notas largas o historias secretas. 💡</li>
  <li>Los comentarios ayudan a explicar el código, dejar pistas, anotar ideas o simplemente poner un mensaje divertido que nadie más entenderá... excepto los iniciados. 👀</li>
</ul>

<p>Prepárate para dejar tus primeras pistas y mensajes secretos en Python. 🕵️‍♂️💻  
El consejo es: <strong>copia los comentarios de los siguientes ejercicios, léelos con atención y teclea tú mismo el código</strong>. Prohibido copiar el código directamente; solo los comentarios pueden ser copiados. Así aprenderás a medida que lees y escribes. 📖✍️  
A partir de aquí comienzan las misiones, que son ejercicios divertidos basados en la teoría que acabas de leer. 🎯📝</p>

<br><hr><br>

## Indice de Misiones

- [🐶🐱 Misión 001 – ⚪ Básico: Comentarios con tu mascota](#-mision-001---básico-comentarios-con-tu-mascota)
- [🦸‍♂️🦸‍♀️ Misión 002 – 🔵 Intermedio: Mini diario del super-héroe](#-mision-002---intermedio-mini-diario-del-superhéroe)
- [👽👾 Misión 003 – 🔴 Avanzado: Código secreto del alienígena](#-mision-003---avanzado-código-secreto-del-alienígena)

<br><hr><br>

## [🐶🐱 MISION 001 – ⚪ BÁSICO: COMENTARIOS CON TU MASCOTA](#indice-de-misiones)

```python
# ============================================================
# 🐶🐱 MISION 001 – ⚪ BÁSICO: COMENTARIOS CON TU MASCOTA
# ============================================================
# NIVEL: Muy básico 🐣
# 🎯 OBJETIVO: Aprender a usar comentarios de una sola línea.
# 📌 ENUNCIADO:
# 1. Crear un programa que tenga variables con el nombre, tipo y edad de tu mascota.
# 2. Usar comentarios para describir cada variable.
# 3. Imprimir un mensaje divertido sobre tu mascota usando print().
# ============================================================

# ------------------------------------------------------------
# 1️⃣ DEFINIR VARIABLES CON INFORMACIÓN DE LA MASCOTA
# ------------------------------------------------------------
# En Python, una variable es un nombre que almacena un valor.
# Para crearla, simplemente escribimos: nombre_variable = valor

# Creamos una variable llamada 'mascota' y le asignamos el nombre de nuestra mascota
mascota = "Fido"  # Nombre de mi perro más travieso

# Creamos una variable llamada 'tipo' para indicar el tipo de mascota
tipo = "Perro"  # Tipo de mascota: perro, gato, etc.

# Creamos una variable llamada 'edad' para guardar la edad de la mascota
edad = 5  # Edad en años

# ------------------------------------------------------------
# 2️⃣ USO DE COMENTARIOS
# ------------------------------------------------------------
# Los comentarios comienzan con el símbolo '#' y no son ejecutados por Python.
# Sirven para explicar qué hace cada línea de código, y son útiles para recordar detalles.

# Ejemplo:
# print(mascota)  # Esto imprimirá el nombre de la mascota

# ------------------------------------------------------------
# 3️⃣ IMPRIMIR MENSAJE DIVERTIDO
# ------------------------------------------------------------
# Usamos la función print() para mostrar información en la pantalla
# Podemos combinar texto y variables para hacerlo divertido

# EN PYTHON:
# - Para unir texto y variables dentro de print(), se recomienda usar comas (,) en lugar de +.
# - Las comas insertan automáticamente un espacio entre los elementos.
# - Esto evita errores de tipo (por ejemplo, intentar sumar str + int)
# - Ejemplo: print("Hola!", mascota, "es un", tipo) -> añade espacios automáticamente

print("Hola! Mi mascota se llama", mascota, "y es un", tipo, "de", edad, "años")

# ------------------------------------------------------------
# ✅ EXPLICACIÓN
# ------------------------------------------------------------
# 1. Las variables 'mascota', 'tipo' y 'edad' almacenan información que luego podemos usar.
# 2. Los comentarios # explican qué hace cada línea y ayudan a recordar conceptos.
# 3. print() muestra el mensaje en pantalla, combinando texto y valores de las variables.
# 4. En Python usamos comas en print() para concatenar; en otros lenguajes a veces se usa +.
# 5. Esto es útil para aprender a documentar tu código desde el inicio.
```

<br>

| 💻                                                      | 📝                                                  | 🎯                                                 |
| ------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------- |
| [Ver código completo](mission001-pet-comments/guide.py) | [Ver Template](mission001-pet-comments/template.py) | [Ver Solo código](mission001-pet-comments/code.py) |

<br><hr><br>

## [🦸‍♂️🦸‍♀️ MISION 002 – 🔵 INTERMEDIO: MINI DIARIO DEL SUPERHÉROE](#indice-de-misiones)

```python
# ============================================================
# 🦸‍♂️🦸‍♀️ MISION 002 – 🔵 INTERMEDIO: MINI DIARIO DEL SUPERHÉROE
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
```

<br>

| 💻                                                              | 📝                                                          | 🎯                                                         |
| --------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| [Ver código completo](mission002-superhero-mini-diary/guide.py) | [Ver Template](mission002-superhero-mini-diary/template.py) | [Ver Solo código](mission002-superhero-mini-diary/code.py) |

<br><hr><br>

## [👽👾 MISION 003 – 🔴 AVANZADO: CÓDIGO SECRETO DEL ALIENÍGENA](#indice-de-misiones)

```python
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
```

<br>

| 💻                                                           | 📝                                                       | 🎯                                                      |
| ------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------- |
| [Ver código completo](mission003-alien-secret-code/guide.py) | [Ver Template](mission003-alien-secret-code/template.py) | [Ver Solo código](mission003-alien-secret-code/code.py) |

<br><hr><br>

| [↩️ Volver al inicio del proyecto](../../README.md) | [↩️ Volver al World 001](../world001.md) | [⬆️ Ir al inicio del Stage 001](#️-stage-001--secret-messages-) |
| :-------------------------------------------------: | :--------------------------------------: | :-------------------------------------------------------------- |
