import boto3

client = boto3.client('iam')

response = client.create_group(
    GroupName='pharmacy1',
)

print(response)