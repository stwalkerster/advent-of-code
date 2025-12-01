import inspect
from pathlib import Path

def load_lines(input_file):
    frame = inspect.stack()[1]
    p = frame[0].f_code.co_filename

    input_file_obj = open(Path(p).parent / input_file)
    all_data = input_file_obj.read()
    input_file_obj.close()

    data = [line for line in all_data.split('\n') if line != ""]
    return data