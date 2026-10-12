from typing import Literal
from pydantic import BaseModel, Field


class SpeakerTurn(BaseModel):
    speaker_id: str
    role: Literal["debater_a", "debater_b", "moderator"]
    content: str
    turn_index: int = Field(ge=0, description="Turn count cannot be negative")


class SessionConfig(BaseModel):
    topic: str
    max_turns: int = Field(default=6, gt=0, description="A debate must consist of at least 1 turn")
    strict_fallacy_check: bool = True


if __name__ == "__main__":
    # Test valid construction
    valid_payload = {
        "speaker_id": "debater_01",
        "role": "debater_a",
        "content": "Renewable energy infrastructure yields long-term net positive margins.",
        "turn_index": 0,
    }

    turn = SpeakerTurn(**valid_payload)
    print("Valid model loaded successfully:\n", turn)

    print("\nTriggering validation error check:")
    try:
        invalid_turn = SpeakerTurn(
            speaker_id="rogue_user",
            role="audience",  # Not in Literal
            content="Testing bad input",
            turn_index=-1,  # Violates ge=0
        )
    except Exception as err:
        print(err)