from bs4 import BeautifulSoup
import requests

subStringURL = 'https://www.bbcgoodfood.com/recipes/'


class Recipe:

    # list of ID, name, type, description, ingredients, healthy, price,
    """
    def __init__(self, nameOfRecipe, prepTime, cookTime, difficulty, servings, ingredients, methods):
        self.nameOfRecipe = nameOfRecipe
        self.prepTime = prepTime
        self.cookTime = cookTime
        self.difficulty = difficulty
        self.servings = servings
        self.ingredients = ingredients
        self.methods = methods
    """

    def __init__(self, URL):
        nameOfRecipe = ''
        prepTime = ''
        cookTime = ''
        difficulty = ''
        servings = ''

        listOfIngredients = []
        listOfMethods = []

        if (checkWebsite):
            source = requests.get(URL).text
            soup = BeautifulSoup(source, 'lxml')

            # Adds each section to a list on html
            sectionList = []
            sectionList.append(
                soup.find('section', class_="header header--masthead post__header mb-lg"))
            sectionList.append(
                soup.find('section', class_="recipe__ingredients col-12 mt-md col-lg-6"))
            sectionList.append(
                soup.find('section', class_="recipe__method-steps mb-lg col-12 col-lg-6"))

            # ###############SECTION 0 ######################

            # #RECIPE NAME
            recipe = soup.find('h1')
            nameOfRecipe = recipe.text

            uls = sectionList[0].find(
                'ul', class_="header__row header__planning mb-xxs list list--horizontal")

            # List for timing
            listOfLi = []
            for li in uls:
                listOfLi.append(li)

            times = listOfLi[0].find('ul')

            # First time is prep and 2nd is cook
            listOfTimes = []
            for li in times:
                listOfTimes.append(li.find('time').text)

            # LIST OF FIRST SECTION
            prepTime = listOfTimes[0]
            cookTime = listOfTimes[1]

            difficulty = listOfLi[1].text
            servings = listOfLi[2].text

            # ###############SECTION 1 ######################

            ul2 = sectionList[1].find('ul')

            for li in ul2:
                listOfIngredients.append(li.text)

            # ###############SECTION 2 ######################

            ul3 = sectionList[2].find('ul')

            for li in ul3:
                listOfMethods.append(li.p.text)

            self.nameOfRecipe = nameOfRecipe
            self.prepTime = prepTime
            self.cookTime = cookTime
            self.difficulty = difficulty
            self.servings = servings
            self.ingredients = listOfIngredients
            self.methods = listOfMethods


def checkWebsite(URL):
    if(subStringURL in URL):
        return True
    else:
        print("Invalid website - please check the substring url for information")
        return False


def getNameOfRecipe(self):
    return self.nameOfRecipe


"""

    def get_recipe_id(self):
        return self.recipe_id

    def get_recipe_name(self):
        return self.recipe_name

    def get_ingredients(self):
        return self.ingredients

    def get_method(self):
        return self.method

    def get_chef_name(self):
        return self.chef_name

    def get_meal_type(self):
        return self.meal_type

    def get_region(self):
        return self.region

    def get_cost(self):
        return self.cost



    def set_recipe_id(self, recipe_id):
        self.recipe_id = recipe_id

    def set_recipe_name(self, recipe_name):
        self.recipe_name = recipe_name

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def set_method(self, method):
        self.method = method

    def set_chef_name(self, chef_name):
        self.chef_name = chef_name

    def set_meal_type(self, meal_type):
        self.meal_type = meal_type

    def set_region(self, region):
        self.region = region

    def set_cost(self, cost):
        self.cost = cost




    def edit_recipe(self):
        pass

    def delete_recipe(self):
        pass




"""
