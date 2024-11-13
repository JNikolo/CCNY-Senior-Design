import requests
from bs4 import BeautifulSoup

class ReviewScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5"
        }

    def get_reviews(self, reviews_url, max_reviews=10):
        """
        Scrape reviews from the Best Buy reviews page.
        
        Parameters:
            max_reviews (int): Maximum number of reviews to scrape.
        
        Returns:
            list of dict: A list of dictionaries, each containing review details.
        """
        reviews = []
        page_num = 1  # Reviews are paginated

        try:
            while len(reviews) < max_reviews:
                # Fetch each review page
                page = requests.get(f"{reviews_url}&page={page_num}", headers=self.headers)
                soup = BeautifulSoup(page.content, 'html.parser')

                # Find each review block
                review_blocks = soup.find_all('div', {'class': 'review-item-content'})
                if not review_blocks:
                    print("No more reviews found.")
                    break

                print(f"Reviews found on page {page_num}:", len(review_blocks))

                for review_block in review_blocks:
                    if len(reviews) >= max_reviews:
                        break

                    # Extract title, rating, text, and date
                    
                    text = review_block.find('p', {'class': 'pre-white-space'}).get_text(strip=True)

                    reviews.append(text)

                # Increment page number to move to the next page of reviews
                page_num += 1

        except Exception as e:
            print("Error fetching reviews:", e)

        return reviews
