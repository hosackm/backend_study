from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired
import random
import string

Base = declarative_base()
secret = "".join([random.choice(string.ascii_uppercase + string.digits) for _ in range(32)])


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def serialize(self):
        return {"username": self.username}

    def generate_auth_token(self, expires=600):
        s = TimedJSONWebSignatureSerializer(secret, expires_in=expires)
        return s.dumps({"id": self.id})

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer(secret)
        try:
            data = s.loads(token)
        except (SignatureExpired, BadSignature):
            return None
        else:
            return data.get("id")


engine = create_engine('sqlite:///bagelusers.db')
Base.metadata.create_all(engine)
