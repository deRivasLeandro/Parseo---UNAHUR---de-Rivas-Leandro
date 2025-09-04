import ply.lex as lex

# Palabras reservadas del lenguaje
reserved = {
    'INICIO': 'INICIO',
    'FIN': 'FIN',
    'SI': 'SI',
    'ENTONCES': 'ENTONCES',
    'SINO': 'SINO',
    'FINSI': 'FINSI',
    'MIENTRAS': 'MIENTRAS',
    'HACER': 'HACER',
    'FINMIENTRAS': 'FINMIENTRAS',
    'IMPRIMIR': 'IMPRIMIR',
    'FUNCION': 'FUNCION',
    'FINFUNCION': 'FINFUNCION',
    'NUM': 'NUM',
    'CAR': 'CAR',
    'ARR': 'ARR',
}

# Lista de tokens
tokens = [
    'VARIABLE',
    'NOMBRE',
    'NUMERO',
    'CARACTER',
    'ARRAY',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIR',
    'MENOR_QUE',
    'MAYOR_QUE',
    'IGUAL_QUE',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'DISTINTO_QUE',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'COMA',
    'PUNTO_Y_COMA',
    'AMPERSAND',
    'PIPE',
    'EXCLAMACION',
] + list(reserved.values())

# Expresiones regulares para tokens simples
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIR = r'/'
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_IGUAL_QUE = r'=='
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_DISTINTO_QUE = r'!='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_COMA = r','
t_PUNTO_Y_COMA = r';'
t_AMPERSAND = r'&&'
t_PIPE = r'\|\|'
t_EXCLAMACION = r'!'

# Expresión regular para números
def t_NUMERO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# Expresión regular para caracteres
def t_CARACTER(t):
    r"'[A-Za-z0-9!@#$%^&*()_+\-=\[\]{}|;:'\",.<>/?`~ ]'"
    t.value = t.value[1:-1]
    return t

# Expresión regular para variables y palabras reservadas
def t_VARIABLE(t):
    r'[A-Z]+[0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# Expresión regular para nombres de funciones
def t_NOMBRE(t):
    r'[A-Z]+'
    t.type = reserved.get(t.value, 'NOMBRE')
    return t
    
# Ignora los espacios y tabulaciones
t_ignore = ' \t'

# Conteo de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print("Carácter inválido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcción el analizador léxico
lexer = lex.lex()

# Prueba del analizador léxico
if __name__ == '__main__':
    data = '''
    INICIO
    X NUM;
    Y CAR;
    Z NUM = 10;
    A = 5 + 7 * 2;
    IMPRIMIR Z;
    SI X > 5 && Y == 'A' ENTONCES
        Z = 20;
    SINO
        Z = 30;
    FINSI;
    FUNCION CALCULAR(ARG1 NUM, ARG2 CAR)
        VAR1 NUM;
        VAR1 = 1 + ARG1;
        IMPRIMIR VAR1;
    FINFUNCION
    CALCULAR(10, 'B');
    MIENTRAS Z > 0 HACER
        IMPRIMIR Z;
        Z = Z - 1;
    FINMIENTRAS;
    FIN
    '''

    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)