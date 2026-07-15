import json
from pathlib import Path
from .evaluators.rubric_evaluator import RubricEvaluator

class BatchEvaluator:
    def __init__(self):
        self.results = []
    
    async def evaluate_dataset(self, dataset_path: str, evaluator: RubricEvaluator):
        with open(dataset_path, 'r') as f:
            data = json.load(f)
        for item in data:
            result = evaluator.evaluate_response(item['model_response'])
            self.results.append(result)
        return self.results