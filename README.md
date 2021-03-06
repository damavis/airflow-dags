<h1> Airflow DAGS example.</h1>
Simple ETL pipeline example. It only has didactic purposes.
You can find all information in this post:

<h2> Dependencies</h2>

- helm (tested with ``v3.4.1``)
- kubectl (tested with ``v1.18``)

<h2> Deployments </h2>

There are two types of deployments available:
- Airflow deployment with CeleryExecutor
- Airflow deployment with KubernetesExecutor

Both use Helm to deploy all the Airflow configuration.

``helm repo add airflow-stable https://airflow-helm.github.io/charts`` and ``helm repo update``

To install the Airflow Chart into your Kubernetes cluster:

``helm install airflow --namespace airflow airflow-stable/airflow --values [CELERY or KUBERNETES YAML]``

<h2> DAGs examples</h2>

`etl_dag_celery.py` : DAG example for CeleryExecutor.

`etl_dag_for_kubernetes.py` : DAG example for KubernetesExecutor. It uses `etl_kubernetes` module in `/scripts`.


Python packages must be added to `requirements.txt`.
