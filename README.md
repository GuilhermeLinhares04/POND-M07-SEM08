# Previsão de Preços Bitcoin

## Introdução
Este projeto consiste em um modelo de Machine Learning que prevê preços para compra e venda de ações da Bitcoin. Ele foi treinado com dados históricos da moeda de setembro de 2023 até setembro de 2024 e utiliza o modelo ARIMA para realizar as previsões.

## Como utilizar
Para utilizar o projeto, siga os seguintes passos:
1. Clone o repositório
2. Abra um terminal na pasta do projeto e instale as dependências do backend com o comando ``pip install -r requirements.txt``
3. Execute os seguintes comandos para rodar o projeto por completo:
    - Execução do backend:
        - Envie o comando ``uvicorn main:app --reload`` no terminal
    - Execução do frontend:
        - Envie o comando ``streamlit run dashboard.py`` em um terminal distinto
4. Acesse o endereço ``http://localhost:8501`` no seu navegador para visualizar o dashboard e realizar as previsões

## Ferraments utilizadas
- Python
    - FastAPI
    - Streamlit
    - ARIMA
    - Pandas
