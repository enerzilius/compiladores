inteiro linear(inteiro: dados[], inteiro: tamanho, inteiro: alvo)
  inteiro: i
  i := 0

  repita
    se dados[i] = alvo então
      retorna(i)
    fim
    i := i + 1
  até i >= tamanho
  retorna(-1)
fim
 
inteiro binario(inteiro: dados[], inteiro: tamanho, inteiro: alvo)
    inteiro: high
    high := tamanho-1

    inteiro: low
    low := 1

    repita
      inteiro: mid
      mid = (low+(high - low)/ 2);

      se dados[mid] = target então 
        returna(mid)
      fim

      se dados[mid] < alvo então 
        low = mid + 1;
      senão 
        high = mid - 1;
      fim
    até low <= high

    returna(-1)
}
