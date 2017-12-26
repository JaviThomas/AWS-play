import json

import boto3

# Create IAM client
iam = boto3.client('iam')

# Create a policy
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
                "dynamodb:ListStreams"
            ],
            "Resource": "*"
        }
    ]
}
response = iam.create_policy(
  PolicyName='patientAdditionPolicy',
  PolicyDocument=json.dumps(patient_adder_policy)
)
print(response)