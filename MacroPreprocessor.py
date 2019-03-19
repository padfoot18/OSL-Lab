import re

source_cleaned = []
macro_name_table = []
macro_definition_table = []
argument_list_array = {}
pass1 = []
pass2 = []


class MacroNameTable(object):
	"""docstring for MacroNameTable"""

	def __init__(self, macro_name, mdt_index):
		self.macro_name = macro_name
		self.mdt_index = mdt_index

	def __repr__(self):
		return "{}\t\t\t{}".format(self.macro_name, self.mdt_index)


class MacroDefinitionTable(object):
	"""docstring for MacrodefinitionTable"""

	def __init__(self, mdt_index, text_card):
		self.mdt_index = mdt_index
		self.text_card = text_card

	def __repr__(self):
		return "{}\t\t\t{}".format(self.mdt_index, self.text_card)


class Argument:
	""" """
	def __init__(self, index, argument):
		self.index = index
		self.argument = argument

	def __repr__(self):
		return "{}\t\t\t{}".format(self.index, self.argument)


def parse_code(filename):
	global source_cleaned
	source_cleaned = []
	with open(filename, 'r') as f:
		for line in f:
			line = re.sub('\s+', ' ', line.strip())
			words = line.split(' ')

			filtered_words = []
			for word in words:
				if word is not None and word != '':
					filtered_words.append(word)

			if len(filtered_words) != 0:
				source_cleaned.append(words)


def pass1():
	mdt_index = 1
	for itr in range(len(source_cleaned)):
		mnt_index = mdt_index
		ala_index = 0
		'''Creating macro name table'''
		if 'MACRO' in source_cleaned[itr]:
			next_line = source_cleaned[itr + 1]
			ala_string = ' '.join(next_line)
			for items in next_line:
				if items[0] != '&':
					macro_name = items
					break
			macro_name_table.append(MacroNameTable(macro_name, mnt_index))

			''' Creating argument list array '''
			argument_list_array.update({macro_name: []})
			arguments_list = re.findall('&[A-Za-z0-9]*', ala_string)
			ala_list = ala_string.split(" ")
			if ala_list[0] == macro_name:
				argument_list_array[macro_name].append(Argument(ala_index, "bbbbbbbb"))
				ala_index += 1

			for items in arguments_list:
				argument_list_array[macro_name].append(Argument(ala_index, items))
				ala_index += 1

			''' Creating Macro definition table '''
			for j in range(itr + 1, len(source_cleaned)):
				if macro_name in source_cleaned[j]:
					mdt_text_card = " ".join(source_cleaned[j])
					macro_definition_table.append(MacroDefinitionTable(mdt_index, mdt_text_card))
					mdt_index += 1
				else:
					mdt_text_card = " ".join(source_cleaned[j])
					for val in argument_list_array.values():
						for v in val:
							mdt_text_card = re.sub(v.argument, '#'+str(v.index), mdt_text_card)
					macro_definition_table.append(MacroDefinitionTable(mdt_index, mdt_text_card))
					mdt_index += 1
				if 'MEND' in source_cleaned[j]:
					source_cleaned[j] = ''
					break
				source_cleaned[j] = ''
			source_cleaned[itr] = ''

	with open('pass1_output.txt', 'w+') as file:
		for items in source_cleaned:
			if items != '':
				file.write(' '.join(items)+'\n')


def pass2():
	replace_macro_text = ''
	parse_code('pass1_output.txt')
	for itr in range(len(source_cleaned)):
		for items in macro_name_table:
			# Search for macro name in MNT
			if items.macro_name in source_cleaned[itr]:
				mdt_index = items.mdt_index  # Get MDT Index from MNT Table
				replace_macro_text += macro_definition_table[mdt_index - 1].text_card + '\n'

				if items.macro_name == source_cleaned[itr][0]:
					args = source_cleaned[itr][1].split(',')
				else:
					args = [source_cleaned[itr][0]]
					args += source_cleaned[itr][2].split(',')

				params = re.findall('&[A-Za-z0-9]*', replace_macro_text)
				for j in range(len(args)):
					replace_macro_text = re.sub(params[j], args[j], replace_macro_text)

				# Set up ALA ( Store values in ALA )
				if argument_list_array[items.macro_name][0].argument == "bbbbbbbb":
					for i in range(1, len(args) + 1):
						argument_list_array[items.macro_name][i].argument = args[i - 1]
				else:
					for i in range(len(args)):
						argument_list_array[items.macro_name][i].argument = args[i]

				# Write the statement formed by MDT Text Card in source file
				for j in range(mdt_index, len(macro_definition_table)):
					if 'MEND' in macro_definition_table[j].text_card:
						temp = re.findall('#[0-9]', replace_macro_text)
						for t in temp:
							replace_macro_text = re.sub(t, argument_list_array[items.macro_name][int(t[-1])].argument, replace_macro_text)
						print(temp)
						source_cleaned[itr] = [replace_macro_text]
						break
					replace_macro_text += macro_definition_table[j].text_card + '\n'
				replace_macro_text = ''
	with open('pass2_output.txt', 'w+') as file:
		for items in source_cleaned:
			file.write(' '.join(items)+'\n')


def print_output():
	print("-----------------Pass 1 Output--------------------")
	print()
	print("Macro Name Table")
	print("Macro Name\t\tMDT Index")
	for items in macro_name_table:
		print(items)

	print()
	print("Macro Definition Table")
	print("MDT Index\t\tText Card")
	for items in macro_definition_table:
		print(items)

	for keys in argument_list_array.keys():
		print()
		print('Argument List Array for ' + keys)
		print("Index\t\tArguments")
		for items in argument_list_array[keys]:
			print(items)
	print("---------------------------------------------------")


if __name__ == '__main__':
	parse_code('macro_input.txt')
	pass1()
	print_output()
	pass2()
	print("-----------------Pass 2 Output---------------------")
	for keys in argument_list_array.keys():
		print()
		print('Argument List Array for ' + keys)
		print("Index\t\tArguments")
		for items in argument_list_array[keys]:
			print(items)
	print("----------------------------------------------------")
