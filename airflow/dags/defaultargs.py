from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 5),
    'email': ['tiagolinhares051@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay':timedelta(seconds=10),
}

dag = DAG('defaultargs', description='Testando argumentos padrão',
        default_args = default_args,
        schedule_interval ='@hourly',
        catchup = False,
        default_view = 'graph',
        tags = ['teste', 'defaultargs'] 
    )

task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag)
task2 = BashOperator(task_id='tsk2', bash_command='sleep 5', dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', dag=dag)

task1 >> [task2, task3]