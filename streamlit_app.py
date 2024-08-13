import streamlit as st

st.title("Kerry's Calorie Helper")

# Get calories per 100g from user input
calories_per_100g = float(st.number_input(label="Calories per 100g", value=200))

# Select amount of grams to calculate calories for
amount_of_grams = int(st.slider(label="Amount of Grams", min_value=1, max_value=3000, value=25))

# Calculate calories based on the formula: (calories_per_100g * amount_of_grams) / 100
calories = round((calories_per_100g * amount_of_grams) / 100)

# Display result to user
st.write(f"{amount_of_grams}g: **{calories}** calories")

# Section for calculating fractions of total calorie and weight
fractions = ["1/2", "1/3", "1/4", "1/5", "1/6", "1/7", "1/8", "1/9"]

for f in fractions:
    num, denom = map(int, f.split('/'))
    fraction_weight = round(amount_of_grams / denom * num)
    fraction_calories = round(calories / denom * num)

    # Display result to user
    st.write(f"{f} of serving: **{fraction_weight}g** | Calories: {fraction_calories}")