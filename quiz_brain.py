

class QuizBrain():
  def __init__(self, question_list):
    self.question_number = 0
    self.score = 0
    self.question_list = question_list

  def check_answer(self, user_input, current_question):
    if user_input == current_question.answer.lower():
      self.score += 1
      print('You got it right!')
    else:
      print('That\'s wrong!')
    print(f'The answer is: {current_question.answer}\nyour score is: {self.score}/{len(self.question_list)}')

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    answer = input(f'Q.{self.question_number} - {current_question.text} (True or Flase)').lower()
    self.check_answer(answer, current_question)
    print('\n')

  def still_has_question(self):
    return len(self.question_list) > self.question_number

