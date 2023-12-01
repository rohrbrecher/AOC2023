from pathlib import Path

def get_input(filename: str):
    filepath = Path(Path(__file__).parent, filename)

    # open the file and read it, while splitting each new line
    with open(filepath, 'r') as file:
        data = file.read().splitlines()
        
    return data