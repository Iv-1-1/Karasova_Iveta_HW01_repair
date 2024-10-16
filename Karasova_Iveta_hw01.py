import json

file = 'alice.txt'

with open(file, 'r', encoding='utf-8') as text_content:
    text = text_content.read()

characters_in_file = {}

clear_text = text.replace(' ', '')

for letter in clear_text:
    if letter.isalpha():
        letter = letter.lower()
    if letter != '\n':
        if letter in characters_in_file:
            characters_in_file[letter] += 1
        else:
            characters_in_file[letter] = 1

with open('hw01_output.json.', mode='w', encoding='utf-8') as text_write:
    json.dump(characters_in_file, text_write, sort_keys=True)

