import os
import csv
# "raw_data", "paragraph_1.txt"

filepath = os.path.join("PyParagraph", "raw_data", "paragraph_2.txt")
with open(filepath, 'r') as filehandle:
    paragraph = filehandle.read()
# #------------------------------------------------------------------------------------------------------------------------------------------------
# #Finding Number of Words:
    words = paragraph.split(" ")
    Total_wordcount = len(words)
#------------------------------------------------------------------------------------------------------------------------------------------------
#Finding Number of Sentences:
#reset file pointer to the start of the file
    filehandle.seek(0)
#assign the read object of the filehandle to a variable.
#This creates a variable containing the entire paragraph
    paragraph = filehandle.read()
#create a list that will hold the individual sentences
    Sentences = []
#split the paragraph string by the period character
#the period character is the logical equivalent to the end of a sentence
    Sentences = paragraph.split(". ")
#the number of sentences will equal to the number of elements within our sentence list
    num_of_sentences = len(Sentences)
#-------------------------------------------------------------------------------------------------------------------------------------------------
#Finding average letters per word:
    Characterlist = []
    Alpha_character_list = []
    
    for i in words:
        mylist = list(i)
        for t in mylist:
            Characterlist.append(t)
    for z in Characterlist:
        if z.isalpha():
            Alpha_character_list.append(z)
    Total_letter_count = len(Alpha_character_list) 
    print(Alpha_character_list)
    Average_letter_count = Total_letter_count / Total_wordcount
# #--------------------------------------------------------------------------------------------------------------------------------------------------
# #Finding Average Sentence Length:
















#split elements of the list dictionary value and append them to a list. 

    
    #could potentially make another list comprised of the individual characters within the element rows 
    
# no_integers = [x for x in mylist if not (x.isdigit() 
#                                          or x[0] == '-' and x[1:].isdigit())]
    
    
#     for row in paragraph_2:



# #Finding Average Letter Count:
#     filehandle.seek(0)
#     Total_character_count = 0
#     for x in Row_ref:
#         Total_character_count += len(Row_ref[x]) 
#find a way to remove period character counts... 
#periods might actually not be in the lists 
#subtract by the number of sentences (which logically corresponds to the number of periods) from the total letter count to get the numner of letter minus the 




#     Row_ref2 = {}
#     #for row in paragraph_2:
# #assign dictionary value associated with the key(row) to equal the list created by splitting the row by space
# #This result in a list of individual sentences for row 
# #conceptually the number of periods will be the indicator of the number of sentences 
#         Row_ref2[row] = row.split(".")
# #create a variable that holds the number of words in a row.
# #we get this value by taking the length of list produced by the dictionary 
#         num_of_row_sents = len(Row_ref2[row])    
#         for i in range(num_of_row_sents)):
#             Total_wordcount += num_of_row_sents


        
        






print("Paragraph Analysis")

print("-----------------------")

print("Approximate Word Count: " + str(Total_wordcount))

print("Approximate Sentence Count: " + str(num_of_sentences))

print("Average Letter Count: " + str(Average_letter_count))

print("Average Sentence Length: ")

