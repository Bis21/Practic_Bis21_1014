# Командный проект от группы "Трио" с учатниками: Батаев Илья, Никита Козлов, Хомяков Кирилл
# Капитан - Батаев И.С.


#nikita - удаление
# func
def delete_file():
    file_path = 'file.txt'
    try:
        import os
        os.remove(file_path)
        return True
    except:
        print("The system cannot find the file specified")
        return False
      
def write_in_txt_file():
	with open('file.txt','w') as writer:
		writer.write('I love this GIT')
		return True

#User2(Kirill): чтение
def read_txt_file():
    file = 'file.txt'
    with open(file,'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
        return data

if __name__ == "__main__":
	if write_in_txt_file():
		print("[ok] write")
	print(read_txt_file())
	
	if delete_file():
		print("[OK] delete")
	
