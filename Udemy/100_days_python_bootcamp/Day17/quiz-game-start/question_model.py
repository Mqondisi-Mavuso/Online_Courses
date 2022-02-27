class Question:
    def __init__(self, text, answer):
        """
        Default constructor that takes two parameters 'text' and 'answer'
        :param text: string containing the question
        :param answer: string containing true or false
        """
        self.text = text
        self.answer = answer