import os
import sys

def make_at(path, dir_name):
    original_path = os.getcwd()
    print ("original parth is", original_path)
    os.chdir(path)
    
    try:
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file = sys.stderr)
        raise
    finally:
         os.chdir(original_path)

def main():
    make_at("/Users/prsharma/Documents/GitHub/Python4Me", "Newdirectory")

main()

