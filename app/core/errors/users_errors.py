from http import HTTPStatus


NOT_FOUND_RESPONSE = {
    HTTPStatus.NOT_FOUND.value: {
        'description': HTTPStatus.NOT_FOUND.phrase,
        'content': {
            'application/json': {
                'example': {'detail': 'Resource not found!'}
            }
        }
    }
}
