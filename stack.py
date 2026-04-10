class Stack:
    """
    Cette classe agit comme une 'coque de protection' (Wrapper).
    Elle transforme une liste ordinaire en une Pile sécurisée.
    """
    def __init__(self, items=None):
        # ÉTAPE 1 : On crée un espace de stockage interne (privé).
        # On ne veut pas que l'utilisateur manipule cet objet directement.
        if items is None:
            self._items = []
        else:
            self._items = list(items)

    def push(self, item):
        # ÉTAPE 2 : DÉLÉGATION de l'ajout.
        # La Stack ne sait pas 'gérer la mémoire', elle demande à la liste
        # interne d'ajouter l'objet à la fin (le sommet de la pile).
        self._items.append(item)

    def pop(self):
        # ÉTAPE 3 : DÉLÉGATION du retrait.
        # On demande à la liste de nous donner le DERNIER élément entré.
        # Cela garantit la règle LIFO (Last-In, First-Out).
        return self._items.pop()

    def __repr__(self) -> str:
        # ÉTAPE 4 : REPRÉSENTATION visuelle.
        # Affiche le contenu de façon lisible : Stack()
        return f"{type(self).__name__}({self._items})"