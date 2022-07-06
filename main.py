

def test():
    file = 'file.txt'
    with open(file, 'r', encoding='utf-8') as f:
        data=f.read()
        print("Test")
        print(data)
        return data
