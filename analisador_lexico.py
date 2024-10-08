import ply.lex as lex
#reserved words
reserved_words={
    'while':'while',
    'if': 'if',
    'else': 'else',
    'for': 'for',
    'do': 'do',
    'break': 'break',
    'int':'int',
    'float':'float',
    'bool':'bool',
    'null':'null',
}

#Tokens are created and reserved words that have already been 
#created are taken into account
tokens = [
    'parenthesis', 'number', 'id','less', 
    'more', 'division', 'multiplication', 'brackets', 
    'operators', 'module', 'equals', 'double_literal',
    'simple_literal','keyword','special','keys',
]

# Add reserved words as additional tokens
tokens += list(reserved_words.values())

# Tokens
t_keys= r'[\{\}]'
t_parenthesis = r'[\(\)]'
t_multiplication =r'\*'
t_brackets = r'[\[\]]'
t_operators = r'==|!=|<=|>=|<|>'
t_module = r'%'
t_equals = r'='
t_less = r'-'
t_more = r'\+'
t_division = r'/'
t_special = r'[@#$%^&_¿?]'

#Ignores white spaces and also line breaks
t_ignore = " \t"

# Functions

#to know if they are numbers
def t_number(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Number value too large %s" % t.value)
        t.value = 0
    return t

#to know if they are double literals
def t_double_literal(t):
    r'"([^"\\]|\\.)*"'
    return t  

#to know if they are simple literals
def t_simple_literal(t):
    r"'([^'\\]|\\.)*'"
    return t

#Check reserved words
# Check reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved_words:
        t.type = 'keyword'
    else:
        t.type = 'id'
    return t

#finds one or more newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#characters that are not recognized as valid or that do 
#not match any of the regular expressions defined for tokens
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Building the lexical analyzer
lexer = lex.lex()

#giving an example for the lexical analyzer
ejemplo_entrada=""" 
int main(){
    julian09= ! "julian"
    for(i=0;i>10;i++){
    print("hola")
    }
}
"""

ejemplo_entrada2="Este es un ejemplo de segunda entrada 2"

ejemplo_entrada3="10+84=94"


print("\nFirst test entry\n")
#pass the input string to the lexer
lexer.input(ejemplo_entrada)
#Iterate over the tokens generated by the lexer
while True:
    token = lexer.token()
    if not token:
        break # When no more tokens are found, it exits
    print(token) 

print("\nSecond test entry\n")
lexer.input(ejemplo_entrada2)
#Iterate over the tokens generated by the lexer
while True:
    token = lexer.token()
    if not token:
        break # When no more tokens are found, it exits
    print(token) 

print("\nThird test entry\n")
lexer.input(ejemplo_entrada3)
#Iterate over the tokens generated by the lexer
while True:
    token = lexer.token()
    if not token:
        break # When no more tokens are found, it exits
    print(token) 
