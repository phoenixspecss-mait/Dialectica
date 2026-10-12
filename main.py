from sqlmodel import SQLModel, Session, select
from database import engine
from models import debatesession, debateTurn

SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    new_session = debatesession(
        topic="Who is the true goat of football",
        agent_a_name="Ronaldo",
        agent_b_name= "Messi",
        tone_style="brutal_roast",
    )
    session.add(new_session)
    session.commit()
    session.refresh(new_session)
    session_id = new_session.id

    print(f"Created session #{session_id} : {new_session.agent_a_name} vs"
          f"{new_session.agent_b_name} [{new_session.tone_style}]"
          )
with Session(engine) as session:
    turns = [
      debateTurn(
          session_id=session_id,
          speaker_type="agent_a",
          agent_name="Ronaldo",
          argument_text=(
              "I won titles in 3 different leagues. You stayed in your comfort"
              " zone!"
          ),
          turn_number=1,
      ),
      debateTurn(
          session_id=session_id,
          speaker_type="agent_b",
          agent_name="Messi",
          argument_text=(
              "I have 8 Ballons d'Or and a World Cup. Keep posting workout"
              " videos."
          ),
          turn_number=2,
      ),
      # User Live Interruption!
      debateTurn(
          session_id=session_id,
          speaker_type="user",
          agent_name="Yash",
          argument_text=(
              "Both of you are washed up, Pele' is the real GOAT!"
          ),
          turn_number=3,
      ),
      # AI Roasted the User
      debateTurn(
          session_id=session_id,
          speaker_type="agent_a",
          agent_name="Ronaldo",
          argument_text="Who invited this user? Stick to watching from the bench!",
          turn_number=4,
      ),
  ]

    for turn in turns:
        session.add(turn)
    session.commit()
    print("All turns (including the user interuption) are saved")

with Session(engine) as session:
    statement = (
        select(debateTurn)
        .where(debateTurn.session_id == session_id)
        .order_by(debateTurn.turn_number)
    )

    results = session.exec(statement).all()
    print("\n--- Debate History ---")

    for turn in results:
        tag = "[INTERRUPTION]" if turn.speaker_type == "user" else ""
        print(f"Turn {turn.turn_number} {tag} {turn.agent_name}: {turn.argument_text}")