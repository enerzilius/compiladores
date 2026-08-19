# Como funciona
Um compilador vai transformar um código fonte em um programa executável em uma linguagem destino
- O código destino pode ser um código intermediário, código de montagem (assembly), código de máquina ou uma máquina virtual

- `Frontend`: clang, clang++, gcc+, gfortran
- `Middleend`: LLVM-IR
- `BACKEND`: X86-64, NVMPTX, ARM, RISC-V, CPP -> Mais otimizadas para o processador

Compialdores também vão ter como função a melhoria de código.

Outros sistemas podem ser classificados como *compiladores*:
- **Markdown** com *pandoc*
- **Latex**

## Grandes Fases de Compilação
- Análise Léxica
- Análise Sintática
- Análise Semântica
- Otimização de código fonte
- Geração de código intermediário
- Otimização do código alvo
