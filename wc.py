# wc.py
 
import sys
 
# wc -l <file...>
#    number of lines in the file(s)
# wc -w <file...>
#    number of words in the file(s)
# wc -b <file...>
#    number of characters in the file(s)
# wc -nbl <files...>
#    number of non-blank-lines in the file
 
def count_lines(text):
    return len(text.splitlines())
 
def count_words(text):
    return len(text.split())
 
def count_characters(text):
    return len(text)
 
def count_non_blank_lines(text):
    lines = text.splitlines()
    non_blank_lines = [line  for line in lines if line.strip()]
    return len(non_blank_lines)
 
modes = {'-l': count_lines,
         '-w': count_words,
         '-b': count_characters,
         '-nbl': count_non_blank_lines}
 
if __name__ == '__main__':
    mode      = sys.argv[1]  if len(sys.argv) >= 3 else '-l'
    filenames = sys.argv[2:] if len(sys.argv) >= 3 else [__file__]
 
    func = modes[mode]
 
    total = 0
    for filename in filenames:
        with open(filename) as f:
            text = f.read()
            count = func(text)
            total += count
                 
        print filename, count
