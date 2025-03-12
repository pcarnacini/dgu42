# Projeto de Análise da Violência contra Mulheres no Brasil

## Contexto e Objetivo

A violência contra mulheres é um problema social urgente, que demanda ações baseadas em dados para conscientização e formulação de políticas públicas eficazes. Este projeto tem como objetivo analisar padrões de violência contra mulheres no Brasil, utilizando dados de registros criminais para extrair insights e evidenciar tendências.

## Perguntas-Chave

Qual é a média de vítimas por evento criminoso?

Qual a proporção de vítimas femininas em relação ao total de crimes?

Como a incidência de feminicídio, estupro e homicídio doloso evoluiu ao longo do tempo?

Existem padrões sazonais ou regiões com maior incidência desses crimes?

## Escopo do Projeto

Este projeto abrange todo o pipeline de dados, incluindo:

### Extração:
Coleta de arquivos XLSX contendo registros criminais de fontes públicas.

### Transformação e Limpeza:
Processamento dos dados com Python e Pandas para remoção de inconsistências, tratamento de valores nulos e adição de colunas temporais.

### Armazenamento:
Organização dos dados tratados em estrutura preparada para análise.

### Visualização:
Desenvolvimento de um dashboard interativo no Power BI para apresentação dos insights.

### Controle de Versão:
Gerenciamento do projeto com Git e GitHub.

## Fonte de Dados

Os dados utilizados são registros da Base de Dados e Notas Metodológicas dos Gestores Estaduais - Sinesp VDE 2015 a 2025, permitindo uma análise detalhada dos crimes.

## Tecnologias Utilizadas

### Python:
Para ETL (extração, transformação e carregamento de dados) com Pandas.

### Power BI:
Para visualização interativa dos dados.

### Git/GitHub:
Para controle de versão e compartilhamento do projeto.

## Processamento dos Dados

### Leitura e Padronização:

Carregamento dos arquivos XLSX.

Conversão de formatos de datas e padronização de colunas.

### Filtragem de Eventos Relevantes:

Seleção de registros com vítimas femininas.

Foco em crimes como feminicídio, estupro e homicídio doloso.

## Visualização dos Dados

O dashboard desenvolvido no Power BI apresenta:

### KPIs principais:
Total de vítimas, percentual de mulheres afetadas e média de vítimas por evento.

### Análises temporais:
Evolução dos crimes ao longo do tempo.

### Comparativos regionais:
Mapa interativo para identificar regiões com maior incidência.

### Filtros interativos:
Permitem explorar os dados por tipo de crime e período.

Acesse o dashboard interativo: [Dashboard interativo no Power BI](https://app.powerbi.com/view?r=eyJrIjoiNTlmMWY1MTYtNjFiYS00Y2UzLWIxNzUtZTMyNzExYmRiNjBjIiwidCI6IjIzZGQzNGE4LWRjMGUtNDU0YS05OTE3LTlhNjQ1OWY0OGJhOCJ9)

## Considerações Finais

Este projeto demonstra como dados podem ser utilizados para gerar insights valiosos e apoiar iniciativas de combate à violência contra mulheres. A metodologia utilizada pode ser expandida para incluir novas fontes de dados e análises mais detalhadas.
