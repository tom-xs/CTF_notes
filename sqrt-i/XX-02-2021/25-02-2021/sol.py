import json
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES

key = "REDACTED​​​​‍‌​​​​​‌‏‏​​​​‍​‎​​​​‍​‍​​​​‍​‎​​​​‍​‌​​​​‍​‍​​​​‌‏‏​​​​‌‏‏​​​​‍​‌​​​​‌‏‏​​​​‍​‍​​​​‍​‌​​​​‌‏‏​​​​‍‌​​​​​‍​‌"
iv =  305391053562888545371714674049318800655
ciphertext =  28048967036896554615791698028016955617934752356413153805804958928455841229159

key = long_to_bytes(key)


