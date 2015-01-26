from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto import Random

get_random_bytes = Random._UserFriendlyRNG.get_random_bytes

class AESCipher:
	def __init__(self, SharedSecret):
		#Name courtesy of dx
		self.encryptifier = AES.new(SharedSecret, AES.MODE_CFB, IV=SharedSecret)
		self.decryptifier = AES.new(SharedSecret, AES.MODE_CFB, IV=SharedSecret)

	def encrypt(self, data):
		return self.encryptifier.encrypt(data)

	def decrypt(self, data):
		return self.decryptifier.decrypt(data)

class RSACipher:
	def __init__(self, pub_key):
		self.rsa_cipher = PKCS1_v1_5.new(RSA.importKey(pubkey))

	def encrypt(self, data):
		return self.rsa_cipher.encrypt(data)
