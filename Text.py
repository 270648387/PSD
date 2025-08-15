def main():
    input_path = r"C:\Users\Y\Desktop\PSD\Week3\demo_file.txt"   
    output_path = r"C:\Users\Y\Desktop\PSD\Week3\demo.txt"       
    output_path_1 = r"C:\Users\Y\Desktop\PSD\Week3\demo_1.txt"  

    with open(input_path, "r", encoding="utf-8") as infile:
        content = infile.read()

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("Hello World !\n")

    with open(output_path_1, "a", encoding="utf-8") as outfile_1:
        outfile_1.write("Hello World Again!\n")
    
    print(f"File '{output_path}' created with first line.")
    print(f"File '{output_path_1}' appended with second line.")

if __name__ == "__main__":
    main()
