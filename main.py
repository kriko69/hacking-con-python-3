# This is a sample Python script.
from Crypto.Hash import SHA512
def main():
    name=input("Nombre: ")
    hash= SHA512.new(data=b'chris')
    print(f"hola mundo y {name} \n")
    print(hash.hexdigest())

if __name__ == '__main__':
    main()