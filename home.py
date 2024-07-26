import streamlit as st
import pandas as pd
import pickle
from Training import calculate_course_weights
from Training import calculate_intern_weights
from Training import calculate_skill_score





# Main function to predict and display results
def predict_and_display(test_data):
    # Load the trained model
    with open('/home/ashiqarch/Documents/Placed/model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    test_df = pd.DataFrame(test_data)
    test_df['InternWeights'] = test_df['Internships'].apply(calculate_intern_weights)
    test_df['CourseWeights'] = test_df['Courses'].apply(calculate_course_weights)
    test_df['SkillScore'] = test_df['Skills'].apply(calculate_skill_score)

    # Extract features for prediction
    features = ['CGPA', 'LeetCode Score', 'Projects', 'Certifications', 'No_of_Certs', 
                '10th Grade Percentage', '12th Grade Percentage', 'InternWeights', 
                'CourseWeights', 'IQ', 'Gender', 'SkillScore']
    test_features = test_df[features]

    # Predict placement status for test data
    test_predictions = model.predict(test_features)

    if test_predictions == 0:
        st.write("Better luck next time!")
    else:
        st.write("Predicted Placement Status for Test Data:", test_predictions[0])
        test_skill_score = test_df['SkillScore'].iloc[0]
        st.write("Skill Score:", test_skill_score)
        st.write("Skill Improvement Suggestions:", suggest_skill_improvements(test_skill_score))
        placement_likelihood = likelihood_of_placement(test_skill_score)
        st.write("Likelihood of Placement:", placement_likelihood)
        st.write("Suggested Companies:", suggest_companies(placement_likelihood))

# Define function to suggest skill improvements
def suggest_skill_improvements(skill_score):
    suggestions = []
    if skill_score <= 2:
        suggestions.append("Improve your skills: ML")
    if 'Python' not in test_data['Skills'][0]:
        suggestions.append("Learn Python")
    if 'Java' not in test_data['Skills'][0]:
        suggestions.append("Learn Java")
    return suggestions

# Define function to determine likelihood of placement
def likelihood_of_placement(skill_score):
    if skill_score <= 2:
        return "Regular"
    elif skill_score <= 4:
        return "Dream"
    else:
        return "Super Dream"

# Function to suggest companies based on likelihood of placement
def suggest_companies(placement_likelihood):
    if placement_likelihood == "Regular":
        return ["IBM", "CodeVault", "Volvo"]
    elif placement_likelihood == "Dream":
        return ["Altair", "ALE", "Intel", "Zomato"]
    else:
        return ["AMD", "Marvell", "JP Morgan", "Uber"]

# Test data
test_data = {
    'Registration Number': ['20CSE0092'],
    'Name': ['Ashley Esparza'],
    'CGPA': [9.66],
    'Projects': [10],
    'Internships': [['UI Design']],  
    'Courses': [['CSC Frontend', 'VLSI', 'Cloud Engineer']],  
    'No_of_Certs': [4],
    'Certifications': [4],
    'LeetCode Score': [234],
    '10th Grade Percentage': [57],
    '12th Grade Percentage': [82],
    'IQ': [85],  
    'Gender': [1],
    'Skills': [['Data Analysis']],
}

# Streamlit UI
st.title("Placement Predictor")
st.header("Predictor")
st.write("Fill in the details below to predict placement status.")

# User input form
with st.form(key='prediction_form'):
    test_cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01, value=9.66)
    test_projects = st.number_input("Projects", min_value=0, step=1, value=10)
    test_internships = st.text_input("Internships (comma-separated)", value='UI Design')
    test_courses = st.text_input("Courses (comma-separated)", value='CSC Frontend, VLSI, Cloud Engineer')
    test_no_of_certs = st.number_input("Number of Certifications", min_value=0, step=1, value=4)
    test_leetcode_score = st.number_input("LeetCode Score", min_value=0, step=1, value=234)
    test_10th_grade_percentage = st.number_input("10th Grade Percentage", min_value=0, max_value=100, step=1, value=57)
    test_12th_grade_percentage = st.number_input("12th Grade Percentage", min_value=0, max_value=100, step=1, value=82)
    test_iq = st.number_input("IQ", min_value=0, step=1, value=85)
    test_gender = st.radio("Gender", ["Male", "Female"])
    test_skills = st.text_input("Skills (comma-separated)", value='Data Analysis')

    submitted = st.form_submit_button("Predict")

if submitted:
    test_data = {
        'CGPA': [test_cgpa],
        'Projects': [test_projects],
        'Internships': [test_internships.split(",")],
        'Courses': [test_courses.split(",")],
        'No_of_Certs': [test_no_of_certs],
        'Certifications': [test_no_of_certs],
        'LeetCode Score': [test_leetcode_score],
        '10th Grade Percentage': [test_10th_grade_percentage],
        '12th Grade Percentage': [test_12th_grade_percentage],
        'IQ': [test_iq],
        'Gender': [1 if test_gender == "Male" else 0],
        'Skills': [test_skills.split(",")],
    }
    predict_and_display(test_data)
