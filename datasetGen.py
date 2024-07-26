import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_student_data(num_students, department, grade_10_range=(60, 100), grade_12_range=(60, 100)):
    data = []
    for i in range(num_students):
        reg_no = f'20{department}{i+1:04d}'  # Example: 20CSE0001
        name = fake.name()
        cgpa = round(random.uniform(6.0, 10.0), 2)
        projects = random.randint(1, 10)
        
        # Generate internships as a list of roles
        internships = []
        num_internships = random.randint(1, 3)
        for _ in range(num_internships):
            role = random.choice(['Software Engineer', 'Hardware Engineer', 'UI Design', 'Robotics', 
                                  'Business Management', 'ML/AI', 'Cloud Engineer', 'System Design', 'Chip Design', 'ML Engineer'])
            internships.append(role)
        
        # Generate courses as a list of streams
        courses = []
        num_courses = random.randint(1, 4)
        for _ in range(num_courses):
            stream = random.choice(['CSC Frontend', 'CSC Backend', 'VLSI', 'Chip Design', 
                                    'ML Engineer', 'Cloud Engineer', 'System Design'])
            courses.append(stream)
        
        certifications = random.randint(0, 10)
        leetcode_score = random.randint(0, 500)
        
        # Adjust placement probability based on grade percentages
        grade_10_percentage = random.randint(grade_10_range[0], grade_10_range[1])
        grade_12_percentage = random.randint(grade_12_range[0], grade_12_range[1])
        placement_probability = 0.7 if grade_10_percentage >= 80 and grade_12_percentage >= 85 else 0.3
        placement_status = 'Placed' if random.random() < placement_probability else 'Not Placed'
        
        company_portfolio = random.choice(['DREAM', 'SUPER DREAM', 'REGULAR']) if placement_status == 'Placed' else 'None'
        
        ctc = random.choice(['4 LPA', '6 LPA', '8 LPA', '10 LPA', '15 LPA', '20 LPA', '25 LPA', '30 LPA',
                             '40 LPA', '50 LPA', '60 LPA', '70 LPA', '80 LPA', '90 LPA', '1 CR LPA'])
        if cgpa >= 8.5 and leetcode_score > 150 and grade_10_percentage >= 85 and grade_12_percentage >= 85:
            ctc = random.choice(['50 LPA', '60 LPA', '70 LPA', '80 LPA', '90 LPA', '1 CR LPA'])
        
        # Add IQ and Gender features
        iq = random.randint(80, 150)
        gender = random.choice(['Male', 'Female'])
        
        # Add Skills and Skill Score features
        skills = ['Python', 'Java', 'C++', 'Data Analysis', 'Machine Learning', 'Web Development', 'Database Management', 'Communication']
        num_skills = random.randint(1, 5)
        student_skills = random.sample(skills, num_skills)
        skill_score = random.randint(1, 10)
        
        data.append({
            'Registration Number': reg_no,
            'Name': name,
            'CGPA': cgpa,
            'Projects': projects,
            'Internships': internships,
            'Courses': courses,
            'No_of_Certs' : num_courses,
            'Certifications': certifications,
            'LeetCode Score': leetcode_score,
            'Placement Status': placement_status,
            'Company Portfolio': company_portfolio,
            '10th Grade Percentage': grade_10_percentage,
            '12th Grade Percentage': grade_12_percentage,
            'CTC': ctc,
            'IQ': iq,
            'Gender': gender,
            'Skills': student_skills,
            'Skill Score': skill_score
        })
    return data

# Generate data for CSE, ECE, and EEE students combined
total_students = 1000
cse_students = generate_student_data(total_students//3, 'CSE')
ece_students = generate_student_data(total_students//3, 'ECE')
eee_students = generate_student_data(total_students//3, 'EEE')

# Combine all students' data
all_students = cse_students + ece_students + eee_students
random.shuffle(all_students)  

# Convert to DataFrame
df = pd.DataFrame(all_students)

df.to_csv('all_students_data.csv', index=False)

print("Data generation complete.")
