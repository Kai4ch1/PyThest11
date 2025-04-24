import pytest



@pytest.fixture()
def user_credentials():
    return {
        "email": "valid@qa.com",
        "password": "StrongPass123"
    }

@pytest.fixture()
def invalid_emails():
    return [
        "noatsign.com", "bad@com", "wrongmail@domain"
    ]

@pytest.fixture()
def invalid_password():
    return [
        "0qwe", "qwe", "StrongValidGigaChadPassword229"
    ]

@pytest.mark.parametrize(
    "invalid_email",[
    "noatsign.com",
    "bad@com",
    "wrongmail@domain"
    ],
    ids = [
        "No @",
        "No .",
        "Format"])


def test_invalid_emails(user_credentials, invalid_email):
    #Replace email in fixture
    user_credentials["email"] = invalid_email

    assert "@" in invalid_email, f"❌ The @ is absent: {invalid_email}"
    assert "." in invalid_email, f"❌ The dot is absent: {invalid_email}"
    assert invalid_email.endswith('com') or invalid_email.endswith('org'), f"❌ Wrong: {invalid_email}"

@pytest.mark.parametrize(
    "invalid_password",[
    "0qwe",
    "qwe",
    "StrongValidGigaChadPassword229"
        ],
    ids = [
        "Wrong Amount of characters",
        "No numbers applied",
        "Valid Format"
]
)

def test_invalid_passwords(user_credentials, invalid_password):
    # Replace password in fixture
    user_credentials["password"] = invalid_password
    assert len(invalid_password) >= 8, f"❌ Password is too short: {invalid_password}"
    contains_digit = any(check.isdigit() for check in invalid_password)
    assert contains_digit, f"❌ No digit found: {invalid_password}"