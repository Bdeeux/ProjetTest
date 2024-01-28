class StringCalculator:

    @staticmethod
    def Add(numbers):
        parts = numbers.split(';')
        sum = 0
        for part in parts:
            try:
                number = int(part)
            except ValueError:
                number = 0
            if number <= 1000:
                sum += number
        return sum
    
    # Rouge
    #def Multiply(numbers):
        # Implémentation temporaire
        return 0

 
    # vert
    def Multiply(numbers):
        parts = numbers.split(';')
        product = 1
        for part in parts:
            try:
                number = int(part)
            except ValueError:
                continue  # Ignore les valeurs non numériques
            if 0 < number <= 1000:
                product *= number
        return product