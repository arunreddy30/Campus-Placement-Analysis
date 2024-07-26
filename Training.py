import pandas as pd

# Sample data
data = pd.DataFrame({
    'Registration Number': ['20CSE0092'],
    'Name': ['Ashley Esparza'],
    'CGPA': [8.66],
    'Projects': [10],
    'Internships': [['UI Design']],
    'Courses': [['CSC Frontend', 'CSC Frontend', 'VLSI', 'Cloud Engineer']],
    'No_of_Certs': [4],
    'Certifications': [4],
    'LeetCode Score': [234],
    'Placement Status': ['Not Placed'],
    'Company Portfolio': [None],
    '10th Grade Percentage': [77],
    '12th Grade Percentage': [82],
    'CTC': ['6 LPA'],
    'IQ': [82],
    'Gender': ['Female'],
    'Skills': [['Java', 'Machine Learning', 'Web Development', 'Database Management', 'Data Analysis']],
    'Skill Score': [4]
})

# Define weights
role_weights = {
    'Software Engineer': 1.2,
    'Hardware Engineer': 1.5,
    'UI Design': 0.8,
    'Robotics': 1.3,
    'Business Management': 0.9,
    'ML/AI': 2.0,
    'Cloud Engineer': 1.7,
    'System Design': 1.4
}

stream_weights = {
    'CSC Frontend': 1.2,
    'CSC Backend': 1.5,
    'VLSI': 2.3,
    'Chip Design': 1.5,
    'ML Engineer': 1.8,
    'Cloud Engineer': 1.7,
    'System Design': 2.4
}

skill_weights = {
    'Python': 1.5,
    'Java': 1.2,
    'C++': 1.0,
    'Data Analysis': 1.8,
    'Machine Learning': 2.0,
    'Web Development': 1.5,
    'Database Management': 1.2,
    'Communication': 1.2
}

def calculate_intern_weights(internships):
    if isinstance(internships, str):  # Check if internships is a string
        internships = [internships]  # Convert string to list with a single element
    total_weight = sum(role_weights.get(role, 0) for role in internships)
    return total_weight

# Calculate intern weights for each row
data['InternWeights'] = data['Internships'].apply(calculate_intern_weights)

def calculate_skill_score(skills):
    if isinstance(skills, str):  # Check if skills is a string
        skills = ast.literal_eval(skills)  # Convert string to list
    total_weight = sum(skill_weights.get(skill, 0) for skill in skills)
    return total_weight

# Calculate skill score for each row
data['Skill Score'] = data['Skills'].apply(calculate_skill_score)

def calculate_course_weights(courses):
    if isinstance(courses, str):  # Check if courses is a string
        courses = ast.literal_eval(courses)  # Convert string to list
    total_weight = sum(stream_weights.get(stream, 0) for stream in courses)
    return total_weight



# Calculate course weights for each row
data['CourseWeights'] = data['Courses'].apply(calculate_course_weights)
