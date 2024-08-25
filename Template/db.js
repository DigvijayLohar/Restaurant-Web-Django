document.addEventListener('DOMContentLoaded', function() {
    const recipe = {
        "id": "2",
        "name": "Chicken Curry",
        "ingredients": [
            "1 kg chicken breast, cut into pieces",
            "2 onions, finely chopped",
            "4 cloves garlic, minced",
            "1 piece of ginger, minced",
            "2 tomatoes, chopped",
            "200 ml coconut milk",
            "2 tbsp curry powder",
            "1 tsp turmeric",
            "1 tsp cumin",
            "1 tsp coriander",
            "Salt",
            "Pepper",
            "Fresh cilantro, for garnish"
        ],
        "instructions": [
            "Heat oil in a large pan over medium heat.",
            "Add onions, garlic, and ginger; sauté until onions are golden brown.",
            "Add tomatoes and cook until they break down and form a thick paste.",
            "Stir in curry powder, turmeric, cumin, and coriander.",
            "Add chicken pieces and cook until they are browned on all sides.",
            "Pour in coconut milk and bring to a simmer.",
            "Reduce heat and let it simmer for about 20 minutes, or until chicken is cooked through and tender.",
            "Season with salt and pepper to taste.",
            "Garnish with fresh cilantro before serving."
        ],
        "preptime": 15,
        "cooktime": 30,
        "servings": 6,
        "difficulty": "medium",
        "cuisine": "Indian",
        "caloriesperserving": 350,
        "tags": [
            "spicy",
            "comfort food",
            "gluten-free"
        ],
        "img": "https://i.imgur.com/BOs3bPG.png",
        "rating": 4.7,
        "reviewcount": 200,
        "mealtype": "dinner"
    };

    document.getElementById('recipe-name').innerText = recipe.name;
    document.getElementById('recipe-img').src = recipe.img;
    document.getElementById('recipe-cuisine').innerText = recipe.cuisine;
    document.getElementById('recipe-mealtype').innerText = recipe.mealtype;
    document.getElementById('recipe-difficulty').innerText = recipe.difficulty;
    document.getElementById('recipe-servings').innerText = recipe.servings;
    document.getElementById('recipe-preptime').innerText = recipe.preptime;
    document.getElementById('recipe-cooktime').innerText = recipe.cooktime;
    document.getElementById('recipe-calories').innerText = recipe.caloriesperserving;
    document.getElementById('recipe-rating').innerText = recipe.rating;
    document.getElementById('recipe-reviewcount').innerText = recipe.reviewcount;
    document.getElementById('recipe-tags').innerText = recipe.tags.join(', ');

    const ingredientsList = document.getElementById('recipe-ingredients');
    recipe.ingredients.forEach(ingredient => {
        const li = document.createElement('li');
        li.innerText = ingredient;
        ingredientsList.appendChild(li);
    });

    const instructionsList = document.getElementById('recipe-instructions');
    recipe.instructions.forEach(instruction => {
        const li = document.createElement('li');
        li.innerText = instruction;
        instructionsList.appendChild(li);
    });
});
