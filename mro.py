# LA HIÉRARCHIE DU DIAMANT 

class A:
    def method(self):
        print("A.method()")

class B(A):
    # B redéfinit la méthode de A
    def method(self):
        print("B.method()")

class C(A):
    # C redéfinit aussi la méthode de A
    def method(self):
        print("C.method()")

class D(B, C):
    # D n'a pas de méthode propre, elle doit choisir entre ses parents.
    # Selon la règle du MRO : c'est le parent de GAUCHE qui gagne.
    pass