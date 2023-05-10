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


def score_ascii_text(message: bytes) -> float:
    score = 0
    for letter in message:
        if letter < 0 or letter > 127:
            # not ASCII
            return -1000000000000
        letter = chr(letter)
        if letter.isalpha() or letter in (' ', "'"):
            score += 5
        else:
            score -= 5
    return score / len(message)

def xor_repeating_key(message: str, key: str, key_size: int = None) -> bytes:
    if key_size is None:
        key_size = len(key)
    key_bytes = str.encode(key)
    xored_bytes = []
    key_pos = 0
    for text_byte in str.encode(message):
        xored_bytes.append(text_byte ^ key_bytes[key_pos])
        key_pos += 1
        key_pos %= key_size

    return bytes(xored_bytes)

