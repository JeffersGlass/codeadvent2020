import re
import logging
from copy import deepcopy

logging.basicConfig(level=logging.INFO)

pattern = re.compile(r'(.+)\(contains (.+)\)')

with open('input.txt', 'r') as infile:
    inputData = [re.search(pattern, line.strip()).group(1,2) for line in infile]
    recipies = [({i for i in data[0].split(' ') if i != ''}, {a.strip() for a in data[1].split(',')}) for data in inputData]

allIngredients = set().union(*[r[0] for r in recipies])

allergenPairs = list()
allAllergens = list(set().union(*[r[1] for r in recipies]))
logging.info(f"Looking for {len(allAllergens)} allergens in {len(allIngredients)} ingredients")

allergenCouldBeIn = dict()

for a in allAllergens:
    allergenCouldBeIn[a] = allIngredients.intersection(*[r[0] for r in recipies if a in r[1]])
    logging.debug(f"{a} could be in {allergenCouldBeIn[a]}")

while len(allergenPairs) < len(allAllergens):
    toRemove = list()
    for a in allergenCouldBeIn:
        ingredients = allergenCouldBeIn[a]
        if len(allergenCouldBeIn[a]) == 1:
            onlyIngredient = list(ingredients)[0]
            logging.debug(f"{a} can only be in {onlyIngredient}")
            allergenPairs.append((a, onlyIngredient))
            for other in allergenCouldBeIn:
                allergenCouldBeIn[other].discard(onlyIngredient)
            toRemove.append(a)
    for t in toRemove:
        allergenCouldBeIn.pop(t, None)

#Print the final ingredient/allergen matches for examiniation
formatString = "{: <15}{: <15}"
logging.debug(formatString.format("Ingredient", "Allergen"))
for p in allergenPairs:
    logging.debug(formatString.format(p[0], p[1]))

goodIngredients = {i for i in allIngredients if not any([True if i == p[1] else False for p in allergenPairs])}
logging.debug(f"Non-allergenic ingredients: {goodIngredients}")

#Use the recipies list to its unmodified form.
origRecipies = [({i for i in data[0].split(' ') if i != ''}, {a.strip() for a in data[1].split(',')}) for data in inputData]
totalGoodIngredients = sum([1 if i in goodIngredients else 0 for r in origRecipies for i in r[0]])
print(f"Solution to part 1 is: {totalGoodIngredients}")
print("Solution to part 2 is: ", end = "")
print(','.join([p[1] for p in sorted(allergenPairs, key=lambda x:x[0])]))