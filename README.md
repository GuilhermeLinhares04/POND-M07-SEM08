# Previsão de Preços Bitcoin/Bitcoin Price Prediction

## Sumário/Summary
- [Introdução/Introduction](#introduçãointroduction)
- [Como utilizar/How to use](#como-utilizarhow-to-use)
- [Escolha do modelo/Model choice](#escolha-do-modelomodel-choice)
- [Descrição do backend/Backend description](#descrição-do-backendbackend-description)
- [Retreino do modelo/Model retraining](#retreino-do-modelomodel-retraining)
- [Implementação do Docker/Docker implementation](#implementação-do-dockerdocker-implementation)
- [Utilização de data lakes/Data lakes usage](#utilização-de-data-lakesdata-lakes-usage)

## Introdução/Introduction
Este projeto consiste em um modelo de Machine Learning que prevê preços para compra e venda de ações da Bitcoin. Ele foi treinado com dados históricos da moeda de setembro de 2023 até setembro de 2024 e utiliza o modelo ARIMA para realizar as previsões.

----------------------------------------------------------------------------------------------------------------------------

This project consists of a Machine Learning model that predicts prices for buying and selling Bitcoin stocks. It was trained with historical data of the currency from September 2023 to September 2024 and uses the ARIMA model to make predictions.

## Como utilizar/How to use
Para utilizar o projeto, siga os seguintes passos:
1. Clone o repositório
2. Abra um terminal na pasta do projeto e instale as dependências do backend com o comando ``pip install -r requirements.txt``
3. Execute os seguintes comandos para rodar o projeto por completo:
    - Execução do backend:
        - Envie o comando ``uvicorn main:app --reload`` no terminal
    - Execução do frontend:
        - Envie o comando ``streamlit run dashboard.py`` em um terminal distinto
4. Acesse o endereço ``http://localhost:8501`` no seu navegador para visualizar o dashboard e realizar as previsões

----------------------------------------------------------------------------------------------------------------------------

To use the project, follow these steps:
1. Clone the repository
2. Open a terminal in the project folder and install the backend dependencies with the command ``pip install -r requirements.txt``
3. Run the following commands to run the project in full:
    - Backend execution:
        - Send the command ``uvicorn main:app --reload`` in the terminal
    - Frontend execution:
        - Send the command ``streamlit run dashboard.py`` in a different terminal
4. Access the address ``http://localhost:8501`` in your browser to view the dashboard and make predictions

## Escolha do modelo/Model choice
O modelo ARIMA é um modelo estatístico que utiliza a autocorrelação dos dados para prever valores futuros. Para este projeto, ele foi escolhido por ser um modelo simples, porém eficaz para séries temporais. Além disso, ele pode ser considerado versátil e flexível pela facilidade de ajustar os parâmetros do modelo. Por fim, suas previsões são baseadas em valores passados, o que é ideal para prever o possíveis valores de compras e vendas de ativos como é o caso deste projeto.

----------------------------------------------------------------------------------------------------------------------------

The ARIMA model is a statistical model that uses the autocorrelation of the data to predict future values. For this project, it was chosen because it is a simple but effective model for time series. In addition, it can be considered versatile and flexible because of the ease of adjusting the model parameters. Finally, its predictions are based on past values, which is ideal for predicting the possible values of buying and selling assets as is the case with this project.

## Descrição do backend/Backend description
O backend deste projeto foi feito realizado utilizando a biblioteca fastAPI. Seguindo o propósito do projeto, ele envia o modelo treinado previamente junto com os dados atualizados para uma rota _post_ denominada "predict". Esta rota recebe um JSON com os dados de datas de início e final da previsão, retornando um arquivo _.log_ com as previsões de compra e venda da Bitcoin.

----------------------------------------------------------------------------------------------------------------------------

The backend of this project was done using the fastAPI library. Following the purpose of the project, it sends the previously trained model along with the updated data to a _post_ route called "predict". This route receives a JSON with the start and end date data of the prediction, returning a _.log_ file with the predictions of buying and selling Bitcoin.

## Retreino do modelo/Model retraining
O retreino do modelo pode ser realizado para buscar previsões mais precisas. Para isso, basta seguir os seguintes passos:
1. Atualize o arquivo ``data/Bitcoin_1Y_Normalizado.csv`` com os novos dados
2. Caso necessário, verifique e ajuste parâmetros do modelo no arquivo ``exploration.ipynb``
3. Execute o arquivo ``exploration.ipynb`` para treinar o modelo com os novos dados

O modelo será treinado com os novos dados e será salvo como um novo arquivo ``arima_model.pkl``, estará pronto para ser utilizado no dashboard.

----------------------------------------------------------------------------------------------------------------------------

Model retraining can be performed to seek more accurate predictions. To do this, simply follow these steps:
1. Update the file ``data/Bitcoin_1Y_Normalizado.csv`` with the new data
2. If necessary, check and adjust model parameters in the file ``exploration.ipynb``
3. Run the file ``exploration.ipynb`` to train the model with the new data

The model will be trained with the new data and will be saved as a new file ``arima_model.pkl``, ready to be used in the dashboard.

## Implementação do Docker/Docker implementation
A dockerização deste projeto foi realizada para facilitar a a utilização do projeto em qualquer ambiente. Neste caso, tanto o backend quando o frontend foram dockerizados em _Docker Compose_, para que sua execução conjunta possa ser realizada de forma instantânea e facilitada e também para que não haja interferência de dependências necessárias para sua execução. Além disso, o deploy do projeto pode ser feito de forma mais simples já que sua execução se torna independente do sistema operacional e consequentemente menos complexa.
Como utilizar o Docker Compose:
1. Construa a imagem do Docker Compose com o comando ``docker-compose up --build``
2. Execute o container com o comando ``docker-compose up`` (apenas se o container não estiver em execução)

----------------------------------------------------------------------------------------------------------------------------

The dockerization of this project was carried out to facilitate the use of the project in any environment. In this case, both the backend and the frontend were dockerized in _Docker Compose_, so that their joint execution can be done instantly and facilitated and also so that there is no interference of dependencies necessary for its execution. In addition, the project deployment can be done more simply since its execution becomes independent of the operating system and consequently less complex.
How to use Docker Compose:
1. Build the Docker Compose image with the command ``docker-compose up --build``
2. Run the container with the command ``docker-compose up`` (only if the container is not running)

## Utilização de data lakes/Data lakes usage
Para esta aplicação em específico, a utilização de data lakes não se faz necessária, pois o modelo é treinado com um único arquivo _.csv_ simples, que contém os dados históricos da Bitcoin. No entanto, sua utilização pode ser interessante para projetos que necessitam de uma grande quantidade de dados, pois eles permitem o armazenamento de grandes volumes de dados de diferentes formatos e estruturas, facilitando o acesso e a análise desses dados.

----------------------------------------------------------------------------------------------------------------------------

For this specific application, the use of data lakes is not necessary, as the model is trained with a single simple _.csv_ file, which contains the historical data of Bitcoin. However, its use may be interesting for projects that require a large amount of data, as they allow the storage of large volumes of data of different formats and structures, facilitating access and analysis of this data.