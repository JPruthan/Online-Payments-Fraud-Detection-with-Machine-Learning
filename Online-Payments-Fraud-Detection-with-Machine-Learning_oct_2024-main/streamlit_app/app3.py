import joblib
import pandas as pd
import streamlit as st
import os

# Load the saved model
log_reg_loaded = joblib.load(r'C:\Users\prasa\OneDrive\Desktop\infosys_online\website\random_forest.pkl')

# Transaction types for dropdown
transaction_types = {
    "Select Transaction Type": -1,
    "Cash-in": 0,
    "Cash-out": 1,
    "Debit": 2,
    "Payment": 3,
    "Transfer": 4,
    "Deposit": 5,
}

# Create or load transaction history
history_path = "transactions_history.csv"
if not os.path.exists(history_path):
    pd.DataFrame(columns=["Transaction Type", "Amount", "Old Balance", "New Balance", "Prediction"]).to_csv(history_path, index=False)

# Horizontal Navigation
st.set_page_config(page_title="Fraud Detection", layout="wide")
tabs = st.tabs(["Home", "Single Transaction", "Bulk Upload", "Transaction History", "About"])

st.markdown("""
<style>
    .stApp { background-color: #34495e; }
</style>
""", unsafe_allow_html=True)

# Styling (CSS)
st.markdown("""
    <style>
        body{
            # background-color:#455d7a;   
        }
        .streamlit-expanderHeader {
            font-size: 60px !important;  /* Triple the font size of tab names */
            font-weight: bold;
        }

        .stTabs{
            font-size:1.5em !important;
        }
        .stTabs [role="tablist"] {
            display: flex;
            justify-content: space-evenly;
            background-color: #5e63b6;  /* Black background for navbar */
            border:5px solid #42b883;
            position: sticky;
            top: 0;
            border-radius:10px;
            z-index: 100;
            padding: 10px 0;
        }

        .stTabs [role="tab"] {
            font-size: 40px !important;
            font-weight: bold !important;
            color: white !important;
        }

        .stTabs [role="tab"]:hover {
            color: #ffd700 !important;
        }

        .stTabs [role="tab"][aria-selected="true"] {
            padding:10px;
            border-radius:5px;
            border:3px solid black;
            background-color: red !important;  /* Light blue background when selected */
            color: #000000 !important;  /* Optional: change text color to black for better contrast */
        }



        .img{
            display:block;
            float:centre;
            transform: scale(1.5);
            margin:40px;
            padding:10px;
        }
        .half-width {
            width: 45%;
            display: inline-block;
            margin-bottom: 10px;
        }
        .right-align {
            text-align: right;
        }
        .main-title {
            text-align: center;
            font-size: 48px;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 24px;
            color: #4caf50;
            margin-top: 10px;
        }
        .highlight-box {
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-size: 18px;
        }
        .fraud {
            background-color: lightcoral;
            color: white;
        }
        .not-fraud {
            background-color: lightgreen;
            color: black;
        }
        .home-box {
            background: linear-gradient(to right, #83a4d4, #b6fbff);
            padding: 20px;
            border-radius: 10px;
            color: #2c3e50;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

if "transaction_type" not in st.session_state:
    st.session_state.transaction_type = "Select Transaction Type"
if "transaction_amount" not in st.session_state:
    st.session_state.transaction_amount = 0.0
if "old_balance" not in st.session_state:
    st.session_state.old_balance = 0.0
if "new_balance" not in st.session_state:
    st.session_state.new_balance = 0.0

with tabs[0]:
    st.markdown('<h1>Online Payment Fraud Detection</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 18px; line-height: 1.8;">
        Welcome to the <b>Online Payment Fraud Detection Tool</b>! This application is designed to safeguard your financial transactions by identifying and preventing fraudulent activities using cutting-edge machine learning technologies. 
    </div>
    
    <h2>What Can This Tool Do?</h2>
    <ul style="font-size: 16px; line-height: 1.8;">
        <li><b>Detect Fraud in Real-Time:</b> Analyze individual transactions instantly to determine their legitimacy.</li>
        <li><b>Bulk Transaction Analysis:</b> Upload transaction datasets to detect anomalies across multiple records simultaneously.</li>
        <li><b>Track Transaction History:</b> Maintain a detailed log of past transactions for review and compliance purposes.</li>
        <li><b>Educate and Inform:</b> Access comprehensive resources to understand fraud trends and how to protect yourself.</li>
    </ul>

    <h2>How It Works:</h2>
    <ol style="font-size: 16px; line-height: 1.8;">
        <li><b>Data Input:</b> Provide transaction data manually or upload a file containing multiple transactions.</li>
        <li><b>Fraud Detection Analysis:</b> The system uses machine learning algorithms trained on historical fraud data to flag suspicious transactions.</li>
        <li><b>Output Report:</b> Receive a detailed report highlighting potential fraudulent activities with actionable insights.</li>
    </ol>
    
    <h2>Why Choose This Tool?</h2>
    <p style="font-size: 16px; line-height: 1.8;">
        Fraudulent transactions not only cause financial losses but also erode trust in digital platforms. Our tool offers:
    </p>
    <ul style="font-size: 16px; line-height: 1.8;">
        <li><b>High Accuracy:</b> Machine learning algorithms continuously learn and adapt to new fraud patterns.</li>
        <li><b>User-Friendly Interface:</b> Designed for simplicity and ease of use, enabling anyone to detect fraud effortlessly.</li>
        <li><b>Data Security:</b> Built with robust encryption and compliance with industry standards to protect your sensitive data.</li>
    </ul>

    <h2>Steps to Get Started:</h2>
    <p style="font-size: 16px; line-height: 1.8;">
        Follow these easy steps to begin using the Online Payment Fraud Detection Tool:
    </p>
    <ol style="font-size: 16px; line-height: 1.8;">
        <li>Navigate to the <b>Fraud Detection</b> tab.</li>
        <li>Input transaction details or upload your dataset.</li>
        <li>Click <b>Analyze</b> to view results.</li>
        <li>Explore the <b>Tips</b> section to learn about secure online payment practices.</li>
    </ol>

    <h2>Stay Ahead of Fraud:</h2>
    <p style="font-size: 16px; line-height: 1.8;">
        Fraud prevention starts with awareness and proactive measures. By leveraging advanced technologies, 
        this tool empowers you to stay one step ahead of cybercriminals. Whether you're an individual or a business, 
        safeguarding your transactions has never been more important.
    </p>
    
    <p style="font-size: 16px; line-height: 1.8; text-align: center; color: #007BFF;">
        Start your journey toward secure digital transactions today!
    </p>
    """, unsafe_allow_html=True)

with tabs[1]:
    # Layout with columns for left-aligned inputs and right-aligned button/results
    col1, col2 = st.columns([2, 1])  # First column is wider, second column is for right alignment

    # Left column: Input fields
    with col1:
        st.markdown('<h2 class="section-title">Single Transaction Fraud Detection</h2>', unsafe_allow_html=True)
        st.session_state.transaction_type = st.selectbox("Transaction Type", options=list(transaction_types.keys()), index=list(transaction_types.keys()).index(st.session_state.transaction_type))
        st.session_state.transaction_amount = st.number_input("Transaction Amount", min_value=0.0, value=st.session_state.transaction_amount, help="Amount should be greater than 0.")
        st.session_state.old_balance = st.number_input("Old Balance of Origin Account", min_value=0.0, value=st.session_state.old_balance)
        st.session_state.new_balance = st.number_input("New Balance of Origin Account", min_value=0.0, value=st.session_state.new_balance)

    # Right column: Button and Results
    with col2:
        # Predict button on the right
        if st.button("Predict", key="predict_single"):
            if st.session_state.transaction_type == "Select Transaction Type":
                st.error("Transaction type not selected! Please choose a valid transaction type.")
            elif st.session_state.transaction_amount <= 0:
                st.error("Transaction amount must be greater than 0.")
            else:
                # Create input data for the prediction
                input_data = pd.DataFrame({
                    'type': [transaction_types[st.session_state.transaction_type]],
                    'amount': [st.session_state.transaction_amount],
                    'oldbalanceOrg': [st.session_state.old_balance],
                    'newbalanceOrig': [st.session_state.new_balance]
                })
                
                # Predict the result
                prediction = log_reg_loaded.predict(input_data)
                prediction_text = "Fraud" if prediction[0] == "Fraud" else "Not Fraud"
                color_class = "fraud" if prediction_text == "Fraud" else "not-fraud"
                
                # Display prediction result
                st.markdown(f"""
                <div class="highlight-box {color_class}">
                    <strong>Prediction: {prediction_text}</strong>
                </div>
                """, unsafe_allow_html=True)

                # Log the transaction
                transaction = pd.DataFrame([[st.session_state.transaction_type, st.session_state.transaction_amount, st.session_state.old_balance, st.session_state.new_balance, prediction_text]],
                                        columns=["Transaction Type", "Amount", "Old Balance", "New Balance", "Prediction"])
                transaction.to_csv(history_path, mode='a', header=False, index=False)

        # Reset button
        if st.button("Reset", key="reset_button"):
            # Reset the form fields by clearing session state values
            st.session_state.transaction_type = "Select Transaction Type"
            st.session_state.transaction_amount = 0.0
            st.session_state.old_balance = 0.0
            st.session_state.new_balance = 0.0
            # st.experimental_rerun()  # Rerun the app to reflect changes
        

# Bulk Upload Page
with tabs[2]:
    st.markdown('<h2 class="section-title">Bulk Transaction Fraud Detection</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if uploaded_file:
        transactions = pd.read_csv(uploaded_file)
        required_columns = ["Transaction Type", "Amount", "Old Balance", "New Balance"]
        
        # Check if required columns are present
        if all(column in transactions.columns for column in required_columns):
            # Map 'Transaction Type' to integer values for prediction
            transactions["Transaction Type"] = transactions["Transaction Type"].map(transaction_types)
            
            # Handle rows with invalid 'Transaction Type' (e.g., empty or unrecognized types)
            transactions = transactions[transactions["Transaction Type"].notna()]
            
            # Prepare the data for prediction, include 'Transaction Type'
            input_data = transactions[required_columns].values  # Include 'Transaction Type'
            
            # Predict using the model
            predictions = log_reg_loaded.predict(input_data)
            
            # Map numeric predictions back to 'Fraud' or 'Not Fraud'
            transactions["Prediction"] = ["Fraud" if pred == "Fraud" else "Not Fraud" for pred in predictions]
            
            # Map 'Transaction Type' back to original values for display (reverse map)
            reverse_transaction_types = {v: k for k, v in transaction_types.items()}
            transactions["Transaction Type"] = transactions["Transaction Type"].map(reverse_transaction_types)
            
            # Display the results with appropriate styling
            st.write("### Prediction Results")
            st.dataframe(transactions.style.applymap(
                lambda x: "background-color: lightcoral; color: white;" if x == "Fraud" else "background-color: lightgreen; color: black;",
                subset=["Prediction"]
            ))
            
            # Save the results to the history file
            transactions.to_csv(history_path, mode='a', header=False, index=False)
        else:
            st.error(f"CSV must include columns: {required_columns}")




# Transaction History Page
with tabs[3]:
    st.markdown('<h2 class="section-title">Transaction History</h2>', unsafe_allow_html=True)
    if os.path.exists(history_path):
        history = pd.read_csv(history_path)
        st.dataframe(history.style.map(
            lambda x: "background-color: lightcoral; color: white;" if x == "Fraud" else "background-color: lightgreen; color: black;",
            subset=["Prediction"]
        ))
    else:
        st.write("No transaction history available.")

import streamlit as st

with tabs[4]:
    st.markdown('<h2 class="section-title">About Online Payment Fraud Detection</h2>', unsafe_allow_html=True)
    st.markdown("""
    Fraudulent activities in online payments are on the rise due to the rapid growth of digital transactions. 
    Cybercriminals use various techniques, such as phishing, identity theft, and malware, to exploit vulnerabilities 
    in online payment systems. Protecting users and businesses from such fraud requires advanced tools and awareness.
    """)
    
    # Add an image related to fraud detection
    st.markdown('<img class="img" style="margin-left:100px;" src="https://5logistics.com/wp-content/uploads/Fraud-1.jpg" alt="Fraud Detection">', unsafe_allow_html=True)
        
    st.markdown("""
    ### Features of Fraud Detection:
    
    - **Real-Time Analysis:** 
      Fraudulent transactions are identified as they happen, minimizing potential losses. Real-time monitoring uses algorithms to detect anomalies in payment patterns.
    - **Machine Learning:** 
      Leveraging historical data, machine learning models can identify patterns and predict fraudulent behavior. These systems improve over time, adapting to new threats.
    - **Multi-Layer Security:** 
      Modern fraud detection systems combine multiple security protocols, including encryption, tokenization, and biometric authentication, to ensure robust protection.
    - **Risk Scoring:** 
      Transactions are assigned risk scores based on factors like geolocation, transaction amount, and device used, helping to identify suspicious activities.
    - **Behavioral Analytics:** 
      Monitoring user behavior, such as login patterns and spending habits, to flag deviations that may indicate fraud.
    """)
    
    # Add an image for machine learning or analytics
    st.markdown('<img style="margin-left:100px;margin-right:auto;" src="https://www.digipay.guru/static/24fb1b1f75d3f9ddb1373c2e1cebbd75/16546/online-payment-security-Image_04.png" alt="Fraud Detection">', unsafe_allow_html=True)
    
    st.markdown("""
    ### Tips for Staying Protected During Online Transactions:
    - **Verify Website Security:** 
      - Only transact on websites with HTTPS protocols. Look for a padlock icon in the browser's address bar.
      - Avoid using public Wi-Fi for online transactions unless you're connected to a trusted VPN.
    - **Enable Multi-Factor Authentication (MFA):**
      - Add an extra layer of security by requiring a one-time password (OTP) or biometric authentication alongside your login credentials.
    - **Keep Devices Updated:**
      - Regularly update your operating system, browser, and payment apps to patch known vulnerabilities.
    - **Monitor Bank Statements:**
      - Review your bank statements and transaction history regularly to detect unauthorized activities early.
    - **Avoid Phishing Scams:**
      - Be cautious of emails, messages, or calls requesting sensitive information. Cybercriminals often pose as legitimate entities.
    - **Use Virtual Cards or Wallets:** 
      - Where possible, use virtual debit/credit cards or digital wallets for online payments. These options provide an extra layer of protection by masking your actual card details.
    - **Educate Yourself and Others:** 
      - Stay informed about common fraud techniques, such as skimming, spoofing, and account takeover fraud, to recognize red flags.
    """)

    # Add an image related to online security or phishing
    st.markdown('<img style="height:400px;width:600px;" src="https://pbsorg.siuat.visa.com/content/dam/financial-literacy/practical-business-skills/images/non-card/types-of-fraud-graphic.jpg" alt="Fraud Detection">', unsafe_allow_html=True)

    
    st.markdown("""
    ### Common Types of Online Payment Fraud:
    - **Phishing Attacks:**
      Fraudsters trick users into providing login credentials or credit card information through fake websites or emails.
    - **Card-Not-Present (CNP) Fraud:**
      Unauthorized transactions occur using stolen card details during online payments.
    - **Man-in-the-Middle (MitM) Attacks:**
      Hackers intercept communication between the user and the payment system to steal sensitive information.
    - **Account Takeover:**
      Cybercriminals gain access to user accounts and initiate fraudulent transactions.
    - **Chargeback Fraud:**
      Customers falsely claim a legitimate transaction was unauthorized to receive a refund.
    """)

    st.markdown('<img src="https://blogimage.vantagefit.io/vfitimages/2021/06/MENTEL-HEALTH-AWARNESS-CELEBRATION--1.png" alt="Fraud Detection">', unsafe_allow_html=True)


    st.markdown("""
    ### Raising Awareness:
    - **Use Reputable Services:**
      Opt for well-known and trusted payment gateways.
    - **Educate Your Network:** 
      Share tips and resources with friends and family to promote safer online transaction habits.
    - **Report Suspicious Activity:** 
      Inform your bank or payment service provider immediately if you notice any unusual activity.
    - **Leverage Fraud Detection Tools:** 
      Use services or tools that proactively monitor transactions and send alerts for suspicious activities.

    By adopting these practices and leveraging advanced fraud detection tools, you can significantly minimize the risk of falling victim to online payment fraud.
    """)



