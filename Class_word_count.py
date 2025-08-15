class WordCounter:
    def __init__(self, filename):
        self.filename = filename

    def count_words(self):
        with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read()

        words = content.split()
        return len(words)
       


def main():
    file_path = r"C:\Users\Y\Desktop\PSD\Week3\demo_file.txt" 
    counter = WordCounter(file_path)

    total_words = counter.count_words()
    print(f"Total number of words in '{file_path}': {total_words}")


if __name__ == "__main__":
    main()
