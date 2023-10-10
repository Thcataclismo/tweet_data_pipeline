### Twitter Data Pipeline
Este é um projeto de pipeline de dados para extrair e processar tweets do Twitter usando a biblioteca Tweepy e o Apache Airflow. O pipeline é projetado para coletar e armazenar tweets de um usuário específico, realizar transformações nos dados e armazenar os resultados em um arquivo CSV.

## Uso
Execute o Apache Airflow para programar a execução do DAG dag_twitter.py. O DAG extrairá tweets do usuário especificado no arquivo twitter_etl.py e os processará conforme necessário.

Os tweets refinados serão armazenados em um arquivo CSV chamado tweets_refinados.csv no diretório de trabalho.

## Dependências
Python 3.x
Tweepy
Apache Airflow
Pandas
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para criar problemas, enviar solicitações de pull e melhorar este projeto.

## Licença
Este projeto está licenciado sob a MIT License.

