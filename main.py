import streamlit as st
from functionality import generate_markdown

def main():
    st.title("Upsonic LinkedIn Post Generator")
    st.subheader("Create professional LinkedIn posts for Upsonic with different tones")
    
    # Input for company name (required)
    company_name = st.text_input("Enter Company Name", placeholder="Required")
    
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
            
            # Display alternative post versions
            st.markdown("### Alternative Post Versions")
            
            # Alternative 1
            st.markdown("#### Alternative 1")
            st.text_area("Alternative 1:", value=post1, height=150)
            if st.button("Copy Alternative 1"):
                st.success("✅ Alternative 1 selected. Use Ctrl+C or Cmd+C to copy")
                st.code(post1, language="markdown")
            
            # Alternative 2
            st.markdown("#### Alternative 2")
            st.text_area("Alternative 2:", value=post2, height=150)
            if st.button("Copy Alternative 2"):
                st.success("✅ Alternative 2 selected. Use Ctrl+C or Cmd+C to copy")
                st.code(post2, language="markdown")
            
            # Alternative 3
            st.markdown("#### Alternative 3")
            st.text_area("Alternative 3:", value=post3, height=150)
            if st.button("Copy Alternative 3"):
                st.success("✅ Alternative 3 selected. Use Ctrl+C or Cmd+C to copy")
                st.code(post3, language="markdown")
        else:
            st.error("Please enter a company name.")

if __name__ == "__main__":
    main() 