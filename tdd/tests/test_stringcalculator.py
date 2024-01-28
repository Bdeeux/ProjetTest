from tdd.src.stringcalculator import StringCalculator


#Test que un paramètre vide retourne zéro : ""==0
def test_Add_ParamVide_ReturnZero():
    # arrange
    mon_param = ""
    mon_resultat = 0
    # act
    somme = StringCalculator.Add(mon_param)
    # assert
    assert somme == mon_resultat


def test_Add_ParamSeul_ReturnMeme():
    # arrange
    mon_param = "5"
    mon_resultat = 5
    # act
    somme = StringCalculator.Add(mon_param)
    # assert
    assert somme == mon_resultat


## PARTIE 1 ##

# Premier test
def test_Multiply():
    mon_param = "3;4;1"
    mon_resultat = 12  # La multiplication attendue est de 3 * 4 * 1 = 12
    produit = StringCalculator.Multiply(mon_param)
    assert produit == mon_resultat

# Deuxième test (On essaye de multiplier par un nombre négatif)
def test_Multiply_negative_numbers():
    assert StringCalculator.Multiply("-2;3") == -6

# Troisième test (On essaye de multiplier des lettres)
def test_Multiply_InvalidInput():
    assert StringCalculator.Multiply("2;3;abc;4") == -1

## PARTIE 2 ##

# Premier test structurelle (On test avec une entrée vide)
def test_Mutiply_Empty():
    assert StringCalculator.Multiply("") == 1

# Deuxième test structurelle (On test avec un délimitateur différent du ";")
def test_Multiply_DifferentSeparator():
    assert StringCalculator.Multiply("2,3,4", ",") == 24

# Troisième test structurelle (On test avec des nombres à virgules)
#def test_Multiply_DecimalNumbers():
    #assert StringCalculator.Multiply("2.5;3.5") == 8.75


