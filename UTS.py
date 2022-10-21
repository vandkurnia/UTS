# Deklarasi abjad
abjad = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print('========================================')
key = int(input('Masukkan key (angka): '))

# Membuat fungsi enkripsi untuk caesar cipher
def enkripsi(kalimat,cipher_key):
  kalimat = kalimat.upper()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in abjad:
      index_lama = abjad.index(karakter)
      index_baru = (index_lama + cipher_key ) % len(abjad)
      abjad_baru = abjad[index_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode


# Menampilkan Hasil Enkripsi dengan Caesar Cipher
print('========================================')
print('=====Enkripsi Pertama Caesar Cipher=====')
print('========================================')

kalimat = input('Masukkan Teks : ')
kalimat_hasil = enkripsi(kalimat,key)
print('Plaintext :',kalimat)
print('Enkripsi  :',kalimat_hasil)

# Meng-generate key
def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
# Fungsi Enkripsi Vigenere Cipher
def encrypt(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 

# Fungsi Deskripsi Vigenere Cipher
def decrypt(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text))

# Pengenkripisian kedua dengan Vigenere Chiper
print('========================================')
print('=====Enkripsi Kedua Vigenere Chiper=====')
print('========================================')
if __name__ == "__main__":
  string = input('Masukkan Hasil Enkripsi Pertama: ')
  keyword = "DEVAN"
  key = generateKey(string, keyword) 
  encrypt_text = encrypt(string,key)

  # Menampilkan Hasil
  print("Enkripsi  :", encrypt_text) 
  print("Deskripsi :", decrypt(encrypt_text, key))

  print('========================================')
  print('==========Hasil Final Enkripsi==========')
  print('========================================')
  print('Hasil :',encrypt_text) 