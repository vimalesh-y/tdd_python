# Import unittest and string Python packages
import unittest
import string 

# Define encrypt function later to be used in tests
def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(message)])
    print(encrypted_message)
    return encrypted_message

# Create class for tests I will create 
class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "apple pie is the best"

    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    def test_functionReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))

    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message), str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(self.my_message)])
        print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.my_message))

# This code runs the unit tests automatically when script is directly executed
if __name__ == "__main__":
    unittest.main()


