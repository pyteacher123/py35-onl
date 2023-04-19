from dataclasses import dataclass
from typing import Optional


@dataclass
class SponsorTeamDTO:
    sponsor_id: int
    team_id: int
    start_date: int
    end_date: Optional[int]
