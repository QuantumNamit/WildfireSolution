import boto3
import json


# Create a Bedrock client
bedrock_client = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the prompt and parameters for the model invocation
prompt = "what is the evacuation plan for the wildfire in jasper for the residents"

kwargs = {
    "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    })
}

# Invoke the model using the Bedrock client
response = bedrock_client.invoke_model(**kwargs)

# Parse the response body
body = json.loads(response['body'].read())

# Print the response
print(body)
