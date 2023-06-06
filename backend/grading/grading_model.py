from sentence_transformers import SentenceTransformer
import torch
from torch.nn import CosineSimilarity


class GradeModel:

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')
        self.cosine_sim = CosineSimilarity()

    def get_cosine_sim(self, correct_answer, your_answer):
        embedded_example_answers = self.model.encode([correct_answer], convert_to_tensor=True)
        embedded_your_answers = self.model.encode([your_answer], convert_to_tensor=True)
        cosine_scores = self.cosine_sim(embedded_your_answers, embedded_example_answers)
        return cosine_scores

    def grade(self, question, correct_answer, your_answer):
        cosine_sim = float(self.get_cosine_sim(your_answer, correct_answer,).detach().cpu().numpy()[0])
        print(cosine_sim)
        # When cosine_sim is greater than 0.7, the answer is correct else it is false.
        # Too simple for now can apply better logic later.
        return cosine_sim, cosine_sim > 0.7

