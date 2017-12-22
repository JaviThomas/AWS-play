import boto3
from pprint import pprint

#MrSteve was here

#user name inserted here:
user_name = 'Colombian'

client = boto3.client('iam')

iam = boto3.resource('iam')
# Defines group premade
group = iam.Group('Patient_adders')
# Check if group is correct
pprint (group)

response = client.create_user(
    
    UserName=user_name
)
# Checks if response is correct
pprint (response)

# https://boto3.readthedocs.io/en/latest/reference/services/iam.html#IAM.Client.create_login_profile


response = client.create_login_profile(
    UserName=user_name,
    Password='string',
    PasswordResetRequired=True
)

# https://boto3.readthedocs.io/en/latest/reference/services/iam.html#IAM.Group.add_user
# Adds user to group
response = group.add_user(
    UserName=user_name
)
