from typing import List

import time

class Proposal:
    def __init__(
            self, 
            owner: str, 
            proposal: str, 
            choises: List[str]
        ) -> None:
        
        self.proposal_owner = owner
        self.proposal = proposal 
        self.choises = choises
        self.timestamp = time.time()