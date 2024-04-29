from django.shortcuts import render

# Create your views here.

def home(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "info" : "It is a popular Canadian pastry, originating in Ottawa, Ontario. These iconic treats are hand-stretched pieces of fried dough, resembling the shape of a beaver's tail. They are often served hot and topped with various sweet toppings such as cinnamon sugar, chocolate hazelnut spread, or maple syrup."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "info": "Breakfast potatoes are a classic morning dish often served alongside eggs, bacon, or sausage. These hearty potatoes are typically diced or sliced and seasoned with herbs and spices like rosemary, paprika, or garlic powder before being pan-fried or roasted until golden brown and crispy."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "info": "Canadian Butter Tarts are a beloved sweet treat that originated in Canada, particularly in Ontario. These delectable pastries consist of a flaky pastry crust filled with a rich and gooey mixture made primarily from butter, sugar, and eggs. Some variations may also include ingredients like maple syrup, raisins, pecans, or walnuts, adding layers of flavor and texture to the filling"
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "info": "Montreal Smoked Meat is a flavorful and iconic deli meat that originated in Montreal, Quebec, Canada. It is made from beef brisket that has been cured with a blend of spices, including black pepper, coriander, garlic, and mustard seeds, and then smoked and steamed to perfection. The result is tender, juicy meat with a rich, smoky flavor and a slightly peppery and aromatic taste."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "info": "Nanaimo Bars are a decadent and indulgent dessert that originated in Nanaimo, British Columbia, Canada. These no-bake bars consist of three distinct layers: a crumbly base made from graham cracker crumbs, shredded coconut, and chopped nuts, a creamy custard-flavored filling, and a rich chocolate ganache topping."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "info": "Pâté Chinois is a comforting and hearty dish that has its roots in Quebec, Canada. Despite its name, which translates to 'Chinese pie', it is not of Chinese origin but rather a French-Canadian dish. Pâté Chinois consists of layers of ground beef (or sometimes other meats like pork or turkey), corn, and mashed potatoes. These layers are typically baked together in a casserole dish until the top is golden and crispy."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "info": "Pouding Chômeur, which translates to 'unemployed man's pudding', is a classic French-Canadian dessert that originated in Quebec. This indulgent dessert consists of a simple cake batter poured over a rich, sweet sauce made from butter, brown sugar, and cream. During baking, the cake batter rises to the top, creating a moist and fluffy cake layer, while the sauce forms a caramelized bottom layer."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "info":"Poutine is a quintessential Canadian dish that originated in the province of Quebec. It consists of crispy French fries topped with cheese curds and smothered in rich gravy. The combination of hot fries, squeaky cheese curds, and savory gravy creates a uniquely delicious and comforting flavor experience. Poutine has evolved over the years, with variations incorporating additional toppings such as pulled pork, bacon, or vegetables."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "info": "Rappie Pie is a traditional Acadian dish originating from the Maritime provinces of Canada, particularly Nova Scotia. This hearty and comforting casserole-like dish is made with grated potatoes, typically mixed with meat (such as chicken, pork, or seafood) and seasoned with onions, salt, and pepper."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "info": "Split pea soup is a hearty and nutritious dish that is enjoyed worldwide, but it has particularly strong roots in Canadian cuisine, where it is often associated with comfort and warmth, especially during colder months. The soup is made from dried split peas, typically green or yellow, which are simmered with vegetables such as onions, carrots, and celery, along with flavorful herbs and spices like thyme and bay leaves."
        },
    ]
    return render (request, 'index.html', {'meals': meals})
