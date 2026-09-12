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
)

letra = r"([a-zA-ZáÁãÃàÀéÉíÍóÓõÕ])"
digito = r"([0-9])"
sinal = r"([\-\+]?)"

id = r"(" + letra + r"(" + digito + r"+|_|" + letra + r")*)"

inteiro = r"(" + sinal + digito + r"+)"
flutuante = r"(" + sinal + digito + r"+" + r"\." + digito + r"+)"

t_MAIS = r"\+"
t_MENOS = r"-"
t_VEZES = r"\*"
t_DIVIDE = r"/"
t_ABRE_PARENTESE = r"\("
t_FECHA_PARENTESE = r"\)"
t_ABRE_COLCHETE = r"\["
t_FECHA_COLCHETE = r"\]"
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
