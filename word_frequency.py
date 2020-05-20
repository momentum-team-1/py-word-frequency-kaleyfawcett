STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def clean_text(text):
    text = text.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz -"
    text_to_keep = ""
    for char in text:
        if char in all_letters:
            text_to_keep += char
    return text_to_keep

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    file = open ("seneca_falls.txt")
    text = file.read()
    line_break = text.replace ("\n", " ")
    replaced_space = line_break.replace ("  ", " ")
    remove_double_dash = replaced_space. replace ("--", " ") 
    cleaner_text = clean_text(remove_double_dash) 
    split_text = cleaner_text.split(" ")
    word_scramble = []
    for word in split_text:
        if not word in STOP_WORDS:
            word_scramble.append(word)
    sort_words = sorted (word_scramble) 
    
       
    multiple_words = dict()

    for word in sort_words:
        if word in multiple_words:
            multiple_words[word] += 1
        else:
            multiple_words[word] = 1
    multiple_words = {key: value for key, value in multiple_words.items() if value >=1} 

    sorted_words = sorted(multiple_words.items(), key=lambda seq: seq[1], reverse=True) 
    

    for key, value in sorted_words:
            print (key.rjust(16) , ' | ', value, value * ("*")) 




    



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
