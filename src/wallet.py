class Wallet:
    def __init_(
        self
    ) -> None:
    
        self.__tokens = 0
        self.__unique_identifier = None

    def get_tokens(
        self
    ) -> int:

        return self.__tokens

    def get_unique_identifier(
        self,
    ) -> str:
        
        return self.__unique_identifier

    def __repr__(
        self
    ) -> str:
    
        return f'''
                wallet: {self.__unique_identifier}, 
                tokens: {self.__tokens}
            '''
