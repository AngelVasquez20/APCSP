def palindrome():
    palindrome_word = input("Enter a word for a palindrome: ")
    palindrome_word.lower()
    palindrome_word.replace(" ", "")
    if palindrome_word == palindrome_word[::-1]:
        print("This is a palindrome")
        return True

    else:
        print("This is not a palindrome")
        return False


palindrome()
