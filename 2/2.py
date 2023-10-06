from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os, random, struct

def decrypt_file(key, filename):
	
	chunk_size = 1024
	
	output_filename = os.path.splitext(filename)[0]+'.decrypted'
	
	#open the encrypted file and the initialization vector. 
	#The IV is required for creating the cipher.
	with open(filename, 'rb') as infile:
		#iv = infile.read(16)
		iv = b'Netsec@Soongsil.'
		
                
		origsize = struct.unpack('>L', infile.read(4))[0]
		#create the cipher using the key and the IV.
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		
		#We also write the decrypted data to a verification file, 
		#so we can check the results of the encryption 
		#and decryption by comparing with the original file.
		with open(output_filename, 'wb') as outfile:
			while True:

				chunk = infile.read(chunk_size)
				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(origsize)

password = b"ABCDEF0123456789"

def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()
	
decrypt_file(password, 'enc1.txt');
