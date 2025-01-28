import json

def read_input_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def process_lines(lines):
    result = []
    for line in lines:
        words = line.strip().split()
        if words:  # Check if the line is not empty
            english_word = words[0]
            hebrew_word = ' '.join(words[1:])
            result.append({"english": english_word, "hebrew": hebrew_word})
    return result

def write_output_file(output_file, data):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    lines = read_input_file(input_file)
    data = process_lines(lines)
    write_output_file(output_file, data)

if __name__ == "__main__":
    main()