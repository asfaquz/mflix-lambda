def lambda_handler(event, context):
    # Simulate listing users
    return {
        "statusCode": 200,
        "body": "['user1', 'user2', 'user3']"
    }
