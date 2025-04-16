from http import HTTPStatus


UNAUTHORIZED_ENTITY_RESPONSE = {
    HTTPStatus.UNAUTHORIZED.value: {
        'description': HTTPStatus.UNAUTHORIZED.phrase,
        'content': {
            'application/json': {
                'examples': {
                    'credentials_expired': {
                        'summary': 'The token expired',
                        'value': {'detail': 'Your credentials have expired!'}
                    },
                    'error_in_decoding': {
                        'summary': 'Problem with decoding of JWT',
                        'value': {'detail': 'An error occurred in the decoding!'}
                    },
                    'error': {
                        'summary': 'Unknown problem during decoding of JWT',
                        'value': {'detail': 'An error occurred!'}
                    },
                    'invalid_authentication_credentials': {
                        'summary': 'Your credentials does not in database',
                        'value': {'detail': 'Invalid authentication credentials!'}
                    },
                    'divergent_data': {
                        'summary': 'The user ID in JWT different of user ID associate operation',
                        'value': {'detail': 'Diferente data!'}
                    }
                }
            }
        }
    }
}
