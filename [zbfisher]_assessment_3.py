# Personal info
name = "Zian Fisher"
email = "zbfisher@ncat.edu"
hometown = "Charlotte, NC"
grad_semester = "Spring 2029"
major = "Computer Science"

# Academic data lists
current_courses = ["COMP 163", "MATH 131", "ENG 100", "HIST 106", "COMP 121", "GEEN 111"]
completed_courses = []
credit_hrs = [3, 4, 3, 3, 1, 1]
gpa_history = [4.0]

# Contact info tuples
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", 5, 22, 2006)

# Interest tracking sets
current_skills = {"Python basics", "JavaScript basics", "Java basics", "Problem solving", "Time management", "Data entry"}
skills_to_learn = {"C++", "Cybersecurity", "Game design", "Game programming"}
career_interests = {"Software development", "Game development"}
hobbies = {"Gaming", "Gardening", "Drawing"}
entertainment_backlog = {"One Piece", "Youtube"}

# Organizational mapping dictionaries
course_credits = {"COMP 163" : 3, "MATH 131" : 4, "ENG 100" : 3, "HIST 106" : 3, "COMP 121" : 1, "GEEN 111" : 1}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 131" : "Dr. Roop", "ENG 100" : "Prof. Rhodes", "HIST 106" : "Prof. Devoe", "COMP 121" : "Prof. Rhodes", "GEEN 111" : "Dr. Parrish"}
course_rooms = {"COMP 163" : "Gibbs 337", "MATH 131" : "Marteena 216", "ENG 100" : "Merrick 327", "HIST 106" : "N/A", "COMP 121" : "Graham 210", "GEEN 111" : "McNair 240"}
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
print(current_courses[1], "-", course_credits["MATH 131"], "credits -", course_professors["MATH 131"], "-", course_rooms["MATH 131"])
print(current_courses[2], "-", course_credits["ENG 100"], "credits -", course_professors["ENG 100"], "-", course_rooms["ENG 100"])
print(current_courses[3], "-", course_credits["HIST 106"], "credits -", course_professors["HIST 106"], "-", course_rooms["HIST 106"])
print(current_courses[4], "-", course_credits["COMP 121"], "credits -", course_professors["COMP 121"], "-", course_rooms["COMP 121"])
print(current_courses[5], "-", course_credits["GEEN 111"], "credits -", course_professors["GEEN 111"], "-", course_rooms["GEEN 111"])
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



