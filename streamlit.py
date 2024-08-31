import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import urllib.parse

def scrape_scholar_articles(query, num_pages):
    articles = []
    page = 0
    while page < num_pages:
        url = f"https://scholar.google.com/scholar?start={page*10}&q={urllib.parse.quote(query)}&hl=en&as_sdt=0,5"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("div", class_="gs_ri")

        for result in results:
            title_tag = result.find("h3", class_="gs_rt")
            title = title_tag.text if title_tag else "No title available"
            
            abstract_div = result.find("div", class_="gs_rs")
            abstract = abstract_div.text.strip() if abstract_div else "No abstract available"
            
            # Truncate abstract to ensure it’s not too long but contains enough content
            abstract = (abstract[:250] + '...') if len(abstract) > 250 else abstract
            
            authors_div = result.find("div", class_="gs_a")
            authors = authors_div.text if authors_div else "No authors available"

            link_tag = result.find("a")
            link = link_tag["href"] if link_tag else "No link available"

            articles.append({"Title": title, "Abstract": abstract, "Authors": authors, "Link": link})

        page += 1

    return articles

def main():
    st.title("Google Scholar Scraper")
    
    query = st.text_input("Article Title or Keyword:")
    num_pages = st.number_input("Number of Pages:", min_value=1, max_value=10, value=1)
    if st.button("Extract Data"):
        if query:
            with st.spinner('Scraping data...'):
                articles = scrape_scholar_articles(query, num_pages)
                if articles:
                    df = pd.DataFrame(articles)
                    st.write("### Results", df)
                    st.download_button(
                        label="Download Excel File",
                        data=df.to_excel(index=False, engine='openpyxl'),
                        file_name=f"{query}_scholar_articles.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                else:
                    st.write("No articles found. Please try a different query.")
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
