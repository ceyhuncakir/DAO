class Simulation:
    def __init__(
        self, 
        iterations: int
    ) -> None:

        self.__iterations = iterations

    def run(
        self
    ) -> None:
        
        for t in range(self.__iterations):
            pass
            

if __name__ == "__main__":
    simulation = Simulation(iterations=100)
    simulation.run()