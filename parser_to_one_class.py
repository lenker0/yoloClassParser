import os


if __name__ == '__main__':
	txt_files = filter(lambda x: x[-4:] == '.txt', os.listdir("./"))
	gun_class = '0'
	knife_class = '1'
	for file in txt_files:
		lines = []
		with open(file, 'r+') as file_in:
			for line in file_in:
				lines.append(line)

			file_in.truncate(0)
			file_in.seek(0)
			if lines != []:
				for line_id in range(len(lines)):
					if (lines[line_id][0] != gun_class) and (lines[line_id][0] != knife_class):
						lines[line_id] = f'{gun_class}{lines[line_id][1:]}'
						file_in.write(lines[line_id])
					elif lines[line_id][0] != knife_class:
						file_in.write(lines[line_id])

