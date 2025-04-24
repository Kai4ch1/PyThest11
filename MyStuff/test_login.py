def test_invalid_login():
    invalid_email = "charliluckgmailcom"     # Missing @ and .
    invalid_password = "qwe23"               # Too short

    assert "@" in invalid_email              # Should fail
    assert invalid_email.endswith(".org")    # Should fail
    assert "." in invalid_email              # Should fail
    assert len(invalid_password) >= 8        # Should fail
    assert invalid_email.startswith("cahr")  # Should fail

# ✅ Positive test: valid email and password
def test_valid_login():
    valid_email = "carl4welps@gmail.com"
    valid_password = "qweqwe123"

    assert "@" in valid_email
    assert valid_email.endswith(".com")
    assert valid_email.startswith("c")
    assert "q" in valid_password
    assert valid_password == "qweqwe123"
    assert len(valid_password) >= 8