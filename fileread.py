with open('data.txt', 'r') as file:
    content = file.read()
words = content.split()
print(f"Number of words: {len(words)}")