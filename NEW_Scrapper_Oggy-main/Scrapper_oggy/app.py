 
import pandas as pd
import streamlit as st
from src.cloud_io import MongoIO
from src.constants import SESSION_PRODUCT_KEY
from src.scrapper.scrape import ScrapeReviews

# Set the page configuration
st.set_page_config(page_title="Enhanced Myntra Review Scraper")

st.title("Enhanced Myntra Review Scraper")
st.session_state["data"] = False

def form_input():
    """
    Collect user input for product search, filters, and scraping parameters.
    """
    # Collect basic inputs
    product = st.text_input("Search Products")
    st.session_state[SESSION_PRODUCT_KEY] = product
    
    no_of_products = st.number_input(
        "Number of products to search",
        step=1,
        min_value=1
    )

    # Filters
    category = st.selectbox("Select Category", ["Clothing", "Footwear", "Accessories", "All"])
    min_price = st.number_input("Minimum Price", min_value=0, step=1)
    max_price = st.number_input("Maximum Price", min_value=0, step=1)

    # Sorting options
    sort_option = st.selectbox(
        "Sort By",
        ["Relevance", "Popularity", "Customer Ratings", "Newest"]
    )

    # Button to scrape reviews
    if st.button("Scrape Reviews"):
        if not product.strip():
            st.error("Please enter a valid product name!")
            return

        try:
            # Initialize scraper with additional features
            scrapper = ScrapeReviews(
                product_name=product,
                no_of_products=int(no_of_products),
                category=category if category != "All" else None,
                price_range=(min_price, max_price) if min_price < max_price else None,
                sort_option=sort_option.lower()
            )

            # Fetch review data
            scrapped_data = scrapper.get_review_data()

            # Check if data was retrieved
            if scrapped_data is not None:
                # Store data in MongoDB
                st.session_state["data"] = True
                mongoio = MongoIO()
                mongoio.store_reviews(product_name=product, reviews=scrapped_data)

                st.success("Stored data into MongoDB")

                # Display data with metadata
                st.dataframe(scrapped_data)
            else:
                st.warning("No reviews found for the given search parameters.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    form_input()
# intialize the commit before making changes..... 