# Purpose: Given a word, count the number of vowels in the word
# Input Type: str
# Output Type: int
# Example Input: "hello"
# Output of given input: 2
class vowels():
    def __init__(self):
    def vowel_count(word: str) -> int:
        count = 0
        vowels = ["a","e","i","o","u"]
        for letters in word:
            if letters.lower() in vowels:
                count += 1
        print(count)