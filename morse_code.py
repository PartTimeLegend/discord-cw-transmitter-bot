def load_morse_code_dict(file_path):
    morse_code_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            morse_code_dict[key] = value
    return morse_code_dict
