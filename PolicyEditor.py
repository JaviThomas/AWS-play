import json

import boto3
from pprint import pprint

# Create IAM client
iam = boto3.client('iam')

# Create a policy
def create_patientadder_policy (policy_name) :
    patient_adder_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {   
                "Effect": "Allow",
                "Action": [
                    "dynamodb:BatchGetItem",
                    "dynamodb:PutItem",
                    "dynamodb:DescribeTable",
                    "dynamodb:GetShardIterator",
                    "dynamodb:GetItem",
                    "dynamodb:Scan",
                    "dynamodb:DescribeStream",
                    "dynamodb:Query",
                    "dynamodb:GetRecords"
                ],
                "Resource": "arn:aws:dynamodb:us-east-1:308565516874:table/bob"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:DescribeReservedCapacityOfferings",
                    "dynamodb:ListTables",
                    "dynamodb:DescribeReservedCapacity",
                    "dynamodb:ListTagsOfResource",
                    "dynamodb:DescribeTimeToLive",
                    "dynamodb:DescribeLimits",
                    "dynamodb:ListStreams",
                    "iam:ChangePassword",
                    "iam:GetAccountPasswordPolicy"
                ],
                "Resource": "*"
            }
        ]
    }


    response = iam.create_policy(
    PolicyName= policy_name,
    PolicyDocument=json.dumps(patient_adder_policy)
    )
    pprint(response["Policy"])
    return response["Policy"]['Arn']


if __name__ == '__main__' :
    arn = create_patientadder_policy("Fred") 
    pprint (arn)