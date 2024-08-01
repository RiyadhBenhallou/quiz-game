from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
  quiz_brain.next_question()

print(f'You\'ve completed the quiz\nYour final score is: {quiz_brain.score}/{len(question_bank)}')
