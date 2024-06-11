"""_summary_
"""

from helpers.langchain_helper import generate_course_platform
from dotenv import load_dotenv
import streamlit as st
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()


st.title("langchain Testing")

course_name = st.sidebar.selectbox("select the course name", ("Python", "Flask", "Sanic", "LLMs", "GenAI"))

if course_name:
    print(f"runing for course {course_name}")
    result = generate_course_platform(course_name)
    print("result",result)
    result = f"Best platforms to learn {course_name} are:\n\n" + result
    st.text(result)
    