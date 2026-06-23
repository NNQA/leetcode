

class Solotion:
    def addBinary(self, a: str, b: str):
       return bin(int(a, 2) + int(b, 2))[2:] 


solution = Solotion()
print(solution.addBinary("11", "1"))