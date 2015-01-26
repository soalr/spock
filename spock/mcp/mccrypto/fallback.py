from spock.crypto.pyaes import aes
from spock.crypto.pkcs1 import rsaes_pkcs1_v15, keys
from spock.crypto import asn1
from spock.mcp.mccrypto import standard

AESCipher = standard.AESCipher
get_random_bytes = standard.get_random_bytes

def decode_der(obj_class, binstr):
	"""Instantiate a DER object class, decode a DER binary string in it, and
	return the object."""
	der = obj_class()
	der.decode(binstr)
	return der

"""
class AESCipher:
	def __init__(self, secret):
		self.enbuf = b''
		self.debuf = b''
		self.encryptifier = aes.AESModeOfOperationCFB(secret, secret, 16)
		self.decryptifier = aes.AESModeOfOperationCFB(secret, secret, 16)

	def encrypt(self, data):
		data = self.enbuf + data
		cut = (len(data)//16)*16
		self.enbuf, data = data[cut:], data[:cut]
		return self.encryptifier.encrypt(data)

	def decrypt(self, data):
		data = self.debuf + data
		cut = (len(data)//16)*16
		self.debuf, data = data[cut:], data[:cut]
		return self.decryptifier.decrypt(data)
"""

class RSACipher:
	def __init__(self, pub_key):
		der = decode_der(asn1.DerSequence, pub_key)
		bitmap = decode_der(asn1.DerBitString, der[1])
		rsa_pub = decode_der(asn1.DerSequence, bitmap.value)
		self.pub_key = keys.RsaPublicKey(rsa_pub[0], rsa_pub[1])


	def encrypt(self, data):
		return rsaes_pkcs1_v15.encrypt(self.pub_key, data)
