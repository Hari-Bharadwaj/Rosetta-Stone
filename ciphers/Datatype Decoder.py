import base64

def is_binary(text):
    despace_text=text.replace(' ','')
    if not all(i in '01' for i in despace_text):
        return False
    if len(despace_text)%8!=0:
        return False
    return True

def is_base64(text):
    try:
        decoded = base64.b64decode(text, validate=True)
        return True
    except Exception:
        return False
    
def is_base32(text):
    try:
        decoded = base64.b32decode(text, casefold=True)
        return True
    except Exception:
        return False

def is_hex(text):
    try:
        bytes.fromhex(text)
        return True
    except ValueError:
        return False

def identify_encoding(text):
    text = text.strip()

    if is_binary(text):
        return "binary"
    elif is_hex(text):
        return "hex"
    elif is_base64(text):
        return "base64"
    elif is_base32(text):
        return "base32"
    else:
        return "unknown"



if __name__=="__main__":
    test_cases = {
    "01001000 01100101 01101100 01101100 01101111": "binary",
    "48656c6c6f": "hex",
    "SGVsbG8=": "base64",
    "JBSWY3DP": "base32",
    "this is clearly not encoded": "unknown",
    "1234===": "unknown",
    }
    for input_text, expected in test_cases.items():
        result = identify_encoding(input_text)
        print("Input:",input_text,"Detected:",result)
