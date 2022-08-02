from concurrent.futures.process import _ExceptionWithTraceback
from random import randrange, choice
import logging
from pprint import pformat

logging.basicConfig(level=logging.INFO)


# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.INFO)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
# formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s') # has module name, useful later
formatter    = logging.Formatter('%(asctime)s : %(levelname)s :   %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
# logger.debug('A debug message')
# logger.info('An info message')
# logger.warning('Something is not right.')
# logger.error('A Major error has happened.')
# logger.critical('Fatal error. Cannot continue')

players = [] #where the players will be added

#gets how many players are playing, no more than 7, no less than 2, throws error message if input is something other than an integer
while True:
    try:
        player_count = int(input('How many players are playing today?: '))
       #collects and appends player names to players list
        if player_count >= 2 and player_count <= 7:
            if player_count >= 2:
                player1 = input('Player 1: ')
                players.append(player1)
                player2 = input('Player 2: ')
                players.append(player2)
            if player_count >= 3:
                player3 = input('Player 3: ')
                players.append(player3)
            if player_count >= 4:
                player4 = input('Player 4: ')
                players.append(player4)
            if player_count >= 5:
                player5 = input('Player 5: ')
                players.append(player5)
            if player_count >= 6:
                player6 = input('Player 6: ')
                players.append(player6)
            if player_count == 7:
                player7 = input('Player 7: ')
                players.append(player7)
            break
        elif player_count < 2:
            print('Error occured, you need at least 2 players to play, please try again')
        elif player_count > 7:
                print('Error, you cannot have more than 7 players')
    except:
        print('Error occured, please try again')

current_position = [0,0,0,0,0,0,0]  #where they currently are on the board
current_balance = [1500,1500,1500,1500,1500,1500,1500]  #how much money held currently
properties_owned = [[],[],[],[],[],[],[]] #Where properties owned will be stored

def roll(rounds):
    dice = randrange(2, 12)
    speed_die = choice(['bus', 'mr', 1, 2, 3, 'mr'])
    if rounds > 0:
        return [dice, speed_die]
    return dice


def get_property(name):
    ...

def get_user_balance(user):
    ...


def main():
    properties = {
            "Go": {
                "purchase_price": None,
                "position": 0,
                "rent": None,
                "owner": None,
                "action": "collect $200",
                "group": None
            },
            "Mediterranean Avenue": {
                "purchase_price": 60,
                "position": 1,
                "rent": [2, 10, 30, 90, 160, 250, 30], # based on house count, -2 = hotel, -1 = mortgage [0 houses, 1 houses, ...]
                "owner": None,
                "action": None,
                "group": "brown"
            },
            "Comm Chest_0": {
                "purchase_price": None,
                "position": 2,
                "rent": None,
                "owner": None,
                "group": None,
                "action": {1:"Advance to Go, collect $200",
                2:"Bank error in your favor, collect $200",
                3:"Doctors fee. Pay $50",
                4:"From sale of stock you get $50",
                5:"Get Out of Jail Free",
                6:"Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
                7:"Holiday fund matures. Receive $100",
                8:"Income tax refund. Collect $20",
                9:"It is your birthday. Collect $10 from every player",
                10:"Life insurance matures. Collect $100",
                11:"Pay hospital fees of $100",
                12:"Pay school fees of $50",
                13:"Receive $25 consultancy fee",
                14:"You are assessed for street repair. $40 per house. $115 per hotel",
                15:"You have won second prize in a beauty contest. Collect $10",
                16:"You inherit $100"}
            },
            "Baltic Avenue": {
                "purchase_price": 60,
                "position": 3,
                "rent": [4, 20, 60, 180, 320, 450, 30],
                "owner": None,
                "group": "brown",
                "action": None
            },
            "Income_tax": {
                "purchase_price": None,
                "position": 4,
                "owner": None,
                "group": None,
                "tax": True,
                "tax_amount": 200,
                "action": "pay_tax"
            },
        "Reading RR": {
                "purchase_price": 200,
                "position": 5,
                "rent": [25, 50, 100, 200],
                "owner": None,
                "group": "railroad",
                "action": None
            },
            "Oriental Avenue":  {
                    "purchase_price": 100,
                    "position": 6,
                    "rent": [6, 30, 90, 270, 400, 550, 50],
                    "owner": None,
                    "group": "light blue",
                    "action": None
                },
            "Chance_0": {
                "purchase_price": None,
                "position": 7,
                "rent": None,
                "owner": None,
                "group": None,
                "action": {1:"Advance to Boardwalk",
                2:"Advance to Go, collect $200",
                3:"Advance to Illinois Avenue. If you pass Go, collect $200",
                4:"Advance to St. Charles Place. If you pass Go, collect $200",
                5:"Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
                6:"Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
                7:"Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",
                8:"Bank pays you dividend of $50",
                9:"Get Out of Jail Free",
                10:"Go Back 3 Spaces",
                11:"Go to Jail. Go directly to Jail, do not pass Go, do not collect $200",
                12:"Make general repairs on all your property. For each house pay $25. For each hotel pay $100",
                13:"Speeding fine $15",
                14:"Take a trip to Reading Railroad. If you pass Go, collect $200",
                15:"You have been elected Chairman of the Board. Pay each player $50",
                16:"Your building loan matures. Collect $150"}
            },
            "Vermont Avenue": {
                "purchase_price": 100,
                "position": 8,
                "rent": [6, 30, 90, 270, 400, 550, 50],
                "owner": None,
                "group": "light blue",
                "action": None
            },
            "Connecticut Avenue": {
                "purchase_price": 120,
                "position": 9,
                "rent": [8, 40, 100, 300, 450, 600, 60],
                "owner": None,
                "group": "light blue",
                "action": None
            },
            "Jail": {
                "purchase_price": None,
                "position": 10,
                "rent": None,
                "owner": None,
                "group": None,
                "action": None
            },
        "St. Charles Place": {
                "purchase_price": 140,
                "position": 11,
                "rent": [10, 50, 150, 450, 625, 750, 70],
                "owner": None,
                "group": "maroon",
                "action": None
            },
            "Electric Company": {
                "purchase_price": 150,
                "position": 12,
                "rent": [5, 20, 60, 180, 320, 450], #rent should be equal to dice roll times 4?
                "owner": None,
                "group": None,
                "action": None
            },
            "States Avenue": {
                "purchase_price": 140,
                "position": 13,
                "rent": [10, 50, 150, 450, 625, 750, 70],
                "owner": None,
                "group": "maroon",
                "action": None
            },
            "Virginia Avenue": {
                "purchase_price": 160,
                "position": 14,
                "rent": [12, 60, 180, 500, 700, 900, 80],
                "owner": None,
                "group": "maroon",
                "action": None
            },

            "Pennsylvania RR": {
                "purchase_price": 200,
                "position": 15,
                "rent": [25, 50, 100, 200],
                "owner": None,
                "group": "railroad",
                "action": None
            },
            "St. James Place": {
                "purchase_price": 180,
                "position": 16,
                "rent": [14, 70, 200, 550, 750, 950, 90],
                "owner": None,
                "group": "orange",
                "action": None
            },
        "Comm Chest_2": {
            "purchase_price": None,
            "position": 17,
            "rent": None,
            "owner": None,
            "group": None,
            "action": {1:"Advance to Go, collect $200",
                2:"Bank error in your favor, collect $200",
                3:"Doctors fee. Pay $50",
                4:"From sale of stock you get $50",
                5:"Get Out of Jail Free",
                6:"Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
                7:"Holiday fund matures. Receive $100",
                8:"Income tax refund. Collect $20",
                9:"It is your birthday. Collect $10 from every player",
                10:"Life insurance matures. Collect $100",
                11:"Pay hospital fees of $100",
                12:"Pay school fees of $50",
                13:"Receive $25 consultancy fee",
                14:"You are assessed for street repair. $40 per house. $115 per hotel",
                15:"You have won second prize in a beauty contest. Collect $10",
                16:"You inherit $100"}
        },
            "Tennessee Avenue": {
                "purchase_price": 180,
                "position": 18,
                "rent": [14, 70, 200, 550, 750, 950, 90],
                "owner": None,
                "group": "orange",
                "action": None
            },
            "New York Avenue": {
                "purchase_price": 200,
                "position": 19,
                "rent": [16, 80, 220, 600, 800, 1000, 100],
                "owner": None,
                "group": "orange",
                "action": None
            },
            "Free Parking": {
                "purchase_price": None,
                "position": 20,
                "owner": None,
                "action": None,
                "group": None
            },

        "Kentucky Avenue": {
                "purchase_price": 220,
                "position": 21,
                "rent": [18, 90, 250, 700, 875, 1050, 110],
                "owner": None,
                "group": "red",
                "action": None
            },
        "Chance_2": {
            "purchase_price": None,
            "position": 22,
            "rent": None,
            "owner": None,
            "group": None,
            "action": {1:"Advance to Boardwalk",
                2:"Advance to Go, collect $200",
                3:"Advance to Illinois Avenue. If you pass Go, collect $200",
                4:"Advance to St. Charles Place. If you pass Go, collect $200",
                5:"Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
                6:"Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
                7:"Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",
                8:"Bank pays you dividend of $50",
                9:"Get Out of Jail Free",
                10:"Go Back 3 Spaces",
                11:"Go to Jail. Go directly to Jail, do not pass Go, do not collect $200",
                12:"Make general repairs on all your property. For each house pay $25. For each hotel pay $100",
                13:"Speeding fine $15",
                14:"Take a trip to Reading Railroad. If you pass Go, collect $200",
                15:"You have been elected Chairman of the Board. Pay each player $50",
                16:"Your building loan matures. Collect $150"}
        },
        "Indiana Avenue": {
                "purchase_price": 220,
                "position": 23,
                "rent": [18, 90, 250, 700, 875, 1050, 110],
                "owner": None,
                "group": "red",
                "action": None
            },
            "Illinois Avenue": {
                "purchase_price": 240,
                "position": 24,
                "rent": [20, 100, 300, 750, 925, 1100, 120],
                "owner": None,
                "group": "red",
                "action": None
            },
            "B&O RR": {
                "purchase_price": 200,
                "position": 25,
                "rent": [25, 50, 100, 200],
                "owner": None,
                "group": "railroad",
                "action": None
            },
            "Atlantic Avenue": {
                "purchase_price": 260,
                "position": 26,
                "rent": [22, 110, 330, 800, 975, 1150, 130],
                "owner": None,
                "group": "yellow",
                "action": None
            },
            "Ventnor Avenue": {
                "purchase_price": 260,
                "position": 27,
                "rent": [22, 110, 330, 800, 975, 1150, 130],
                "owner": None,
                "group": "yellow",
                "action": None
            },
            "Water Works": {
                "purchase_price": 150,
                "position": 28,
                "rent": [5, 20, 60, 180, 320, 450], #rent should be dice times 4?
                "owner": None,
                "group": None,
                "action": None
            },
            "Marvin Gardens": {
                "purchase_price": 280,
                "position": 29,
                "rent": [24, 120, 360, 850, 1025, 1200, 140],
                "owner": None,
                "group": "yellow",
                "action": None
            },
            "Go To Jail": {
                "purchase_price": None,
                "position": 30,
                "owner": None,
                "group": None,
                "action": "go_to_jail"
            },
            "Pacific Avenue": {
                "purchase_price": 300,
                "position": 31,
                "rent": [26, 130, 390, 900, 1100, 1275, 150],
                "owner": None,
                "group": "green",
                "action": None
            },
            "North Carolina Avenue": {
                "purchase_price": 300,
                "position": 32,
                "rent": [26, 130, 390, 900, 1100, 1275, 150],
                "owner": None,
                "group": "green",
                "action": None
            },
        "Comm Chest_3": {
            "purchase_price": None,
            "position": 33,
            "rent": None,
            "owner": None,
            "group": None,
            "action": {1:"Advance to Go, collect $200",
                2:"Bank error in your favor, collect $200",
                3:"Doctors fee. Pay $50",
                4:"From sale of stock you get $50",
                5:"Get Out of Jail Free",
                6:"Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
                7:"Holiday fund matures. Receive $100",
                8:"Income tax refund. Collect $20",
                9:"It is your birthday. Collect $10 from every player",
                10:"Life insurance matures. Collect $100",
                11:"Pay hospital fees of $100",
                12:"Pay school fees of $50",
                13:"Receive $25 consultancy fee",
                14:"You are assessed for street repair. $40 per house. $115 per hotel",
                15:"You have won second prize in a beauty contest. Collect $10",
                16:"You inherit $100"}
        },
            "Pennsylvania Avenue": {
                "purchase_price": 320,
                "position": 34,
                "rent": [28, 150, 450, 1000, 1200, 1400, 160],
                "owner": None,
                "group": "green",
                "action": None
            },
            "Short Line RR": {
                "purchase_price": 200,
                "position": 35,
                "rent": [25, 50, 100, 200],
                "owner": None,
                "group": "railroad",
                "action": None
            },
        "Chance_3": {
            "purchase_price": None,
            "position": 36,
            "rent": None,
            "owner": None,
            "group": None,
            "action": {1:"Advance to Boardwalk",
                2:"Advance to Go, collect $200",
                3:"Advance to Illinois Avenue. If you pass Go, collect $200",
                4:"Advance to St. Charles Place. If you pass Go, collect $200",
                5:"Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
                6:"Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
                7:"Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",
                8:"Bank pays you dividend of $50",
                9:"Get Out of Jail Free",
                10:"Go Back 3 Spaces",
                11:"Go to Jail. Go directly to Jail, do not pass Go, do not collect $200",
                12:"Make general repairs on all your property. For each house pay $25. For each hotel pay $100",
                13:"Speeding fine $15",
                14:"Take a trip to Reading Railroad. If you pass Go, collect $200",
                15:"You have been elected Chairman of the Board. Pay each player $50",
                16:"Your building loan matures. Collect $150"}
        },
        "Park Place": {
                "purchase_price": 350,
                "position": 37,
                "rent": [35, 175, 500, 1100, 1300, 1500, 175],
                "owner": None,
                "group": "blue",
                "action": None
            },
            "Luxury_tax": {
                "purchase_price": None,
                "position": 38,
                "rent": None,
                "owner": None,
                "tax": True,
                "tax_amount": 100,
                "group": None,
                "action": "pay_tax"
            },
        "Boardwalk": {
                "purchase_price": 400,
                "position": 39,
                "rent": [50, 200, 600, 1400, 1700, 2000, 200],
                "owner": None,
                "group": "blue",
                "action": None
            },



    }
    logger.info(player_count)
    logger.info(players)
    logger.info(roll(rounds=1))
    logger.info(roll(rounds=0))

    logger.info(pformat(properties.get("Mediterranean Avenue"), indent=4))
    logger.info(pformat(properties.get("Comm Chest_3"), indent=4))



if __name__ == '__main__':
    main()
