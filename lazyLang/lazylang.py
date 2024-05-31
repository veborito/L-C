import ply.lex as lex
import ply.yacc as yacc
import sys 

tokens = ('RANGE', 'INTEGER', 'FLOAT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'VAR', 'ASSIGN', 'PRINT', 'SQRT')

t_ignore = ' '

t_RANGE = r'rng'
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LETTER  = r'[a-zA-Z]'
t_WORD = r'\w'
t_EQUAL = r'\='
t_MODULO = r'\%'
t_PRINT = r'pnt'
t_VAR = r'\w+'

def t_INTEGER(t):
    r'\d+|\-\d+'
    t.value = int(t.value) 
    return t

def t_FLOAT(t):
    r'\d+.\d+|\-\d+.\d+'
    t.value = float(t.value) 
    return t

    
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    

lexer = lex.lex()

#----------------- PARSER -----------------------------

var = {}

def p_statement_var(p):
    '''statement : VAR ASSIGN expression'''
    var[p[1]] = p[3]
    p[0] = p[3]

def p_statement_print(p):
    '''statement : PRINT expression'''
    print(num_to_stars(p[2]))

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
    '''term : term TIMES NUMBER'''
    p[0] = p[1] * p[3]

def p_term_divide(p):
    '''term : term DIVIDE NUMBER'''
    p[0] = p[1] / p[3]

def p_term_modulo(p):
    '''term : term MODULO NUMBER'''
    p[0] = p[1] % p[3]

def p_term_number(p):
    '''term : NUMBER'''
    p[0] = p[1]

def p_term_var(p):
    '''term : VAR'''
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
            s = input('star > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s + ' ')
        print(result)
elif argc == 2:
        f = open(sys.argv[1])
        file = f.read().splitlines()
        for line in file:
            s = line
            result = parser.parse(s + ' ')