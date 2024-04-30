# How to Triggering Dataform (GCP's version of dbt) via Cloud Function

## Overview
Cloud Function code to trigger Dataform via API call.  This code uses the <i>google.cloud.dataform_v1beta1</i> library to trigger a Google Bigquery Dataform workflow as defined by the variables set in config.py. 

## Setup Dataform variables
Set up the variables in a file config.py
```python
project_id = "my-gcp-project"
region = "europe-west2"
repository_id = "my-dataform-repository-id"
git_commitish = "main"
tags = ['daily']
```
For [custom compliation](https://cloud.google.com/dataform/docs/configure-dataform#create-compilation-variables) variables in your Dataform project, you can include by uncommenting this block and replacing <b>var_key</b> & <b>var_value</b> with your custom variables.

```python
    compilation_result["code_compilation_config"] = {
        "vars": {"var_key": "var_value"}
        }
```

## Credits & Acknowledgements
I found this [repository](https://github.com/ArtemKorneevGA/dataform-cloud-functions/blob/main/ga4-table-updated-dataform-run-func/main.py) by Artem Korneev very useful. He went through the trouble of decoding what and how Dataform liked to be served the compilation result and the invocation request.