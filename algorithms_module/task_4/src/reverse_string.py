def reverse_string(text: str) -> str:
    assert isinstance(text, str), TypeError()

    if len(text) == 0:
        return ''

    return text[-1] + reverse_string(text[:-1])