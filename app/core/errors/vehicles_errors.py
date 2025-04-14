from http import HTTPStatus

NOT_FOUND_RESPONSE = {
    HTTPStatus.NOT_FOUND.value: {
        'description': HTTPStatus.NOT_FOUND.phrase,
        'content': {
            'application/json': {'example': {'detail': 'Resource not found!'}}
        }
    }
}

UNPROCESSABLE_ENTITY_RESPONSE = {
    HTTPStatus.UNPROCESSABLE_ENTITY.value: {
        'description': HTTPStatus.UNPROCESSABLE_ENTITY.phrase,
        'content': {
            'application/json': {
                'examples': {
                    'invalid_data': {
                        'summary': 'Invalid Data',
                        'value': {'detail': 'Unable to process the provided data!'}
                    },
                    'missing_field': {
                        'summary': 'Missing Field',
                        'value': {
                            'detail': [
                                {
                                    "loc": ["string", 0],
                                    "msg": "string",
                                    "type": "string"
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
}

INTERNAL_SERVER_ERROR_RESPONSE = {
    HTTPStatus.INTERNAL_SERVER_ERROR.value: {
        'description': HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
        'content': {
            'application/json': {'example': {'detail': 'An error has occurred!'}}
        }
    }
}
