class Calculator:

    def sum(self, numbers: list[float]) -> float:
        sum = 0
        for number in numbers:
            sum += number
        return sum
    
    def multiplication(self, numbers: list[float]) -> float:
        multiply = 1
        for number in numbers:
            multiply = number * multiply
        return multiply
    
    def division(self, numbers:list[float]) -> float:
        division = numbers[0]
        for number in numbers[1:]:
            if division == 0:
                return 0
            else:
                division = division / number
        return division
    
if __name__ == "__main__":

    resultado = Calculator().division(numbers=[5,2])
    print(resultado)
        
    

