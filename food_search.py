import requests

def search_food(search_term):
    """
    Search for food items using the OpenFoodFacts API and return relevant nutritional information.
    :param search_term: The term to search for (e.g., "apple", "banana").
    :return: A list of food products with name, calories, protein, etc.
    """
    if not search_term.strip():
        return []  # Don't make an API call for empty or whitespace search terms

    search_term = search_term.strip()  # Remove leading/trailing whitespace
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={search_term}&search_simple=1&action=process&json=1&page_size=10"  # Limit to 10 results
    
    try:
        response = requests.get(url, timeout=30)  # Add timeout to prevent long waits
        response.raise_for_status()  # Raises HTTPError if the response code is not 200 (OK)
        
        data = response.json()
        products = data.get('products', [])
        
        # Extract relevant nutritional data for each product
        food_list = []
        for product in products:
            product_name = product.get('product_name', 'Unknown Product')
            calories = product.get('nutriments', {}).get('energy-kcal_100g', 'N/A')
            proteins = product.get('nutriments', {}).get('proteins_100g', 'N/A')
            carbs = product.get('nutriments', {}).get('carbohydrates_100g', 'N/A')
            fats = product.get('nutriments', {}).get('fat_100g', 'N/A')

            food_item = {
                'name': product_name,
                'calories': calories,
                'proteins': proteins,
                'carbs': carbs,
                'fats': fats,
            }
            food_list.append(food_item)
        
        return food_list

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return []  # Return an empty list if there's an error
