# CPTM Simulador de Carros

# Resumo
  Na nossa aplicação os carros de manutenção não transitam entre linhas. 
  Fizemos dessa forma porque haviam diversas duvidas sobre essa funcionalidade que não puderam ser esclarecidas a tempo.

  Desenvolvemos um simulador de operação de linha que imprime na tela um roteiro com informações sobre o que acontece nas linhas à cada 5 minutos.

  Consideramos que um trem em movimento leva 5 minutos para avançar de uma estação para a próxima.

# Roteiro de funcionamento
  [04h40]
    Carros de passageiro saem do patio com intervalos de 10 minutos. Percorrem a linha em circulos até a meia noite.
  [00h00]
    Os carros de passageiro começam a ser recolhidos
    Inicia-se o período de manutenção:
      Calculamos o tempo necessário para que um carro de manutenção dê uma volta completa na linha.
        Só é dada a autorização para a saída se o carro puder dar a volta completa e retornar antes das 04h40
  [04h40]
    A regra de saída para carros de manutenção garante que às 04h40 não haverá nenhum trem na linha. 
    A operação do dia seguinte pode começar.

# Como rodar

Compile o projeto
```bash
javac Main.java
```

Rode o projeto
```bash
java Main
```

### Versão de programas utilizadas e testadas
- java 11.0.10