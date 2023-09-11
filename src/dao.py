class Dao:
    def __init__(
            self
        ) -> None:
        
        self.current_proposal = None
        self.rejected_proposals = []
        self.accepted_proposals = []
        self.past_proposals = []
        self.time = 0
        self.treasury = 0

    def get_current_proposal(
            self
        ) -> object:

        return self.current_proposal

    def update(
            self, 
            time: int
        ) -> int:

        self.time = time

    def __repr__(
            self
        ) -> str:
        
        return f''