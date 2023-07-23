

def base64_encode(string):
    """Encode a string in base64 format. with out built-in functions."""
    BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result = ""
    for i in range(0, len(string), 3):
        if i + 3 <= len(string):
            result += BASE64_TABLE[(ord(string[i]) & 0xFC) >> 2]
            result += BASE64_TABLE[((ord(string[i]) & 0x03) << 4) | ((ord(string[i + 1]) & 0xF0) >> 4)]
            result += BASE64_TABLE[((ord(string[i + 1]) & 0x0F) << 2) | ((ord(string[i + 2]) & 0xC0) >> 6)]
            result += BASE64_TABLE[ord(string[i + 2]) & 0x3F]
        else:
            result += BASE64_TABLE[(ord(string[i]) & 0xFC) >> 2]
            result += BASE64_TABLE[((ord(string[i]) & 0x03) << 4) | ((ord(string[i + 1]) & 0xF0) >> 4)]
            result += BASE64_TABLE[((ord(string[i + 1]) & 0x0F) << 2)]
            result += "="
    return result

print(base64_encode("Man"))
    