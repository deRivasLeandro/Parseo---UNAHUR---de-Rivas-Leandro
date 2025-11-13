# ldr_yacc.py
import ply.yacc as yacc
from scanner import tokens

# ------------------------------------------------------------------
# Precedencias y asociatividades (para expresiones y condiciones)
# ------------------------------------------------------------------
precedence = (
    ('left', 'PIPE'),             # ||
    ('left', 'AMPERSAND'),        # &&
    ('right', 'EXCLAMACION'),     # !
    ('nonassoc', 'MENOR_QUE', 'MAYOR_QUE', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'IGUAL_QUE', 'DISTINTO_QUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIR'),
)

# ------------------------------------------------------------------
# Programa
# ------------------------------------------------------------------
def p_programa(p):
    'programa : INICIO bloque FIN'
    p[0] = ('programa', p[2])

# ------------------------------------------------------------------
# Bloque: definiciones de función + sentencias
# ------------------------------------------------------------------
def p_bloque(p):
    'bloque : definiciones_funcion sentencias'
    p[0] = ('bloque', p[1], p[2])

# ------------------------------------------------------------------
# Definiciones de función (cero o más)
# ------------------------------------------------------------------
def p_definiciones_funcion_list(p):
    'definiciones_funcion : definicion_funcion definiciones_funcion'
    p[0] = [p[1]] + p[2]

def p_definiciones_funcion_empty(p):
    'definiciones_funcion : '
    p[0] = []

# ------------------------------------------------------------------
# Definición de función (procedimiento sin return en esta versión)
# FUNCION NOMBRE(PARAMS) <sentencias> FINFUNCION
# Nota: usamos VARIABLE como nombre de función (unificado)
# ------------------------------------------------------------------
def p_definicion_funcion(p):
    'definicion_funcion : FUNCION VARIABLE PARENTESIS_IZQ parametros_opt PARENTESIS_DER sentencias FINFUNCION'
    p[0] = ('funcion', p[2], p[4], p[6])  # (nombre, params, cuerpo)

# parámetros opcionales: lista o vacío
def p_parametros_opt(p):
    'parametros_opt : parametros'
    p[0] = p[1]

def p_parametros_opt_empty(p):
    'parametros_opt : '
    p[0] = []

def p_parametros(p):
    'parametros : parametro'
    p[0] = [p[1]]

def p_parametros_more(p):
    'parametros : parametro COMA parametros'
    p[0] = [p[1]] + p[3]

def p_parametro(p):
    'parametro : VARIABLE tipo'
    p[0] = ('param', p[1], p[2])

def p_tipo(p):
    '''tipo : NUM
            | CAR
            | ARR'''
    p[0] = p[1]

# ------------------------------------------------------------------
# Sentencias (cero o más)
# ------------------------------------------------------------------
def p_sentencias_list(p):
    'sentencias : sentencia sentencias'
    p[0] = [p[1]] + p[2]

def p_sentencias_empty(p):
    'sentencias : '
    p[0] = []

# ------------------------------------------------------------------
# Tipos de sentencia
# ------------------------------------------------------------------
def p_sentencia(p):
    '''sentencia : declaracion PUNTO_Y_COMA
                 | asignacion PUNTO_Y_COMA
                 | impresion PUNTO_Y_COMA
                 | condicional PUNTO_Y_COMA
                 | iteracion PUNTO_Y_COMA
                 | llamado_funcion PUNTO_Y_COMA'''
    p[0] = p[1]

# ------------------------------------------------------------------
# Declaración (con o sin inicialización)
# ------------------------------------------------------------------
def p_declaracion_simple(p):
    'declaracion : VARIABLE tipo'
    p[0] = ('decl', p[1], p[2], None)

def p_declaracion_init(p):
    'declaracion : VARIABLE tipo IGUAL valor'
    p[0] = ('decl', p[1], p[2], p[4])

# ------------------------------------------------------------------
# Asignación
# ------------------------------------------------------------------
def p_asignacion(p):
    'asignacion : VARIABLE IGUAL valor'
    p[0] = ('asig', p[1], p[3])

# ------------------------------------------------------------------
# Impresión
# ------------------------------------------------------------------
def p_impresion(p):
    'impresion : IMPRIMIR valor_o_variable'
    p[0] = ('print', p[2])

def p_valor_o_variable(p):
    '''valor_o_variable : valor
                        | VARIABLE'''
    p[0] = p[1]

# ------------------------------------------------------------------
# Condicional
# ------------------------------------------------------------------
def p_condicional(p):
    'condicional : SI condicion ENTONCES sentencias SINO sentencias FINSI'
    p[0] = ('if', p[2], p[4], p[6])

# ------------------------------------------------------------------
# Iteración
# ------------------------------------------------------------------
def p_iteracion(p):
    'iteracion : MIENTRAS condicion HACER sentencias FINMIENTRAS'
    p[0] = ('while', p[2], p[4])

# ------------------------------------------------------------------
# Condición booleana (con &&, ||, !, paréntesis y comparaciones)
# ------------------------------------------------------------------
def p_condicion_binaria(p):
    '''condicion : condicion AMPERSAND condicion
                 | condicion PIPE condicion'''
    op = '&&' if p[2] == '&&' else '||'
    p[0] = ('bool_bin', op, p[1], p[3])

def p_condicion_not(p):
    'condicion : EXCLAMACION condicion'
    p[0] = ('not', p[2])

def p_condicion_parentizada(p):
    'condicion : PARENTESIS_IZQ condicion PARENTESIS_DER'
    p[0] = p[2]

def p_condicion_cmp(p):
    '''condicion : valor MENOR_QUE valor
                 | valor MAYOR_QUE valor
                 | valor IGUAL_QUE valor
                 | valor MENOR_IGUAL valor
                 | valor MAYOR_IGUAL valor
                 | valor DISTINTO_QUE valor'''
    p[0] = ('cmp', p[2], p[1], p[3])

# ------------------------------------------------------------------
# Valores y expresiones aritméticas
# ------------------------------------------------------------------
def p_valor_num(p):
    'valor : NUMERO'
    p[0] = ('num', p[1])

def p_valor_char(p):
    'valor : CARACTER'
    p[0] = ('char', p[1])

def p_valor_var(p):
    'valor : VARIABLE'
    p[0] = ('var', p[1])

def p_valor_array(p):
    'valor : array'
    p[0] = p[1]

def p_valor_op(p):
    'valor : valor operador valor'
    p[0] = ('op', p[2], p[1], p[3])

def p_operador(p):
    '''operador : MAS
                | MENOS
                | POR
                | DIVIDIR'''
    p[0] = p[1]

# ------------------------------------------------------------------
# Arrays literales
# ------------------------------------------------------------------
def p_array(p):
    'array : CORCHETE_IZQ array_content_opt CORCHETE_DER'
    p[0] = ('arr', p[2])

def p_array_content_opt(p):
    'array_content_opt : array_content'
    p[0] = p[1]

def p_array_content_opt_empty(p):
    'array_content_opt : '
    p[0] = []

def p_array_content_one(p):
    'array_content : item'
    p[0] = [p[1]]

def p_array_content_more(p):
    'array_content : item COMA array_content'
    p[0] = [p[1]] + p[3]

def p_item_num(p):
    'item : NUMERO'
    p[0] = ('num', p[1])

def p_item_char(p):
    'item : CARACTER'
    p[0] = ('char', p[1])

# ------------------------------------------------------------------
# Llamado a función
# ------------------------------------------------------------------
def p_llamado_funcion(p):
    'llamado_funcion : VARIABLE PARENTESIS_IZQ argumentos_opt PARENTESIS_DER'
    p[0] = ('call', p[1], p[3])

def p_argumentos_opt(p):
    'argumentos_opt : argumentos'
    p[0] = p[1]

def p_argumentos_opt_empty(p):
    'argumentos_opt : '
    p[0] = []

def p_argumentos_one(p):
    'argumentos : valor'
    p[0] = [p[1]]

def p_argumentos_more(p):
    'argumentos : valor COMA argumentos'
    p[0] = [p[1]] + p[3]

# ------------------------------------------------------------------
# Errores
# ------------------------------------------------------------------
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (línea {getattr(p, 'lineno', '?')})")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

# Construcción del parser
parser = yacc.yacc(start='programa')

if __name__ == '__main__':
    data = '''
    INICIO
      X = 1;
      IMPRIMIR X;
    FIN
    '''
    result = parser.parse(data)
    print("PROGRAMA 1 - Parsing exitoso:", result is not None)
    print(result)

    data2 = '''
    INICIO
      X NUM NUM;
      X = 1;
      IMPRIMIR X;
    FIN
    '''
    result2 = parser.parse(data2)
    print("PROGRAMA 2 - Parsing exitoso:", result2 is not None)
    print(result2)

    data3 = '''
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
    '''
    result3 = parser.parse(data3)
    print("PROGRAMA 3 - Parsing exitoso:", result3 is not None)
    print(result3)


