import requests
from bs4 import BeautifulSoup
import json
class ReviewScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5"
        }

    def get_reviews(self, reviews_url, max_pages=3):
        """
        Scrape reviews from the Best Buy reviews page.
        
        Parameters:
            max_reviews (int): Maximum number of reviews to scrape.
        
        Returns:
            list of dict: A list of dictionaries, each containing review details.
        """
        reviewsText = []
        page_num = 1  # Reviews are paginated

        try:
            for i in range(page_num, max_pages + 1):
                # Fetch each review page
                page = requests.get(f"{reviews_url}?page={i}", headers=self.headers)
                soup = BeautifulSoup(page.text, 'html.parser')
                if not soup:
                    print("No more reviews found.")
                    break
                print(f"Fetching reviews from page {page_num}...")

                # Find each review block
                nextTag = soup.find("script",{"id":"__NEXT_DATA__"})
                jsonData = json.loads(nextTag.text)

                if not jsonData:
                    print("No more reviews found.")
                    break

                reviews = jsonData['props']['pageProps']['initialData']['data']['reviews']['customerReviews']
                for review in reviews:
                    reviewsText.append(review['reviewText'])
                # print(reviewsText)
                # print(f"Reviews found on page {page_num}:", len(review_blocks))

                # for review_block in review_blocks:
                #     if len(reviews) >= max_reviews:
                #         break

                #     # Extract text from review block
                    
                #     text = review_block.find('span', {'class': 'tl-m db-m'}).get_text(strip=True)

                #     reviews.append(text)

                # # Increment page number to move to the next page of reviews
                # page_num += 1

        except Exception as e:
            print("Error fetching reviews:", e)

        return reviewsText

# Example usage
def main():
    scraper = ReviewScraper()
    reviews = scraper.get_reviews("https://www.walmart.com/reviews/product/8112457916", max_pages=2)
    for i, review in enumerate(reviews, start=1):
        print(f"Review {i}: {review}\n")

if __name__ == "__main__":
    main()
# Example output:
# Review 1: I love these AirPods. They are so comfortable and the sound quality is amazing. The noise cancellation works great too.
