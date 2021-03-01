import json
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from Crypto.Util.Padding import pad

key = (b'<REDACTED>')
data = (b'<REDACTED>')
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = bytes_to_long(cipher.iv)
ct = bytes_to_long(ct_bytes)
key= bytes_to_long(key)
print(json.dumps({'key' : str(key), 'iv' : iv, 'ciphertext' : ct}))
#{"key": "REDACTED​​​​‍‌​​​​​‌‏‏​​​​‍​‎​​​​‍​‍​​​​‍​‎​​​​‍​‌​​​​‍​‍​​​​‌‏‏​​​​‌‏‏​​​​‍​‌​​​​‌‏‏​​​​‍​‍​​​​‍​‌​​​​‌‏‏​​​​‍‌​​​​​‍​‌", "iv": 305391053562888545371714674049318800655, "ciphertext": 28048967036896554615791698028016955617934752356413153805804958928455841229159}