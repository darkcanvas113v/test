import secrets
import string
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(30))
print(password)