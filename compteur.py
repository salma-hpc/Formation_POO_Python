class ObjectCounter:
    num_instances = 0  #attribut d classeE (le compteur global)

    def __init__(self):
       # On remonte à la classe pour incrémenter le compteur général
        ObjectCounter.num_instances += 1