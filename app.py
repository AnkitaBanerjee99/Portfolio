import streamlit as st
from PIL import Image

# --- PROFILE PHOTO ---
'''image = Image.open("your_profile_photo.jpg")
st.image(image, width=150)'''

# --- NAME & SUMMARY ---
st.title("Your Full Name")
st.subheader("Summary")
st.write("""
A brief summary about yourself, your career interests, goals, and what makes you unique.
""")

# --- SOCIAL LINKS ---
st.markdown("""
*LinkedIn:* [Your LinkedIn](https://linkedin.com/in/your-profile)  
*GitHub:* [Your GitHub](https://github.com/your-username)  
*Twitter:* [Your Twitter](https://twitter.com/your-handle)  
*Email:* your.email@example.com
""")

# --- EDUCATION ---
st.subheader("Education")
st.write("""
*Degree Name* – University Name (Year - Year)  
Description or Achievements

*Another Degree* – College Name (Year - Year)  
Description
""")

# --- EXPERIENCE ---
st.subheader("Experience")
st.write("""
*Job Title* – Company Name (Year - Year)  
Description of role, responsibilities, and achievements.

*Internship* – Organization (Year)  
What you worked on, skills gained.
""")

# --- SKILLS ---
st.subheader("Skills")
st.write("""
- Skill 1
- Skill 2
- Skill 3
- Tools and Technologies: Python, SQL, Tableau, etc.
""")

# --- PROJECTS ---
st.subheader("Projects")
st.write("""
*Project Title*  
Short description, tools/technologies used. [GitHub Repo](https://github.com/your-username/project-repo)

*Another Project*  
Short description, purpose, outcome.
""")

# --- CERTIFICATIONS & ACHIEVEMENTS ---
st.subheader("Certifications & Achievements")
st.write("""
- Certification Name – Issued by (Year)
- Award or Achievement – Description
- Online Courses: Name of course – Platform (with link if available)
""")
