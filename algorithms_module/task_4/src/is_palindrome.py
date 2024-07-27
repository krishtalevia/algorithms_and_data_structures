def is_palindrome(text: str) -> bool:
    assert isinstance(text, str), TypeError()

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])