import itertools
import os
import sys
from colorama import Fore, Back, Style, init as init_colorama
from prettytable import PrettyTable
import re
import numpy as np


class StdObject(object):
    pass


class TruetableGenerator(object):
    def __init__(self, atoms=None, premises=None):
        if not atoms:
            raise Exception('Atoms items are required')
        self.atoms = atoms
        self.premises = premises if premises is not None else []
        # generate the sets of booleans for the atoms
        self.atoms_conditions = list(itertools.product([False, True],
                                                       repeat=len(atoms)))

        # Patron regex utilizado para localizar los atomos cuando se evaluen las premisas
        self.atoms_regex = re.compile(r'(?<!\w)(' + '|'.join(self.atoms) + ')(?!\w)')

        # Generate Table
        self.table = None
        self._clean_rows = []
        self.generateTable()

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
        # save a copy of all rows tables before adding escaping code colours
        self._clean_rows.append(row)
        colorized_row = []
        # Colorize colums table
        for r in row:
            if r:
                colorized_row.append(f"{Back.GREEN}{r}{Back.RESET}")
            else:
                colorized_row.append(f"{Back.RED}{r}{Back.RESET}")

        return colorized_row

    def generateTable(self):

        # Add header tables with all variables
        t = PrettyTable(field_names=self.atoms + self.premises)
        # Add row with values computed in Truetables
        for conditions_set in self.atoms_conditions:
            t.add_row(self.evaluate(*conditions_set))
        self.table = t

    def analizeTable(self):
        interpretations = self._clean_rows
        # transpose (T) table for get list values of columns instead rows and get only premises+conclusion colums
        interpretations_trasposed = np.array(self._clean_rows).T.tolist()[len(self.atoms):]
        self.check1(interpretations)

    # si en todas las interpretaciones en que las premisas sean verdaderas y la conclusion es verdadera
    # el enunciado es valido y premisas consistentees.
    def check1(self,interpretations):
        for k,interpretation in enumerate(interpretations):
            interpretations[k] = interpretation[len(self.atoms):]

        print(interpretations)




    def __str__(self):
        return str(self.table)


def main():
    init_colorama()
    '''
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
    '''
    truetable = TruetableGenerator(atoms=['A','B'],
                                   premises=['not A','not B','not(A and B)'])
    print(truetable)

    truetable.analizeTable()


if __name__ == '__main__':
    main()
