def main():

    consonants = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v',
    'w','x','y','z')

    while True:
        word = (input("Please insert a word or press Enter to exit\n")).strip()
        word = list(word)
        
        if len(word) == 0:
            break
       
        first_letter = word[0].lower()

        if first_letter in consonants:
            word = word[1::]
            word.append(first_letter)
            word.append('ay')
            new_str = ""
            new_word = new_str.join(word)
            print(new_word)
        if first_letter not in consonants:
            word.append('ay')
            new_str = ""
            new_word = new_str.join(word)
            print(new_word)

if __name__== "__main__":
    main()
  