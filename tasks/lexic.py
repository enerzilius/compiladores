from ply import lex

tokens = (
    "ID",
    "NUM_INTEIRO",
    "NUM_FLUTUANTE",
    "MAIS",
    "MENOS",
    "VEZES",
    "DIVISAO",
    "E",
    "OU",
    "IGUAL",
    "DIFERENTE",
    "MENOR_IGUAL",
    "MAIOR_IGUAL",
    "MENOR",
    "MAIOR",
    "NAO",
    "ABRE_PARENTESES",
    "FECHA_PARENTESES",
    "ABRE_COLCHETES",
    "FECHA_COLCHETES",
    "VIRGULA",
    "DOIS_PONTOS",
    "ATRIBUICAO",
    "COMENTARIO",
)

reserved_words = {
    "se": "SE",
    "então": "ENTAO",
    "senão": "SENAO",
    "fim": "FIM",
    "repita": "REPITA",
    "flutuante": "FLUTUANTE",
    "retorna": "RETORNA",
    "até": "ATE",
    "leia": "LEIA",
    "escreva": "ESCREVA",
    "inteiro": "INTEIRO",
}

tokens = tokens + tuple(reserved_words.values())

letra = r"([a-zA-ZáÁãÃàÀéÉíÍóÓõÕ])"
digito = r"([0-9])"
sinal = r"([\-\+]?)"

id = r"(" + letra + r"(" + digito + r"+|_|" + letra + r")*)"

inteiro = r"(" + sinal + digito + r"+)"
flutuante = r"(" + sinal + digito + r"+" + r"\." + digito + r"+)"

t_MAIS = r"\+"
t_MENOS = r"-"
t_VEZES = r"\*"
t_DIVISAO = r"/"
t_ABRE_PARENTESES = r"\("
t_FECHA_PARENTESES = r"\)"
t_ABRE_COLCHETES = r"\["
t_FECHA_COLCHETES = r"\]"
t_VIRGULA = r","
t_ATRIBUICAO = r":="
t_DOIS_PONTOS = r":"
t_E = r"&&"
t_OU = r"\|\|"
t_NAO = r"!"
t_DIFERENTE = r"<>"
t_MENOR_IGUAL = r"<="
t_MAIOR_IGUAL = r">="
t_MENOR = r"<"
t_MAIOR = r">"
t_IGUAL = r"="

t_ignore = " \t"


def t_ID(token):
    token.type = reserved_words.get(token.value, "ID")
    return token


t_ID.__doc__ = id


def t_NUM_PONTO_FLUTUANTE(token):
    return token


t_NUM_PONTO_FLUTUANTE.__doc__ = flutuante


def t_NUM_INTEIRO(token):
    return token


t_NUM_INTEIRO.__doc__ = inteiro


def t_COMENTARIO(token):
    r"(\{((.|\n)*?)\})"
    token.lexer.lineno += token.value.count("\n")
    return token


def t_newline(token):
    r"\n+"
    token.lexer.lineno += len(token.value)


lexer = lex.lex()

data = """somaVetores(inteiro: n)
  inteiro: i
  i := 0 { inicialização }
  repita
    C[i] := A[i] + B[i]
    i := i + 1
  até i = n
fim
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
