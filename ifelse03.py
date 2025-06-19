import os 

name_of_file = input("enter the name:")
if os.path.exists(name_of_file):
    print(f"there is {name_of_file} file")
else:
    print(f"there is not {name_of_file}file")
