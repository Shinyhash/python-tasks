def ispalindrome(word):
    reversedW = word[::-1]
    if word == reversedW:
        return True
    else:
        return False

inputW = input("Введите слово: ")
ispalindrome = ispalindrome(inputW)
if ispalindrome:
    print(f"Слово '{inputW}' является перевертышем")
else:
    print(f"Слово '{inputW}' не является перевертышем")
