import os
import sys
import boto3
import json
from boto3 import resource, client
import pytest
import moto

from .app import lambda_handler

@moto.mock_aws
class TestappDynamoDB():
    def test_data_table(test):
        client = boto3.client("dynamodb", "us-east-1")
        client.create_table(
            TableName = 'ViewCounter',
            KeySchema=[{'AttributeName': 'Resource','KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'Resource','AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1,'WriteCapacityUnits': 1}
        )
        client.put_item(
            TableName='ViewCounter',
            Item={"Resource": {"S": "Resume"}, "Views": {"N": "0"}}
        )
        response = lambda_handler(event = '', context = '')
        print(response)
        assert response == {"statusCode": 200, "headers": {"Content-Type": "application/json", "Access-Control-Allow-Headers": "Content-Type", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET"}, "body": "{\"N\": \"1\"}"}
