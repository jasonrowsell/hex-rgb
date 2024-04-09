VALID_HEX_LENGTHS = (8, 6, 4, 3)
HEX_TO_DEC = {hex_digit: i for i, hex_digit in enumerate("0123456789abcdef")}
RGB_LABEL = "rgb"
RGBA_LABEL = "rgba"
MAX_RGB_VALUE = 255


def normalize(hex: str) -> str:
    """
    Normalize a hexadecimal string to the full format (e.g., 'f0a' -> 'ff00aa').
    """
    if len(hex) in {3, 4}:
        return "".join(char * 2 for char in hex)
    return hex


def xx_to_dec(xx: str) -> int:
    """
    Convert a pair of hexadecimal characters to their decimal representation.
    """
    return (HEX_TO_DEC[xx[0]] << 4) | HEX_TO_DEC[xx[1]]


def hex_to_dec(hex: str) -> str:
    """
    Convert a hexadecimal color string to its decimal representation.
    """
    if len(hex) not in VALID_HEX_LENGTHS:
        raise ValueError("Hex string must be valid length")

    norm = normalize(hex)
    dec = [xx_to_dec(norm[i : i + 2]) for i in (0, 2, 4)]

    label = RGBA_LABEL if len(norm) == 8 else RGB_LABEL

    if label == RGBA_LABEL:
        alpha = round(xx_to_dec(norm[-2:]) / MAX_RGB_VALUE, 5)
        dec.append(alpha)

    return f'{label}({", ".join(str(i) for i in dec)})'
