import ply.lex as lex
import ply.yacc as yacc
import sys 

tokens = ('LOOP', 'VAR', 'COMMA', 'RANGE', 'INTEGER', 'FLOAT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'ASSIGN', 'PRINT', 'SQRT', 'STRING', 'LPAREN', 'RPAREN', 'EQUAL')

t_ignore = ' '

t_LOOP = r'LOOP'
t_RANGE = r'RNG'
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_STRING  = r'\"\w*\"'
t_EQUAL = r'\='
t_MODULO = r'\%'
t_PRINT = r'PNT'
t_VAR = r'([a-z_]+(\d+|([a-z_]|)+)*)'
t_SQRT = r'SQRT'
t_COMMA = r'\,'

def t_FLOAT(t):
    r'\d+\.\d+|\-\d+\.\d+'
    t.value = float(t.value) 
    return t


def t_INTEGER(t):
    r'\d+|\-\d+'
    t.value = int(t.value) 
    return t
    
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    

lexer = lex.lex()

# while True:
#     data = input('> ')
#     lexer.input(data)
#     while True:
#         tok = lexer.token()
#         if not tok: 
#             break      # No more input
#         print(tok)


#----------------- PARSER -----------------------------

var = {}

def p_statement_var(p):
    '''statement : VAR EQUAL expression'''
    var[p[1]] = p[3]
    p[0] = p[3]

#print an expression
def p_statement_print(p):
    '''statement : PRINT expression'''
    print(p[2])

# print range from n to m
def p_statement_range(p):
    '''statement : RANGE INTEGER COMMA INTEGER'''
    rng = ""
    for i in range(p[2], p[4] + 1):
        rng += str(i)
        if (i <= p[4]):
            rng += ' '
    print(rng)

def p_statement_sqrt(p):
    '''statement : SQRT expression'''
    p[0] = p[2]**0.5

def p_statement_expr(p):
    '''statement : expression'''
    p[0] = p[1]

def p_expression_plus(p):
    '''expression : expression PLUS term '''
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    '''expression : expression MINUS term'''
    p[0] = p[1] + p[3]
    
def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term_times(p):
    '''term : term TIMES factor'''
    p[0] = p[1] * p[3]

def p_term_divide(p):
    '''term : term DIVIDE factor'''
    p[0] = p[1] / p[3]

def p_term_modulo(p):
    '''term : term MODULO factor'''
    p[0] = p[1] % p[3]

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]


def p_factor_integer(p):
    '''factor : INTEGER'''
    p[0] = p[1]

def p_factor_float(p):
    '''factor : FLOAT'''
    p[0] = p[1]

def p_factor_expression(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_factor_var(p):
    '''factor : VAR'''
    p[0] = var[p[1]]
    
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print(p)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

argc = len(sys.argv)
if argc == 1:
    while True:
        try:
            s = input('lazy > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)
elif argc == 2:
        f = open(sys.argv[1])
        file = f.read().splitlines()
        for line in file:
            s = line
            result = parser.parse(s)