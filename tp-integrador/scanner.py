# ldr_lex.py
import ply.lex as lex

# Palabras reservadas del lenguaje (se reconocen en mayúsculas)
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
    'VARIABLE',         # Identificadores: [A-Z]+[0-9]*
    'NUMERO',           # [0-9]+
    'CARACTER',         # 'A' , 'x' , '1' , ' ' , etc.
    'IGUAL',            # =
    'MAS',              # +
    'MENOS',            # -
    'POR',              # *
    'DIVIDIR',          # /
    'MENOR_QUE',        # <
    'MAYOR_QUE',        # >
    'IGUAL_QUE',        # ==
    'MENOR_IGUAL',      # <=
    'MAYOR_IGUAL',      # >=
    'DISTINTO_QUE',     # !=
    'PARENTESIS_IZQ',   # (
    'PARENTESIS_DER',   # )
    'CORCHETE_IZQ',     # [
    'CORCHETE_DER',     # ]
    'COMA',             # ,
    'PUNTO_Y_COMA',     # ;
    'AMPERSAND',        # &&
    'PIPE',             # ||
    'EXCLAMACION',      # !
] + list(reserved.values())

# Tokens de un solo (o pocos) caracteres
t_IGUAL         = r'='
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIVIDIR       = r'/'
t_MENOR_QUE     = r'<'
t_MAYOR_QUE     = r'>'
t_IGUAL_QUE     = r'=='
t_MENOR_IGUAL   = r'<='
t_MAYOR_IGUAL   = r'>='
t_DISTINTO_QUE  = r'!='
t_PARENTESIS_IZQ= r'\('
t_PARENTESIS_DER= r'\)'
t_CORCHETE_IZQ  = r'\['
t_CORCHETE_DER  = r'\]'
t_COMA          = r','
t_PUNTO_Y_COMA  = r';'
t_AMPERSAND     = r'&&'
t_PIPE          = r'\|\|'
t_EXCLAMACION   = r'!'

# Números
def t_NUMERO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# Caracteres: un carácter entre comillas simples (incluye espacios y varios signos)
def t_CARACTER(t):
    r"'[A-Za-z0-9!@#$%^&*()_+\-=\[\]{}|;:'\",.<>/?`~ ]'"
    t.value = t.value[1:-1]
    return t

# Identificadores del lenguaje: [A-Z]+[0-9]*  (p.ej., X, VAR, ABC12)
def t_VARIABLE(t):
    r'[A-Z]+[0-9]*'
    # Si coincide con palabra reservada, tipificamos como reservada
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter inválido: '{t.value[0]}' en línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

if __name__ == '__main__':
    data = '''
    INICIO
      X NUM;
      X = 1;
      IMPRIMIR X;
    FIN
    '''
    lexer.input(data)
    for tok in iter(lexer.token, None):
        print(tok)
