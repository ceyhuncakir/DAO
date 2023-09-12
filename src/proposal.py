from typing import List

import time

class Proposal:
    def __init__(
            self, 
            proposer: str, 
            proposal: str, 
            choises: List[str]
        ) -> None:
        
        self.proposer = owner
        self.proposal = proposal 
        self.choises = choises
        self.timestamp = time.time()