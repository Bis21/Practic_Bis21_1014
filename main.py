# Командный проект от группы "Трио" с учатниками: Батаев Илья, Никита Козлов, Хомяков Кирилл
# Капитан - Батаев И.С.

#nikita - удаление
def delete_file():
    file_path = 'file.txt'
    try:
        os.remove(file_path)
        return True
    except:
        print("The system cannot find the file specified")
        return False