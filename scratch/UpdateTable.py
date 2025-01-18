import boto3
import json

dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

responseGet = dynamodb.get_item(
    TableName='View_Counter',
    Key={
        'Resource': {'S': 'Resume'}
    }
)

##Pair = responseGet['Item']['Views']

print(responseGet['Item'])

responseUpdate = dynamodb.update_item(
    TableName='View_Counter',
    Key={
        'Resource': {'S': 'Resume'},
    },
    ##UpdateExpression='ADD Views :increment'
    ##UpdateExpression = 'ADD #usage :increase'
    ##UpdateExpression= "ADD Views :inc"
    ExpressionAttributeNames = {
            '#Views': 'Views'
        },
    ExpressionAttributeValues = {
            ':increase': {
                'N': '1'
            },
        },
    UpdateExpression = 'SET #Views = #Views + :increase'
)

print(responseUpdate)

responseGet = dynamodb.get_item(
    TableName='View_Counter',
    Key={
        'Resource': {'S': 'Resume'}
    }
)

##Pair = responseGet['Item']['Views']

print(responseGet['Item'])
