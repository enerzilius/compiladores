# Sistema de Varredura
**Sistema da verredura = Analisador Léxico = Scanner = Lexer**

Análise Léxica é a fase do compilador que lê o código fonte como um arquivo texto e separa em tokens
Ex:
```c++
int main() {
  a = b+c;
  return 0;
}
```
*Lexema*  --> *Token*
"int"   --> *INT*
"main"  --> *ID*
"("     --> *ABRE_PAR*
")"     --> *FECHA_PAR*
"{"     --> *ABRE_CHAVE*
**[...]**

A análise léxica pode ser feita usando autômatos, só que mesmo em uma linguagem simplificada como o C-, ainda são necessários muitos estados. Logo, pode ser usado geradores léxicos para realizar essa tarefa. 
No entanto, em compiladores como o gcc, a falta de controle/claridade nesse processo os levou a criar os automatos manualmente.

Cada marca representa uma unidade: 
- if, while, then,... : palavras reservadas
- identificadores
- +, *, /, ==, ... : símbolos especiais

Expressões regulares serão usadas para identificar

```
Para o código abaixo, conte quantos tokens de cada tipo ele tem:

x = 0;\nwhile (x < 10) {\n\tx++;\n}
Tipos: id (3), espaço (10), num (2), while (1), outros (9)
```


