def mergeAlternately(word1: str, word2: str):
    merged = []
    i, j = 0, 0

    # Loop through both string untill all characters are processed
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged.append(word1[i])
            i = i + 1
        if j < len(word2):
            merged.append(word2[j])
            j = j + 1
    return "".join(merged)

# Taking input from user
word1 = input("Enter the first string: ")
word2 = input("Enter the second string: ")
result = mergeAlternately(word1, word2)
print("Merged string:", result)