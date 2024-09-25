import scipy.stats
import streamlit as st
import time

st.header('Tossing a Coin')

# Unique key for the first slider
number_of_trials = st.slider('Number of trials?', 1, 1000, 10, key="slider_1")
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')

chart = st.line_chart([0.5])

def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')
