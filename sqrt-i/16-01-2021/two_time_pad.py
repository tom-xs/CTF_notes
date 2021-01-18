import os
import time
from ictf import secret, message2


BLOCK_SIZE = 8


def gen_iv():
    return os.urandom(BLOCK_SIZE)


def bxor(b1: bytes, b2: bytes) -> bytes:
    key = bytes([a ^ b for a, b in zip(b1, b2)])
    return key


def invert(b: bytes) -> bytes:
    return bytes([~x & 0xff for x in b])


def rpad(i: bytes) -> bytes:
    padded = i + (b'\xff' * (BLOCK_SIZE * 2 - len(i) % (BLOCK_SIZE * 2)))
    return padded


def lpad(i: bytes) -> bytes:
    padded = (b'\xff' * (BLOCK_SIZE * 2 - len(i) % (BLOCK_SIZE * 2))) + i
    return padded


def encrypt(key: bytes, ptxt: bytes) -> str:
    assert len(ptxt) % len(key) == 0, f'Lengths don\'t work: {len(key)}, {len(ptxt)} :('
    ctxt = bytes([a ^ b for a, b in zip(key, ptxt)])
    return ctxt.hex()


if __name__ == '__main__':
    message1 = b"I am creative with my plaintexts"

    a = gen_iv()
    k1 = rpad(a)
    k2 = lpad(bxor(a, invert(secret)))

    key = bxor(k1, k2)

    ctxt1 = encrypt(key, message1)
    ctxt2 = encrypt(key, message2)

    with open('out.txt', 'w') as f:
        f.write(f'message1 = {message1.decode()}\n')
        f.write(f'ctxt1 = {ctxt1}\n')
        f.write(f'ctxt2 = {ctxt2}\n')
