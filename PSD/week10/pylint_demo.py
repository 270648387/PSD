"""A simple Object-Oriented Python project that reads either a string or a list
#then calculates the total length and the numer of uppercase characters"""

class TextAnalyzer:
    """Analyzes a string to find its total length and number of uppercase characters"""
    def __init__(self, text):
        self.text = text

    def analyze(self):
        """Return the total length and number of uppercase characters in the string"""
        total_length = len(self.text)
        uppercase_count = sum(1 for c in self.text if c.isupper())
        digit_count = sum(1 for c in self.text if c.isdigit())
        special_count = sum(1 for c in self.text if not c.isalnum())
        return total_length, uppercase_count, digit_count, special_count

def main():
    """Main program"""
    string_input = input("Please enter a string:")
    analyzer = TextAnalyzer(string_input)
    total, upper, digit, special = analyzer.analyze()

    print(f"Total length is: {total}")
    print(f"Uppercase count is: {upper}")
    print(f"Total digits: {digit}")
    print(f"Special character: {special}")

if __name__ == "__main__":
    main()
