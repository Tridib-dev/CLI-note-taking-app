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
        json.dump({},file)

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
        except(FileNotFoundError,json.JSONDecodeError):
            DATA = {}
            
        # --------------------------------------------------
          
        # getting the new id for the note and saving it in the file
        id = str(max(map(int, DATA.keys()), default=0) + 1)
        DATA[id] = data
        
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
    
    mapping = {1: "High", 2: "Medium", 3: "Low"}
    return mapping[n]
      

# ============================================================================================================      

#Global priority order for sorting the notes
PRIORITY_ORDER = {"High": 3, "Medium": 2, "Low": 1}

# ============================================================================================================

def sort_notes(data: dict) -> dict:
    
    ''' 
    sorting the nots based on their priority level
    
    '''
    
    sorted_items = sorted(
        data.items(),
        key=lambda item: PRIORITY_ORDER[item[1]["priority"]],
        reverse=True
    )
    return {k: v for k, v in sorted_items}
  
  # ============================================================================================================