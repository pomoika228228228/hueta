word = "наворован"

left = 0
right = 8

while left!=right:
    if (word[left] == word[right]):
        print(f"буквы равны")
        left+=1
        right-=1
    else:
        print("Слово," ,word,"не палиндром")
        break