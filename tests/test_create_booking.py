import pytest, allure
from pydantic import ValidationError
from core.models.booking import BookingResponse


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with random data')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)
    assert 'bookingid' in response
    assert response['booking'] ['firstname'] == generate_random_booking_data['firstname']
    assert response['booking'] ['lastname'] == generate_random_booking_data['lastname']
    assert response['booking'] ['depositpaid'] == generate_random_booking_data['depositpaid']


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-02-01"
        },
        "additionalneeds": "Dinner"
    }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response ['booking'] ['firstname'] == booking_data['firstname']
    assert response ['booking'] ['lastname'] == booking_data['lastname']
    assert response ['booking'] ['totalprice'] == booking_data['totalprice']
    assert response ['booking'] ['depositpaid'] == booking_data['depositpaid']
    assert response ['booking'] ['bookingdates'] ['checkin'] == booking_data['bookingdates'] ['checkin']
    assert response ['booking'] ['bookingdates'] ['checkout'] == booking_data['bookingdates'] ['checkout']
    assert response ['booking'] ['additionalneeds'] == booking_data['additionalneeds']


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking without unrequired field')
def test_create_booking_without_unrequired_field(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-02-01"
        }
    }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response ['booking'] ['firstname'] == booking_data['firstname']
    assert response ['booking'] ['lastname'] == booking_data['lastname']
    assert response ['booking'] ['totalprice'] == booking_data['totalprice']
    assert response ['booking'] ['depositpaid'] == booking_data['depositpaid']
    assert response ['booking'] ['bookingdates'] ['checkin'] == booking_data['bookingdates'] ['checkin']
    assert response ['booking'] ['bookingdates'] ['checkout'] == booking_data['bookingdates'] ['checkout']


@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with invalid data')
def test_create_booking_with_invalid_data(api_client):
    booking_data = {
        "firstname": 123,
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-02-01"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['status_code'] == 400


@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with empty field')
def test_create_booking_with_empty_field(api_client):
    booking_data = {
        "firstname": 123,
        "lastname": "",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-02-01"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['status_code'] == 400


@allure.feature('Test creating booking')
@allure.story('Negative: creating booking without required field')
def test_create_booking_without_required_field(api_client):
    booking_data = {
        "firstname": 123,
        "lastname": "Brown",
        "totalprice": 150,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-02-01"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['status_code'] == 400