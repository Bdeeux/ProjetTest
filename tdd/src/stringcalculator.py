from functools import reduce

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
    

## Tests Fonctionnelle ##
# Première itération # 

#Red
    #def Multiply(numbers):
        return 0

 
#Green
    #def Multiply(numbers):
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
    
#Blue
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if 0 < number <= 1000 else 1
            except ValueError:
                return 1

        parts = numbers.split(';')
        product = 1
        for part in parts:
            product *= parse_and_filter_number(part)

        return product
    
# Deuxième itération # 

#Red
    def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if 0 < number <= 1000 else 1
            except ValueError:
                return 1

        parts = numbers.split(';')
        product = 1
        for part in parts:
            product *= parse_and_filter_number(part)

        return product
    
#Green
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else 1
            except ValueError:
                return 1

        parts = numbers.split(';')
        product = 1
        for part in parts:
            product *= parse_and_filter_number(part)

        return product
    
#Blue 
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else 1
            except ValueError:
                return 1

        # On utilise reduce pour éviter la boucle for
        parts = numbers.split(';')
        product = reduce(lambda x, y: x * parse_and_filter_number(y), parts, 1)

        return product
    
    # Troisième itération #

#Red
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else 1
            except ValueError:
                return 1

        # On utilise reduce pour éviter la boucle for
        parts = numbers.split(';')
        product = reduce(lambda x, y: x * parse_and_filter_number(y), parts, 1)

        return product
#Green
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else 1
            except ValueError:
                return None

        parts = numbers.split(';')
        product = 1
        for part in parts:
            number = parse_and_filter_number(part)
            if number is not None:
                product *= number
            else:
                return -1

        return product


#Blue
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        parts = numbers.split(';')
        product = reduce(lambda x, y: x * y if y is not None else x, (parse_and_filter_number(part) for part in parts), 1)

        return -1 if None in (parse_and_filter_number(part) for part in parts) else product
    
## Tests Structurelle ##
    # Premier test #
