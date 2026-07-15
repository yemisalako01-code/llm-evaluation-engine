from typing import List, Dict, Any
from pydantic import BaseModel

class EvaluationCriteria(BaseModel):
    name: str
    weight: float
    threshold: float

class RubricEvaluator:
    def __init__(self, criteria: List[EvaluationCriteria]):
        self.criteria = criteria
    
    def evaluate_response(self, response: str) -> Dict[str, Any]:
        results = {}
        total_score = 0
        for c in self.criteria:
            score = 0.85 # Mock score
            results[c.name] = {'score': score, 'weight': c.weight}
            total_score += score * c.weight
        results['overall_score'] = total_score
        return results