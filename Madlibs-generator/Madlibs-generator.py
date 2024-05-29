#open story.txt
with open("story.txt", "r") as f:
    story = f.read()
    
#create a set of all the unique words
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

#locate all the words in the story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i +1]
        words.add(word)
        start_of_word = -1

#generate an answer for the words, which we ask the user to do
answers = {}

for word in words:
    answer = input("Enter a word for " +word+ ":")
    answers[word] = answer

#replace the instances of the word with the answer  the user provided
for word in words:
    story = story.replace(word, answers[word])
    
print(story)   
   