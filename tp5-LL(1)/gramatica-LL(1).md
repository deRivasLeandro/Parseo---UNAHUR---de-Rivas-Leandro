1) Gramática LDR (simplificada)

Se trabaja sobre la cadena `INICIO x = 1; FIN`:

1) \<programa>              → INICIO \<bloque> FIN  
2) \<bloque>                → \<definiciones_funcion> \<sentencias>  
3) \<definiciones_funcion>  → λ  
4) \<sentencias>            → \<sentencia> \<sentencias>  
5) \<sentencias>            → λ  
6) \<sentencia>             → \<asignacion> ;  
7) \<asignacion>            → \<variable> = \<valor>  
8) \<variable>              → x  
9) \<valor>                 → \<numero>  
10) \<numero>               → 1

---

2) Algoritmo de conjunto de primeros:

| PRIM                             |
| --                               |
| PRIM(programa) = {INICIO}        |
| PRIM(bloque) = {x, λ}            |
| PRIM(definiciones_funcion) = {λ} | 
| PRIM(sentencias) = {x, λ}        |
| PRIM(sentencia) = {x}            |
| PRIM(asignacion) = {x}           |
| PRIM(variable) = {x}             |
| PRIM(valor) = {1}                |
| PRIM(numero) = {1}               |

---

3) Algoritmo de conjunto de siguientes:

| SIG                                  |
| --                                   |
| SIG(programa) = {\$}                 |
| SIG(bloque) = {FIN}                  |
| SIG(definiciones_funcion) = {x, FIN} | 
| SIG(sentencias) = {FIN}              |
| SIG(sentencia) = {x, FIN}            |
| SIG(asignacion) = {;}                |
| SIG(variable) = {=}                  |
| SIG(valor) = {;}                     |
| SIG(numero) = {;}                    |

---

4) Algoritmo de conjunto de predicciones:

| PRED                                                            |
| --                                                              |
| PRED(programa → INICIO \<bloque> FIN) = {INICIO}                |
| PRED(bloque → \<definiciones_funcion> \<sentencias>) = {x, FIN} | 
| PRED(definiciones_funcion → λ) = {x, FIN}                       |
| PRED(sentencias → \<sentencia> \<sentencias>) = {x}             |
| PRED(sentencias → λ) = {FIN}                                    |
| PRED(sentencia → \<asignacion> ;) = {x}                         |
| PRED(asignacion → \<variable> = \<valor>) = {x}                 |
| PRED(variable → x) = {x}                                        |
| PRED(valor → \<numero>) = {1}                                   |
| PRED(numero → 1) = {1}                                          |

---

5) Verificación LL(1):

| VERIF                         |
| --                            |
| programa → ∩ = {}             |
| bloque → ∩ = {}               |
| definiciones_funcion → ∩ = {} | 
| sentencias → {x} ∩ {FIN} = {} |
| sentencia → ∩ = {}            |
| asignacion → ∩ = {}           |
| variable → ∩ = {}             |
| valor → ∩ = {}                |
| numero → ∩ = {}               |

* Es LL(1)