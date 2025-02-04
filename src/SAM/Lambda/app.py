import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name = 'us-east-1')

    responseUpdate = dynamodb.update_item(
    TableName='ViewCounter',
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
        TableName='ViewCounter',
        Key={
            'Resource': {'S': 'Resume'}
        }
    )

    bodycontents = json.dumps(responseGet['Item']['Views'])
    
    print("this is a test")

    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        },
        "body": bodycontents
        }
    