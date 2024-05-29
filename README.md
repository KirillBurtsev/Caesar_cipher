# Encryption Script

This Python script implements a two-stage encryption process using a Caesar cipher and transposition based on a keyword. It allows secure encoding and decoding of messages in the Russian language.

## Usage

1. **Encrypt a Message:**
   - Run the script.
   - Select option "1".
   - Input the message to encrypt, shift key, and keyword for the second stage of encryption.

2. **Decrypt a Message:**
   - Run the script.
   - Select option "2" to decrypt the previously encrypted message using the same key and keyword.

3. **Exit the Program:**
   - To exit the program, select option "0".

## Functions

### Encryption Function

The `encrypt` function encrypts a given message using the provided shift key and keyword for transposition.

```python
def encrypt(message, shift_key, keyword):
    # Implementation details...
    return encrypted_message
