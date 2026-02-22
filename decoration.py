
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
    