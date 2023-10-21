from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# 암호화할 텍스트 데이터 읽기
with open('1.txt', 'rb') as file:
    textData = file.read()

# 공개 키를 로드하여 암호화
with open('Alice_public.pem', 'rb') as file:
    pubkey_data = file.read()
    pubkey = RSA.import_key(pubkey_data)
    encryptor = PKCS1_OAEP.new(pubkey)
    encData = encryptor.encrypt(textData)

# 암호화된 데이터를 파일에 저장
with open('enc.txt', 'wb') as output_file:
    output_file.write(encData)

