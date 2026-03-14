import streamlit as st
import sqlite3
import pandas as pd

# Database connection
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    age INTEGER,
    place TEXT,
    gender TEXT,
    state TEXT,
    skillset TEXT
)
""")
conn.commit()

st.set_page_config(page_title="Student Management System", layout="wide")

st.title("🎓 Student Management System")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Add Student", "View Students"]
)

# ---------------- DASHBOARD ----------------

if menu == "Dashboard":

    st.subheader("📊 Dashboard")

    df = pd.read_sql("SELECT * FROM students", conn)

    col1, col2 = st.columns(2)

    col1.metric("Total Students", len(df))

    if len(df) > 0:
        state_counts = df["state"].value_counts()
        st.bar_chart(state_counts)

# ---------------- ADD STUDENT ----------------

elif menu == "Add Student":

    st.subheader("➕ Add Student")

    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", 18, 60)
    place = st.text_input("Place")

    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"]
    )

    state = st.selectbox(
        "State",
        ["Andhra Pradesh", "Telangana", "Karnataka", "Tamil Nadu"]
    )

    skillset = st.multiselect(
        "Skills",
        ["Python", "Django", "HTML", "CSS", "JavaScript", "SQL"]
    )

    if st.button("Add Student"):

        skills = ",".join(skillset)

        cursor.execute("""
        INSERT INTO students
        (name,email,age,place,gender,state,skillset)
        VALUES (?,?,?,?,?,?,?)
        """, (name,email,age,place,gender,state,skills))

        conn.commit()

        st.success("Student Added Successfully")

# ---------------- VIEW STUDENTS ----------------

elif menu == "View Students":

    st.subheader("📋 Student List")

    df = pd.read_sql("SELECT * FROM students", conn)

    search = st.text_input("Search Student")

    if search:
        df = df[df["name"].str.contains(search, case=False)]

    st.dataframe(df)

    if len(df) > 0:

        student_id = st.number_input("Enter Student ID to Delete", step=1)

        if st.button("Delete Student"):
            cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
            conn.commit()
            st.success("Student Deleted")