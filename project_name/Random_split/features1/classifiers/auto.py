import os
from nbconvert import PythonExporter

# specify the directory path
directory = '.'
# iterate through all files in the directory
for filename in os.listdir(directory):
    # check if the file is a Jupyter Notebook
    if filename.endswith('.ipynb'):
        # construct the full path to the file
        path = os.path.join(directory, filename)
        # print the file name
        print(f'Running {filename}...')
        # convert the notebook to python file
        python_script, _ = PythonExporter().from_filename(path)
        # run the python script
        exec(python_script)
