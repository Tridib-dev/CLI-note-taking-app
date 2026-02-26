# Importing modules
import json 
import os
import datetime

# ============================================================================================================

# Getting the recent directory 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Joining the file with directory
FILE_NAME = os.path.join(BASE_DIR,"Notes.json")

# ============================================================================================================

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME,"w") as file:
        json.dump([],file)

# ============================================================================================================ 

class Note:
    # class attributes
    def __init__(self,note,time,priority):
        self.note = note
        self.time = time
        self.priority = priority
        
    # --------------------------------------------------------------------

    
    def note_save(self):
        # making a dictionary to save the note in json file
        data = {
            "note" : self.note,
            "time" : self.time.isoformat(),
            "priority" : self.priority
        }
        
        # --------------------------------------------------
        
        # getting the previosus file
        try:
            with open(FILE_NAME,"r") as file:
                DATA = json.load(file)
                if not isinstance(DATA, list): DATA = []
        # handling the case when the file is not found or is empty
        except(FileNotFoundError,json.JSONDecodeError):
            DATA = []
            
        # --------------------------------------------------
          
        # getting the new id for the note and saving it in the file
        DATA.append(data)        
        # --------------------------------------------------
        
        # sorting the notes based on priority before saving
        DATA = sort_notes(DATA)
    
        # --------------------------------------------------
        
        #saving the data in the file
        with open(FILE_NAME,"w")as file:
            json.dump(DATA,file,indent=4)
            
# ============================================================================================================     

def get_time():
    ''' 
    Getting the current time to save with the note
    
    '''
    
    return datetime.datetime.now()


# ============================================================================================================

def priority_decider(n: int) -> str:
    
    # mapping the input number to the corresponding priority level
    
    mapping = {1: "High", 2: "Medium", 3: "Low",0: "Unneccessary"}
    return mapping[n]
      

# ============================================================================================================      

#Global priority order for sorting the notes
PRIORITY_ORDER = {"High": 3, "Medium": 2, "Low": 1,"Unneccessary": 0}

# ============================================================================================================

def sort_notes(data: list) -> list:
    
    ''' 
    sorting the nots based on their priority level
    
    '''
    
    sorted_items = sorted(
        data,
        # sorting the items based on the priority order defined above
        key=lambda item: PRIORITY_ORDER.get(item["priority"],0),
        reverse=True
    )
    return sorted_items
  
# ============================================================================================================
  
def search_keyword(word):
    if not word:
        return f" No word provided in the notes like {word}\n"
    try:
        with open(FILE_NAME,"r") as file:
            data = json.load(file)
            if not isinstance(data, list):
                return f"No notes found in the file.\n"
              
    except (FileNotFoundError, json.JSONDecodeError):
        return f"No notes found in the file.\n"
    
    # Searching for the word in the notes
    for tasks in data:
        if word.lower() in tasks["note"].lower():
            return f"Found note: \nNote : {tasks['note']} \n Priority : {tasks["priority"]} \n\t  {format_relative_time(tasks['time'])}\n"
    return f"No notes found with the word '{word}'\n"

# ============================================================================================================


def search_time(priority):
    if not priority:
        return f" No Priority provided to find !...\n"
    try:
        with open(FILE_NAME,"r") as file:
            data = json.load(file)
    except ( FileNotFoundError,json.JSONDecodeError):
        return f" No notes found in the file !...\n"
    
    for tasks in data:
        if priority == tasks["priority"]:
            return f"Found note: \nNote : {tasks['note']} \n Priority : {tasks["priority"]} \n\t {format_relative_time(tasks['time'])}\n"
    return f" No notes with such priority is found !...\n"

# ============================================================================================================

def format_relative_time(iso_time_str):
    """
    Important function to format the time stord in json to show properly for the users
    """
    
    # turning the iso time (string) to an object again
    note_time = datetime.datetime.fromisoformat(iso_time_str)
    
    # Getting current time to compare
    now = datetime.datetime.now()
    
    #comparing those times
    diff = now - note_time
    
    seconds = diff.total_seconds()
    days = diff.days
    
    if seconds < 60:
        return f"Added just now"
    elif seconds < 3600:
        minutes = (seconds // 60)
        return f"Added {minutes} {'min' if minutes == 1 else 'mins'} ago"
    elif seconds < 86400:
        hours = (seconds // 3600)
        return f"Added {hours} {'hour' if hours == 1 else 'hours'} ago"
    elif days < 30:
        return f"Added {days} {'day' if days == 1 else 'days'} ago"
    elif days < 366:
        months = days //30
        return f"Added {months} {'month' if months == 1 else 'months'} ago"
    else:
        return f"Added on {note_time.strftime('%b %d, %Y')}"