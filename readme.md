# Google Scholar Scraper with Streamlit & tinkter interface
## Overview

This project includes two primary components:
- **`proxytinkter.py`**: A script designed for proxy management to facilitate web scraping.
- **`streamlit.py`**: A Streamlit application for interacting with and visualizing web scraping results.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Streamlit
- Any other dependencies listed in `requirements.txt` or `environment.yml`

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Mohdnihal03/Google-Scholar-Web-Scrapping.git
    cd Google-Scholar-Web-Scrapping
    ```

2. **Install Dependencies**

    If you have a `requirements.txt` file, install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, if you are using a conda environment, install dependencies from `environment.yml`:

    ```bash
    conda env create -f environment.yml
    conda activate your-env-name
    ```

## Usage

### Running `proxytinkter.py`

To execute the `proxytinkter.py` script:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `proxytinkter.py`.
3. Run the script using:

    ```bash
    python proxytinkter.py
    ```

### Running `streamlit.py`

To start the Streamlit application:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `streamlit.py`.
3. Launch the Streamlit app with:

    ```bash
    streamlit run streamlit.py
    ```

## Known Issues

1. **Request Blocking**: Google Scholar is blocking requests from scraping tools, limiting the ability to make multiple requests simultaneously. Solutions being explored include using proxies, implementing request delays, rotating User-Agent headers, and potentially using API services.

2. **Publication Year Filtering**: There are challenges with filtering articles by publication year. Work is ongoing to resolve this issue.

## Contact

For further assistance or feedback, please contact Mohdnihal03 at mohd.nihalll03@gmail.com.

---

