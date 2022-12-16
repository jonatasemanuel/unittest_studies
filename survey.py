"""Module doc"""

class AnonymousSurvey():
    """Collect answers anonymous for a survey question"""
    def __init__(self, question) -> None:
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the search question"""
        print(self.question)

    def store_response(self, new_response):
        """Stores only one survey response"""
        self.responses.append(new_response)

    def show_results(self):
        """Shows all answers given"""
        print('Survey results: ')
        for response in self.responses:
            print(f'- {response}')
