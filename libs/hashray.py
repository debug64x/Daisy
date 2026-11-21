import hashlib

def securepass(passw):
    return hashlib.sha512(passw.encode("utf-8")).hexdigest()
def bypassQ(input, passw):
    if hashlib.sha512(input.encode("utf-8")).hexdigest() == passw:
        return True
