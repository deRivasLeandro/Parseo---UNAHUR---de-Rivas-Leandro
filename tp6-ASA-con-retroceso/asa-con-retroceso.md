1) GIC (mínima) usada

GIC = < ΣN, ΣT, S, P >

ΣN = { `<programa>`, `<bloque>`, `<definiciones_funcion>`, `<sentencias>`, `<sentencia>`, `<asignacion>`, `<variable>`, `<valor>`, `<numero>` }

ΣT = { INICIO, FIN, x (IDENT), =, 1 (NUMERO), ; }

S = `<programa>`

P = (1)  `<programa>`               ::= INICIO `<bloque>` FIN
    (2)  `<bloque>`                 ::= `<definiciones_funcion>` `<sentencias>`
    (3)  `<definiciones_funcion>`   ::= λ
    (4)  `<sentencias>`             ::= `<sentencia>` `<sentencias>`
    (5)  `<sentencia>`              ::= `<asignacion>` ";"
    (6)  `<asignacion>`             ::= `<variable>` "=" `<valor>`
    (7)  `<variable>`               ::= x
    (8)  `<valor>`                  ::= `<numero>`
    (9)  `<numero>`                 ::= 1
    (10) `<sentencias>`             ::= λ

2) PDA — transiciones δ (estilo ejemplo)

Estados: q0, q1, q2, q3. Símbolo inicial de pila: Z.

Las transiciones se escriben como:

δ(estado_actual, símbolo_entrada, símbolo_tope_pila) => (nuevo_estado, símbolos_a_empujar_sobre_pila)


Transiciones de inicialización y expansión de axioma:

δ(q0, λ, λ) = (q1, #)
δ(q1, λ, S) = (q2, λ)


Expansiones (cuando en tope hay un no terminal lo expandimos empujando el RHS):

δ(q1, λ, `<programa`)                              => (q1, S)

δ(q1, λ, INICIO `<bloque>` FIN)                    => (q1, `<programa`)

δ(q1, λ, `<definiciones_funcion>` `<sentencias>`)  => (q1, `<bloque>`)
δ(q1, λ, λ)                                        => (q1, `<definiciones_funcion>`)

δ(q1, λ, `<sentencia>` `<sentencias>`)             => (q1, `<sentencias>`)
δ(q1, λ, λ)                                        => (q1, `<sentencias>`)

δ(q1, λ, `<asignacion>`;)                          => (q1, `<sentencia>`)
δ(q1, λ, `<variable>` = `<valor>`)                 => (q1, `<asignacion>`;)
δ(q1, λ, x)                                        => (q1, `<variable>`)                      
δ(q1, λ, `<numero>`)                               => (q1, `<valor>`)
δ(q1, λ, 1)                                        => (q1, `<numero>`)


Transiciones de consumo de terminales (cuando el tope coincide con token actual):

δ(q1, INICIO, λ)               => (q1, INICIO)
δ(q1, x, λ)                    => (q1, x)
δ(q1, =, λ)                    => (q1, =)
δ(q1, 1, λ)                    => (q1, 1)
δ(q1, ;, λ)                    => (q1, ;)
δ(q1, FIN, λ)                  => (q1, FIN)


Transición de aceptación:

δ(q2, λ, #)                    => (q3, λ)

3)
| Pila (tope derecha)                                           | Entrada de tokens  | Transición aplicada   |
| ------------------------------------------------------------- | ------------------ | -------------------   |
| λ                                                             | INICIO x = 1; FIN  | δ(q0, λ, λ) = (q1, #) |
| #                                                             | INICIO x = 1; FIN  | shift                 |
| #INICIO                                                       | x = 1; FIN         | reduce                 |
| #INICIO `<definiciones_funcion>`                              | x = 1; FIN         | shift                 |
| #INICIO `<definiciones_funcion>` x                            | = 1; FIN           | reduce                |
| #INICIO `<definiciones_funcion>` `<variable>`                 | = 1; FIN           | shift                 |
| #INICIO `<definiciones_funcion>` `<variable>` =               | 1; FIN             | shift                 |
| #INICIO `<definiciones_funcion>` `<variable>` = 1             | ; FIN              | reduce                |
| #INICIO `<definiciones_funcion>` `<variable>` = `<numero>`    | ; FIN              | reduce                |
| #INICIO `<definiciones_funcion>` `<variable>` = `<valor>`     | ; FIN              | reduce                |
| #INICIO `<definiciones_funcion>` `<asignacion>`               | ; FIN              | shift                 |
| #INICIO `<definiciones_funcion>` `<asignacion>`;              | FIN                | reduce                |
| #INICIO `<definiciones_funcion>` `<sentencia>`                | FIN                | reduce                |
| #INICIO `<definiciones_funcion>` `<sentencia>` `<sentencias>` | FIN                | reduce                |
| #INICIO `<definiciones_funcion>` `<sentencias>`               | FIN                | reduce                |
| #INICIO `<bloque>`                                            | FIN                | shift                 |
| #INICIO `<bloque>` FIN                                        |                    | reduce                |
| #`<programa>`                                                 |                    | reduce                |
| #S                                                            |                    | δ(q1, λ, S) = (q2, λ) |
| #                                                             | λ                  | δ(q2, λ, #) = (q3, λ) |
| λ	                                                            | λ                  | accept                |
