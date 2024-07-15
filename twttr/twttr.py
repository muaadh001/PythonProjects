def main():
    msg = input("Input: ")
    msg_wv = shorten(msg)
    print("Output: " + msg_wv)

def shorten(word):
    word_wv = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            word_wv += letter
    return word_wv

if __name__ == "__main__":
    main()
