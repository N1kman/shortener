import hashlib

class Sha256Coder:
    @staticmethod
    def get_short_url(url: str, length: int = 8):
        hash_object = hashlib.sha256(url.encode())
        hex_digest = hash_object.hexdigest()
        return hex_digest[:length]
