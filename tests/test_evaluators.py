import pytest
from src.evaluators.rubric_evaluator import RubricEvaluator, EvaluationCriteria

def test_basic_evaluation():
    criteria = [EvaluationCriteria(name="accuracy", weight=0.8, threshold=0.7)]
    evaluator = RubricEvaluator(criteria)
    result = evaluator.evaluate_response("Test")
    assert 'overall_score' in result
    assert result['overall_score'] > 0