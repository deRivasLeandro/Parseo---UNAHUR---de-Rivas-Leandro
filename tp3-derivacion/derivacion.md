Ejemplo a derivar:
INICIO 
    x = 1; 
FIN

🔹 Derivación por la izquierda (ASD: análisis sintáctico descendente)

Siempre reemplazamos el primer no terminal de izquierda a derecha.

| cadena de derivacion | proxima producción |
| <programa> | <programa> -> INICIO <sentencias> FIN |
| INICIO <sentencias> FIN | <sentencias> -> <sentencia> <sentencias> |
| INICIO <sentencia> <sentencias> FIN | <sentencia> -> <asignacion>; |
| INICIO <asignacion>; <sentencias> FIN | <asignacion> -> <variable> = <valor>; |
| INICIO <variable> = <valor>; <sentencias> FIN | <variable> -> x |
| INICIO x = <valor>; <sentencias> FIN | <valor> -> <numero> |
| INICIO x = <numero>; <sentencias> FIN | <numero> -> 1 |
| INICIO x = 1; <sentencias> FIN | <sentencias> ->  λ |
| INICIO x = 1; FIN | accepted |

✅ Resultado: accepted

🔹 Derivación por la derecha (ASA: análisis sintáctico ascendente)

Siempre reemplazamos el primer no terminal de derecha a izquierda.

| cadena de derivacion | proxima producción |
| <programa> | <programa> -> INICIO <sentencias> FIN |
| <programa> -> INICIO <sentencias> FIN | <sentencias> -> <sentencia> <sentencias> |
| <programa> -> INICIO <sentencia> <sentencias> FIN | <sentencias> -> λ |
| <programa> -> INICIO <sentencia> FIN | <sentencia> -> <asignacion> |
| <programa> -> INICIO <asignacion> FIN | <asignacion> -> <variable> = <valor>; |
| <programa> -> INICIO <variable> = <valor>; FIN | <valor> -> <numero> |
| <programa> -> INICIO <variable> = <numero>; FIN | <numero> -> 1 |
| <programa> -> INICIO <variable> = 1; FIN | <variable> -> x |
| <programa> -> INICIO x = 1; FIN | accepted |


✅ Resultado: accepted