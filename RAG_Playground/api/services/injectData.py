import tensorflow_hub as hub
import faiss
import numpy as np

class VectorDB:
    def __init__(self, use_url="https://tfhub.dev/google/universal-sentence-encoder/4"):
        # Load the Universal Sentence Encoder model
        self.model = hub.load(use_url)
        self.index = faiss.IndexFlatL2(512)  # USE has a 512-dimensional output
        self.reviews = []  # To store raw review text

    def add_reviews(self, reviews):
        """
        Adds a list of reviews to the vector database.
        
        Parameters:
            reviews (list of str): List of review texts.
        """
        self.reviews.extend(reviews)
        
        # Encode the reviews into vectors using USE
        vectors = self.model(reviews).numpy()
        
        # Convert vectors to numpy array of type float32 (required by FAISS)
        vectors = np.array(vectors).astype("float32")
        
        # Add vectors to the FAISS index
        self.index.add(vectors)
        print(f"Added {len(reviews)} reviews to the vector database.")

    def search(self, query, top_k=5):
        """
        Searches for the top_k most similar reviews to the query.
        
        Parameters:
            query (str): The query text to search for similar reviews.
            top_k (int): Number of similar reviews to retrieve.
        
        Returns:
            list of dict: List of top-k similar reviews with their distances.
        """
        # Encode the query to a vector
        query_vector = self.model([query]).numpy().astype("float32")
        
        # Perform the search
        distances, indices = self.index.search(query_vector, top_k)
        
        # Retrieve and return the results
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx < len(self.reviews):
                results.append(self.reviews[idx])
        
        return results
