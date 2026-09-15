class Utils:
    def reversed(number: int) -> int:
        return int(str(number)[::-1])

    def formatter(number: int) -> int:
        binary = bin(number)[2:]
        octal = oct(number)[2:]
        
        return binary, octal