
# Asking user to choose file, if he/she types something else choosing first file automatically
selection = input('Please select file to open: [1] paragraph_1.txt   [2] paragraph_2.txt   [3] paragraph_3.txt : ')

if selection == "1":
    file_path = "raw_data/paragraph_1.txt"
elif selection == "2":
    file_path = "raw_data/paragraph_2.txt"
elif selection == "3":
    file_path = "raw_data/paragraph_3.txt"
else:
    print('')
    print('There is no such file! Will open paragraph_1.txt')
    print('')
    file_path = "raw_data/paragraph_1.txt"
print('')
print('Paragraph Analysis')
print('--------------------')

# Declaring empty string where we will keep all text from file
my_text = ''
with open(file_path, "r") as text_file:
    # Adding all text into one single string, some files contains "new line" characters like \n
    for line in text_file:
        my_text = my_text + line    
    
    # Calculating and printing amount of words by splitting string into list and returning number of elements in list
    print(f'Approximate Word Count: {len(str.split(my_text))}')
    
    # Declaring new blank variable, it will contain string without any special characters like : - , . # () and so on
    no_special_characters = ''
    
    # Using this function to remove special characters
    no_special_characters = no_special_characters.join(e for e in my_text if e.isalnum())
    
    # Calculating amount of letters in string which is equal the total amount of letters of all words. Dividing it by amount of words in text
    print (f"Average Letter Count: {str(round(len(no_special_characters) / len(str.split(my_text)),2))}")

    # Counting amount of periods in string, this will be the amount of sentences (string doesn't have any ? or !)
    print(f"Approximate Sentence Count: {my_text.count('.')}")
    
    # Dividing amount of words by amount of sentences
    print(f"Average Sentence Length: {str(round(len(str.split(my_text)) / my_text.count('.'),2))}")
