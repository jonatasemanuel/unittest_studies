"""Unit test about survey"""

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the AnonymousSurvey class"""

    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas que poderão ser usados
        em todos os métodos de teste."""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Português', 'English', 'Spanish']

    def test_store_single_response(self):
        """Tests whether a single response kept"""

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """Tests whether three response is kept"""

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
