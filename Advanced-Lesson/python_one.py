# File One

print("Print From File One")

def hello():
    print("Print Function From File One")
    print(__name__)

print(__name__)
if True:
    print('True')

else:
    print('False')

if __name__ == "__main__":
    print('Directly')
else:
    print('No')