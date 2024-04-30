import functions_framework
from google.cloud import dataform_v1beta1
from config import (
  project_id,
  region,
  repository_id,
  git_commitish,
  tags
  )


@functions_framework.http
def hello_dataform(request):

    compilation_result = {
        "git_commitish": git_commitish,
    }

# Update var_key and var_value accordingly if used in Dataform project
    # compilation_result["code_compilation_config"] = {
    #     "vars": {"var_key": "var_value"}
    #     }

    parent = f"projects/{project_id}/locations/{region}/repositories/{repository_id}"
    try:
        client = dataform_v1beta1.DataformClient()
        result = client.create_compilation_result(
            request={
                "parent": parent,
                "compilation_result": compilation_result,
            }
        )

        workflow_invocation = {"compilation_result": result.name}
        workflow_invocation["invocation_config"] = {"included_tags": tags}

        workflow_invocation_request = {
            "parent": parent,
            "workflow_invocation": workflow_invocation
            }

        client.create_workflow_invocation(
            request=workflow_invocation_request,
        )
        return {"operation": "success"}

    except Exception as e:
        print(str(e))
