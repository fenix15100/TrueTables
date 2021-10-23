import itertools
from prettytable import PrettyTable
import re


class StdObject(object):
    pass


class TruetableGenerator(object):
    def __init__(self, atoms=None, premises=None, ints=False):
        if not atoms:
            raise Exception('Atoms items are required')
        self.atoms = atoms
        self.premises = premises if premises is not None else []
        self.ints = ints

        # generate the sets of booleans for the atoms
        self.atoms_conditions = list(itertools.product([False, True],
                                                       repeat=len(atoms)))

        # Patron regex utilizado para localizar los atomos cuando se evaluen las premisas
        self.atoms_regex = re.compile(r'(?<!\w)(' + '|'.join(self.atoms) + ')(?!\w)')

    def evaluate(self, *args):
        # store atoms in an object context
        g = StdObject()
        for a, b in zip(self.atoms, args):
            setattr(g, a, b)

        # add object context to any base variables in self.phrases
        # then evaluate each
        eval_phrases = []
        for item in self.premises:
            item = self.atoms_regex.sub(r'g.\1', item)
            eval_phrases.append(eval(item))

        # add the bases and evaluated phrases to create a single row
        row = [getattr(g, b) for b in self.atoms] + eval_phrases

        # Mostrar valores de la tabla en formato (True/False) o (0/1)
        if self.ints:
            return [int(item) for item in row]
        else:
            return row

    def __str__(self):
        # Add header tables with all variables
        t = PrettyTable(self.atoms + self.premises)
        # Add row with values computed in Truetables
        for conditions_set in self.atoms_conditions:
            t.add_row(self.evaluate(*conditions_set))
        return str(t)


def main():

    atoms = input("Introduce los atomos del enunciado separados por comas:\n")
    try:
        atoms = atoms.split(',')
    except Exception as e:
        print("Atomos mal introducidos.!!")
        exit(1)

    premisas = input("Introduce las premisas y conclusion del enunciado separados por comas (usando los operadores "
                     "logicos de python):\n")
    try:
        premisas = premisas.split(',')
    except Exception as e:
        print("premisas mal introducidos.!!")
        exit(1)


    table = TruetableGenerator(atoms=atoms,
                               premises=premisas)
    print(table)


if __name__ == '__main__':
    main()
