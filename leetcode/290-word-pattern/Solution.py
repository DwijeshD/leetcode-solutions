
            if char in char_to_word and char_to_word[char] != 
            word:
                return False

            if word in word_to_char and word_to_char[word] != 
            char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True

        
