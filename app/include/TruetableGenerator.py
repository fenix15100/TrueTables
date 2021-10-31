import itertools
import re

class StdObject(object):
    pass

class TruetableGenerator(object):
    def __init__(self, atoms=None, premises=None):
        if not atoms:
            raise Exception('Atoms items are required')
        self.atoms = atoms
        self.premises = premises if premises is not None else []
        # generate the sets of booleans for the atoms
        self.atoms_conditions = list(itertools.product([True, False],
                                                       repeat=len(atoms)))

        # Patron regex utilizado para localizar los atomos cuando se evaluen las premisas
        self.atoms_regex = re.compile(r'(?<!\w)(' + '|'.join(self.atoms) + ')(?!\w)')

        # Generate Table
        self.table = []
        self.generatetable()

    def evaluate(self, *args):
        # store atoms in an object context
        g = StdObject()
        for a, b in zip(self.atoms, args):
            setattr(g, a, b)

        # add object context to any base variables in self.premises
        # then evaluate each
        eval_phrases = []
        for item in self.premises:
            item = self.atoms_regex.sub(r'g.\1', item)
            eval_phrases.append(eval(item))

        # add the atoms and evaluated premises to create a single row for print final table
        row = [getattr(g, b) for b in self.atoms] + eval_phrases
        self.table.append(row)

        return row

    def generatetable(self):
        # Add row with values computed in Truetables
        for conditions_set in self.atoms_conditions:
            self.evaluate(*conditions_set)

    def __str__(self):
        print(self.table)