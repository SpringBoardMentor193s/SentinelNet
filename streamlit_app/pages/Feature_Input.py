import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="SentinelNet Features", layout="centered")

st.title("🧮 NSL-KDD Feature Input")

# Load selected model from session_state
if "selected_model" not in st.session_state:
    st.error("⚠️ Please go back and select a model first!")
    st.stop()

st.write(f"### Selected Model: {st.session_state['selected_model']}")

# ==============================
# Define 41 Features (NSL-KDD)
# ==============================
protocol_type = st.selectbox("Protocol Type", ["tcp", "udp", "icmp"])
service = st.selectbox("Service", ["http", "ftp", "telnet", "smtp", "other"])
flag = st.selectbox("Flag", ["SF", "S0", "REJ", "RSTO", "RSTR"])

duration = st.number_input("Duration", min_value=0, step=1)
src_bytes = st.number_input("Source Bytes", min_value=0, step=1)
dst_bytes = st.number_input("Destination Bytes", min_value=0, step=1)
land = st.selectbox("Land (Same Host/Same Port)", [0, 1])
wrong_fragment = st.number_input("Wrong Fragment", min_value=0, step=1)
urgent = st.number_input("Urgent Packets", min_value=0, step=1)
hot = st.number_input("Hot Indicators", min_value=0, step=1)
num_failed_logins = st.number_input("Failed Logins", min_value=0, step=1)
logged_in = st.selectbox("Logged In", [0, 1])
num_compromised = st.number_input("Num Compromised", min_value=0, step=1)
root_shell = st.selectbox("Root Shell", [0, 1])
su_attempted = st.selectbox("Su Attempted", [0, 1])
num_root = st.number_input("Num Root", min_value=0, step=1)
num_file_creations = st.number_input("Num File Creations", min_value=0, step=1)
num_shells = st.number_input("Num Shells", min_value=0, step=1)
num_access_files = st.number_input("Num Access Files", min_value=0, step=1)
num_outbound_cmds = st.number_input("Num Outbound Cmds", min_value=0, step=1)
is_host_login = st.selectbox("Is Host Login", [0, 1])
is_guest_login = st.selectbox("Is Guest Login", [0, 1])

count = st.number_input("Count", min_value=0, step=1)
srv_count = st.number_input("Service Count", min_value=0, step=1)
serror_rate = st.slider("SYN Error Rate", 0.0, 1.0, 0.0)
srv_serror_rate = st.slider("Srv SYN Error Rate", 0.0, 1.0, 0.0)
rerror_rate = st.slider("R Error Rate", 0.0, 1.0, 0.0)
srv_rerror_rate = st.slider("Srv R Error Rate", 0.0, 1.0, 0.0)
same_srv_rate = st.slider("Same Service Rate", 0.0, 1.0, 0.0)
diff_srv_rate = st.slider("Diff Service Rate", 0.0, 1.0, 0.0)
srv_diff_host_rate = st.slider("Srv Diff Host Rate", 0.0, 1.0, 0.0)

dst_host_count = st.number_input("Dst Host Count", min_value=0, step=1)
dst_host_srv_count = st.number_input("Dst Host Srv Count", min_value=0, step=1)
dst_host_same_srv_rate = st.slider("Dst Host Same Srv Rate", 0.0, 1.0, 0.0)
dst_host_diff_srv_rate = st.slider("Dst Host Diff Srv Rate", 0.0, 1.0, 0.0)
dst_host_same_src_port_rate = st.slider("Dst Host Same Src Port Rate", 0.0, 1.0, 0.0)
dst_host_srv_diff_host_rate = st.slider("Dst Host Srv Diff Host Rate", 0.0, 1.0, 0.0)
dst_host_serror_rate = st.slider("Dst Host Serror Rate", 0.0, 1.0, 0.0)
dst_host_srv_serror_rate = st.slider("Dst Host Srv Serror Rate", 0.0, 1.0, 0.0)
dst_host_rerror_rate = st.slider("Dst Host Rerror Rate", 0.0, 1.0, 0.0)
dst_host_srv_rerror_rate = st.slider("Dst Host Srv Rerror Rate", 0.0, 1.0, 0.0)

# ==============================
# Encode categorical variables
# ==============================
protocol_map = {"tcp": 0, "udp": 1, "icmp": 2}
service_map = {"http": 0, "ftp": 1, "telnet": 2, "smtp": 3, "other": 4}
flag_map = {"SF": 0, "S0": 1, "REJ": 2, "RSTO": 3, "RSTR": 4}

# ==============================
# Build input vector (41 features)
# ==============================
input_data = [
    duration,
    protocol_map[protocol_type],
    service_map[service],
    flag_map[flag],
    src_bytes,
    dst_bytes,
    land,
    wrong_fragment,
    urgent,
    hot,
    num_failed_logins,
    logged_in,
    num_compromised,
    root_shell,
    su_attempted,
    num_root,
    num_file_creations,
    num_shells,
    num_access_files,
    num_outbound_cmds,
    is_host_login,
    is_guest_login,
    count,
    srv_count,
    serror_rate,
    srv_serror_rate,
    rerror_rate,
    srv_rerror_rate,
    same_srv_rate,
    diff_srv_rate,
    srv_diff_host_rate,
    dst_host_count,
    dst_host_srv_count,
    dst_host_same_srv_rate,
    dst_host_diff_srv_rate,
    dst_host_same_src_port_rate,
    dst_host_srv_diff_host_rate,
    dst_host_serror_rate,
    dst_host_srv_serror_rate,
    dst_host_rerror_rate,
    dst_host_srv_rerror_rate,
]

# ==============================
# Load Model and Predict
# ==============================
if st.button("🚀 Load Model and Predict"):
    try:
        model_path = f"models/{st.session_state['selected_model'].replace(' ', '_')}.pkl"
        model = joblib.load(model_path)

        prediction = model.predict([input_data])[0]

        if prediction == 0:
            st.success("✅ Normal Traffic")
        else:
            st.error("🚨 Attack Detected")

    except Exception as e:
        st.error(f"Error loading model: {e}")
