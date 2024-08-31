import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def scrape_scholar_articles(query, num_pages):
    articles = []
    page = 0
    while page < num_pages:
        url = f"https://scholar.google.com/scholar?start={page*10}&q={query}&hl=en&as_sdt=0,5"
        print(f"Requesting URL: {url}")  # Debug: Print the URL being requested
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")  # Debug: Status code
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("div", class_="gs_ri")

        if not results:
            print("No results found on page.")  # Debug: No results found
            break

        for result in results:
            title_tag = result.find("h3", class_="gs_rt")
            authors_tag = result.find("div", class_="gs_a")
            link_tag = result.find("a")

            if title_tag and authors_tag and link_tag:
                title = title_tag.text
                authors = authors_tag.text
                link = link_tag["href"]
                articles.append({"Title": title, "Authors": authors, "Link": link})
            else:
                print("Missing data in one of the results.")  # Debug: Missing data

        page += 1

    return articles

def save_to_excel(articles, filename):
    df = pd.DataFrame(articles)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")  # Debug: Print filename where data is saved

def browse_folder():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(tk.END, folder_path)

def scrape_articles():
    query = entry_query.get()
    num_pages = int(entry_pages.get())

    articles = scrape_scholar_articles(query, num_pages)
    
    if not articles:
        label_status.config(text="No data scraped. Check the query or the URL.")
        return

    folder_path = entry_folder.get()
    if folder_path:
        filename = f"{folder_path}/scholar_articles.xlsx"
    else:
        filename = "scholar_articles.xlsx"

    save_to_excel(articles, filename)
    label_status.config(text=f"Extraction complete. Data saved to {filename}.")

# Create the main window
window = tk.Tk()
window.title("Google Scholar Scraper")
window.geometry("400x250")

# Create input fields and labels
label_query = tk.Label(window, text="Article Title or Keyword:")
label_query.pack()
entry_query = tk.Entry(window, width=40)
entry_query.pack()

label_pages = tk.Label(window, text="Number of Pages:")
label_pages.pack()
entry_pages = tk.Entry(window, width=40)
entry_pages.pack()

label_folder = tk.Label(window, text="Output Folder (optional):")
label_folder.pack()
entry_folder = tk.Entry(window, width=40)
entry_folder.pack()

# Create browse button
button_browse = tk.Button(window, text="Browse", command=browse_folder)
button_browse.pack()

# Create extract button
button_extract = tk.Button(window, text="Extract Data", command=scrape_articles)
button_extract.pack()

# Create status label
label_status = tk.Label(window, text="")
label_status.pack()

# Run the main window loop
window.mainloop()
