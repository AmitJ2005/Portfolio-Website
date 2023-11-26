from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Amit resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Amit Jaishwal"
PAGE_ICON = "📊"
NAME = "Amit Jaishwal"
DESCRIPTION = """
Data Science Enthusiast | Aspiring Data Scientist
"""
EMAIL = "amitjaisawal0123@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/amit-jaishwal-7abb7b288/",
    "GitHub": "https://github.com/AmitJ2005",
}

certificate_links = {
    "📜 Crash Course in Machine Learning – Nov 2023": "https://drive.google.com/file/d/1Ku6ofDyY6GtV0Z0JiaCEIzpmMl1_vxs2/view",
    "📜 Data Visualization With Power BI": "https://drive.google.com/file/d/1RgNFd-Gaz5kwIxzQwzSDmjmtkCi-6t5a/view",
    "📜 Data Analysis using Excel": "https://drive.google.com/file/d/13ktma5DQT_14mA9X_QLor9PJn0p7i3ZH/view",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(f"{NAME}  {DESCRIPTION}")
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience")
st.write("---")
# 1st experience
st.write("👨‍💻", "**Data-Science-Virtual-Experience –BCG X**")
st.write(
    """
  - Led the project, collaborated with the client to formulate data science problems and develop a roadmap for successful execution.
  - Conducted in-depth exploratory data analysis to verify hypotheses, identify key findings, and suggest data augmentation sources.
  - Provided valuable insights into potential cost savings for the client through the implementation of the churn model, contributing to the project's success.
"""
)
st.write('\n')
# 2nd experience
st.write("👨‍💻"," **Data Visualization: Empowering Business with Effective Insights - Tata Group**")
st.write(
"""
  - Contributed to data visualization projects, providing valuable insights for business decisions.
  - Worked with Power BI and other visualization tools to create compelling data representations.
"""
)
st.write('\n')
st.write( "👨‍💻","**Power BI Virtual Case Experience – PWC**")
st.write(
"""
  - Participated in a virtual case experience, gaining hands-on experience with Power BI.
  - Developed data dashboards and reports to address real-world business scenarios.
"""
)

st.write('\n')
st.subheader("Qualifications")
st.write("---")
st.write(
    """
- 🎓 **degree** 
  - BSc in Data Science | Mumbai University | 2021-2024
"""
)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write("---")

for cert_name, cert_link in certificate_links.items():
    st.markdown(f"{cert_name}  <span style='float:right;'>[View Certificate]({cert_link})</span>", unsafe_allow_html=True)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write("---")
st.write(
    """
- 👩‍💻 **Programming: Python, R, Linux**
- 📊 **Data Analysis: Excel, NumPy, Pandas**
- 📊 **Data Visualization: Power BI, Matplotlib, Seaborn**
- 🤖 **Machine Learning: scikit-learn**
- 🧠 **Deep Learning: Tensorflow**
- 🗃️ **Databases: SQL, SQLite**
- 🌐 **Web development: Flask, HTML, CSS**
- ☁️ **Model deployment: streamlit, Heroku, AWS, Digital Ocean**
- 🔄 **Version Control: Git and GitHub**
"""
)

# --- PROJECTS ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- Project 1
st.write("🚀", "**Stock Market Chatbot (Self-idea Project)**")
st.write("November - Present")
st.write(
    """
- Developed a real-time stock market chatbot with data scraping and NLP techniques.
- Integrated machine learning models for intent recognition and Spacy for Named Entity Recognition.
- Established a PostgreSQL database for efficient data storage and retrieval.
- Deployed the chatbot on Streamlit with a user-friendly Flask-based web interface.
"""
)

# --- Project 2
st.write('\n')
st.write("🚀", "**College Canteen Attendance Web App (Self-idea Project)**")
st.write("September - October")
st.write(
    """
- Designed and developed a web application for tracking student attendance in the college canteen.
- Utilized Python, Streamlit, and SQLite to create a user-friendly interface.
- Implemented features for attendance recording and reporting.
"""
)

# --- Project 3
st.write('\n')
st.write("🚀", "**Spam Message Classifier**")
st.write("September - October")
st.write(
    """
- Built a machine learning model to classify text messages as spam or not.
- Utilized natural language processing techniques and scikit-learn.
- Achieved high accuracy in message classification.
""")
