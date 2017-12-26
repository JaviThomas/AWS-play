import boto3
import json
import PolicyEditor
import time
from pprint import pprint

#user name inserted here:
client = boto3.client('iam')
iam2 = boto3.resource('iam')
iam = boto3.client('iam')

def add_aws_user (user_name, password) :
	
	response = client.create_user(
	    
	    UserName=user_name
	)
	# Checks if response is correct
	pprint (response)

	# https://boto3.readthedocs.io/en/latest/reference/services/iam.html#IAM.Client.create_login_profile

	response = client.create_login_profile(
	    UserName=user_name,
	    Password= password,
	    PasswordResetRequired=True
	)

# https://boto3.readthedocs.io/en/latest/reference/services/iam.html#IAM.Group.add_user
# Adds user to group
# Defines group premade

#INSERT OF VALUES
group_name = "Pharmacy11"
user_name = "John_jenkins11"
policy_name = "chuck11"

#Create group
response = client.create_group(
    GroupName=group_name
)

print(response)

#Create Policy
arn = PolicyEditor.create_patientadder_policy (policy_name)

#Attach policy to group
response = client.attach_group_policy(
    GroupName=group_name,
    PolicyArn=arn
)

#Create user
add_aws_user (user_name, "string")

#Add user to Group
time.sleep(2)
group = iam2.Group(group_name)
response = group.add_user(
    UserName=user_name
)