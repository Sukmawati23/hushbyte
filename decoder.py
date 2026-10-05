import base64

def decode_message(encoded_message):
    encoded_bytes = encoded_message.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_bytes)
    return decoded_bytes.decode("utf-8")