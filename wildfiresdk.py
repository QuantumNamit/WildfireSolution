import boto3
import json


# Create a Bedrock client
bedrock_client = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the prompt and parameters for the model invocation
prompt = "if the temperature is 35 degress and wind is 10 km/hr what is percentage of wildfire happening? just answer in 1 word high , medium , low"

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
