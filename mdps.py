# Diabetes Prediction Page
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(r'C:\Users\Patil\OneDrive\Desktop\Ayush\Project\Saved Models\diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(r"C:\Users\Patil\OneDrive\Desktop\Ayush\Project\Saved Models\heart_disease_model.sav", 'rb'))

parkinsons_model = pickle.load(open(r"C:\Users\Patil\OneDrive\Desktop\Ayush\Project\Saved Models\parkinsons_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.slider('Number of Pregnancies', min_value=0, max_value=17, step=1)

    with col2:
        Glucose = st.slider('Glucose Level', min_value=0, max_value=200, step=1)

    with col3:
        BloodPressure = st.slider('Blood Pressure value', min_value=0, max_value=150, step=1)

    with col1:
        SkinThickness = st.slider('Skin Thickness value', min_value=0, max_value=100, step=1)

    with col2:
        Insulin = st.slider('Insulin Level', min_value=0, max_value=900, step=1)

    with col3:
        BMI = st.slider('BMI value', min_value=0.0, max_value=70.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value', min_value=0.0, max_value=3.0, step=0.01)

    with col2:
        Age = st.slider('Age of the Person', min_value=21, max_value=90, step=1)

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider('Age', min_value=0, max_value=100, step=1)

    with col2:
        sex = st.selectbox('Sex', ['Male', 'Female'])

    with col3:
        cp = st.slider('Chest Pain types', min_value=0, max_value=3, step=1)

    with col1:
        trestbps = st.slider('Resting Blood Pressure', min_value=90, max_value=200, step=1)

    with col2:
        chol = st.slider('Serum Cholestoral in mg/dl', min_value=100, max_value=400, step=1)

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])

    with col1:
        restecg = st.slider('Resting Electrocardiographic results', min_value=0, max_value=2, step=1)

    with col2:
        thalach = st.slider('Maximum Heart Rate achieved', min_value=60, max_value=200, step=1)

    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])

    with col1:
        oldpeak = st.slider('ST depression induced by exercise', min_value=0.0, max_value=6.2, step=0.1)

    with col2:
        slope = st.slider('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1)

    with col3:
        ca = st.slider('Major vessels colored by flourosopy', min_value=0, max_value=4, step=1)

    with col1:
        thal = st.slider('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, step=1)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input[1] = 1 if user_input[1] == 'Male' else 0
        user_input[6] = 0 if user_input[6] == 'No' else 1
        user_input[9] = float(user_input[9])  # Converting oldpeak to float

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinsons Prediction Page
# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.slider('MDVP:Fo(Hz)', min_value=0.0, max_value=300.0, step=0.1)

    with col2:
        fhi = st.slider('MDVP:Fhi(Hz)', min_value=0.0, max_value=300.0, step=0.1)

    with col3:
        flo = st.slider('MDVP:Flo(Hz)', min_value=0.0, max_value=300.0, step=0.1)

    with col4:
        Jitter_percent = st.slider('MDVP:Jitter(%)', min_value=0.0, max_value=2.0, step=0.01)

    with col5:
        Jitter_Abs = st.slider('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.1, step=0.001)

    with col1:
        RAP = st.slider('MDVP:RAP', min_value=0.0, max_value=0.1, step=0.001)

    with col2:
        PPQ = st.slider('MDVP:PPQ', min_value=0.0, max_value=0.1, step=0.001)

    with col3:
        DDP = st.slider('Jitter:DDP', min_value=0.0, max_value=0.1, step=0.001)

    with col4:
        Shimmer = st.slider('MDVP:Shimmer', min_value=0.0, max_value=0.1, step=0.001)

    with col5:
        Shimmer_dB = st.slider('MDVP:Shimmer(dB)', min_value=0.0, max_value=5.0, step=0.01)

    with col1:
        APQ3 = st.slider('Shimmer:APQ3', min_value=0.0, max_value=0.1, step=0.001)

    with col2:
        APQ5 = st.slider('Shimmer:APQ5', min_value=0.0, max_value=0.1, step=0.001)

    with col3:
        APQ = st.slider('MDVP:APQ', min_value=0.0, max_value=0.1, step=0.001)

    with col4:
        DDA = st.slider('Shimmer:DDA', min_value=0.0, max_value=0.1, step=0.001)

    with col5:
        NHR = st.slider('NHR', min_value=0.0, max_value=0.5, step=0.01)

    with col1:
        HNR = st.slider('HNR', min_value=0.0, max_value=35.0, step=0.1)

    with col2:
        RPDE = st.slider('RPDE', min_value=0.0, max_value=1.0, step=0.01)

    with col3:
        DFA = st.slider('DFA', min_value=0.0, max_value=1.0, step=0.01)

    with col4:
        spread1 = st.slider('spread1', min_value=-10.0, max_value=10.0, step=0.1)

    with col5:
        spread2 = st.slider('spread2', min_value=-10.0, max_value=10.0, step=0.1)

    with col1:
        D2 = st.slider('D2', min_value=0.0, max_value=10.0, step=0.1)

    with col2:
        PPE = st.slider('PPE', min_value=0.0, max_value=1.0, step=0.01)

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


