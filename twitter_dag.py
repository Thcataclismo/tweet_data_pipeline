from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import executar_etl_twitter

argumentos_padrao = {
    'proprietário': 'airflow',
    'depende_do_passado': False,
    'data_de_início': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'enviar_email_em_falha': False,
    'enviar_email_na_retrieda': False,
    'retries': 1,
    'intervalo_de_retrieda': timedelta(minutes=1)
}

dag = DAG(
    'dag_twitter',
    default_args=argumentos_padrao,
    description='Nosso primeiro DAG com processo ETL!',
    schedule_interval=timedelta(days=1),
)

executar_etl = PythonOperator(
    task_id='executar_twitter_etl',
    python_callable=executar_etl_twitter,
    dag=dag, 
)
