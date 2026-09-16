class Utils:
    @staticmethod
    def reversed(number: int) -> int:
        if not isinstance(number, int):
            return -1
        return int(str(number)[::-1])

    @staticmethod
    def formatter(number: int) -> tuple[str, str]:
        if not isinstance(number, int):
            return -1
        binary = bin(number)[2:]
        octal = oct(number)[2:]
        
        return binary, octal