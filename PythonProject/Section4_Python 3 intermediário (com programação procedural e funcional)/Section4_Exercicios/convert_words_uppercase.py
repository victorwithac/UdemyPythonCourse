#Convert words to Uppercase:
#Given a list of words, create a new list that contains the words in uppercase


#Answer
list_words = ['python', 'php', 'java', 'javascript', 'django']
uppercase_words = [word.upper() for word in list_words]
print(uppercase_words)

#Another way of thinking
# list_words = ['MONKEY', 'SHARK', 'cow', 'CAT', 'dolphin', 'DOG', 'bear', 'capybara']
# uppercase_words = [word for word in list_words if word == word.upper()]
# print(uppercase_words)

