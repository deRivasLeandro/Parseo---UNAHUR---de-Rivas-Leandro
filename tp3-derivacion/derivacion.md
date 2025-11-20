Ejemplo a derivar:
INICIO 
    x = 1; 
FIN

🔹 Derivación por la izquierda (ASD: análisis sintáctico descendente)

Siempre reemplazamos el primer no terminal de izquierda a derecha.

| cadena de derivacion                          | proxima producción    |
| --                                            |                       |
| <programa>                                    | <programa> -> INICIO <bloque> FIN |
| <programa> -> INICIO <bloque> FIN         | <bloque> -> <definiciones_funcion> <sentencias> |
| INICIO <definiciones_funcion> <sentencias> FIN                       | <definiciones_funcion> -> λ |
| INICIO <sentencias> FIN                       | <sentencias> -> <sentencia> <sentencias> |
| INICIO <sentencia> <sentencias> FIN           | <sentencia> -> <asignacion>; |
| INICIO <asignacion>; <sentencias> FIN         | <asignacion> -> <variable> = <valor>; |
| INICIO <variable> = <valor>; <sentencias> FIN | <variable> -> x |
| INICIO x = <valor>; <sentencias> FIN          | <valor> -> <numero> |
| INICIO x = <numero>; <sentencias> FIN         | <numero> -> 1 |
| INICIO x = 1; <sentencias> FIN                | <sentencias> ->  λ |
| INICIO x = 1; FIN                             | accepted |

✅ Resultado: accepted

🔹 Derivación por la derecha (ASA: análisis sintáctico ascendente)

Siempre reemplazamos el primer no terminal de derecha a izquierda.

| cadena de derivacion  | proxima producción    |
| --                    |                       |
| <programa> | <programa> -> INICIO <bloque> FIN |
| <programa> -> INICIO <bloque> FIN         | <bloque> -> <definiciones_funcion> <sentencias> |
| <programa> -> INICIO <definiciones_funcion> <sentencias> FIN | <sentencias> -> <sentencia> <sentencias> |
| <programa> -> INICIO <definiciones_funcion> <sentencia> <sentencias> FIN | <sentencias> -> λ |
| <programa> -> INICIO <definiciones_funcion> <sentencia> FIN | <sentencia> -> <asignacion> |
| <programa> -> INICIO <definiciones_funcion> <asignacion> FIN | <asignacion> -> <variable> = <valor>; |
| <programa> -> INICIO <definiciones_funcion> <variable> = <valor>; FIN | <valor> -> <numero> |
| <programa> -> INICIO <definiciones_funcion> <variable> = <numero>; FIN | <numero> -> 1 |
| <programa> -> INICIO <definiciones_funcion> <variable> = 1; FIN | <variable> -> x |
| <programa> -> INICIO <definiciones_funcion> x = 1; FIN | <definiciones_funcion> -> λ |
| <programa> -> INICIO x = 1; FIN | accepted |

✅ Resultado: accepted