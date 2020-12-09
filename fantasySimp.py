# fantasy logic 
import numpy
class Player:
    def __init__(self, name, ID, positions, health_status, avg_stats, current_stats=[]):
        self.name, self.ID, self.positions, self.health_status self.avg_stats = name, ID, positions, health_status, avg_stats
        # name (string) - for developer identification
        # ID (int) - for accessing 
        # positions (list[strings]) - at least one of seven positions (G, PG, SG, F, SF, PF, C)
        # health_status (Boolean) - True for healthy, False for unhealthy
        # avg stats (list[double]) - 11 stat categories that players are evaluated upon

    def get_name(self):
        return self.name

    def get_ID(self):
        return self.ID

    def get_positions(self):
        return self.positions

    def get_avg_stats(self):
        return self.avg_stats

    def get_health_status(self):
        return self.health_status

    def injury(self):
        self.health_status = False

    def recover(self):
        self.health_status = True

class Owner:
    def __init__(self, name, team=[], lineup=[], record=[0, 0, 0], draft_pos, weekly_totals):
        self.name, self.team, self.lineup, self.record, self.draft_pos, self.weekly_totals = name, team, lineup, record, draft_pos, weekly_totals
        # name (string) - for developer identification
        # team (list[Player]) - list of players owned by the owner
        # lineup (list[Player]) - subset of team, limited by positions
        # record (list[int]) - number of wins, losses, and ties

    def update_record(self, wins, losses, ties):
        self.record[1] += wins
        self.record[2] += losses
        self.record[3] += ties

    def add_player(self, player, available_players):
        self.team.append(player)
        available_players.remove(player)

    def drop_player(self, player):
        self.team.remove(player)
        self.lineup.remove(player)

    def activate_player(self, player, lineup):
        self.lineup.append(player)

    def deactivate_player(self, player, lineup):
        self.lineup.remove(player)

    def get_weekly_totals(self, weekly_totals):
        return weekly_totals

class League:
    def __init__(self, ID, owners=[], available_players, standings, date, ):
        self.ID, self.owners, self.available_players, self.standings = ID, owners, available_players, standings
        # ID (int) - for keeping track of how many leagues have been simulated
        # owners (list[Owner]) - for carrying out league operations
        # available_players (list[Player]) - list of players available to draft/pick-up

    def create_owners(self, owners):
        for i in range(12):
            x = Owner(i,i, numpy.zeros(11))
            self.owners.append(x)

    def draft(self, owners, available_players):
        pass

    def create_schedule(self, owners):
        pass
    
    def injure_players(self, owners, available_players):
        pass

    def recover_players(self, owners, available_players):
        pass

    def sim_day(self, owners, available_players):
        pass

    def sim_week(self, owners, available_players, standings):
        pass

    def sim_season(self, owners, available_players, standings):
        pass

    def create_playoff_schedule(self, owners, standings):
        pass

