def palindrome():
    palindrome_word = input("Enter a word for a Palindrome: ")
    palindrome_word.lower()
    if palindrome_word.replace(" ", "") == palindrome_word.replace(" ", "")[::-1]:
        print("This is a Palindrome")
        return True

    elif palindrome_word.replace(".", "") == palindrome_word.replace(".", "")[::-1]:
        print("This is a Palindrome")
        return True

    elif palindrome_word.replace("?", "") == palindrome_word.replace("?", "")[::-1]:
        print("This is a Palindrome")

    elif palindrome_word.replace(",", "") == palindrome_word.replace(",", "")[::-1]:
        print("This is a Palindrome")

    elif palindrome_word.replace(";", "") == palindrome_word.replace(";", "")[::-1]:
        print("This is a Palindrome")

    else:
        print("This is not a Palindrome")
        return False


palindrome()