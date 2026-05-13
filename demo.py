# Name: demo.py
# Date: 5/12/26
# Author: Alex Vu

import cmath 
import math
# import plotly.express as px

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def calculations():
    # [mils pk-pk, degrees]
    REFERENCE_VIBRATION = cmath.rect(5.6, math.radians(135))
    RESPONSE_VECTOR = cmath.rect(3.3, math.radians(238))

    TRIAL_WEIGHT = cmath.rect(74, math.radians(315))

    T_VECTOR = RESPONSE_VECTOR - REFERENCE_VIBRATION

    INFLUENCE_COEFFICIENT = TRIAL_WEIGHT / T_VECTOR
    HEAVY_SPOT = REFERENCE_VIBRATION * INFLUENCE_COEFFICIENT
    CORRECTION_WEIGHT = -HEAVY_SPOT
    
    AMPLITUDE = abs(CORRECTION_WEIGHT)
    ANGLE = math.degrees(cmath.phase(CORRECTION_WEIGHT)) % 360

    return REFERENCE_VIBRATION, RESPONSE_VECTOR, T_VECTOR, CORRECTION_WEIGHT, AMPLITUDE, ANGLE

def scatter():
   
    REFERENCE_VIBRATION, RESPONSE_VECTOR, T_VECTOR, CORRECTION_WEIGHT, AMPLITUDE, ANGLE = calculations()

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[0,abs(REFERENCE_VIBRATION)],
        theta=[0, math.degrees(cmath.phase(REFERENCE_VIBRATION)) % 360],
        mode="lines+markers",
        name="Original Vibration (O)",
    ))

    fig.add_trace(go.Scatterpolar(
        r=[0,abs(RESPONSE_VECTOR)],
        theta=[0, math.degrees(cmath.phase(RESPONSE_VECTOR)) % 360],
        mode="lines+markers",
        name="Response Vibration (O+T)"
    ))

    fig.add_trace(go.Scatterpolar(
        r=[abs(REFERENCE_VIBRATION), abs(RESPONSE_VECTOR)],
        theta=[(math.degrees(cmath.phase(REFERENCE_VIBRATION)) % 360), 
               (math.degrees(cmath.phase(RESPONSE_VECTOR)) % 360)],
        mode="lines+markers",
        name="T Vector"
    ))

    st.metric(label="Alex Vu",  value="Correction Weight Calculation")

    st.text_area(label="Description", value="I used Plotly to make an " \
    "interactive polar plot for a sample vibration analysis. Hover over vector " \
    "endpoints to see amplitude and angle." \
    " The full GitHub repository of my work is available upon request.")
    st.plotly_chart(fig)

    
    st.metric(label="CW", label_visibility="hidden", value="Correction Weight")

    col1, col2 = st.columns(2)
    col1.metric("Correction Weight", f"{AMPLITUDE:.2f} oz-in", border=True)
    col2.metric("Placement Angle", f"{ANGLE:.1f}°", border=True)

def main():
    scatter()

if __name__ == "__main__":
    main()