from pathlib import Path

cwd = Path.cwd()
print('\nCurrent working directory :\n' +str(cwd))

new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

print('\nDoes that file exist?:\n' + str(new_file.exists()))