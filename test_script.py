from file_handler import AdvancedFileHandler

#create a AdvancedFileHandler from combined file
adv = AdvancedFileHandler("combined_file.txt") 



#print the object
print(adv)


#count and print total number of words
print("Total words:", adv.count_words())