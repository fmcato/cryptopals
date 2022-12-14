def xor_byte(a: bytes, key: int) -> bytes:
    return bytes(
        [x ^ key for x in a]
    )


def xor(a: bytes, b: bytes) -> bytes:
    if len(a) != len(b):
        raise (ValueError('different lengths in a and b'))
    if len(a) <= 0:
        return bytes([])
    return bytes([x ^ y for x, y in zip(a, b)])


def score_ascii_text(message: bytes) -> int:
    score = 0
    for letter in message:
        if letter < 0 or letter > 127:
            # not ASCII
            return -1000000000000
        letter = chr(letter)
        if not letter.isalnum():
            score -= 1
        elif letter.isalpha():
            score += 1
    return score
