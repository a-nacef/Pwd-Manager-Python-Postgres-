from fernet import Fernet
import os
import base64

key = bytes(os.environ["pwdkey"], "utf-8")
f = Fernet(key)

u = 'gAAAAABhG7DgTKR1tOQ5s47VRXYtcgyumAsakHGx27nZ1HGGynxU8VTdIkDdN99SkA3WSlUiIh0iP5gD5BYGOFmx0s_7Pb8HcA=='
z = bytes(u, 'utf-8')
test = f.decrypt(b'gAAAAABhHEfuxvX1-kAReNuepuiJ9Y-z-dWpVsAuZUXuVo5YjBHOkuW80s3mcaBVNtaB-XVGHMmBV7L53CBN-nLP7y2eAEhiww==')

print(f"""
           pg = {u}
           z = {z}
           test = {test}
        """
               )

