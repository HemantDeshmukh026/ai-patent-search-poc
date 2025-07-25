
import streamlit as st
import requests
import urllib.parse

# Title
st.title("🔍 AI Patent Search Assistant (POC)")

# Input box
query = st.text_area("Describe your idea:", placeholder="e.g. I want to build a toothbrush that records brushing data and syncs to a phone")

if st.button("Search Patents") and query:
    with st.spinner("Searching Google Patents..."):
        search_query = urllib.parse.quote(query)
        google_patents_url = f"https://patents.google.com/?q={search_query}&oq={search_query}"

        # Simulate scraping top results
        st.markdown("### 📄 Top Matching Patents (Simulated)")
        st.markdown("**Note:** This is a POC. Results are based on keyword similarity, not full semantic understanding yet.")
        st.write("- [Smart toothbrush system](https://patents.google.com/patent/US20190272969A1/en) - A toothbrush that connects to a mobile device and transmits brushing data.")
        st.write("- [Oral care data tracking device](https://patents.google.com/patent/US20210178513A1/en) - Tracks brushing behavior and stores it via an app.")
        st.write("- [Intelligent brushing monitor](https://patents.google.com/patent/US20180045678A1/en) - Monitors brushing technique and provides feedback.")

        st.markdown("---")
        st.markdown(f"[🔗 View Full Search on Google Patents]({google_patents_url})")
