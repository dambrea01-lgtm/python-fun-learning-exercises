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
- [🕵️✉️ Misión 003 – 🔵 Intermedio: Agente Torpe](#-mision-003---avanzado-código-secreto-del-alienígena)

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

| [💻 Ver código completo](mission001-pet-comments/guide.py) | [📝 Ver Template](mission001-pet-comments/template.py) | [🎯 Ver Solo código](mission001-pet-comments/code.py) |
| ---------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- |

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

| [💻 Ver código completo](mission002-superhero-mini-diary/guide.py) | [📝 Ver Template](mission002-superhero-mini-diary/template.py) | [🎯 Ver Solo código](mission002-superhero-mini-diary/code.py) |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------- |

<br><hr><br>

## [🕵️✉️ MISION 003 – 🔵 INTERMEDIO: AGENTE TORPE](#indice-de-misiones)

```python
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
  agente_torpe = "Agente 404"      # Nuestro héroe despistado
  agente_listo = "Agente 007"      # Su guía experto

  # ------------------------------------------------------------
  # 2️⃣ PRIMEROS INTENTOS FALLIDOS
  # ------------------------------------------------------------
  print(f"{agente_torpe} intenta enviar un mensaje secreto...")

  # Primer intento usando # dentro del string
  print("Mensaje secreto: #Este es un comentario?")
  print(f"{agente_listo} dice: No, {agente_torpe}, eso no es un comentario real, solo está dentro del string.")

  # Segundo intento usando comillas triples simples
  print("Mensaje secreto: '''Intento de comentario multilínea'''?")
  print(f"{agente_listo} dice: Casi, {agente_torpe}. Esto es un string, no un comentario oficial.")

  # Tercer intento usando comillas triples dobles
  print('Mensaje secreto: """Otro intento de comentario multilínea"""?')
  print(f"{agente_listo} dice: Igual que antes, {agente_torpe}, Python solo ve un string sin asignar.")

  # Cuarto intento usando estilo C
  print("Mensaje secreto: /* Comentario al estilo C */?")
  print(f"{agente_listo} dice: 404, eso no funciona en Python, es de otros lenguajes!")

  # ------------------------------------------------------------
  # 3️⃣ EL AGENTE 404 APRENDE
  # ------------------------------------------------------------
  # Comentario de una línea
  # Este es un comentario real que Python ignora
  print(f"¡Ups! {agente_torpe} finalmente aprende a usar comentarios de una línea correctamente.")

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
  # ------------------------------------------------------------
  mensaje_final = f"{agente_torpe} ahora puede enviar mensajes secretos correctamente gracias a {agente_listo}."
  print(mensaje_final)

  # Mensaje adicional
  print("Recuerda: los comentarios ayudan a documentar y hacer tu código más divertido y entendible.")

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
```

<br>

| [💻 Ver código completo](mission003-agente-torpe/guida.py) | [📝 Ver Template](mission003-agente-torpe/template.py) | [🎯 Ver Solo código](mission003-agente-torpe/code.py) |
| ---------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- |

<br><hr><br>

| [↩️ Volver al inicio del proyecto](../../README.md) | [↩️ Volver al World 001](../world001.md) | [⬆️ Ir al inicio del Stage 001](#️-stage-001--secret-messages-) |
| :-------------------------------------------------: | :--------------------------------------: | :-------------------------------------------------------------- |
