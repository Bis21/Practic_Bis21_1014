#User2(Kirill): чтение
def read_txt_file():
    file = 'file.txt'
    with open(file,'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
        print("poverka")
        return data
