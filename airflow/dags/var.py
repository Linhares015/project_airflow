from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.models import Variable

dag = DAG('Variaveis', description='Variaveis',
        schedule_interval=None,start_date=datetime(2023, 3, 5),
        catchup=False
    )

def print_variable(**context):
    minha_var_ = Variable.get('minha_var')
    print(f'O valor da Variavel é: {minha_var_}')

task1 = PythonOperator(task_id ='tsk2', python_callable = print_variable, dag = dag)


task1