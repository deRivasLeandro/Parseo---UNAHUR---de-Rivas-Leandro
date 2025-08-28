# Lenguaje seleccionado para trabajar durante la cursada:

## 📘 Documentación del Lenguaje LDR

{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "339b73b3-3b1c-4557-b285-de10177f9ece",
   "metadata": {},
   "source": [
    "# TP Introducción\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "724e08c5-5e77-4a0e-9202-4da97c865066",
   "metadata": {},
   "source": [
    "## Mapa conceptual"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be8ee74b-c406-4cd5-ae30-f1e703db5fb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "```mermaid\n",
    "graph TD;\n",
    "  A[LDR] --> B[Tipos de datos];\n",
    "  B --> B1[NUM];\n",
    "  B --> B2[CAR];\n",
    "  B --> B3[ARR];\n",
    "\n",
    "  A --> C[Sentencias];\n",
    "  C --> C1[Declaración];\n",
    "  C --> C2[Asignación];\n",
    "  C --> C3[Impresión];\n",
    "  C --> C4[Condicional];\n",
    "  C --> C5[Iteración];\n",
    "  C --> C6[Funciones];\n",
    "\n",
    "  A --> D[Operadores];\n",
    "  D --> D1[NUM y CAR: +, -, *, /];\n",
    "  D --> D2[ARR + ARR: concat];\n",
    "  D --> D3[ARR * NUM: repetición];\n",
    "\n",
    "  A --> E[Características];\n",
    "  E --> E1[Imperativo estructurado];\n",
    "  E --> E2[Tipado estático y fuerte];\n",
    "  E --> E3[Sensible a mayúsculas];\n",
    "  E --> E4[Control de flujo];\n",
    "  E --> E5[Subprogramas con parámetros];\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14578311-401c-4d2a-b6ab-74d488448a12",
   "metadata": {},
   "source": [
    "## Lenguaje a crear"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3cbd96bc-7509-4909-9ffc-30f12a9433a1",
   "metadata": {},
   "source": [
    "### Objetivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd6e006d-3615-44d4-a3cf-bc6bbb948461",
   "metadata": {},
   "outputs": [],
   "source": [
    "LDR es un lenguaje de propósito general orientado al aprendizaje de los conceptos básicos de programación:\n",
    "- Paradigma imperativo y estructurado.\n",
    "- Incluye asignación, iteración y condicionales.\n",
    "- Define tipos primitivos simples y un tipo compuesto (arrays).\n",
    "- Integra funciones con parámetros posicionales como subprogramas.\n",
    "Su objetivo es facilitar la comprensión de gramática, semántica y sistemas de tipos en los lenguajes de programación."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72e244b4-a7b5-44ff-9c81-f2de96871542",
   "metadata": {},
   "source": [
    "### Alcance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf619b67-00ea-4ad3-b2e5-9a743da248c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "- Programas con estructura `INICIO ... FIN`.\n",
    "- Declaración de variables globales y locales.\n",
    "- Uso de control de flujo mediante `SI`, `SINO`, `MIENTRAS`.\n",
    "- Definición de funciones sin retorno (procedimientos).\n",
    "- Manejo de arreglos con operaciones básicas (+ para concatenar, * para repetir).\n",
    "- Operaciones aritméticas entre números y caracteres con conversión ASCII implícita.\n",
    "- No posee manejo de errores ni recursividad."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa8516b2-701f-4afe-aafc-5a2acfda3df6",
   "metadata": {},
   "source": [
    "### Especificaciones léxicas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "935c8a41-027b-4d53-ba65-37954e2be427",
   "metadata": {},
   "outputs": [],
   "source": [
    "- Variables: [A-Z]+[0-9]* (ej: `X`, `VAR1`).\n",
    "- Números: secuencia de dígitos [0-9]+.\n",
    "- Caracteres: `'c'` donde `c` es un carácter ASCII.\n",
    "- Arrays: `[elementos]` separados por coma.\n",
    "- Palabras reservadas: `INICIO`, `FIN`, `SI`, `SINO`, `FINSI`, `MIENTRAS`, `HACER`, `FINMIENTRAS`, `FUNCION`, `FINFUNCION`, `IMPRIMIR`.\n",
    "- Operadores: `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`, `!`.\n",
    "- Sensibilidad a mayúsculas: sí."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3034dce-4b36-4e2c-b264-d2e388087546",
   "metadata": {},
   "source": [
    "### Especificaciones sintácticas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5fabb53-5075-4d70-ab58-eb4cac5639ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "```bnf\n",
    "<programa> ::= \"INICIO\" <bloque> \"FIN\"\n",
    "<bloque> ::= <definiciones_funcion> <sentencias>\n",
    "<definiciones_funcion> ::= <definicion_funcion> <definiciones_funcion> | λ\n",
    "<definicion_funcion> ::= \"FUNCION\" <nombre> \"(\" <parametros>* \")\" <sentencias> \"FINFUNCION\"\n",
    "<parametros> ::= <parametro> (\",\" <parametro>)*\n",
    "<parametro> ::= <variable> <tipo>\n",
    "<sentencias> ::= <sentencia> <sentencias> | λ\n",
    "<sentencia> ::= <declaracion> \";\" | <asignacion> \";\" | <impresion> \";\" | <condicional> \";\" | <iteracion> \";\" | <llamado_funcion> \";\"\n",
    "<tipo> ::= \"NUM\" | \"CAR\" | \"ARR\"\n",
    "<declaracion> ::= <variable> <tipo> | <variable> <tipo> \"=\" <valor>\n",
    "<asignacion> ::= <variable> \"=\" <valor>\n",
    "<impresion> ::= \"IMPRIMIR\" (<variable> | <valor>)\n",
    "<condicional> ::= \"SI\" <condicion> \"ENTONCES\" <sentencias> \"SINO\" <sentencias> \"FINSI\"\n",
    "<condicion> ::= <valor> <operador_comparacion> <valor> | \"(\" <condicion> \")\" | <condicion> \"&&\" <condicion> | <condicion> \"||\" <condicion> | \"!(\" <condicion> \")\"\n",
    "<operador_comparacion> ::= \"<\" | \">\" | \"==\" | \"<=\" | \">=\" | \"!=\"\n",
    "<iteracion> ::= \"MIENTRAS\" <condicion> \"HACER\" <sentencias> \"FINMIENTRAS\"\n",
    "<valor> ::= <numero> | <caracter> | <array> | <operacion> | <variable>\n",
    "<operacion> ::= <valor> <operador> <valor>\n",
    "<operador> ::= \"+\" | \"-\" | \"*\" | \"/\"\n",
    "<llamado_funcion> ::= <nombre> \"(\" <argumentos>* \")\"\n",
    "<argumentos> ::= <valor> (\",\" <valor>)*\n",
    "<array> ::= \"[\" <array-content> \"]\"\n",
    "<array-content> ::= <item> \",\" <array-content> | <item>\n",
    "<item> ::= <numero> | <caracter>\n",
    "<numero> ::= [0-9]+\n",
    "<caracter> ::= \"'\" <cualquier_caracter> \"'\"\n",
    "<variable> ::= [A-Z]+[0-9]*\n",
    "<nombre> ::= [A-Z]+\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cdbe9002-6fba-404a-89d2-90d55294b58e",
   "metadata": {},
   "source": [
    "### Especificaciones semánticas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "daf2f5f8-c636-48f8-8749-a94750132377",
   "metadata": {},
   "outputs": [],
   "source": [
    "- **Operaciones con CAR y NUM:** un `CAR` se convierte a su valor ASCII para operar con `NUM`.\n",
    "  - Ejemplo: `'A' + 1 = 66`.\n",
    "- **Operaciones con ARR:**\n",
    "  - `ARR + ARR` → concatena dos arreglos.\n",
    "  - `ARR * NUM` → repite el arreglo tantas veces como indique el número.\n",
    "- **Funciones:**\n",
    "  - Definidas con `FUNCION <nombre>(<parametros>) ... FINFUNCION`.\n",
    "  - Parámetros posicionales, variables locales.\n",
    "  - No poseen retorno explícito (procedimientos), pueden imprimir resultados.\n",
    "  - Errores semánticos:\n",
    "    - Error de aridad: número de argumentos distinto a la definición.\n",
    "    - Error de tipos: incompatibilidad entre tipo esperado y tipo recibido.\n",
    "- **Tipado:** estático y fuerte. No se permite operar entre tipos incompatibles salvo reglas de sobrecarga definidas.\n",
    "- **Ámbito:** variables globales y locales a funciones."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

---

### 📌 Descripción en Lenguaje Natural
LDR es un lenguaje de programación de propósito general, simple y de paradigma imperativo estructurado.

- Las variables se escriben con letras mayúsculas (A–Z) seguidas opcionalmente de uno o más números.  
  Ejemplos: `X`, `Z1`, `VAR99`.
- Las sentencias, incluyendo bloques de control de flujo, se escriben en mayúscula y finalizan con punto y coma ;.
- Un programa inicia con la palabra clave `INICIO` y finaliza con `FIN`.
- La identación no es obligatoria, pero se recomienda para mejorar la claridad del programa.

### Tipos de datos
- **Primitivos:** `NUM` (número entero), `CAR` (carácter).
- **Compuestos:** `ARR` (arreglo).

### Sentencias válidas:
- **Declaración:**
  - `VAR tipo;`  
  - Ejemplo: `X NUM;`
  - También se permite declarar e inicializar: `VAR tipo = valor;`

- **Asignación:**
  - `VAR = valor;`  
  - Ejemplo: `X = 10;`
  - La reasignación funciona de la misma manera

- **Condicional:**
```ldr
SI condición ENTONCES
  sentencias
SINO
  sentencias
FINSI;
```

- **Iteración:**
```ldr
MIENTRAS condición HACER
  sentencias
FINMIENTRAS;
```

- **Impresión:** (similar a `console.log()`)
  - `IMPRIMIR VAR;`

- **Funciones/Subprogramas:**
  - Se pueden invocar con `NOMBRE(ARGUMENTOS);`

```ldr
FUNCION NOMBRE(PARAMS)
  sentencias
FINFUNCION
```

---

## 📘 Gramática en BNF de LDR
```bnf
<programa> ::= "INICIO" <bloque> "FIN"

<bloque> ::= <definiciones_funcion> <sentencias>

<definiciones_funcion> ::= <definicion_funcion> <definiciones_funcion> | λ

<definicion_funcion> ::= "FUNCION" <nombre> "(" <parametros>* ")" <sentencias> "FINFUNCION"

<parametros> ::= <parametro> ("," <parametro>)*

<parametro> ::= <variable> <tipo>

<sentencias> ::= <sentencia> <sentencias> | λ

<sentencia> ::= <declaracion> ";"
              | <asignacion> ";"
              | <impresion> ";"
              | <condicional> ";"
              | <iteracion> ";"
              | <llamado_funcion> ";"

<tipo> ::= "NUM" | "CAR" | "ARR"

<declaracion> ::= <variable> <tipo> | <variable> <tipo> "=" <valor>

<asignacion> ::= <variable> "=" <valor>

<impresion> ::= "IMPRIMIR" (<variable> | <valor>)

<condicional> ::= "SI" <condicion> "ENTONCES" <sentencias> "SINO" <sentencias> "FINSI"

<condicion> ::= <valor> <operador_comparacion> <valor> | "(" <condicion> ")" | <condicion> "&&" <condicion> | <condicion> "||" <condicion> | "!(" <condicion> ")"

<operador_comparacion> ::= "<" | ">" | "==" | "<=" | ">=" | "!="

<iteracion> ::= "MIENTRAS" <condicion> "HACER" <sentencias> "FINMIENTRAS"

<valor> ::= <numero> | <caracter> | <array> | <operacion> | <variable>

<operacion> ::= <valor> <operador> <valor>

<operador> ::= "+" | "-" | "*" | "/"

<llamado_funcion> ::= <nombre> "(" <argumentos>* ")"

<argumentos> ::= <valor> ("," <valor>)*

<array> ::= "[" <array-content> "]"

<array-content> ::= <item> "," <array-content> | <item>

<item> ::= <numero> | <caracter>

<numero> ::= [0-9]+ 

<caracter> ::= "'" <cualquier_caracter> "'"
<cualquier_caracter> ::= [A-Za-z0-9!@#$%^&*()_+-=\[\]{}|;:'",.<>/?`~] | " "

<variable> ::= [A-Z]+[0-9]*

<nombre> ::= [A-Z]+
```

---

## 📘 Reglas Semánticas para Operaciones Sobrecargadas

### 1. 🔤 CAR con NUM
Los caracteres se interpretan como su código ASCII.

**Operaciones permitidas:** `+`, `-`, `*`, `/` entre `CAR` y `NUM` (en cualquier orden).

**Regla:** Convertir `CAR` a su valor ASCII (entero), luego operar.

**Ejemplos:**
| Expresión | Resultado |
|-----------|-----------|
| `'A' + 1` | 66        |
| `1 + 'A'` | 66        |
| `'C' - 1` | 66        |
| `2 * 'B'` | 132       |
| `'D' / 2` | 34        |

### 2. 🧱 ARR con ARR y ARR con NUM

**Operaciones permitidas:**
- `ARR + ARR`: concatenación.
- `ARR * NUM`: repetición.

**Ejemplos:**
| Expresión             | Resultado                |
|----------------------|--------------------------|
| `[1] + ['A']`         | `[1, 'A']`               |
| `[1,2] + [3,4]`       | `[1,2,3,4]`              |
| `[1]*3`               | `[1,1,1]`                |
| `['X','Y']*2`         | `['X','Y','X','Y']`      |

---

## 🎯 Semántica de Funciones

- Más que funciones son procedimientos, puesto que no tienen un return.
- Las funciones se definen con `FUNCION <nombre>(<parametros>)` y terminan con `FINFUNCION`.
- No devuelven valores (procedimientos), pero pueden usar `IMPRIMIR`.
- Los parámetros son **ligados posicionalmente**, y son **variables locales**.

### Reglas de Tipos
| Situación                                     | Regla                            |
|----------------------------------------------|----------------------------------|
| Llamado con cantidad incorrecta de argumentos | ❌ Error de aridad               |
| Tipos incompatibles                           | ❌ Error de tipo                 |
| Variables locales                             | ✔️ Solo accesibles en la función |
| Parámetros duplicados                         | ❌ Error de declaración          |

---

## 🧾 Clasificación de LDR (Cuadro extendido de características)

| Características                     | LDR                                                                 |
|-------------------------------------|----------------------------------------------------------------------|
| Paradigma                           | Imperativo, estructurado                                             |
| Tipos de datos                      | Primitivos: NUM, CAR<br>Compuestos: ARR                              |
| Asignación                          | Sí (`<variable> = <valor>`)                                          |
| Iteración                           | Sí (`MIENTRAS <condición> HACER ... FINMIENTRAS`)                   |
| Condicional                         | Sí (`SI <condición> ENTONCES ... SINO ... FINSI`)                   |
| Tipado                              | Estático (en tiempo de declaración)                                 |
| Sistema de Tipos                    | Fuerte                                                              |
| Conversión de Tipos                 | Implícita para CAR -> NUM (ASCII)                                     |
| Sobrecarga de operadores            | Parcial: `+`, `-`, `*`, `/` sobre NUM y CAR;<br>`+`, `*` sobre ARR    |
| Nivel de abstracción                | Alto                                                                |
| Independencia de la máquina         | Sí                                                                  |
| Orientación a objetos               | No                                                                  |
| Sensible a mayúsculas               | Sí (`X` y `x` son diferentes). No aplica para identificadores de variables (solo se permiten mayúsculas).         |
| Control de flujo                    | Secuencia, selección, iteración, subprogramas                       |
| Subprogramas                        | Sí (funciones definidas con parámetros)                             |
| Funciones anidadas / Closures       | No                                                                  |
| Polimorfismo                        | Limitado: por sobrecarga de operadores                              |
| Paso de parámetros                  | Sí (posicional, con tipo explícito)                                 |
| Ámbito de variables                 | Global y local (funciones tienen su propio entorno local)           |
| Recursividad                        | No soportada explícitamente                                         |
| Evaluación de expresiones           | Estricta                                                            |
| Expresiones soportadas              | Infijas (`a + b`), con paréntesis opcionales                        |
| Evaluación de condiciones           | Booleana con comparación de NUM y CAR                               |
| Tiempo de ligadura de tipos         | Estático                                                            |
| Valores por defecto                 | No                                                                  |
| Inicialización implícita            | No                                                                  |
| Mutabilidad                         | Sí (las variables pueden reasignarse)                               |
| Representación interna de CAR       | Código ASCII                                                        |
| Compatibilidad de tipos             | Por nombre, con conversión limitada semánticamente                  |
| Representación de arrays            | Corchetes: `[1, 'A']`                                               |
| Operaciones con arrays              | `+` (concat), `*` (repetir con NUM)                                 |
| Longitud de identificadores         | [A-Z]+[0-9]?                                                        |
| Constantes                          | Numéricas (`3`), caracteres (`'A'`)                                 |
| Manejo de errores / excepciones     | No                                                                  |
| Eventos                             | No                                                                  |
| Forma de comentario                 | No definida (convención: `//`, `#` a implementar)                          |
---

## 🧪 Ejemplos de Programas

### Ejemplo 1: Condicional simple
```ldr
INICIO
  X NUM;
  X = 7;
  SI X > 0 ENTONCES
    IMPRIMIR X;
  SINO
    IMPRIMIR 'N';
  FINSI;
FIN
```

### Ejemplo 2: Arrays, operaciones y sobrecarga
```ldr
INICIO
  A NUM;
  B NUM;
  C CAR;
  D NUM;
  LISTA ARR;

  A = 5;
  B = 10;
  C = 'A';
  D = A + B;
  IMPRIMIR D;
  D = D + C;
  IMPRIMIR D;

  LISTA = [1, 2, 3, 4, 5];
  I NUM;
  I = 0;

  MIENTRAS I < 5 HACER
    IMPRIMIR LISTA[I];
    I = I + 1;
  FINMIENTRAS;

  SI D > 50 ENTONCES
    IMPRIMIR 'S';
  SINO
    IMPRIMIR 'N';
  FINSI;
FIN
```

### Ejemplo 3: Uso de función SUMAR
```ldr
INICIO
  FUNCION SUMAR(X NUM, Y NUM)
    RES NUM;
    RES = X + Y;
    IMPRIMIR RES;
  FINFUNCION

  A NUM;
  B NUM;
  A = 5;
  B = 7;
  SUMAR(A, B);
FIN
```