from database.models import Result, db, Rating

def get_rating_db(level):
    # getting data of all levels of difficulty
    user_position = Rating.query.order_by(Rating.user_correct_answer.desc()).filter(level=level)
    user_ids = [{i.user_id: i.user_correct_answers} for i in user_position]

    return user_ids[:5]

# add user answer hw
def add_user_answer_db(user_id, user_answer, correctness):
    result = Rating(user_id=user_id,user_answer=user_answer,correctness=correctness)
    db.session.add(result)
    db.session.commit()


def add_user_rating_db(user_id, correct_answer, level):
    # check if user in table rating += correct answer db
    user_rating = Rating.query.filter_by(user_id=user_id, level=level).first()

    if user_rating:
        user_rating.user_correct_answers += correct_answer
    else:
        user_rating = Rating(user_id=user_id, user_correct_answers=correct_answer, level=level)
        db.session.add(user_rating)
    db.session.commit()

# get user position in top
def get_user_position(user_id, level, correct_answers):

    register_user_rating = add_user_rating_db(user_id, correct_answers, level)
    user_position = Rating.query.order_by(Rating.user_correct_answers.desc()).filter_by(level=level)
    user_ids = [i.user_id for i in user_position]
    return user_ids.index(user_id) + 1