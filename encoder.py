import base64

def encode_message(message):
    message_bytes = message.encode("utf-8")
    encoded_bytes = base64.b64encode(message_bytes)
    return encoded_bytes.decode("utf-8")