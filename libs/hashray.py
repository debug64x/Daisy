import hashlib

def securepass(passw):
    return hashlib.sha512(passw.encode("utf-8")).hexdigest() # is sha512 neccesary? or we could use 256 for UI's sake
# for the one who wrote the comment up there : you can convert sha512 to 256 but why just write a paragragh if we can just leave it, and you could buy a monitor not you etchasketch monitor
def bypassQ(input, passw):
    if hashlib.sha512(input.encode("utf-8")).hexdigest() == passw: # fat func
        return True