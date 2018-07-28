import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class"""

    def test_store_response(self):
        question="What is your language?"
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)

unittest.main()
