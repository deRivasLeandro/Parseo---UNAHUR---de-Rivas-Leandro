1) GIC (mínima) usada

GIC = < ΣN, ΣT, S, P >

ΣN = { <programa>, <bloque>, <definiciones_funcion>, <sentencias>, <sentencia>, <asignacion>, <variable>, <valor>, <numero> }

ΣT = { INICIO, FIN, x (IDENT), =, 1 (NUMERO), ; }

S = <programa>

P = (1)  <programa>               ::= INICIO <bloque> FIN
    (2)  <bloque>                 ::= <definiciones_funcion> <sentencias>
    (3)  <definiciones_funcion>   ::= λ
    (4)  <sentencias>             ::= <sentencia> <sentencias>
    (5)  <sentencia>              ::= <asignacion> ";"
    (6)  <asignacion>             ::= <variable> "=" <valor>
    (7)  <variable>               ::= x
    (8)  <valor>                  ::= <numero>
    (9)  <numero>                 ::= 1
    (10) <sentencias>             ::= λ

2) PDA — transiciones δ (estilo ejemplo)

Estados: q0, q1, q2, q3. Símbolo inicial de pila: Z.

Las transiciones se escriben como:

δ(estado_actual, símbolo_entrada, símbolo_tope_pila) => (nuevo_estado, símbolos_a_empujar_sobre_pila)


Transiciones de inicialización y expansión de axioma:

δ(q0, λ, λ)                    => (q1, Z)
δ(q1, λ, λ)                    => (q2, <programa>)


Expansiones (cuando en tope hay un no terminal lo expandimos empujando el RHS):

δ(q2, λ, <programa>)           => (q2, INICIO <bloque> FIN)

δ(q2, λ, <bloque>)             => (q2, <definiciones_funcion> <sentencias>)
δ(q2, λ, <definiciones_funcion>)=> (q2, λ)                      ; producción (3)

δ(q2, λ, <sentencias>)         => (q2, <sentencia> <sentencias>) ; producción (4)
δ(q2, λ, <sentencias>)         => (q2, λ)                        ; producción (10) alternativa

δ(q2, λ, <sentencia>)          => (q2, <asignacion> ;)
δ(q2, λ, <asignacion>)         => (q2, <variable> = <valor>)     ; producción (6)
δ(q2, λ, <variable>)           => (q1, x)                        ; producción (7) - empuja terminal x
δ(q2, λ, <valor>)              => (q2, <numero>)
δ(q2, λ, <numero>)             => (q2, 1)                        ; producción (9) - empuja terminal 1


Transiciones de consumo de terminales (cuando el tope coincide con token actual):

δ(q2, INICIO, INICIO)          => (q2, λ)
δ(q2, x, x)                    => (q2, λ)
δ(q2, =, =)                    => (q2, λ)
δ(q2, 1, 1)                    => (q2, λ)
δ(q2, ;, ;)                    => (q2, λ)
δ(q2, FIN, FIN)                => (q2, λ)


Transición de aceptación:

δ(q2, λ, Z)                    => (q3, λ)   ;

3)
| Pila (tope derecha)                                             | Entrada de tokens  | Transición aplicada                                                                                                                                  |
| --------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| λ                                                               | INICIO x = 1 ; FIN | δ(q0, λ, λ) ⇒ (q1, Z)                                                                                                                                |
| Z                                                               | INICIO x = 1 ; FIN | δ(q1, λ, λ) ⇒ (q2, <programa>)                                                                                                                       |
| Z FIN `<bloque>` INICIO                                         | INICIO x = 1 ; FIN | δ(q2, λ, `<programa>`) ⇒ (q2, **FIN `<bloque>` INICIO**)                                                                 |
| Z FIN `<bloque>` INICIO                                         | INICIO x = 1 ; FIN | δ(q2, INICIO, INICIO) ⇒ (q2, λ)                                                                   |
| Z FIN `<bloque>`                                                | x = 1 ; FIN        | δ(q2, λ, `<bloque>`) ⇒ (q2, **`<sentencias>` `<definiciones_funcion>`**) |
| Z FIN `<sentencias>` `<definiciones_funcion>`                   | x = 1 ; FIN        | δ(q2, λ, `<definiciones_funcion>`) ⇒ (q2, λ)                                  |
| Z FIN `<sentencias>`                                            | x = 1 ; FIN        | δ(q2, λ, `<sentencias>`) ⇒ (q2, **`<sentencias>` `<sentencia>`**) |
| → **pila: Z FIN `<sentencias>` `<sentencia>`**                  |                    |                                                                                                                                                      |
| Z FIN `<sentencias>` `<sentencia>`                              | x = 1 ; FIN        | δ(q2, λ, `<sentencia>`) ⇒ (q2, **`;` `<asignacion>`**)                                            |
| → **pila: Z FIN `<sentencias>` `;` `<asignacion>`**             |                    |                                                                                                                                                      |
| Z FIN `<sentencias>` `;` `<asignacion>`                         | x = 1 ; FIN        | δ(q2, λ, `<asignacion>`) ⇒ (q2, **`<valor>` `=` `<variable>`**)                                      |
| → **pila: Z FIN `<sentencias>` `;` `<valor>` `=` `<variable>`** |                    |                                                                                                                                                      |
| Z FIN `<sentencias>` `;` `<valor>` `=` `<variable>`             | x = 1 ; FIN        | δ(q2, λ, `<variable>`) ⇒ (q1, x)                                                                 |
| → **pila: Z FIN `<sentencias>` `;` `<valor>` `=` x**            |                    |                                                                                                                                                      |
| Z FIN `<sentencias>` `;` `<valor>` `=` x                        | x = 1 ; FIN        | δ(q2, x, x) ⇒ (q2, λ)                            |
| Z FIN `<sentencias>` `;` `<valor>` `=`                          | = 1 ; FIN          | δ(q2, =, =) ⇒ (q2, λ)                                  |
| Z FIN `<sentencias>` `;` `<valor>`                              | 1 ; FIN            | δ(q2, λ, `<valor>`) ⇒ (q2, **`<numero>`**)                                                   |
| → **pila: Z FIN `<sentencias>` `;` `<numero>`**                 |                    |                                                                                                                                                      |
| Z FIN `<sentencias>` `;` `<numero>`                             | 1 ; FIN            | δ(q2, λ, `<numero>`) ⇒ (q2, **`1`**)                                                        |
| → **pila: Z FIN `<sentencias>` `;` 1**                          |                    |                                                                                                                                                      |
| Z FIN `<sentencias>` `;` 1                                      | 1 ; FIN            | δ(q2, 1, 1) ⇒ (q2, λ)                                         |
| Z FIN `<sentencias>` `;`                                        | ; FIN              | δ(q2, ;, ;) ⇒ (q2, λ)                                                    |
| Z FIN `<sentencias>`                                            | FIN                | δ(q2, λ, `<sentencias>`) ⇒ (q2, λ)                                                 |
| Z FIN                                                           | FIN                | δ(q2, FIN, FIN) ⇒ (q2, λ)                                                               |
| Z                                                               | (vacío)            | δ(q2, λ, Z) ⇒ (q3, λ)                                                                                                                 |
| λ (estado q3)                                                   | (vacío)            | accept                                                                                                                                               |
