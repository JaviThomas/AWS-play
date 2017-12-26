import boto3

client = boto3.client('iam')

response = client.attach_group_policy(
    GroupName='pharmacy1',
    PolicyArn='arn:aws:iam::308565516874:policy/patientAdditionPolicy'
)