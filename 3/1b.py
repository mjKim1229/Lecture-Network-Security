from Crypto.Hash import HMAC

# 사용자로부터 키 입력 받기
key = input("키를 입력하세요: ").encode()

# H.txt 파일 읽기 (이진 모드로)
with open('H.txt', 'rb') as file:
    data = file.read()

print("H.txt에서 읽은값: ",data)
# HMAC 값 추출
file_data, mac_received = data.split(b'\n', 1)
file_data += b'\n'
print(file_data)
print(mac_received)
# HMAC 생성
h = HMAC.new(key)
h.update(file_data)
mac_calculated = h.digest()

# HMAC 값을 출력
print("받은 HMAC:", mac_received.hex())
print("계산된 HMAC:", mac_calculated.hex())

# HMAC 검증 및 무결성 검사
if mac_received == mac_calculated:
    print("OK")
else:
    print("NOK")

