from encryption import Encryption

class TestEncryption:
    def test_encrypt(self):
        enc = Encryption()
        encrypted_data = enc.encrypt("data")
        assert isinstance(encrypted_data, bytes)  # Check if the result is a byte string
        assert len(encrypted_data) > 0  # Ensure the encrypted data is not empty

    def test_decrypt(self):
        enc = Encryption()
        original_data = "data"
        encrypted_data = enc.encrypt(original_data)
        decrypted_data = enc.decrypt(encrypted_data)
        assert decrypted_data == original_data  # Check if decrypted data matches the original
