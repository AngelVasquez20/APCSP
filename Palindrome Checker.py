def palindrome():
    palindrome_word = input("Enter a word for a palindrome: ")
    palindrome_word.lower()
    if palindrome_word.replace(" ", "") == palindrome_word.replace(" ", "")[::-1]:
        print("This is a palindrome")
        return True

    elif palindrome_word.replace(".", "") == palindrome_word.replace(".", "")[::-1]:
        print("This is a palindrome")
        return True
    else:
        print("This is not a palindrome")
        return False


palindrome()
