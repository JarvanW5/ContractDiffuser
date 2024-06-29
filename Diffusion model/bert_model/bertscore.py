from bert_score import BERTScorer
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
candidates = ["This is a sample sentence.", "Here is another example sentence."]
references = ["This is a sample sentence.", "Here is a different example sentence."]

scorer = BERTScorer(lang="en")
P, R, F1 = scorer.score(candidates, references)

for i in range(len(candidates)):
    print(f"Candidate {i + 1} - F1 Score: {F1[i]:.4f}")
