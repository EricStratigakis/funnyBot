
class Player:
    """ 
    We instantiate players at runtime when we want to run
    a simulation.  Therfor, we dont need 'ids', only player
    stats
    """
    def __init__(self, name):
        self.name = name
        pass
    # def __init__(self, name, ID, positions, health_status, avg_stats, current_stats=[]):
    #     self.name, self.ID, self.positions, self.health_status self.avg_stats = name, ID, positions, health_status, avg_stats
    #     # name (string) - for developer identification
    #     # ID (int) - for accessing 
    #     # positions (list[strings]) - at least one of seven positions (G, PG, SG, F, SF, PF, C)
    #     # health_status (Boolean) - True for healthy, False for unhealthy
    #     # avg stats (list[double]) - 11 stat categories that players are evaluated upon
    # def get_name(self):
    #     return self.name
    # def get_ID(self):
    #     return self.ID
    # def get_positions(self):
    #     return self.positions
    # def get_avg_stats(self):
    #     return self.avg_stats
    # def get_health_status(self):
    #     return self.health_status
    # def injury(self):
    #     self.health_status = False
    # def recover(self):
    #     self.health_status = True
