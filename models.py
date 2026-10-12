# from sqlmodel import create_engine, SQLModel, Session


# db_url = "sqlite:///my_test.db"
# engine = create_engine(db_url,echo=True)

# def build_tables():
#     SQLModel.metadata.create_all(engine)

# def perform_db_task():
#     with Session(engine) as session:
#         pass
# from typing import Optional
# from sqlmodel import Field,create_engine,SQLModel,Session,select
# class User(SQLModel,table = True):
#     id: Optional[int] = Field(default =None, primary_key = True)
#     name: str

# engine = create_engine("sqlite:///my_test.db")
# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     user_1 = User(name = "yash")
#     session.add(user_1)
#     session.commit()

#     session.refresh(user_1)
#     print("Inserted user id: ", user_1.id)

#     statement = select(User).where(User.name == 'yash')
#     results = session.exec(statement)
#     user = results.first()

#     print("User found :", user.name if user else "User not found")
from typing import Optional
from sqlmodel import SQLModel,Field

class debatesession(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    topic: str
    status: str = "active"

    agent_a_name:str = "agent_a"
    agent_b_name:str = "agent_b"
    tone_style:str = "academic"



class debateTurn(SQLModel, table = True):
    id: Optional[int] = Field(default=None,primary_key=True)
    session_id: int = Field(foreign_key= "debatesession.id")
    speaker_type:str
    agent_name :str
    argument_text: str
    turn_number: int