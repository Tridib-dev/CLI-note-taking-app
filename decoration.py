
import shutil

def print_welcome():
    width = shutil.get_terminal_size(fallback=(80, 20)).columns

    title = "<=: WELCOME TO NOTER LOG :=>"
    line = "_" * len(title)

    print("\n" + title.center(width))
    print(line.center(width) + "\n")


def print_Welcome_banner(name):
    width = shutil.get_terminal_size(fallback=(80, 20)).columns

    title = f"<=: Welcome {name} to the NOTES world :=>"
    underline = "_" * len(title)

    print("\n" + title.center(width))
    print(underline.center(width) + "\n")
    
    
def terminal_designers():
    print("\n","="*50,"\n")
    
def print_logo():
    # \033[32m is the code for Green
    # \033[1;32m makes it BOLD green (looks even more like a hacker terminal)
    green = "\033[1;32m"
    reset = "\033[0m"
    
    logo = r"""
  _   _  ____  _____ _____ ____  
 | \ | |/ __ \|_   _| ____/ ___| 
 |  \| | |  | | | | |  _| \___ \ 
 | |\  | |__| | | | | |___ ___) |
 |_| \_|\____/  |_| |_____|____/ 
    """
    print(green + logo + reset)
    print(green + "  [ SYSTEM READY ] - NOTES ONLINE" + reset + "\n")