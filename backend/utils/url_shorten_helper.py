from snowflake import SnowflakeGenerator
import string

class URLShortenHelper:
    def __init__(self):
        self.numericChars = [str(num) for num in range(10)]
        self.base62CharsMap = self.numericChars + list(string.ascii_letters)
    
    def snowflakeId(self):
        gen = SnowflakeGenerator(42)
        return next(gen)
    
    def getBase62(self,n:int):
        b = 62
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        res =  digits[::-1]
        strBase = ""
        for num in res:
            strBase+=self.base62CharsMap[num]
        return strBase
