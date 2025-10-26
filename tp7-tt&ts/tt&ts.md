Ejemplo a analizar:
INICIO 
    x = 1; 
FIN

1) Inicialmente, se agregan los tipos básicos a la TT:
|Cod|Nombre|TipoBase|Padre|Dimensión|Mínimo|Máximo|Ámbito|
| 0 | int  |   -1   | -1  |   -1    |  -1  |  -1  |  0   |
| 1 | car  |   -1   | -1  |   -1    |  -1  |  -1  |  0   |
| 2 | bool |   -1   | -1  |   -1    |  -1  |  -1  |  0   |

2) Se procesa la línea 1, luego la 2:
|                         TT                             |
|Cod|Nombre|TipoBase|Padre|Dimensión|Mínimo|Máximo|Ámbito|
| 0 | int  |   -1   | -1  |   -1    |  -1  |  -1  |  0   |
| 1 | car  |   -1   | -1  |   -1    |  -1  |  -1  |  0   |
| 2 | bool |   -1   | -1  |   -1    |  -1  |  -1  |  0   |

|                         TS                             |
|Cod| Nombre |Categoria|Tipo| NumPar | ListaPar | Ámbito |
| 0 |   x    |variable | 0  |   -1   |   null   |   0    |


3) Se procesa la línea 3: la última línea del programa, ya no se necesitan ni la TT ni la TS y por lo tanto se la puede eliminar
|Cod|Nombre|TipoBase|Padre|Dimensión|Mínimo|Máximo|Ámbito|
