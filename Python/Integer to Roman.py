class IntegerToRoman:
    def __init__(self, number):
        self.number = number
        # Dictionary with Roman numeral mapping
        self.mapping = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }

    def convert(self):
        num = self.number
        roman = ""
        # Iterate over dictionary keys in descending order
        for value in sorted(self.mapping.keys(), reverse=True):
            while num >= value:
                roman += self.mapping[value]
                num -= value
        return roman


# Example usage
if __name__ == "__main__":
    number = 1994
    converter = IntegerToRoman(number)
    print(f"Integer: {number} -> Roman: {converter.convert()}")
