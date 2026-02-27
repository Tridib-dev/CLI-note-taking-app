import os
import datetime
import functions
import json
import decoration as func

 
def search_all():
    func.terminaal_designers()
    inputt = input("do you want to search by keyword or priority ? (k/p) : ").strip().lower()
    if inputt  not in [ 'k','p']:
        return "invalid input, please try again !...\n"
    elif inputt == 'k':
        word = input("Enter keyword to search : ").strip().lower()
        return search_keyword(word)
    else:
        priority = int(input(" Note priority (1 => High | 2 => Medium | 3 => Low | 0 => Unneccesary) : "))
        priority = functions.priority_decider(priority)
        return search_priority(priority=priority)
    
        
 
 
def search_keyword(word):
    if not word:
        return f" No word provided in the notes like {word}\n"
    try:
        with open(functions.FILE_NAME,"r") as file:
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


def search_priority(priority):
    if not priority:
        return f" No Priority provided to find !...\n"
    try:
        with open(functions.FILE_NAME,"r") as file:
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