# Airflow

## TL;DR

### Add Airflow Helm repo
```
helm repo add apache-airflow https://airflow.apache.org
helm repo update
```
### Install
```
helm install airflow apache-airflow/airflow -n airflow -f values.yaml --create-namespace
```
### Upgrade

```
helm upgrade --install airflow apache-airflow/airflow -n airflow -f values.yaml
```
