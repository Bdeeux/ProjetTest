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