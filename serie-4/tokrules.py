# List of token names.   This is always required
tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
'LETTER',
'HASHTAG',
'UNDERSCORE',
'LBRACE',
'RBRACE',
'LBRACKET',
'RBRACKET',
'DOLLAR',
'AT',
'EXCLAM',
'EQUAL', 
'AND', 
'COMMA',
'COLON',  
'QUESTION',  
'PERCENT',  
'SEMICOLON', 
'PERIOD', 
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LETTER  = r'[a-zA-Z]'
t_HASHTAG  = r'\#'
t_UNDERSCORE  = r'\_'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOLLAR = r'\$'
t_AT = r'\@'
t_EXCLAM = r'\!'
t_EQUAL = r'\='
t_AND = r'\&'
t_COMMA = r'\,'
t_COLON = r'\:'
t_QUESTION = r'\?'
t_PERCENT = r'\%'
t_SEMICOLON = r'\;'
t_PERIOD = r'\.'

# A regular expression rule with some action code
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)    
	return t

# Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)