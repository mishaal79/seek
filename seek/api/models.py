from seek import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.id == o.id
        else:
            return False
