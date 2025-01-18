import pytest

from contextlib import contextmanager
from conftest import dynamodb_client

@contextmanager
class TestDynamoDB:
    
    Table_Name = 'ViewCounter'
    """
    def test_app(self, dynamodb_client):
        with create_table(dynamodb_client):
            test = exec(file("c:\code\CLOUDRESUME\SAM\.aws-sam\build\queryDynamoDB\app.py"))
            print(test)
    """
    
    
def create_table(dynamodb_client):
    """Create mock DynamoDB table to test full CRUD operations"""

    dynamodb_client.create_table(
            TableName="ViewCounter",
            KeySchema=[{'AttributeName': 'date','KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'date','AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1,'WriteCapacityUnits': 1}
        )
    
    add_item = dynamodb_client.put_item(
            TableName="self.TABLE_NAME",
            Item={"Resource": {"S": "Resume"}, "Views": {"N": "0"}}
        )

create_table()