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
    
# Deuxième itération (On essaye de multiplier des nombres négatifs) # 

#Red
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
    
    # Troisième itération (On essaye de multiplier des lettres) #

#Red
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else 1
            except ValueError:
                return 1

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
    # Premier test structurelle (On test si le paramètre est vide) #

#Red (Le test ne passe pas car le paramètre vide n'est pas géré)
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
    
    
#Green (Le test passe nous avons adapté la fonction)
    def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        # Si numbers est vide, renvoyer 1
        if not numbers:
            return 1

        parts = numbers.split(';')
        product = reduce(lambda x, y: x * y if y is not None else x, (parse_and_filter_number(part) for part in parts), 1)

        return -1 if None in (parse_and_filter_number(part) for part in parts) else product
    
#Blue (On utilise une liste pour que le code soit plus lisible)
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        # Si numbers est vide, renvoyer 1
        if not numbers:
            return 1

        parts = numbers.split(';')
        valid_numbers = [parse_and_filter_number(part) for part in parts]

        if None in valid_numbers:
            return -1

        product = 1
        for number in valid_numbers:
            if number is not None:
                product *= number

        return product


# Deuxième test structurelle (On test si le délimiteur est une virgule) #
#Red (Test de plusieur délimitateur)
    #def Multiply(numbers):
        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        # Si numbers est vide, renvoyer 1
        if not numbers:
            return 1

        parts = numbers.split(';')
        valid_numbers = [parse_and_filter_number(part) for part in parts]

        if None in valid_numbers:
            return -1

        product = 1
        for number in valid_numbers:
            if number is not None:
                product *= number

        return product

#Green (Le test de la mise en place de plusieurs délimiteurs passe)
    #def Multiply(numbers, delimiters=None):
        if delimiters is None:
            delimiters = [';']  # Utilisez le point-virgule comme délimiteur par défaut

        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        if not numbers:
            return 1

        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ';')  # Remplacez tous les délimiteurs par des point-virgules

        parts = numbers.split(';')
        valid_numbers = [parse_and_filter_number(part) for part in parts]

        if None in valid_numbers:
            return -1

        product = 1
        for number in valid_numbers:
            if number is not None:
                product *= number

        return product

#Blue (Meilleur lisibilité du code)
    #def Multiply(numbers, delimiters=None):
        if not numbers:
            return 1  # Retourne 1 si la chaîne de nombres est vide

        if delimiters is None:
            delimiters = [';']  # Utilisez le point-virgule comme délimiteur par défaut

        # Remplacez tous les délimiteurs par des point-virgules
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ';')

        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        parts = numbers.split(';')
        valid_numbers = [parse_and_filter_number(part) for part in parts]

        if None in valid_numbers:
            return -1

        product = 1
        for number in valid_numbers:
            if number is not None:
                product *= number

        return product

#Red (La test ne passe pas)
    #def Multiply(numbers, delimiters=None):
        if not numbers:
            return 1  # Retourne 1 si la chaîne de nombres est vide

        if delimiters is None:
            delimiters = [';']  # Utilisez le point-virgule comme délimiteur par défaut

        # Remplacez tous les délimiteurs par des point-virgules
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ';')

        def parse_and_filter_number(num_str):
            try:
                number = int(num_str)
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        parts = numbers.split(';')
        valid_numbers = [parse_and_filter_number(part) for part in parts]

        if None in valid_numbers:
            return -1

        product = 1
        for number in valid_numbers:
            if number is not None:
                product *= number

        return product
    

#Green (Le test passe)
    #def Multiply(numbers, delimiters=None):
        if delimiters is None:
            delimiters = [';']  # Utilisez le point-virgule comme délimiteur par défaut

        def parse_and_filter_number(num_str):
            try:
                number = float(num_str)  # Utilisez float pour prendre en charge les nombres décimaux
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        # Si numbers est vide, renvoyer 1
        if not numbers:
            return 1

        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ';')  # Remplacez tous les délimiteurs par des point-virgules

        parts = numbers.split(';')
        valid_numbers = [parse_and_filter_number(part) for part in parts]

        if None in valid_numbers:
            return -1

        product = 1
        for number in valid_numbers:
            if number is not None:
                product *= number

        return round(product, 2)

#Blue (On utilise reduce pour améliorer la qualité du code)
    #def Multiply(numbers, delimiters=None):
        if delimiters is None:
            delimiters = [';']  # Utilisez le point-virgule comme délimiteur par défaut

        def parse_and_filter_number(num_str):
            try:
                number = float(num_str)  # Utilisez float pour prendre en charge les nombres décimaux
                return number if -1000 <= number <= 1000 else None
            except ValueError:
                return None

        # Si numbers est vide, renvoyer 1
        if not numbers:
            return 1

        # Remplacez tous les délimiteurs par des point-virgules
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ';')

        parts = numbers.split(';')
        valid_numbers = [parse_and_filter_number(part) for part in parts]

        if None in valid_numbers:
            return -1

        # Utilisez reduce pour calculer le produit des nombres valides
        product = reduce(lambda x, y: x * y if y is not None else x, valid_numbers, 1)

        # Arrondir le produit à 2 décimales
        return round(product, 2)
