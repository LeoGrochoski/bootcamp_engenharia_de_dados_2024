# Um Bilhão de Linhas: Desafio de Processamento de Dados com Python

Na [jornada de Dados](https://jornadadedados.alpaclass.com/) nos foi apresentado o desafio de 1 bilhão de linhas que consiste em desenvolver um programa Python capaz de ler esse arquivo e calcular a temperatura mínima, média (arredondada para uma casa decimal) e máxima para cada estação, exibindo os resultados em uma tabela ordenada por nome da estação.

- 1º desafio era clonar o repositorio do desafio.

- 2º é importar as dependencias e conseguir fetuar boas praticas de desenvolvimento como ambiente virtual, definição de versão da linguagen e suas bibliotecas. 

- 3º desafio se trata de rodar o codigo para geração do arquivo de 1 bilhão de linhas afinal o exemplo contem aproxidamedamente 44 mil, e o script ira multiplicar essa quantidade de forma repetida até gerar o arquivo de 1 bilhão de linhas. 

- 4º desafio consiste em rodar todos os testes (python, pandas, das, polars e duckdb).

## Detalhes do computador que rodaram os testes 

**Processador**: 13th Gen Intel(R) Core(TM) i7-1365U   1.80 GHz

**RAM**: 32.0 GB (31.7 GB usable)

**OS**: Windows

**System Type**: 64-bit operating system, x64-based processor

## Tamanho do arquivo

O arquivo gerado measurementes.txt contendo 1 bilhão de linhas tem o tamanho de mais **16gb**

## Resultados dos testes


Ao rodar os testes a expectativa era clara que o python puro teria o pior desempenho entre os processadores utilizados. Porem o resultado mostra um resultado 6 vezes mais demorado que a segunda opção. E tendo Polars e DuckDB disparadament como opções mais velozes e sendo os unicos abaixo de 1 minuto.

------------------------------------------
|Language |Time (seconds)|Time (minutes) |
----------|--------------|----------------
|Python   |	3004.38      | 50:04         |
|Pandas   |	530.05       | 08:50         |
|Dask     |	263.01       | 04:22         |
|Polars   |	37.96        | 00:37:96      |
|DuckDB   |	28.54        | 00:28:54      |
------------------------------------------

## Melhoria Proposta no Projeto

Buscando realizar um teste para verificar o que é mais importante o metodo de processamento ou o arquivo processado, desenvolvi um gerador de arquivo parquet (create_measurements_parquet.py). 

Inicialmente ja temos claramente uma redução de tamanho significativo caido de mais de **16gb** para aproximadamente **10gb**

E para realizar o teste resolvi alterar pequenas partes do codigo de do python puro para utilizar pandas na leitura do arquivo parquet (processar dataframe) e multiprocessing com pyarrow (para paralelização dos chunks). 

Assim imaginei poder processar o arquivo em parquet de forma mais rapida que anteriormente (pandas_parquet). 

E o resultado realmente foi melhor do que o anterior, sendo processado em 314.06 segundos, que seria algo em torno de 05:23, Ou seja uma redução de mais de 3 minutos e 27 segundos que representa uma diminuição de mais de 39%.

**OBS**: Tanto o codigo para gerar o arquivo parquet quanto o código para processar o arquivo estão no commit.

