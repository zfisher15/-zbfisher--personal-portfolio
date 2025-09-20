# Personal info
name = "Jordan Smith"
email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
grad_semester = "Spring 2028"
major = "Computer Science"

# Academic data lists
current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hrs = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

# Contact info tuples
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", 5, 22, 2006)

# Interest tracking sets
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# Organizational mapping dictionaries
course_credits = {"COMP 163" : 3, "MATH 150" : 3, "ENG 101" : 3, "HIS 105" : 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150" : "Dr. Lee", "ENG 101" : "Dr. Martinez", "HIS 105" : "Dr. Brown"}
course_rooms = {"COMP 163" : "M-Eric 300", "MATH 150" : "Marteena 201", "ENG 101" : "Crosby 121", "HIS 105" : "Crosby 210"}
monthly_budget = {"Food" : 450, "Entertainment" : 200, "Books" : 125, "Transportation" : 100}
study_hrs = {"Programming" : 10, "Math" : 8, "English" : 4, "History" : 3}
contact_directory = {"Mom" : "704-555-0199", "Roommate" : "336-555-7821", "Academic Advisor" : "336-334-5000"}

# Calculations
total_current_credits = sum(credit_hrs)
cumulative_gpa = f"{(sum(gpa_history) / len(gpa_history)):.2f}"
completed_courses_count = len(completed_courses)
total_study_hrs = study_hrs["Programming"] + study_hrs["Math"] + study_hrs["English"] + study_hrs["History"]
academic_load = total_study_hrs + sum(credit_hrs)
monthly_budget_total = monthly_budget["Food"] + monthly_budget["Entertainment"] + monthly_budget["Books"] + monthly_budget["Transportation"]
daily_food_budget = f"{monthly_budget["Food"] / 30:.1f}"
annual_budget = monthly_budget_total * 12
study_cost_per_hr = (monthly_budget["Books"] / total_study_hrs)
total_followers = instagram_info[2] + twitter_info[2]


print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student:", name, "| Email:", email)
print("From:", hometown, "| Graduating:", grad_semester)
print("Major:", major)
print()
print("=== ACADEMIC PROFILE ===")
print("Current Semester:", total_current_credits, "credits across", len(credit_hrs), "courses")
print("Cumulative GPA:", cumulative_gpa)
print("Weekly Study Time:", total_study_hrs, "hours")
print("Academic Investment:", f"${study_cost_per_hr:.1f}", "per study hour")
print()
print("Current Courses:")
print(current_courses[0], "-", course_credits["COMP 163"], "credits -", course_professors["COMP 163"], "-", course_rooms["COMP 163"])
print(current_courses[1], "-", course_credits["MATH 150"], "credits -", course_professors["MATH 150"], "-", course_rooms["MATH 150"])
print(current_courses[2], "-", course_credits["ENG 101"], "credits -", course_professors["ENG 101"], "-", course_rooms["ENG 101"])
print(current_courses[3], "-", course_credits["HIS 105"], "credits -", course_professors["HIS 105"], "-", course_rooms["HIS 105"])
print()
print("=== PERSONAL DEVELOPMENT ===")
print("Current Skills:", current_skills)
print("Learning Goals:", skills_to_learn)
print("Career Interests:", career_interests)
print("Skills Currently Have:", len(current_skills))
print("Skills Want to Learn:", len(skills_to_learn))
print()
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget["Food"]} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")
print()
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print("Social Media Presence:", total_followers, "followers across 2 platforms" )
print("Key Contacts:", len(contact_directory), "people in directory")
print()
print("=== LIFE STATISTICS ===")
print("Total Courses Completed:", len(completed_courses))
print("Current Academic Load:", academic_load, "weekly commitments")
print("Entertainment Backlog:", len(entertainment_backlog), "items")
print("Current Hobbies:", len(hobbies), "activities")
print("================================================================")
