# MLFlow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update configuration manager in src config
6. Update the components
7. Update pipeline
8. Update main.py
9. Update app.py




import dagshub
dagshub.init(repo_owner='zeynepzeytun.2002', repo_name='MLFlow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


  #382e013affcb271e0a5d02a011f6562549f786a0



  ac89574523f379583a7e25f934daca9ce4763e0e

  $env:MLFLOW_TRACKING_USERNAME = "zeynepzeytun.2002" 
$env:MLFLOW_TRACKING_PASSWORD = "ac89574523f379583a7e25f934daca9ce4763e0e"
