import os

import yagmail

from src.models.group import Group
from src.values.user_values import SecretSantaUser


def generate_smtp_session() -> yagmail.SMTP:
    sender = os.environ.get("EMAIL_ADDRESS")
    password = os.environ.get("EMAIL_PASSWORD")
    # initializing the server connection
    yag = yagmail.SMTP(user=sender, password=password)
    return yag


def send_email(yag: yagmail.SMTP, secret_santa_user: SecretSantaUser, group: Group):
    try:
        subject = "Secret Santa Assignement"
        contents = (
            f"Hello {secret_santa_user.santa.name},\n\n"
            "You are the secret santa of "
            f"{secret_santa_user.surprisee.name} for the group {group.name}: {group.description}.\n\n"
            "Merry christmas,\n"
            "Secret Santa Assigner Team"
        )
        yag.send(to=secret_santa_user.santa.email, subject=subject, contents=contents)
    except BaseException as e:
        raise e
