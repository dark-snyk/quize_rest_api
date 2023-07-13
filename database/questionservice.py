from database.models import Question, db
import random

# get random questions
def get_questions_db(level):
    # if level doesn't choosen
    if level == "all":
        # get all quesions from db, then append them  ro new questions list randomly
        questions = []
        all_questions = Question.query.all

        # get 20 random questions
        for i in range(20):
            questions.append(random.choice(all_questions))
        return questions

    # if user choose level, using questions filter which is passing us from frontend, 'all' serving for correct display
    question_from_level = Question.query.filter_by(level=level).all()

    questions = [random.choice(question_from_level) for i in range(20)]
    return questions

# check user answer
def check_user_answer_db(question_id, user_answer):
    # working with primary key in questions id
    current_question = Question.query.get(question_id)

    # check user answer with answer in db
    if current_question.correct_answer == user_answer:
        return True

    return False

# добавление впоросов в базу дз