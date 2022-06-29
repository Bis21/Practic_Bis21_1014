# Командный проект от группы "Трио" с учатниками: Батаев Илья, Никита Козлов, Хомяков Кирилл
# Капитан - Батаев И.С.
def write_in_txt_file():
	with open('test.txt','w') as writer:
		writer.write('I love this GIT')
		return True
