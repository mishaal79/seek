from flask.cli import FlaskGroup
from seek import create_app, db
from seek.api.models import User

cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_database")
def recreate_database():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_database")
def seed_database():
    db.session.add(User(username="Michael", password="Plaintext"))
    db.session.add(User(username="John", password="JohnsPassword"))
    db.session.commit()


if __name__ == "__main__":
    cli()
