import streamlit as st
from functionality import generate_markdown

def main():
    st.title("Upsonic LinkedIn Post Generator")
    st.subheader("Create professional LinkedIn posts for Upsonic with different tones")
    
    # Input for company name
    company_name = st.text_input("Enter Company Name", "Upsonic")
    
    # Tone selection
    tone_options = ["General Tone", "Friendly Tone", "Formal&Professional Tone"]
    selected_tone = st.selectbox("Select Tone", tone_options)
    
    # Generate button
    if st.button("Generate Post"):
        if company_name:
            # Show loading spinner while generating content
            with st.spinner("Generating LinkedIn posts... Please wait"):
                # Generate markdown using the function from functionality.py
                post1, post2, post3 = generate_markdown(company_name, selected_tone)
            
            # Display the generated markdown
            st.subheader("Generated LinkedIn Posts:")
            
            # Post 1 - Company Perspective "We" with company name
            st.markdown("### Post 1: Company Perspective (with company name)")
            st.text_area("Company Post:", value=post1, height=150)
            if st.button("Copy Post 1"):
                st.success("✅ Post 1 text selected. Use Ctrl+C or Cmd+C to copy")
                st.code(post1, language="markdown")
            
            # Post 2 - Personal Perspective "I"
            st.markdown("### Post 2: Personal Perspective")
            st.text_area("Personal Post:", value=post2, height=150)
            if st.button("Copy Post 2"):
                st.success("✅ Post 2 text selected. Use Ctrl+C or Cmd+C to copy")
                st.code(post2, language="markdown")
            
            # Post 3 - Company Perspective "We" without company name
            st.markdown("### Post 3: Company Perspective (without company name)")
            st.text_area("Team Post:", value=post3, height=150)
            if st.button("Copy Post 3"):
                st.success("✅ Post 3 text selected. Use Ctrl+C or Cmd+C to copy")
                st.code(post3, language="markdown")
        else:
            st.error("Please enter a company name.")

if __name__ == "__main__":
    main() 