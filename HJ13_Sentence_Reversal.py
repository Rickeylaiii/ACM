def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the words back together with spaces
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

def main():
    # Read input from user
    sentence = input()
    
    # Reverse the sentence
    reversed_sentence = reverse_sentence(sentence)
    
    # Output the result
    print(reversed_sentence)

if __name__ == "__main__":
    main()