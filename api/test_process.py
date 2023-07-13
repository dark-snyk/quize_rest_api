from flask import Blueprint
from typing import Dict, List
from pydantic import BaseModel
from database.questionservice import get_questions_db, check_user_answer_db
from database.statservice import get_user_position

test_bp = Blueprint("test_process", __name__)

# questions validator
class Questions(BaseModel):
    timer: int
    questions: List[Dict]


# request to get all questions
@test_bp.route("/get-questions/<string:level>", methods=["GET"])
def get_user_questions(level: str) -> Questions.json:
    # to db questions
    questions = get_questions_db(level)

    if questions:
        result = []
        timer = 0
        # get for each questions
        for question in questions:
            generated_question = {'question_text': question.main_question,
                                  'variants': [question.answer_1, question.answer_2, question.answer_3, question.answer_4]}
            result.append({'question_id': question.id, 'question': generated_question})
            timer = question.timer
        # pass to class Questions
        return Questions(**{'timer': timer, 'questions': result}).json()
    return Questions(timer=0, questions=[])


# request to check answer
@test_bp.route("/check-answer/<int:question_id>/<int:user_answer>", methods=["POST"])
def check_current_user_answer(question_id: int, user_answer: str) -> Dict[str, int]:
    result = check_user_answer_db(question_id, user_answer)
    #  pass to frontend 1 or 0
    return {'status': 1 if result else 0}


# request for getting result
@test_bp.route("/done/<int:user_id>/<int:correct_answers>/<string:level>", methods=["POST"])
def user_done_test(user_id: int, correct_answers: int, level: str) -> Dict[str, int]:
    user_position = get_user_position(user_id, level, correct_answers)

    return {'ststus': 1, 'correct_answers': correct_answers, 'position_on_top': user_position}