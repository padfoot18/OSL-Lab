import re
import pprint

database = {
    'keywords': ['break', 'else', 'int', 'include', 'main', 'long', 'switch', 'case', 'enum', 'register', 'typedef',
                 'char', 'extern', 'return', 'union', 'const', 'float', 'short', 'unsigned', 'continue', 'for',
                 'signed', 'void', 'default', 'goto', 'sizeof', 'volatile', 'do', 'if', 'static', 'while'],
    'operators': ['+', '-', '*', '/', '%', '++', '--', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '<<', '>>',
                  '~', '&', '^', '|', '=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '^=', '|=', '?', ':'],
    'seperators': [',', ';'], 'special_symbols': ['@', '#', '$', '(', ')', '{', '}'],
    'predefined_identifier': ['printf', 'scanf']}

regex = '(\/\*[^\*\/]*\*\/)|(\/\/.*\n)|("[^"]*")|(<.*\.h>)|\s|([(){}\[\],;#@$])|([0-9]+\.?[0-9]*)|([a-zA-Z0-9_]+)'
# regex1 = '(".*")|\s|(<.*\.h>)|(\/\/.*)|([(,),{,},\,,;,#,<,>,@,$,%,^,&,*,!,-,=,/])'
pattern1 = re.compile('\/\/.*')  # matches single line comment 
pattern2 = re.compile('".*"')  # matches a string
pattern3 = re.compile('<.*\.h>')  # matches header file

code_words = []
output = {}
code_file = open('analyse.c', 'r')
for line in code_file:
    print(line)
    for word in re.split(regex, line.strip()):
        if word != '' and word is not None:
            code_words.append(word)

id = 1
for word in code_words:
    if word in database['keywords']:
        output.update({word: 'keyword'})
    elif word in database['seperators']:
        output.update({word: 'seperators'})
    elif word in database['operators']:
        output.update({word: 'operators'})
    elif word in database['special_symbols']:
        output.update({word: 'special symbol'})
    elif pattern1.match(word):
        output.update({word: 'comment'})
    elif pattern2.match(word):
        output.update({word: 'string'})
    elif pattern3.match(word):
        output.update({word: 'header file'})
    elif word in database['predefined_identifier']:
        output.update({word: 'predefined identifier'})
    else:
        output.update({word: 'identifier'})

for key, value in output.items():
    if value == 'identifier':
        output[key] = 'identifier' + str(id)
        id = id + 1

pprint.pprint(output)
