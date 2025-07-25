
import streamlit as st
import urllib.parse
import requests
from bs4 import BeautifulSoup

st.title("🔍 AI Patent Search Assistant (v2)")

query = st.text_area("Describe your idea:", placeholder="e.g. A toothbrush that tracks brushing patterns and syncs to a phone")

if st.button("Search Patents") and query:
    with st.spinner("Searching Google Patents..."):

        search_url = f"https://patents.google.com/?q={urllib.parse.quote(query)}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        try:
            response = requests.get(search_url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            st.markdown("### 📄 Top Patent Matches (Preview from Google Patents)")
            st.markdown("*(This is a live query, but simplified due to scraping limitations)*")

            results_found = False
            for result in soup.find_all("search-result-item", limit=3):
                title = result.find("span", {"class": "result-title"}).get_text(strip=True)
                link = "https://patents.google.com" + result.find("a")["href"]
                abstract = result.find("div", {"class": "abstract"}).get_text(strip=True)

                st.markdown(f"**[{title}]({link})**")
                st.markdown(f"> {abstract}")
                st.markdown("---")
                results_found = True

            if not results_found:
                st.warning("Couldn't extract results. Google Patents might have changed their layout or blocked scraping.")

            st.markdown(f"[🔗 View full search on Google Patents]({search_url})")

        except Exception as e:
            st.error(f"Error fetching data: {e}")
