import sys

class test:
    def __init__(self):
        self.state = 0x12345
        # print(self.state)

    def next(self):
        self.state = (self.state * 0xdeadbeef + 0xbaad) & 0xffffffffffff
        print(self.state)
        return self.state >> 16
    

def decrypt(data):
    a = test()
    decrypt_bytes = bytes([x ^ a.next() for x in data])
    decrypt_data = []

    for x,y in [(decrypt_bytes[i], decrypt_bytes[i +1]) for i in range(0, len(decrypt_bytes), 2)]:
        decrypt_data.append((x & 0xf) | ((y & 0xf) << 4))
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ctf2022.py <seed>".format(sys.argv[0]))
    else:
        with open(sys.argv[1], "rb") as f:
            data = f.read()

        a = test()
        b = bytes([x ^ a.next() for x in data])
        print(b)

        for x,y in [((z & 0xf), ((z >> 4) & 0xf)) for z in b]:
            print(chr(x + ord('a')), end='')
            print(chr(y + ord('a')), end='')


if __name__ == "__main__":
    main()