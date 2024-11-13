word_list = []
to_print_words_list = []
num_word_input = 1

while num_word_input < 11:
    word_input = (input(f"Enter 10 words, word {num_word_input}: "))
    word_list.append(word_input)
    num_word_input += 1
    
word_letter_counter = int(input("Enter a number: "))

for word in word_list:
    if len(word) >= word_letter_counter:
        to_print_words_list.append(word)
        continue

print(f"words found with atleast {word_letter_counter} letters:", to_print_words_list)
       