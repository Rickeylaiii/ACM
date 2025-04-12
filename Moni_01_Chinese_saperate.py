import sys

def segment_text(text, dictionary):
    i = 0
    tokens = []
    n = len(text)
    while i < n:
        longest_word = ""
        for j in range(i+1, n+1):
            candidate = text[i:j]
            if candidate in dictionary:
                if len(candidate) > len(longest_word):
                    longest_word = candidate
        if longest_word:
            tokens.append(longest_word)
            i += len(longest_word)
        else:
            tokens.append(text[i])
            i += 1
    return tokens

def main():
    line = sys.stdin.readline().strip()
    dict_line = sys.stdin.readline().strip()
    
    dictionary = set(dict_line.split(","))
    
    delimiters = {",", ";", "."}
    
    result_tokens = []
    temp = ""
    for ch in line:
        if ch in delimiters:
            if temp:
                tokens = segment_text(temp, dictionary)
                result_tokens.extend(tokens)
                temp = ""
        else:
            temp += ch
    if temp:
        tokens = segment_text(temp, dictionary)
        result_tokens.extend(tokens)
    
    print(",".join(result_tokens))
    
if __name__ == "__main__":
    main()