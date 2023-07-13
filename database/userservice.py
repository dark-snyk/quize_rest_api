from database.models import User, db

# process of user registration
def register_user_db(name, phone_number):
    checker = check_user_db(phone_number)
    if checker:
        return checker
    # create, if user doesn't exist
    new_user = User(name=name, phone_number=phone_number)
    # add new user and phone number to db
    db.session.add(new_user)
    db.session.commit()

    # pass it to frontend
    return new_user.id


# checking if phone number in db
def check_user_db(phone_number):
    # request to db User table, by phone_number
    # 'first()' allow us to get format that suitable for display, otherwise we get a raw object
    checker = User.query.filter_by(phone_number=phone_number).first()
    if checker:
        return checker.id
    return False