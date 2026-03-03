
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names_path:
    names_list = names_path.readlines()

    

for name in names_list:
    name = name.strip() # é necessário atribuir a uma variável para salva-lo.
    with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_path:
        letter = letter_path.read()

    correct_letter = letter.replace("[name]",name)
    
    file_name = f"letter_for_{name}.txt"
    with open (f"./Mail Merge Project Start/OutPut/{file_name}", "w") as sending_letter_path:
        sending_letter_path.write(correct_letter)


