from ClassRecipe import Recipe

#from ClassRecipe import Recipe

# list of recipes to search
ListOfURLs = []


# class to contain the information for the recipes
# done

# create an object
pancakes = Recipe(
    'https://www.bbcgoodfood.com/recipes/best-ever-fluffy-american-pancakes-cherry-berry-syrup')

print(pancakes.nameOfRecipe)
print(pancakes.prepTime)
print(pancakes.cookTime)
print(pancakes.difficulty)
print(pancakes.servings)

for ingredient in pancakes.ingredients:
    print('\n'+ingredient)


for method in pancakes.methods:
    print('\n'+method)


# output on to a file


"""
#file location USERNAME/BBCDATA/recipes
#MAKE SURE YOU HAVE THE RIGHT FILE LOCATION OR IT WILL FAIL AND NOT WORK
with open('Data/recipes.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["nameOfRecipe", "prepTime", "cookTime", "difficulty", "servings", "INGREDIENTS", "METHODS"])
    writer.writerow([nameOfRecipe, prepTime, cookTime, difficulty, servings, ingredients[0], methods[0]])
"""
