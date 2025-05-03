import streamlit as st
from functionality import generate_markdown
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    st.title("Upsonic LinkedIn Post Generator")
    st.subheader("Create professional LinkedIn posts for Upsonic with different tones")
    
    # Initialize session state for storing generated posts
    if "post1" not in st.session_state:
        st.session_state.post1 = ""
    if "post2" not in st.session_state:
        st.session_state.post2 = ""
    if "post3" not in st.session_state:
        st.session_state.post3 = ""
    if "posts_generated" not in st.session_state:
        st.session_state.posts_generated = False
    
    # Input for company name (required)
    company_name = st.text_input("Enter Company Name", placeholder="Required")
    
    # Tone selection - changed order to make Professional tone first and default
    tone_options = ["Formal&Professional Tone", "Friendly Tone"]
    selected_tone = st.selectbox("Select Tone", tone_options, index=0)
    
    # Generate button
    if st.button("Generate Post"):
        if company_name:
            # Show loading spinner while generating content
            with st.spinner("Generating LinkedIn posts... Please wait"):
                # Generate markdown using the function from functionality.py
                st.session_state.post1, st.session_state.post2, st.session_state.post3 = generate_markdown(company_name, selected_tone)
                st.session_state.posts_generated = True
            
    # Display the generated markdown if posts have been generated
    if st.session_state.posts_generated:
        st.subheader("Generated LinkedIn Posts:")
        
        # Display alternative post versions
        st.markdown("### Alternative Post Versions")
        
        # Create columns for each alternative to better organize the layout
        col1, col2, col3 = st.columns(3)
        
        # Alternative 1
        with col1:
            st.markdown("#### Alternative 1")
            st.text_area("Post 1:", value=st.session_state.post1, height=150, key="textarea_post1")
            if st.button("Copy Alternative 1", key="copy1"):
                st.code(st.session_state.post1, language="markdown")
                st.success("✅ Post 1 copied to clipboard")
        
        # Alternative 2
        with col2:
            st.markdown("#### Alternative 2")
            st.text_area("Post 2:", value=st.session_state.post2, height=150, key="textarea_post2")
            if st.button("Copy Alternative 2", key="copy2"):
                st.code(st.session_state.post2, language="markdown")
                st.success("✅ Post 2 copied to clipboard")
        
        # Alternative 3
        with col3:
            st.markdown("#### Alternative 3")
            st.text_area("Post 3:", value=st.session_state.post3, height=150, key="textarea_post3")
            if st.button("Copy Alternative 3", key="copy3"):
                st.code(st.session_state.post3, language="markdown")
                st.success("✅ Post 3 copied to clipboard")
    else:
        if company_name == "":
            st.error("Please enter a company name.")

if __name__ == "__main__":
    main()