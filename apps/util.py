import hashlib

def hash(message: str) -> str:
    algo = hashlib.sha256()
    algo.update(message.encode())
    return algo.hexdigest()
