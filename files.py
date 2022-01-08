from pathlib import Path
cwd = Path.cwd()

demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

print('\nFile name is:' + demo_file.name)

print('\nFile suffix is:' + demo_file.suffix)

print('\nFile folder is:' + demo_file.parent.name)

print('\nFile size is :'+ str(demo_file.stat().st_size) + '\n') 