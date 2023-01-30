import re

def tokenize(text):
    reg = re.compile(b"([idel])|(\d+):|(-?\d+)") 
    i = 0
    while i < len(text):
        m = reg.match(text, i)
        s = m.group(m.lastindex)
        i = m.end()
        if m.lastindex == 2:
            yield "s"
            try:
                yield text[i:i+int(s)].decode()
            except UnicodeDecodeError:
                yield text[i:i+int(s)]
            i = i + int(s)
        else:
            yield s.decode()

def decode_item(genobj, token):
    if token == "i":
        # integer: "i" value "e"
        data = int(next(genobj))
        if next(genobj) != "e":
            raise ValueError
    elif token == "s":
        # string: "s" value (virtual tokens)
        data = next(genobj)
    elif token == "l" or token == "d":
        # container: "l" (or "d") values "e"
        data = []
        tok = next(genobj)
        while tok != "e":
            data.append(decode_item(genobj, tok))
            tok = next(genobj)
        if token == "d":
            data = dict(zip(data[0::2], data[1::2]))
    else:
        raise ValueError
    return data

def decode(text):
    try:
        src = tokenize(text)
        data = decode_item(src, next(src))
        for token in src: # look for more tokens
            raise SyntaxError("trailing junk")
    except (AttributeError, ValueError, StopIteration):
        raise SyntaxError("syntax error")
    return data


with open("test.torrent", "rb") as filerb:
    data = filerb.read()
torrent = decode(data)
