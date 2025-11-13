### Es importante considerar que en LDR no se declaran tipos en tiempo de ejecución, así que las únicas entradas nuevas en TT son las declaraciones explícitas de tipos (NUM, CAR, ARR) cuando aparecen.

#### TT:

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | NUM  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | CAR  | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | BOOL | -1 | -1 | -1 | -1 | -1 | 0 |

# PROGRAMA 1:

```
    INICIO
      X = 1;
      IMPRIMIR X;
    FIN
```

### Al procesar la línea 2

#### TS:

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | x | variable | 0 (NUM inferido por asignación) | -1 | null | 0 |

### Luego se procesa la línea 3 y por último la 4 donde se marca el cierre del programa (`FIN`), por lo tanto ya no se necesitan ni la **TT** ni la **TS**, y pueden ser eliminadas.

# PROGRAMA 2:

```
    INICIO
      X NUM NUM;
      X = 1;
      IMPRIMIR X;
    FIN
```

### Como hay un error sintáctico en la línea número 2 se detiene la compilación, hasta llegar al error la TS es la siguiente:

#### TS:

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | x | variable | 0 | -1 | null | 0 |

# PROGRAMA 3:

```
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

### Se procesa la línea 1 y luego la línea 2 donde se crea el ámbito 1 (las funciones abren su propio ámbito) y La función SUMAR se agrega al ámbito global. Sus parámetros (X, Y) pertenecen al ámbito 1.

#### TS

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | SUMAR | funcion | -1 | 2 | [NUM, NUM] | 0 |
| 1	| X	| parametro | 0 | -1 | null | 1 |
| 2 | Y | parametro | 0 | -1 | null | 1 |

### Se procesa la línea 3

#### TS

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | SUMAR | funcion | -1 | 2 | [NUM, NUM] | 0 |
| 1	| X	| parametro | 0 | -1 | null | 1 |
| 2 | Y | parametro | 0 | -1 | null | 1 |
| 3 | RES | variable | 0 | -1 | null | 1 |

### Se procesan las líneas 4 y 5, donde no hay cambios ni en la TT ni en la TS, luego se procesa la línea 6 donde se cierra el ámbito 1 y se vuelve al ámbito 0. Las variables de ámbito 1 permanecen en TS porque son parte de la definición de la función.

### Se procesa la línea 7

#### TS

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | SUMAR | funcion | -1 | 2 | [NUM, NUM] | 0 |
| 1	| X	| parametro | 0 | -1 | null | 1 |
| 2 | Y | parametro | 0 | -1 | null | 1 |
| 3 | RES | variable | 0 | -1 | null | 1 |
| 4 | A | variable | 0 | -1 | null | 0 |

### Se procesa la línea 8

#### TS

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | SUMAR | funcion | -1 | 2 | [NUM, NUM] | 0 |
| 1	| X	| parametro | 0 | -1 | null | 1 |
| 2 | Y | parametro | 0 | -1 | null | 1 |
| 3 | RES | variable | 0 | -1 | null | 1 |
| 4 | A | variable | 0 | -1 | null | 0 |
| 5 | B | variable | 0 | -1 | null | 0 |

### Se procesan las líneas 9, 10 y 11, sin cambios, luego se procesa la línea 12 donde el programa finaliza → TT y TS dejan de ser necesarias y pueden ser destruidas.