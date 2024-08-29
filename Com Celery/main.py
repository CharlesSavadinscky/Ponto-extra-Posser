from celery import Celery
from celery import Celery

# Importando a tarefa do arquivo celery.py
from celery import Celery
from celery.py import run_threaded_code

if __name__ == "__main__":
    result = run_threaded_code.delay()

    print("Esperando que as threads sejam finalizadas...")
    result_output = result.get(timeout=10)
    print(result_output)
