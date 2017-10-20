f = ["Book1.txt", "Book2.txt", "Book3.txt"]

def main():
    big_word = ""
    for books in f:
        fin = open(books)
        for line in fin:
            line_stripped = line.strip()
            line_words = line_stripped.split()
            for word in line_words:
                if len(word) > len(big_word):
                    big_word = word
  fin.close()
    print("Longest word : ", big_word)

if __name__ == '__main__':
    main()
