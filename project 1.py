import math
import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def brute_force_private_exponent(p, q, e):
    phi = (p - 1) * (q - 1)
    d = 1
    while True:
        if (e * d) % phi == 1:
            return d
        d += 1

def generate_keys(bits):
    start_time = time.perf_counter()
    
    if bits == 8:
        p = 53
        q = 47
    else:
        bits == 16
        p = 547
        q = 541
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e =23 # You can choose any suitable value for e
    while math.gcd(e, phi) != 1:
        e += 2

    # Compute the private exponent d
    d = brute_force_private_exponent(p, q, e)
    print("Brute force private exponent (d):", d)

    end_time = time.perf_counter()
    return (n, e), (n, d), end_time-start_time

def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = pow(message, e, n)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message


def main():
    # Test with 8-bit RSA key
    print("8-bit RSA test")
    messages_8bit = [201]  # Different input messages for 8-bit test cases
    for i in range(1):  # Run two 8-bit test cases
        message = messages_8bit[i]
        print("Test case", i+1)
        public_key, private_key, key_gen_time = generate_keys(8)
        print("Public key (N, E):", public_key)
        print("Private key (N, D):", private_key)
        print("Generation time:", key_gen_time, "seconds")
        print("Original message:", message)
        encrypted_message = encrypt(message, public_key)
        print("Encrypted message:", encrypted_message)
        decrypted_message = decrypt(encrypted_message, private_key)
        print("Decrypted message:", decrypted_message)
        print()

        # Test with 16-bit RSA key
    print("16-bit test")
    messages_16bit = [101]  # Different input messages for 16-bit test cases
    for i in range(1):  # Run two 16-bit test cases
        message = messages_16bit[i]
        print("Test case", i+1)
        public_key, private_key, key_gen_time = generate_keys(16)
        print("Public key (N, E):", public_key)
        print("Private key (N, D):", private_key)
        print("Generation time:", key_gen_time, "seconds")
        print("Original message:", message)
        encrypted_message = encrypt(message, public_key)
        print("Encrypted message:", encrypted_message)
        decrypted_message = decrypt(encrypted_message, private_key)
        print("Decrypted message:", decrypted_message)
        print()

if __name__=="__main__":
    main()