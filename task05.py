class Game:
    '''
    Class of game.
    '''
    def __init__(self, teams):
        self.__score = {
            teams['command1']: 0,
            teams['command2']: 0
        }
    
    def ball_thrown(self, command, points):
        '''
        Adds the number of points "points" to the "command" team.
        '''
        self.__score[command] += points

    def get_score(self):
        '''
        Returns the score as a tuple.
        '''
        return tuple(self.__score.values())
    
    def get_winner(self):
        '''
        Returns the winning team or a tie.
        '''
        res_team_1 = list(self.__score.items())[0]
        res_team_2 = list(self.__score.items())[1]
        points_list = [res_team_1[1], res_team_2[1]]
        
        if points_list[0] == points_list[1]:
            result = 'Ничья!'
        elif points_list[0] > points_list[1]:
            result = f'Победитель {res_team_1[0]}'
        else:
            result = f'Победитель {res_team_2[0]}'
        
        return result

teams = {
    'command1': 'Chicago Bulls',
    'command2': 'Toronto Raptors'
}

basketball = Game(teams)

basketball.ball_thrown('Chicago Bulls', 5)
basketball.ball_thrown('Toronto Raptors', 2)
basketball.ball_thrown('Chicago Bulls', 5)
basketball.ball_thrown('Toronto Raptors', 5)

print(basketball.get_score())
print(basketball.get_winner())
