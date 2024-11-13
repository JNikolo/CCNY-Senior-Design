import google.generativeai as genai
from rouge_score import rouge_scorer
from typing import List
import time
from config.variables import GOOGLE_API_KEY

class GeminiSummarizer:
    def __init__(self):
        """Initialize the review summarizer with Gemini API"""
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Few-shot examples with single-sentence summaries
        self.few_shot_examples = """
Here are examples of single-sentence review summaries:

REVIEW 1:
"I bought this coffee maker last month and I've been using it daily. The brewing process is quick and the temperature is perfect. The only downside is that the water tank is a bit small, so I need to refill it often. The coffee taste is excellent though, and it's very easy to clean. The price was reasonable for the quality you get."

SUMMARY 1:
A high-quality coffee maker that delivers excellent taste and quick brewing despite its small water tank.

REVIEW 2:
"This restaurant was a huge disappointment. We waited over an hour for our food, and when it finally arrived, it was cold. The waiter was apologetic and offered to reheat it, but by then we had lost our appetite. The only positive thing was the nice ambiance and decor. The prices were also quite high for the quality of food and service we received."

SUMMARY 2:
Poor service and cold food overshadow the nice ambiance at this overpriced restaurant.

REVIEW 3:
"This backpack has been my daily companion for six months of heavy use. The material is incredibly durable and has survived countless rainy days without any water seeping in. The laptop compartment is well-padded and fits my 15-inch device perfectly. There are plenty of pockets for organization, though I wish the water bottle holder was a bit deeper. The straps are comfortable even when the bag is fully loaded. Great value for money!"

SUMMARY 3:
Durable, well-organized backpack offering excellent laptop protection and comfort for daily use.

Now, please provide a single-sentence summary for the following review:
"""

    def generate_summary(self, review: str, max_retries: int = 3) -> str:
        """Generate a single-sentence summary of a customer review"""
        prompt = f"{self.few_shot_examples}\n\nREVIEW:\n\"{review}\"\n\nSUMMARY:"
        
        retries = 0
        while retries < max_retries:
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.3,
                        top_p=0.8,
                        top_k=40,
                        max_output_tokens=10  # Limited tokens for single sentence
                    )
                )
                # Clean up the response and ensure it's a single sentence
                summary = response.text.strip()
                summary = summary.split('.')[0] + '.'  # Keep only first sentence
                return summary
                
            except Exception as e:
                retries += 1
                if retries == max_retries:
                    print(f"Error generating summary: {str(e)}")
                    return None
                time.sleep(2)
        
        return None

    def summarize_batch(self, reviews: List[str], batch_size: int = 10) -> List[str]:
        """Summarize a batch of reviews with rate limiting"""
        summaries = []
        for i in range(0, len(reviews), batch_size):
            batch = reviews[i:i + batch_size]
            for review in batch:
                summary = self.generate_summary(review)
                if summary:
                    summaries.append(summary)
                time.sleep(1)  # Rate limiting
            if i + batch_size < len(reviews):
                time.sleep(5)  # Pause between batches
        return summaries
    
    def evaluate(self, reference_summary: str, summary: str, metrics: List[str] = ['rouge1', 'rougeL']) -> dict:
        """Evaluate the generated summary against the reference summary"""
        scorer = rouge_scorer.RougeScorer(metrics, use_stemmer=True)
        scores = scorer.score(summary, reference_summary)
        return {metric: score.fmeasure for metric, score in scores.items()}

    def evaluate_batch(self, reference_summaries: List[str], summaries: List[str], metrics: List[str] = ['rouge1', 'rougeL']) -> dict:
        """Evaluate the generated summaries against reference summaries"""
        scorer = rouge_scorer.RougeScorer(metrics, use_stemmer=True)
        scores = scorer.score(summaries, reference_summaries)
        return scores
