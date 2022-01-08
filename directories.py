from pathlib import Path
cwd = Path.cwd()

parent = cwd.parent

print('\n Is this a directory' + str(parent.is_dir()))

print('\n Is this a file' + str(parent.is_file))

print('\n-----directories contents-----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)