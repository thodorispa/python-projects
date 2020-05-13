def is_palindrome(word):
    reversed_word = word[::-1]
    return True if word == reversed_word else False

print(is_palindrome("oso"))
