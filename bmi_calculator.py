
import streamlit as st
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

def calculate_bmi(weight, height):
    """Calculate BMI based on weight (kg) and height (m)."""
    if height == 0:
        return 0
    return round(weight / (height ** 2), 2)

def categorize_bmi(bmi):
    """Categorize BMI based on WHO standards."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def draw_bmi_indicator(bmi):
    """Draw a semi-circle indicator for BMI."""
    # Normalize BMI to a scale of 0-100
    bmi_normalized = min(max(bmi, 0), 40) / 40 * 100
    color = 'green' if 18.5 <= bmi <= 24.9 else 'orange' if bmi < 18.5 or 25 <= bmi <= 29.9 else 'red'

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw={"projection": "polar"})
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)

    # Draw the semi-circle background
    wedges = [
        Wedge((0, 0), 1, 0, 120, facecolor='red'),
        Wedge((0, 0), 1, 120, 240, facecolor='green'),
        Wedge((0, 0), 1, 240, 360, facecolor='orange')
    ]
    for wedge in wedges:
        ax.add_patch(wedge)

    # Draw the BMI indicator
    theta = math.radians(bmi_normalized * 3.6)
    ax.plot([0, theta], [0, 0.9], color=color, linewidth=3)

    # Remove unnecessary details
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 1)

    st.pyplot(fig)

# Streamlit App
st.title("BMI Calculator with Indicator")

# User Inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.1, step=0.01)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    st.write(f"### Your BMI: {bmi}")
    st.write(f"### Category: {category}")
    st.write("### BMI Indicator:")
    draw_bmi_indicator(bmi)
