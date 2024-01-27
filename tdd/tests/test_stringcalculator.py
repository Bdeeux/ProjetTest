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

def test_Add_ParamAlphabet_ReturnZero():
    # arrange
    alphabet = "a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z"
    mon_resultat = 0
    # act
    somme = StringCalculator.Add(alphabet)
    # assert
    assert somme == mon_resultat

def test_Add_ParamNegativeNumber_ReturnNegativeNumber():
    # arrange
    mon_param = "5;-10;15"
    mon_resultat = 10  # La somme attendue est de 10 (5 + (-10) + 15)
    # act
    somme = StringCalculator.Add(mon_param)
    # assert
    assert somme == mon_resultat

def test_Multiply():
    # arrange
    mon_param = "3;4;1;1001"
    mon_resultat = 12  # La multiplication attendue est de 3 * 4 * 1 = 12
    # act
    produit = StringCalculator.Multiply(mon_param)
    # assert
    assert produit == mon_resultat