import pandas as pd

class ScrapeReviews:
    def __init__(self, product_name, no_of_products, category=None, price_range=None, sort_option=None):
        self.product_name = product_name
        self.no_of_products = no_of_products
        self.category = category
        self.price_range = price_range
        self.sort_option = sort_option

    def get_review_data(self):
        """
        Scrape reviews for the specified product with applied filters and sorting.
        """
        reviews = []
        base_url = f"https://www.myntra.com/search?q={self.product_name}"

        if self.category:
            base_url += f"&category={self.category.lower()}"

        if self.price_range:
            min_price, max_price = self.price_range
            base_url += f"&min_price={min_price}&max_price={max_price}"

        if self.sort_option:
            base_url += f"&sort={self.sort_option}"

        for page in range(1, self.no_of_products + 1):
            page_url = f"{base_url}&page={page}"
            page_reviews = self.scrape_single_page(page_url)
            reviews.extend(page_reviews)

        return pd.DataFrame(reviews) if reviews else None

    def scrape_single_page(self, url):
        """
        Extract review data from a single page.
        """
        # Dummy data for demonstration
        return [
            {
                "Review": "Great product!",
                "Rating": 4.5,
                "Date": "2025-01-01",
                "Location": "Delhi"
            },
            {
                "Review": "Not as expected.",
                "Rating": 2.0,
                "Date": "2025-01-02",
                "Location": "Mumbai"
            }
        ]

