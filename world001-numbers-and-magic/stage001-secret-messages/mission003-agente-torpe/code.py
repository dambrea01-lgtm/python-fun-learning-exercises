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

agente_torpe = "Agente 404"      
agente_listo = "Agente 007"      

print(f"{agente_torpe} intenta enviar un mensaje secreto...")


print("Mensaje secreto: #Este es un comentario?")
print(f"{agente_listo} dice: No, {agente_torpe}, eso no es un comentario real, solo está dentro del string.")


print("Mensaje secreto: '''Intento de comentario multilínea'''?")
print(f"{agente_listo} dice: Casi, {agente_torpe}. Esto es un string, no un comentario oficial.")


print('Mensaje secreto: """Otro intento de comentario multilínea"""?')
print(f"{agente_listo} dice: Igual que antes, {agente_torpe}, Python solo ve un string sin asignar.")


print("Mensaje secreto: /* Comentario al estilo C */?")
print(f"{agente_listo} dice: 404, eso no funciona en Python, es de otros lenguajes!")

print(f"¡Ups! {agente_torpe} finalmente aprende a usar comentarios de una línea correctamente.")


'''
Ahora {agente_torpe} prueba comentarios largos usando comillas triples simples.
Python lo interpreta como un string sin asignar, así que actúa como comentario.
Esto sirve para notas largas o historias divertidas dentro del código.
'''


"""
{agente_torpe} también descubre que las comillas triples dobles funcionan igual.
Perfecto para historias, pistas secretas o explicaciones extensas.
Python ignora estas líneas durante la ejecución.
"""
mensaje_final = f"{agente_torpe} ahora puede enviar mensajes secretos correctamente gracias a {agente_listo}."
print(mensaje_final)


