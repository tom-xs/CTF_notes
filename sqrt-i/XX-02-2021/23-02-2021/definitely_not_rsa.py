from Crypto.Random.random import randrange
from Crypto.Util.number import getPrime
from math import gcd
from notsoeasy import flag


def perhaps_rsa_keygen():
	p, q = [getPrime(1024) for _ in range(2)]

	n = p*q
	phi = (p-1)*(q-1)

	e = randrange(n)
	while gcd(e, phi) != 1:
		e = randrange(n)

	return (n, e), (n, pow(e, -1, phi))


def you_thought_it_was_rsa_encryption_but_it_was_me_dio(data, n, e):
	m = randrange(n)
	a = randrange(m)
	b = randrange(m)
	nonce = randrange(m)

	for d in data.hex():
		yield pow(e, int(d, 16), n) * pow(nonce, -1, n) % n
		nonce = (a*nonce + b) % m


def not_rsa_main():
	(n, e), _ = perhaps_rsa_keygen()

	with open('out.txt', 'w') as out:
		out.write('n: ' + str(n) + '\n')
		out.write('e: ' + str(e) + '\n')

		out.write('\nVery secure not RSA encrypted flag:\n[')
		out.write(', '.join(map(str, you_thought_it_was_rsa_encryption_but_it_was_me_dio(flag, n, e))))
		out.write(']')


if __name__ == '__main__':
	not_rsa_main()
