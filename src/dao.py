from typing import List
from agent import Agent

class Dao:
    def __init__(
        self
    ) -> None:
        
        self.__name = None
        self.__founder = None
        self.__co_founders = []
        self.__members = []
        self.__current_proposal = None
        self.__rejected_proposals = []
        self.__accepted_proposals = []
        self.__past_proposals = []
        self.__time = 0
        self.__treasury = 0

    def get_current_proposal(
        self
    ) -> object:

        return self.__current_proposal

    def get_past_proposals(
        self
    ) -> List[object]:
        
        return self.__past_proposals

    def get_accepted_proposals(
        self
    ) -> List[object]:

        return self.__accepted_proposals

    def get_rejected_proposals(
        self,
    ) -> List[object]:

        return self.__rejected_proposals

    def get_members(
        self
    ) -> List[object]:

        return self.__members

    def get_co_founders(
        self
    ) -> List[object]:

        return self.__co_founders

    def get_founder(
        self
    ) -> object: 
        
        return self.__founder

    def get_treasury(
        self
    ) -> int:
        
        return self.__treausre

    def update(
        self, 
        time: int
    ) -> int:

        self.time = time

    def __repr__(
        self
    ) -> str:
        
        return f'''
                DAO: {self.__name}, 
                Founder: {self.__founder}, 
                Co-founders: {self.__co_founders}, 
                Amount of mmebers: {len(self.__members)}
                Treasury: {self.__treasury}
            '''