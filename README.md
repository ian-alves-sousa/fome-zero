# 1. Problema de Negócio
Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados!

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises.

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

Para responder às seguintes perguntas:

## Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## País
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?


# 2. Premissas assumidas para a análise
1. Análise foi feita com dados do Dataset Zomato Restaurants - Autoupdated dataset com link para o Kaggle:
https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv
2. Marketplace foi o modelo de negócio assumido
3. As 4 principais visões de negócio foram: Visão Geral, Visão Países, Visão Cidades, Visão Tipos de Culinárias

# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 4 principais visões do modelo de negócio para a empresa:
1. Visão Geral
2. Visão Países
3. Visão Cidades
4. Visão Tipos de Culinárias
Cada visão é representada pelo seguinte conjunto de métricas:
## Visão Geral
a. Restaurantes cadastrados <br>
b. Países cadastrados <br>
c. Cidades cadastradas <br>
d. Total de avaliações feitas <br>
e. Total de tipos de culinária registrados <br>
f. Mapa com os restaurantes cadastrados <br>

## Visão Países
a. Quantidade de Restaurantes Registrados por país <br>
b. Quantidade de Cidades com Restaurantes cadastrados Registradas por País <br>
c. Média de da quantidade de Avaliações feitas por País <br>
d. Média do Preço de um prato para duas pessoas por País <br>

## Visão Cidades
a. Top 10 Cidades com mais Restaurantes na Base de Dados <br>
b. Top 7 Cidades com Restaurantes com média de avaliação acima de 4 <br>
c. Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5 <br>
d. Top 10 Cidades mais restaurantes com tipos culinários distintos <br>

## Visão Tipos de Culinárias
a. Melhores Restaurantes com tipos de Culinárias: Italiana, Americana, Árabe, Japonesa e Brasileira <br>
b. Top Restaurantes ordenados por média de nota <br>
c. Top melhores tipos de culinárias <br>
d. Top piores tipos de culinárias <br>

# 4. Top 3 Insights
1. A Índia destaca-se no estudo, obtendo a maior quantidade de restaurantes na base de dados, além disso, fica em segundo lugar na média do preço de um prato para duas pessoas, ou seja, além de ter a maioria dos restaurantes do estudo, em média os seus preços são altos.
2. No estudo, apenas as cidades de Brasília, São Paulo e Rio de Janeiro foram apresentadas, e as três fazem parte do Top 7 com as piores médias de avaliações, dessa forma, o Brasil é um dos países com pior média de avaliação e com uma quantidade de restaurantes expressiva.
3. As culinárias orientais tendem a ter avaliações altas, enquanto as culinárias, como apenas bebidas, ou até mesmo a culinária brasileira, apresentam uma média menor de avaliações.

# 5. O produto final do projeto
Dashboard online, hospedado em Cloud e disponível para acesso em qualquer dispositivo conectado a internet.

O painel pode ser acessado através do link:
https://ian-projeto-zero-home.streamlit.app

# 6. Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibem essa métricas da melhor forma possível para o CEO.

O objetivou foi completado, além disso, filtros foram adicionados no dashboard, afim de tirar insights com uma base de comparação mais ajustada, seleciando os países em que estão os restaurantes, ou até mesmo, na Visão Tipos de Culinárias, selecianando os tipos de culinárias.

# 7. Próximos passos
1. Deixar o Dashboard mais apresentavel no conceito visual, a ideia inicial é apresentar os dados e depois deixar o painel bonito.
2. Criar novos filtros.
3. Adicionar novas visões de negócios.
4. No mapa da Visão Geral, ajustar o mapa para que o mesmo agrupe os restaurantes por país e por cidade.
5. Adicionar um ícone no sidebar para o download dos dados tratados.
