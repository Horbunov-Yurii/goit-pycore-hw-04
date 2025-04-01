import sys 
from pathlib import Path
from colorama import Fore, Style


def path_tree(path: Path, level=0):
    for el in path.iterdir():
        if el.is_dir():
            print(f"{Fore.BLUE}{' ' * level}{el.name}")
            path_tree(el,level+1)
        else:
            print(f"{Fore.YELLOW}{' ' * level}{el.name}")    


def main():
    arguments = sys.argv
    if len(arguments) > 1:
        path = Path(arguments[1])
        if path.is_dir() and path.exists():
            path_tree(path)
            print(Style.RESET_ALL)
        else:
            print("Введіть шлях до директорії")

    else:
        print("Введіть шлях до директорії")    
    

    

if __name__ == "__main__":
    main()   