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
| 0 | int  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | char | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | bool | -1 | -1 | -1 | -1 | -1 | 0 |

---

### 2) Se procesa la línea 1 y luego la línea 2

#### Tabla de Tipos (TT)

| Cod | Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito |
|:---:|:-------|:---------|:------|:-----------|:-------|:-------|:-------|
| 0 | int  | -1 | -1 | -1 | -1 | -1 | 0 |
| 1 | char | -1 | -1 | -1 | -1 | -1 | 0 |
| 2 | bool | -1 | -1 | -1 | -1 | -1 | 0 |

#### Tabla de Símbolos (TS)

| Cod | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
|:---:|:-------|:-----------|:----:|:-------:|:----------|:-------:|
| 0 | x | variable | 0 | -1 | null | 0 |

---

### 3) Se procesa la línea 3

La última línea del programa marca el cierre (`FIN`), por lo tanto ya no se necesitan ni la **TT** ni la **TS**, y pueden ser eliminadas.
