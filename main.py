file = open("cookbook.txt")
lines = file.readlines()

cook_book = {}

for line in lines:
    recipe_lines = line.strip().split('\n')
    recipe_name = recipe_lines[0]
    if len(recipe_lines) > 1:
        ingredient_count = int(recipe_lines[1])
    else:
        ingredient_count = 0

    ingredients = {}
    for line in recipe_lines[2:]:
        ingredient_parts = line.split(' | ')
        ingredient_name = ingredient_parts[0]
        ingredient_quantity = int(ingredient_parts[1])
        ingredient_unit = ingredient_parts[2]

        ingredients[ingredient_name] = {'': ingredient_quantity, '': ingredient_unit}

    cook_book[recipe_name] = {'': ingredient_count, '': ingredients}

print(cook_book,  sep='\n')