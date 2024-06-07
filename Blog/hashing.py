import bcrypt

class Hash():
    def bcrypt(password: str):
        hash = bcrypt.hashpw(password, bcrypt.gensalt())
        return hash.decode('utf-8')
    
    def verify(hashed_password, password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


# if bcrypt.checkpw(password, hashed):
#     print("It Matches!")
# else:
#     print("It Does not Match :(")    