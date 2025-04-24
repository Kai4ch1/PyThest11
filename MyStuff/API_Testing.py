import copy
import pytest
import requests


BASE_URL = "https://restful-booker.herokuapp.com"



# == FIXTURE: Booking Payload ===
@pytest.fixture()
def booking_payload():
    return {
        'firstname': "Dexter",
        'lastname': "Morgan",
        'totalprice': 111,
        "depositpaid": True,
        'bookingdates': {
            'checkin': "2025-01-01",
            'checkout': "2026-01-01"
        },
        'additionalneeds': "Breakfast"
    }

# === PARAMETRIZED TEST: TOTALPRICE ===
@pytest.mark.parametrize(
    'totalprice',
    [
        111,
        110,
        -10,
        0,
        -0,
        999999999999999999999999,
        112,
        111.1,
        True,
        False,
        None,
        "",
        " "
    ],
    ids=[
        "Valid",
        "Boundary lesser than original",
        "Negative number",
        "Zero",
        "Minus Zero",
        "Too large",
        "Boundary Decimal more than original",
        "Boundary decimal 0.1 more",
        "Bool True",
        "Bool False",
        "None",
        "Empty string",
        "Space string"
    ]
)
def test_totalprice(totalprice, booking_payload):
    url = BASE_URL + "/booking"
    payload = copy.deepcopy(booking_payload)
    payload["totalprice"] = totalprice

    response = requests.post(
        url,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print(f"Testing totalprice = {totalprice} ➜ Status Code: {response.status_code}")

    if isinstance(totalprice, int) and 110 <= totalprice < 120:
        assert response.status_code == 200
    else:
        assert response.status_code >= 400


# === PARAMETRIZED TEST: FIRSTNAME ===
@pytest.mark.parametrize(
    'firstname',
    [
        'Dexter',
        '',
        ' ',
        'q',
        None,
        0,
        999999999999999999999999,
        True,
        False,
        "\ud83d\udca3\ud83d\udca5\ud83d\udd25"
    ],
    ids=[
        "Valid",
        "Empty String",
        "Space",
        "1 char",
        "None type",
        "zero",
        "Large Number",
        "Bool True",
        "Bool False",
        "Special Unicode"
    ]
)
def test_firstname_validation(firstname, booking_payload):
    url = BASE_URL + "/booking"
    payload = copy.deepcopy(booking_payload)
    payload['firstname'] = firstname

    response = requests.post(
        url,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print(f"First Name is {firstname} -> Status Code is: {response.status_code}")

    if isinstance(firstname, str) and firstname.strip() and len(firstname.strip()) > 1:
        assert response.status_code == 200, f"❌ Expected 200 but got {response.status_code} for: {firstname}"
    else:
        assert response.status_code >= 400, f"❌ Invalid firstname should be rejected but got {response.status_code}"

    if response.status_code >= 500:
        print(f"❗ Unexpected server error for firstname: {firstname}")

@pytest.mark.parametrize(
        'depositpaid', [
        True,
        False,
        ' ',
        'q',
        None,
        0,
        999999999999999999999999,
        "\ud83d\udca3\ud83d\udca5\ud83d\udd25",
        "True",
        "False",
        "1",
        "0",
        1

    ],
        ids = [
            "Valid",
            "False",
            "Space",
            "1 char",
            "None type",
            "zero",
            "Large Number",
            "Special Unicode",
            "String True",
            "String False",
            "number 1 via string",
            "number 0 via string",
            "number 1 as an INT"
        ]

)
def test_depositpaid_validation(depositpaid, booking_payload):
    url = BASE_URL + "/booking"
    payload = copy.deepcopy(booking_payload)
    payload['depositpaid'] = depositpaid


    response = requests.post(
        url,
        json = payload,
        headers = {"Content-Type": "application/json"}
    )
    if isinstance(depositpaid, bool):
        assert response.status_code == 200
    else:
        assert response.status_code >= 400

