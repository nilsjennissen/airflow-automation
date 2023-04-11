from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 9),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'my_first_dag',
    default_args=default_args,
    description='My first DAG in Airflow',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    def print_hello():
        return 'Hello world!'

    def print_first():
        return 'First'

    def print_second():
        return 'Second'

    def print_third():
        return 'Third'

    task1 = PythonOperator(
        task_id='task_1',
        python_callable=print_hello,
    )

    task2 = PythonOperator(
        task_id='task_2',
        python_callable=print_first,
    )

    task3 = PythonOperator(
        task_id='task_3',
        python_callable=print_second,
    )

    task1 >> [task2, task3]

