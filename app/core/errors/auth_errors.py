from http import HTTPStatus


UNAUTHORIZED_RESPONSE = {
    HTTPStatus.UNAUTHORIZED.value: {
        'description': HTTPStatus.UNAUTHORIZED.phrase,
        'content': {
            'application/json': {
                'examples': {
                    'detail': 'Invalid authentication credentials!'
                }
            }
        }
    }
}
