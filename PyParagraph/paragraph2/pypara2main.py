import os
import csv
import re

filepath = os.path.join("paragraph_2.txt" )
with open(filepath, 'r') as filehandle:
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Finding Number of Words:
#------------------------------------------------------------------------------------------------------------------------------------------------
#reorganized file content into a string with no newlines.(if needed)
    paragraph = filehandle.readlines()
    new_paragraph = []
    newer_paragraph = []
    for i in paragraph:
#remove extra newline indicators not attached to setence strings
        if i != '\n':
            new_paragraph.append(i)
#remove newline indicators attached to sentence strings 
    for x in new_paragraph:
        newstr = x.replace("\n", " ")
        newer_paragraph.append(newstr)
    paragraph_string = "".join(newer_paragraph)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#seperate string by space (which is logically the equivalent to a new word indicator).
    words = paragraph_string.split(" ")
#Total word count is equal to the length of our word list
    Total_wordcount = len(words)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Finding Number of Sentences:
# Note: 
# There are inconsistences with the interpretation of the end of a sentence. 
# Some periods appear within quatations thus, are not followed by a space. while other periods are used to abbreviate names.
# Hence a consistent interpretation of the end of a sentence is diffcult
# Consquently we are left with only an approximation of number of sentences rather than an exact. 

#create a list that will hold the individual sentences
    Sentences = []
#create a new paragraph which replaces all instances of sensible (but different) end-of-sentence indicators with "*"
#Doing this will provide us with a reasonable way to seperate the sentences in the paragraph using regular expressions split. 
#This will produce a more accurate count of sentences
    paragraph_edit = re.sub(r"\.\'|\.\"|\. ", "*", paragraph_string)

#split the paragraph string by the "*" character which is now logical equivalent to the end of a sentence
    Sentences = paragraph_edit.split("*")
#the number of sentences will equal to the number of elements within our sentence list
    num_of_sentences = len(Sentences)
#-------------------------------------------------------------------------------------------------------------------------------------------------
#Finding average letters per word:
#Creat a list that will hold all characters
    Characterlist = []
#create a list that will hold all alphabet characters
    Alpha_character_list = []
#Loop through words in word list, then split each into a list of its characters.
    for i in words:
        mylist = list(i)
#for every character in a word, append characters to character list  
        for t in mylist:
            Characterlist.append(t)
#Loop through characters in characters list and if a character satisfies .isalpa() then append character to Alpha_character_list
    for z in Characterlist:
        if z.isalpha():
            Alpha_character_list.append(z)
#Total letter count will be equal to the length of the Alpha_character_list
    Total_letter_count = len(Alpha_character_list)

    Average_letter_count = Total_letter_count / Total_wordcount
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Finding Average Sentence Length:
    average_setence_len = Total_wordcount/ num_of_sentences

print("Paragraph Analysis")

print("-----------------------")

print("Approximate Word Count: " + str(Total_wordcount))

print("Approximate Sentence Count: " + str(num_of_sentences))

print(f'Average Letter Count:  {"{:.2f}".format(Average_letter_count)}')

print(f'Average Sentence Length:  {"{:.2f}".format(average_setence_len)}')