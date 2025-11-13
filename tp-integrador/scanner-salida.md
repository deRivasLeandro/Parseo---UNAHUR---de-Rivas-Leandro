### Salida del parser.parse(PROGRAMA) en formato AST (Abstract Syntax Tree o Árbol de Sintaxis Abstracta)

#### Programa 1:

```
('programa',
  ('bloque',
    [],  # sin funciones
    [
      ('asig', 'X', ('num', 1)),
      ('print', 'X')
    ]
  )
)
```

#### Programa 2:

#### Problemas con el programa, no hay salida del parsing

#### Programa 3:

```
('programa',
  ('bloque',
    [   # definiciones de función
        ('funcion', 'SUMAR',
          [('param', 'X', 'NUM'), ('param', 'Y', 'NUM')],
          [
            ('decl', 'RES', 'NUM', None),
            ('asig', 'RES', ('op', '+', ('var', 'X'), ('var', 'Y'))),
            ('print', 'RES')
          ]
        )
    ],
    [   # sentencias del bloque principal
        ('decl', 'A', 'NUM', None),
        ('decl', 'B', 'NUM', None),
        ('asig', 'A', ('num', 5)),
        ('asig', 'B', ('num', 7)),
        ('call', 'SUMAR', [('var', 'A'), ('var', 'B')])
    ]
  )
)
```
