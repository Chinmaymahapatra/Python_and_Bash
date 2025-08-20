with open("new_file.txt", "r") as file:
	content = file.read()
	print(content)

file.close()
