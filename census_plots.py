# Code for 'census_plots.py' file.
# Import necessary modules.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualise Data")
    st.subheader("Visualisation Selector")

    # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
    # Store the current value of this widget in a variable 'plot_list'.
    plot_list = st.multiselect("Select the Charts/Plots:", ('Count Plot', 'Box Plot', 'Pie Chart')) 

    # Display count plot using seaborn module and 'st.pyplot()' 
    if 'Count Plot' in plot_list:
        st.subheader("Count plot for distribution of records for unique workclass groups")
        plt.figure(figsize = (12, 5))
        sns.countplot(x = 'workclass', hue = 'income', data = census_df)
        st.pyplot()

    # Display pie plot using matplotlib module and 'st.pyplot()'
    if 'Pie Chart' in plot_list:
        st.subheader("Pie Chart")
        column = st.multiselect("Select the column for pie chart",('income', 'gender'))

        for i in column:
            pie_data = census_df[i].value_counts()
            plt.figure(figsize = (5, 5))
            plt.title(f"Distribution of records for different {i} groups")
            plt.pie(pie_data, labels = pie_data.index, autopct = '%1.2f%%', startangle = 30, explode = np.linspace(.01, .05, len(pie_data)))
            st.pyplot()

    # Display box plot using matplotlib module and 'st.pyplot()'
    if 'Box Plot' in plot_list:
        st.subheader("Box Plot for the Hours Worked Per Week")
        hue_columns = st.multiselect("Select the column for grouping the distribution of records in the boxplot",('income', 'gender'))

        for i in hue_columns:
            plt.figure(figsize = (12, 4))
            plt.title(f"Distribution of Hour Worked Per Week for different {i} groups")
            sns.boxplot(census_df['hours-per-week'], y = census_df[i])
            st.pyplot()