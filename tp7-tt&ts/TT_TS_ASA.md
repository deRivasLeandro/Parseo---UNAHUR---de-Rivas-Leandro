## Ejemplo a analizar

```
INICIO 
    x = 1; 
FIN
```

---

### 1) Inicialmente, se agregan los tipos básicos a la TT

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

---

### 2) Se procesa la línea 1 y luego la línea 2

#### Tabla de Tipos (TT)

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

#### Tabla de Símbolos (TS)

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | x | variable | 0 | -1 | null | 0 |

---

### 3) Se procesa la línea 3

La última línea del programa marca el cierre (`FIN`), por lo tanto ya no se necesitan ni la **TT** ni la **TS**, y pueden ser eliminadas.

---

# Ejemplo más elaborado

INICIO
  X NUM;
  X = 7;
  SI X > 0 ENTONCES
    IMPRIMIR X;
  SINO
    IMPRIMIR 'N';
  FINSI;
FIN

---

### 1) Inicialmente, se agregan los tipos básicos a la TT

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

---

### 2) Se procesa la línea 1 y luego la línea 2

#### Tabla de Tipos (TT)

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

#### Tabla de Símbolos (TS)

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | X | variable | 0 | -1 | null | 0 |

---

### 3) Se procesa la línea 3 y posteriormente la 4

#### Tabla de Tipos (TT)

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

#### Tabla de Símbolos (TS)

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | X | variable | 0 | -1 | null | 0 |
| 1 | Y | variable | 1 | -1 | null | 0 |

---

### 4) Se procesa la línea 5
Con la lectura de la línea 5 se genera un nuevo ámbito (`SI`), cualquier tipo o símbolo añadido hasta salir de este ámbito será de tipo 1. Cabe aclarar que al entrar en el SI, se analiza la condición en el ámbito actual (0), y recién al comenzar el bloque “ENTONCES” se crea el nuevo ámbito (1).

---

### 5) Se procesan las líneas 6 y 7
Con la lectura de la línea 7 se sale del ámbito 1 y genera un nuevo ámbito (`SINO`), cualquier tipo o símbolo añadido hasta salir de este ámbito será de tipo 2.

---

### 6) Se procesa la línea 8

#### Tabla de Tipos (TT)

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

#### Tabla de Símbolos (TS)

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | X | variable | 0 | -1 | null | 0 |
| 1 | Y | variable | 1 | -1 | null | 0 |
| 2 | Z | variable | 2 | -1 | null | 2 |

---

### 7) Se procesan las líneas 9 y 10
Al leer la línea 10 (`FINSI`) se sale del ámbito 2, volviendo al ámbito 0.

#### Tabla de Tipos (TT)

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

#### Tabla de Símbolos (TS)

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | X | variable | 0 | -1 | null | 0 |
| 1 | Y | variable | 1 | -1 | null | 0 |

---

### 8) Se procesa la línea 11

La última línea del programa marca el cierre (`FIN`), por lo tanto ya no se necesitan ni la **TT** ni la **TS**, y pueden ser eliminadas.

---