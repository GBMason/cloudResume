import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name = 'us-east-1')

    
    responseUpdate = dynamodb.update_item(
    TableName='View_Counter',
    Key={
        'Resource': {'S': 'Resume'},
    },

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

    responseGet = dynamodb.get_item(
        TableName='View_Counter',
        Key={
            'Resource': {'S': 'Resume'}
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        "body": responseGet['Item']['Views']
        }