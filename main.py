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
	with open('test.txt','w') as writer:
		writer.write('I love this GIT')
		return True
