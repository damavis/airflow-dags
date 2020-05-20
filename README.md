<h1> Airflow DAGS example.</h1>
Simple ETL pipeline example. It only has didactic purposes.
You can find all information in this post:

<h2> Dependencies</h2>

- helm
- kubectl

<h2> Deployments </h2>

There are two types of deployments available:
- Airflow deployment with CeleryExecutor
- Airflow deployment with KubernetesExecutor

Both use Helm to deploy all the Airflow configuration.

``helm repo add stable https://kubernetes-charts.storage.googleapis.com/``

To install the Airflow Chart into your Kubernetes cluster:

``helm install --namespace "airflow" airflow stable/airflow --values [CELERY or KUBERNETES YAML]``

<h2> DAGs examples</h2>

`etl_extract_tranform`
- Gets csv information from winterolympicsmedals.
- Save raw_data.
- Make 2 transfomations. Saves this information into a staging folder.

`etl_load.py`
- reads csv files extracted.

Python packages must be added to `requirements.txt`.
