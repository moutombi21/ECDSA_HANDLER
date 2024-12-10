import time
from ecdsa_handler import ECDSAHandler

def benchmark(handler, iterations=1000):
    data = b"Test data"
    start_time = time.time()
    for _ in range(iterations):
        handler.sign(data)
    end_time = time.time()
    print(f"{iterations} signatures effectuées en {end_time - start_time:.2f} secondes.")

    signature = handler.sign(data)
    start_time = time.time()
    for _ in range(iterations):
        handler.verify(signature, data)
    end_time = time.time()
    print(f"{iterations} vérifications effectuées en {end_time - start_time:.2f} secondes.")

if __name__ == "__main__":
    handler = ECDSAHandler()
    handler.generate_keys()
    benchmark(handler, iterations=10000)
