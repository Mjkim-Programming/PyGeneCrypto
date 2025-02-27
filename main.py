from PyGeneCrypto.main import GeneEncrypt, GeneDecode, Compress

string = 'Hello'
encryptedRes = GeneEncrypt(string)
decryptedRes = GeneDecode(encryptedRes)
compressedRes = Compress(encryptedRes)

# Encrypted : GACAGCGGGCTAGCTAGCTT
print(f"Encrypted : {encryptedRes}")

# Compressed : GACAGCG3CTAGCTAGCT2
print(f"Compressed : {compressedRes}")

# Decrypted : Hello
print(f"Decrypted : {decryptedRes}")