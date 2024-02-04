import streamlit as st
import pandas as pd

# Install required packages
st.subheader("Installing required packages...")
st.code("pip install pandas openpyxl")

# Import the installed packages
import pandas as pd

def main():
    st.title('Duplicate Remover App')

    uploaded_files = st.file_uploader("Upload one or two Excel files", type=["xlsx"], accept_multiple_files=True)

    if not uploaded_files or len(uploaded_files) < 1:
        st.warning("Please upload at least one file.")
        return

    df1 = pd.read_excel(uploaded_files[0])
    df1 = df1.drop_duplicates(subset='email')

    if len(uploaded_files) > 1:
        df2 = pd.read_excel(uploaded_files[1])
        # Remove rows in df1 where the email exists in df2
        df1 = df1[~df1['email'].isin(df2['email'])]

    # Display the modified DataFrame
    st.write("Modified DataFrame:")
    st.write(df1)

    # Save the modified DataFrame to a new Excel file
    output_file = 'output.xlsx'
    df1.to_excel(output_file, index=False)

    # Provide a link to download the modified Excel file
    st.markdown(f"Download the modified Excel file: [output.xlsx](sandbox:/mnt/{output_file})")

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)
