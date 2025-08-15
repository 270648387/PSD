class FileProcessor:
    def __init__(self, input_file):
        self.input_file = input_file

    def read_content(self):
        with open(self.input_file, "r", encoding="utf-8") as infile:
            return infile.read()

    def write_file(self, output_file, text):
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(text)

    def append_file(self, output_file, text):
        with open(output_file, "a", encoding="utf-8") as outfile:
            outfile.write(text)


def main():
    input_path = r"C:\Users\Y\Desktop\PSD\Week3\demo_file.txt"   
    output_path = r"C:\Users\Y\Desktop\PSD\Week3\demo.txt"       
    output_path_1 = r"C:\Users\Y\Desktop\PSD\Week3\demo_1.txt"  

    processor = FileProcessor(input_path)

    content = processor.read_content()

    processor.write_file(output_path, "Hello World !\n")
    processor.write_file(output_path_1, content)  
    processor.append_file(output_path_1, "\nHello World Again!\n")

    print(f"Created '{output_path}' with original content + first line.")
    print(f"Created '{output_path_1}' with original content + appended second line.")


if __name__ == "__main__":
    main()
