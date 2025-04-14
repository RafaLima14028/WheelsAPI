from http import HTTPStatus

NOT_FOUND_VEHICLE_ID_RESPONSE = {
    HTTPStatus.NOT_FOUND.value: {
        'description': HTTPStatus.NOT_FOUND.phrase,
        'content': {
            'application/json': {'example': {'detail': 'Not found the vehicle ID!'}}
        }
    }
}

NOT_FOUND_RESPONSE = {
    HTTPStatus.NOT_FOUND.value: {
        'description': HTTPStatus.NOT_FOUND.phrase,
        'content': {
            'application/json': {'example': {'detail': 'Not found the ad ID!'}}
        }
    }
}
