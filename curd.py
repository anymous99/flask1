from database import db
from models import User, SpeakingTest, ListeningTest


def add_user(data):
    name, email, password = data.get(
        "name"), data.get("email"), data.get("password")
    if not name or not email or not password:
        return {"error": "there is a missing field"}, 400
    user = User(name=name, email=email, password=password)
    try:
        db.session.add(user)
        db.session.commit()
        return {"message": "user added sucessfully", "user_id": user.id}, 201
    except Exception as e:
        db.session.rollback()
        return {"message": f"Got error :{str(e)}"}, 400


def getall_user():
    users = User.query.all()
    return [{"id": user.id, "name": user.name, "email": user.email}for user in users]


def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return [{"id": user.id, "name": user.name, "email": user.email}]
    return {"error": "no user found"}


def update_user(user_id, **kwargs):
    user = User.query.get(user_id)
    if user:
        try:
            for key, values in kwargs.items():
                setattr(user, key, values)
            db.session.commit()
            return {"message": "updated sucessfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": {str(e)}}
    return {"error": "use not found"}


def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            return {"message": "user deleted sucessfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}
    return {"error": "no user found"}

# Speakingtest


def add_Speakingtest(data):
    user_id = data.get("user_id")
    question, response, score = data.get(
        "question"), data.get("response"), data.get("score")
    if not user_id or not question or not response or not score:
        return {"error": "got error missing felids"}, 400
    test = SpeakingTest(user_id=user_id, question=question,
                        response=response, score=score)
    try:
        db.session.add(test)
        db.session.commit()
        return {"message": "sucessfully added"}, 200
    except Exception as e:
        db.session.rollback()
        return {"message": f"got error {str(e)}"}, 400


def selectall_Speakingtest():
    tests = SpeakingTest.query.all()
    return [{"user_id": test.user_id, "question": test.question, "response": test.response, "score": test.score} for test in tests]


def select_Speakingtest(user_id):
    tests = SpeakingTest.query.filter_by(user_id=user_id).all()
    if tests:
        return [{"id": test.id, "question": test.question, "response": test.response, "score": test.score} for test in tests]
    return {"error": "No speaking test found"}


def delete_Speakingtest(user_id):
    tests = SpeakingTest.query.filter_by(user_id=user_id).all()
    if tests:
        try:
            for test in tests:
                db.session.delete(test)
            db.session.commit()
            return {"message": "changed sucessfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": f"got {str(e)}"}


def update_Speakingtest(user_id, **kwargs):
    test = SpeakingTest.query.filter_by(user_id=user_id).all()
    if test:
        try:
            kwargs.pop('user_id', None)
            for tests in test:
                for key, value in kwargs.items():
                    setattr(tests, key, value)
            db.session.commit()
            return {"message": "Updated sucessfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": f"got {str(e)}"}, 400

# Listeningtest


def add_Listeningtest(data):
    user_id = data.get("user_id")
    question, response, score = data.get(
        "question"), data.get("response"), data.get("score")
    if not user_id or not question or not response or not score:
        return {"error": "got error missing felids"}, 400
    test = ListeningTest(user_id=user_id, question=question,
                         response=response, score=score)
    try:
        db.session.add(test)
        db.session.commit()
        return {"message": "data added sucessfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": f"Got {str(e)}"}


def update_Listeningtest(user_id, **kwargs):
    tests = ListeningTest.query.filter_by(user_id=user_id).all()
    if tests:
        try:
            for key, value in kwargs.items():
                setattr(tests, key, value)
            db.session.commit()

            return {"message": "updated sucessfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": f"got {str(e)}"}


def get_Listeningtest():
    tests = ListeningTest.query.all()
    return [{"question": test.question, "response": test.response, "score": test.score}for test in tests]


def gettestbyid_Listeningtest(user_id):
    test = ListeningTest.query.filter_by(user_id=user_id).first()
    if test:
        return {"id": test.id, "question": test.question, "response": test.response, "score": test.score}
    return {"error": "no user found"}


def delete_Listeningtest(user_id):
    test = ListeningTest.query.filter_by(user_id=user_id).all()
    if test:
        try:
            for tests in test:
                db.session.delete(tests)
            db.session.commit()
            return {"message": "changed sucessfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": f"got {str(e)}"}
