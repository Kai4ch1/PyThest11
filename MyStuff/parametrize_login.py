import pytest

@pytest.mark.parametrize(
    "email", [
        "carl4welps@gmail.com",      # Valid email
        "qweeamail.com",             # Missing '@'
        "qwe@gmailcom",              # Missing '.'
        "qwe$mail.com",              # Invalid symbol
        "hogwarts@gmail.org"         # Valid with .org domain
    ],
    ids = [
        "Valid",
        "No @",
        "No .",
        "Invalid symbol",
        "Valid with .org"
    ]
)
def test_valid_email_format(email):
    assert "@" in email, f"❌ The '@' is missing in {email}!"
    print(f"✅ {email} contains the '@'")

    assert "." in email, f"❌ Could not recognize the domain in {email}"
    print(f"✅ {email} contains the '.'")

    assert email.endswith("com") or email.endswith("org"), f"❌ Unsupported domain: {email}"
    print(f"✅ {email} ends with 'com' or 'org'")

@pytest.mark.parametrize(
    "passwords", [
        "qwe123qwe",              # Valid
        "123qw",                  # Too short
        "qeqweqwe",               # No digits
        "clownIsOnYou1",          # Valid
        "victorwillbullyou1!"     # Valid
    ],
    ids = [
        "Valid",
        "Too Short",
        "No digits",
        "Cool Valid",
        "Cool Valid 2"
    ]
)
def test_valid_password_format(passwords):
    assert len(passwords) >= 8, f"❌ Too short: {passwords}"
    print(f"✅ Length OK for {passwords}")

    contains_digit = any(check.isdigit() for check in passwords)
    assert contains_digit, f"❌ No digit found: {passwords}"
    print(f"✅ Contains digit: {passwords}")