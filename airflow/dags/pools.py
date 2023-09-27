from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag = DAG('pool', description='teste de pool',
        schedule_interval=None,start_date=datetime(2023, 3, 5), 
        catchup=False
    )

task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag, pool='meupool')
task2 = BashOperator(task_id='tsk2', bash_command='sleep 5', dag=dag, pool='meupool')
task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', dag=dag, pool='meupool')
task4 = BashOperator(task_id='tsk4', bash_command='sleep 5', dag=dag, pool='meupool')
