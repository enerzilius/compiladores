# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
from ply import lex
from ply.lex import TOKEN

# List of token names.   This is always required
tokens = (
    "ID",
    "AND",
    "OR",
    "NOT",
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "EQUALS",
    "NEGATIVE"
)

# reconhecimento de identificadores

char = r"([a-zA-ZáÁãÃàÀéÉíÍóÓõÕ])"
digit = r"([0-9])"
id = r"(" + char + r"(" + digit + r"+|_|" + char + r")*)"

# Regular expression rules for simple tokens
t_AND = r"&&"
t_OR = r"\|\|"
t_NOT = r"!"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_EQUALS = r"="


@TOKEN(id)
def t_ID(t):
    t.type = "ID"
    return t


# A regular expression rule with some action code
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
