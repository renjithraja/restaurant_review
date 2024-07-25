import streamlit as st
import pandas as pd
import pickle

# Load the trained model from the pickle file
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the Streamlit app
st.title("Restaurant Review Recommendation System")

# Input fields for user to enter the required features
review = st.text_input("Review", "Enter your review here...")
rating = st.number_input("Rating", min_value=1, max_value=5, step=1)
location = st.text_input("Location", "Enter the location...")
food_type = st.text_input("Food Type", "Enter the food type...")
veg_non_veg = st.selectbox("Veg or Non-Veg", ["Veg", "Non-Veg"])
taste_level = st.text_input("Taste Level", "Enter the taste level...")
age_category = st.text_input("Age Category", "Enter the age category...")
price = st.number_input("Price", min_value=0.0, step=0.1)
strength = st.number_input("Strength", min_value=1, step=1)

# Button to make a prediction
if st.button("Predict Restaurant"):
    # Check if the inputs are valid
    if review and rating and location and food_type and veg_non_veg and taste_level and age_category and price and strength:
        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'Review': [review],
            'Rating': [rating],
            'Location': [location],
            'Food Type': [food_type],
            'Veg or Non-Veg': [veg_non_veg],
            'Taste Level': [taste_level],
            'Age Category': [age_category],
            'Price': [price],
            'Strength': [strength]
        })

        # Make a prediction using the loaded model
        prediction = model.predict(input_data)

        # Display the predicted restaurant name
        st.write(f"Recommended Restaurant: {prediction[0]}")
    else:
        st.write("Please enter all the required fields to get a recommendation.")
