import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from hybrid_classifier import hybrid_classify

st.set_page_config(page_title="Hybrid Log Classifier", layout="wide")
st.title("📄 Hybrid Log Classification App")
st.markdown("Upload your log CSV file and classify using Regex + Transformer (E5 + Logistic Regression).")

uploaded_file = st.file_uploader("📁 Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")

        if 'log_message' not in df.columns:
            st.error("❌ Column 'log_message' not found in uploaded CSV!")
        else:
            # Apply classification
            df['predicted_label'] = df['log_message'].apply(hybrid_classify)
            st.success("✅ Logs classified successfully!")

            # Show preview
            st.subheader("🔍 Sample Predictions")
            st.dataframe(df[['log_message', 'predicted_label']].head(10))

            # Pie chart (smaller size)
            st.subheader("📊 Label Distribution")
            label_counts = df['predicted_label'].value_counts()
            fig, ax = plt.subplots(figsize=(4, 4))  # Smaller pie chart
            ax.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

            # Model performance
            st.subheader("📈 Model Performance Summary")
            st.markdown("""
            - **Accuracy**: `99%`  
            - **F1-score (macro avg)**: `0.98`  
            - **Weighted F1-score**: `0.99`
            """)

            # Save output to local path
            output_path = r"C:\Users\arjun\Projectlogs\training\dataset\synthetic_logs.csv"
            df.to_csv(output_path, index=False)

            # Download button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Result CSV",
                data=csv,
                file_name="classified_logs.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")
else:
    st.info("👆 Please upload a CSV file to begin.")
