import pandas as pd
import streamlit as st
import time

st.title('Startup Dashboard')
st.header('I am Learning Streamlit')
st.subheader('Salman Khan!')

st.write('This is a normal text')

st.markdown("""
### My favourite Movies
- Race 3
- Humshakals
- Housefull
""")

st.code("""
def foo(input):
    return foo**2

x = foo(2)
""")

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '-3%')

st.json({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.image('edinburgh.jfif')

st.sidebar.title('Sidebar ka Title')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('empire_state.jfif')

with col2:
    st.image('Burj_Khalifa.jpg.webp')

with col3:
    st.image('petronas.jpg')

st.error('Login Failed')

st.success('Login Successful')

bar = st.progress(0)

for i in range(1, 101):
    # time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter email')
number = st.number_input('Enter age')
st.date_input('Enter Resistration date')


# Login page
import streamlit as st

email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select Gender', ['Male', 'Female', 'Others'])

button = st.button('Login Karo')

# if the button is clicked
if button:
    if email == 'skn329986@gmail.com' and password == '1234':
        st.balloons()
        st.write(gender)
        # st.success('Login Successful')
    else:
        st.error('Login Failed')



# Uploading a s file
import streamlit as st
import pandas as pd

file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())