import hashlib

def hash_string(input_string):
    # Create a sha256 hash object
    sha_signature = hashlib.sha256(input_string.encode()).hexdigest()
    return sha_signature

# Example usage
input_string = "Hello, World!"
hashed_string = hash_string(input_string)
print("Original String:", input_string)
print("Hashed String:", hashed_string)
