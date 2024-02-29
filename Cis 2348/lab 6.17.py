Oluwatodimu Olaleye
2087951

password = input()
replacements = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'
}
for old, new in replacements.items():
    password = password.replace(old, new)
password += 'q*s'
print(password)