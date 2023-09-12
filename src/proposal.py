from typing import List

class Proposal:
    def __init__(
        self, 
        proposer: str, 
        proposal: str, 
        choises: List[str],
        time: int
    ) -> None:
        
        self.__proposer = proposer
        self.__proposal = proposal 
        self.__choises = choises
        self.__timestamp = time

    
    def __repr__(
        self
    ) -> str:

        return f'''
                proposer: {self.__proposer}, 
                proposal: {self.__proposal}, 
                choises: {self.__choises}, 
                timestamp: {self.__timestamp}
            '''