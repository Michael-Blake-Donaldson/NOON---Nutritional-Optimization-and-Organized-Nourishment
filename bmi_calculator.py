def calculate_bmi(weight_lbs, feet, inches, age, gender, activity_level):
    # Convert weight to kilograms (1 lb = 0.453592 kg)
    weight_kg = weight_lbs * 0.453592
    # Convert height to centimeters (1 foot = 30.48 cm, 1 inch = 2.54 cm)
    height_cm = (feet * 30.48) + (inches * 2.54)

    # Calculate BMI
    bmi = weight_kg / ((height_cm / 100) ** 2)

    # Calculate BMR (Basal Metabolic Rate) using Harris-Benedict equation based on gender
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:  # Female
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)

    # Adjust BMR for activity level
    activity_factors = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Extra active": 1.9,
    }
    calorie_needs = bmr * activity_factors.get(activity_level, 1.2)

    return bmi, calorie_needs
