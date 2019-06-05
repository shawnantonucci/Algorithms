#!/usr/bin/python

import math

recipe1 = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients1 = { 'milk': 132, 'butter': 48, 'flour': 51 }

def recipe_batches(recipe, ingredients):
    batches = 0
    complete = False
    try:
        while not complete:
            is_less = False
            for key in recipe.keys():
                ingredients[key] -= recipe[key]
                if ingredients[key] == 0:
                    complete = True
                elif ingredients[key] < 0:
                    complete = True
                    is_less = True
            if not is_less:
                batches += 1
    except KeyError:
        pass
    return batches


print(recipe_batches(recipe1, ingredients1))
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
