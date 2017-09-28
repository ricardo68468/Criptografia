
# coding: utf-8

# In[15]:


from Crypto.Cipher import ChaCha20
from Crypto.Hash import HMAC, SHA256

path = '/home/ricardo/Documents/Cripto/plaintext.txt'
myfile = open(path,'rb')
mytext = myfile.read()
print(mytext)


#plaintext = b'Attack at dawn'
secret = b'*Thirty-two byte (256 bits) key*'
cipher = ChaCha20.new(key=secret)
msg = cipher.nonce + cipher.encrypt(mytext)
print(msg)



# In[16]:


from Crypto.Cipher import ChaCha20
secret = b'*Thirty-two byte (256 bits) key*'
msg_nonce = msg[:8]
ciphertext = msg[8:]
cipher = ChaCha20.new(key=secret, nonce=msg_nonce)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)


# In[21]:


#secret = b'Swordfish'
h = HMAC.new(secret, digestmod=SHA256)
#msg = b'Hello'
h.update(msg)
mac = h.digest()
print(h.hexdigest())


# In[22]:


from Crypto.Hash import HMAC, SHA256

# We have received a message 'msg' together
# with its MAC 'mac'

secret = b'*Thirty-two byte (256 bits) key*'
h = HMAC.new(secret, digestmod=SHA256)
h.update(msg)
try:
  h.verify(mac)
  print("The message '%s' is authentic" % msg)
except ValueError:
  print("The message or the key is wrong")

