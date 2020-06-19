from game import Game
from funcs import playMatchesBetweenVersions
import loggers as lg

run_version = 1
ai_player_version = 1
env = Game()
#how many rounds
episodes = 1


def play_one_round():
    go_first = raw_input('Do you want to go first (y/n)?')
    if go_first.lower() == "y": 
        #use -1 for human player
        player1_version = -1
        player2_version = ai_player_version
    else:
        player1_version = ai_player_version
        player2_version = -1

    playMatchesBetweenVersions(env, run_version, player1_version, player2_version, episodes, lg.logger_play_game, 0)

print "Playing %s against AI." % env.name

while True:
    play_one_round()
    play_again = raw_input('Do you want to play again (y/n)?')
    if play_again.lower() != 'y':
        print "Good Bye.."
        break
