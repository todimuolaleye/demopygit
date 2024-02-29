Oluwatodimu Olaleye
2087951

def is_palindrome(phrase):
    clean_phrase = ''.join(phrase.split()).lower()
    return clean_phrase == clean_phrase[::-1]

if __name__ == '__main__':
    input_phrase = input()
    if is_palindrome(input_phrase):
        print(f'{input_phrase} is a palindrome')
    else:
        print(f'{input_phrase} is not a palindrome')