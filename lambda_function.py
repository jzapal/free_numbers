from check_free_numbers import search_for_numbers


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': search_for_numbers()
    }
