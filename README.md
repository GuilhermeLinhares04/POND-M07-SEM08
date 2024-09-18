# Previsão de Preços Bitcoin/Bitcoin Price Prediction

## Introdução/Introduction
Este projeto consiste em um modelo de Machine Learning que prevê preços para compra e venda de ações da Bitcoin. Ele foi treinado com dados históricos da moeda de setembro de 2023 até setembro de 2024 e utiliza o modelo ARIMA para realizar as previsões.

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

The ARIMA model is a statistical model that uses the autocorrelation of the data to predict future values. For this project, it was chosen because it is a simple but effective model for time series. In addition, it can be considered versatile and flexible because of the ease of adjusting the model parameters. Finally, its predictions are based on past values, which is ideal for predicting the possible values of buying and selling assets as is the case with this project.