import streamlit as st
from user import User
from database import Database
from utils.notifications import send_notification

def main():
    st.title("Grievance Submission Form")

    with st.form(key='grievance_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        title = st.text_input("Title")
        description = st.text_area("Description")
        category = st.selectbox("Category", ["HR", "Facilities", "IT", "Other"])
        
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            user = User(name, email, title, description, category)
            if user.validate():
                db = Database()
                db.save_grievance(user)
                send_notification(user)
                st.success("Grievance submitted successfully!")
            else:
                st.error("Please fill in all fields correctly.")

if __name__ == "__main__":
    main()