from Crypto.Hash import HMAC

# 사용자로부터 키 입력 받기
key = input("키를 입력하세요: ").encode()

# H.txt 파일 읽기 (이진 모드로)
with open('H.txt', 'rb') as file:
    allDataInText = file.read()

print("H.txt 전체 읽은값: ",allDataInText)

#H.txt에서 plaintext와 mac값 분리 
plainText, macInText = allDataInText.split(b'\n', 1)
plainText+=b'\n'
print("plainText", plainText)
print("macInText", macInText)

# HMAC 생성 : User input Key 이용 
#H.txt와 현재 User이 공유하는 Key
h = HMAC.new(key)
h.update(plainText)
macMadeByKey = h.digest()

# HMAC 값을 출력
print("H.text에 있는 HMAC:", macInText)
print("Key이용하여 만든 HMAC:", macMadeByKey)

# MAC 무결성 검사
if macInText == macMadeByKey:
    print("OK")
else:
    print("NOK")

