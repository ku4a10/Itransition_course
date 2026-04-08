import hashlib
import os

ZIP_PATH = r'task2\data\data'
EMAIL    = ""

def sha3_256_of_file(data: bytes) -> str:
    h = hashlib.sha3_256()
    h.update(data)
    return h.hexdigest()

def sort_key(hex_hash: str) -> int:
    product = 1
    for ch in hex_hash:
        product *= (int(ch, 16) + 1)
    return product

def main():
    EMAIL_lower = EMAIL.lower()

    all_files = sorted([
        f for f in os.listdir(ZIP_PATH)
        if os.path.isfile(os.path.join(ZIP_PATH, f))
    ])
    print(f"Files in folder: {len(all_files)}")
    assert len(all_files) == 256, f"Expected 256 files,  {len(all_files)}"

    hashes = []
    for filename in all_files:
        filepath = os.path.join(ZIP_PATH, filename)
        with open(filepath, 'rb') as f:
            data = f.read()
        hashes.append(sha3_256_of_file(data))

    hashes_sorted = sorted(hashes, key=sort_key)
    concatenated = "".join(hashes_sorted)
    final_string = concatenated + EMAIL_lower


    final_hash = hashlib.sha3_256(final_string.encode('ascii')).hexdigest()

    print(f"\nResult: {final_hash}")


if __name__ == "__main__":
    main()