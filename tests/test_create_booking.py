import pytest, allure


@allure.feature('Test Booking')
@allure.story('Test Create Booking')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)
    assert 'bookingid' in response
    assert response['booking'] ['firstname'] == generate_random_booking_data['firstname']
    assert response['booking'] ['lastname'] == generate_random_booking_data['lastname']
    assert response['booking'] ['depositpaid'] == generate_random_booking_data['depositpaid']

