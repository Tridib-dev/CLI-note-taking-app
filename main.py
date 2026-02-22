import json 
import os
import datetime
import functions
import decoration as func
  
def main():
    func.print_welcome()
    
    # Getting the name of the user and welcoming on board
    name = input("Enter your name : ")
    func.print_Welcome_banner(name)
    
    # ------------------------------------------------------------------------
    
    Running = True
    
    while Running:
        
        # Getting the note input from the user
        note = input("Enter your note : ")
        if not note.strip():
            print("Note cannot be empty.")
            continue
        
        # --------------------------------------------------------------------
        
        # Getting the note's timestamp
        note_time = functions.get_time()
        
        # --------------------------------------------------------------------
        
        # getting the notes's priority
        try:
            note_priority = int(input("Note priority (1 => High | 2 => Medium | 3 => Low) : "))
        except ValueError:
            print("Priority must be a number.")
            continue
        
        if note_priority not in [1,2,3]:
            print("\nFallback error because of wrong input,\n\nTry again with appropriate choice !...\n\n")
            continue
    
        # --------------------------------------------------------------------
        
        # evaluating the note's priority with its ranking 
        note_priority = functions.priority_decider(note_priority)
        
        # creating an object  to save the note in the file
        NOTE = functions.Note(note=note,time=note_time,priority=note_priority)    
        
        # saving the note in the json file
        NOTE.note_save()
        
        # --------------------------------------------------------------------
        
        
        # taking decision of deleting or keeping data  on the input of user
        
        user_input_deletion = input("Enter [y => delete all notes]  or [n => keep all notes] : ")
        if user_input_deletion.lower() == 'y':
            try:
                with open(functions.FILE_NAME,"w") as file:
                    json.dump({},file,indent=4)
                print("\nAll notes deleted successfully.\n")
            except Exception as e:
                print(f"\nAn error occurred while deleting notes: {e}\n")
        elif user_input_deletion.lower() == 'n':
            print("\nAll notes kept successfully.\n")
            
        else:
            print("\nInvalid input ! \n\n")
            print("Note taking stopped because of invalid input\n")
            continue
        
        
        # --------------------------------------------------------------------
        
        # taking decision of finishing note taking on the input of user
        user_input_continue = input("Enter [y => continue]  or [n => stop] : ")
        if user_input_continue.lower() == 'y':
            continue
        elif user_input_continue.lower() == 'n':
            print("\nNote taking stopped successfully.\n")
            break
        else:
            print("\nNote taking stopped because of invalid input\n\n")
            continue
        
        
        # --------------------------------------------------------------------
        print("\n")
                

# Running main function
if __name__ == '__main__':
        main()
        