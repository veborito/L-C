import ply.lex as lex
import ply.yacc as yacc
import sys 

tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'VAR', 'ASSIGN', 'PRINT')

t_PLUS    = r'\*{11}\s+'
t_MINUS   = r'\*{12}\s+'
t_TIMES   = r'\*{13}\s+'
t_DIVIDE  = r'\*{14}\s+'
t_MODULO = r'\*{15}\s+'
t_VAR = r'\*{18,}\s+'
t_ASSIGN = r'\*{16}\s+'
t_PRINT = r'\*{17}\s+'

t_ignore = ' '

def t_NUMBER(t):
    r'(\*{1,10}\s)+'
    number = t.value.split(' ')
    number.remove('')
    power = len(number) - 1
    t.value = 0
    for digit in number:
        val = len(digit)
        if (val == 10):
            t.value += 0
        else:
            t.value += val * 10**power
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

def num_to_stars(num):
    stars = ""
    while (num != 0):
        if num % 10 == 0:
            stars += (num % 10) * '*'
        else:
            stars += (num % 10) * '*' + ' '
        num //= 10
    return stars
            
    

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
        print(num_to_stars(result))
elif argc == 2:
        f = open(sys.argv[1])
        file = f.read().splitlines()
        for line in file:
            s = line
            result = parser.parse(s + ' ')