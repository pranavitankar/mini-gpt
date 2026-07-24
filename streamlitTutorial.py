# import packages
import streamlit as st #frontend userinterface design
import numpy as np # it is use for scinetific calculation
import pandas as pd #it is used for data analysys

st.title("Hello , streamlit")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets go started")
st.write ("MY NMAE IS PRANAV")

#conditional logic
name = st.text_input("Enter Your Name :")
if st.button("Greet"):
        st.success(f"Hello {name}")
        st.text(f"Nice to meet you") 

#Displaying data and charts
df = pd.DataFrame(np.random.randn(10, 2), columns=["A","B"])
st.line_chart(df)
st.bar_chart(df)

#file uploading and caching
upload_file = st.file_uploader("Upload File", type="csv")
if upload_file:
        df = pd.read_csv(upload_file)
        st.dataframe(df)

#all the userinterface od Streamlit
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**,*Italic*, [Link](https://www.help4code.com/)")
st.text_area("Write your message")
st.number_input("pick a number",min_value=0,max_value=100)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["Apple","Banana","Mango"])
st.multiselect("choode toppings",["cheese","Tomato","Olives"])
st.radio("Pick one",["Option A","Option B"])
st.checkbox("I agree terms and condition")

#form code
with st.form("Login form"):
        username = st.text_input("username")
        password = st.text_input("password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
                st.success(f"welcome, {username}")

# check radio Button
import streamlit as st

option = st.radio("Choose View", ["Show Chart", "Show Table"])

if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

if st.checkbox("Show details"):
    st.info("Here are more details")

    # Media layout and advanced widgets
    st.sidebar.title("New Chat")
    st.image("")   # Replace with actual image path or URL
    st.video("")   # Replace with actual video path or URL

