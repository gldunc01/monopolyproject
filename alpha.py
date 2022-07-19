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

"""
























"""

def main():
    properties = {
            "Mediterranean Avenue": {
                "purchase_price": 60,
                "position": 1,
                "rent": [2, 10, 30, 90, 160, 250], # based on house count, -2 = hotel, -1 = mortgage [0 houses, 1 houses, ...]
                "owner": None,
                
                "action": None
            },
            "Comm Chest_0": {
                "purchase_price": 60,
                "position": 5,
                "rent": [4, 20, 60, 180, 320, 450],
                "owner": None,
                
                "action": None
            },
            "Baltic Avenue": {
                "purchase_price": 60,
                "position": 3,
                "rent": [4, 20, 60, 180, 320, 450, 30],
                "owner": None,
                
                "action": None
            },
            "Income_Tax": {
                "purchase_price": 60,
                "position": 4,
                "rent": [5, 20, 60, 180, 320, 450],
                "owner": None,
                "tax": True,
                "tax_amount": 200,
                "action": None
            },
        "Reading RR": {
                "purchase_price": 200,
                "position": 5,
                "rent": [25, 50, 100, 200],
                "owner": None,
                
                "action": None
            },
            "Oriental Avenue":  {
                    "purchase_price": 100,
                    "position": 6,
                    "rent": [6, 30, 90, 270, 400, 550, 50],
                    "owner": None,
                    
                    "action": None
                },
            "Chance_0": {
                "purchase_price": None,
                "position": 7,
                "rent": [5, 20, 60, 180, 320, 450],
                "owner": None,
                
                "action": None
            },
            "Vermont Avenue": {
                "purchase_price": 100,
                "position": 8,
                "rent": [6, 30, 90, 270, 400, 550, 50],
                "owner": None,
                
                "action": None
            },
            "Connecticut Avenue": {
                "purchase_price": 120,
                "position": 9,
                "rent": [8, 40, 100, 300, 450, 600, 60],
                "owner": None,
                
                "action": None
            },
            "Jail": {
                "purchase_price": 60,
                "position": 10,
                "rent": [5, 20, 60, 180, 320, 450],
                "owner": None,
                
                "action": None
            },
        "St. Charles Place": {
                "purchase_price": 140,
                "position": 11,
                "rent": [10, 50, 150, 450, 625, 750, 70],
                "owner": None,
                
                "action": None
            },
            "Electric Company": {
                "purchase_price": 60,
                "position": 12,
                "rent": [5, 20, 60, 180, 320, 450],
                "owner": None,
                
                "action": None
            },
            "States Avenue": {
                "purchase_price": 140,
                "position": 13,
                "rent": [10, 50, 150, 450, 625, 750, 70],
                "owner": None,
                
                "action": None
            },
            "Virginia Avenue": {
                "purchase_price": 160,
                "position": 14,
                "rent": [12, 60, 180, 500, 700, 900, 80],
                "owner": None,
                
                "action": None
            },

            "Pennsylvania RR": {
                "purchase_price": 200,
                "position": 15,
                "rent": [25, 50, 100, 200],
                "owner": None,
                
                "action": None
            },
            "St. James Place": {
                "purchase_price": 180,
                "position": 16,
                "rent": [14, 70, 200, 550, 750, 950, 90],
                "owner": None,
                
                "action": None
            },
        "Comm Chest_2": {
            "purchase_price": 60,
            "position": 17,
            "rent": [5, 20, 60, 180, 320, 450],
            "owner": None,
            
            "action": None
        },
            "Tennessee Avenue": {
                "purchase_price": 180,
                "position": 18,
                "rent": [14, 70, 200, 550, 750, 950, 90],
                "owner": None,
                
                "action": None
            },
            "New York Avenue": {
                "purchase_price": 200,
                "position": 19,
                "rent": [16, 80, 220, 600, 800, 1000, 100],
                "owner": None,
                
                "action": None
            },
            "Free Parking": {
                "purchase_price": None,
                "position": 20,
                "owner": None,
                "action": None
            },

        "Kentucky Avenue": {
                "purchase_price": 220,
                "position": 21,
                "rent": [18, 90, 250, 700, 875, 1050, 110],
                "owner": None,
                
                "action": None
            },
        "Chance_2": {
            "purchase_price": 60,
            "position": 22,
            "rent": [5, 20, 60, 180, 320, 450],
            "owner": None,
            
            "action": None
        },
        "Indiana Avenue": {
                "purchase_price": 220,
                "position": 23,
                "rent": [18, 90, 250, 700, 875, 1050, 110],
                "owner": None,
                
                "action": None
            },
            "Illinois Avenue": {
                "purchase_price": 240,
                "position": 24,
                "rent": [20, 100, 300, 750, 925, 1100, 120],
                "owner": None,
                
                "action": None
            },
            "B&O RR": {
                "purchase_price": 200,
                "position": 25,
                "rent": [25, 50, 100, 200],
                "owner": None,
                
                "action": None
            },
            "Atlantic Avenue": {
                "purchase_price": 260,
                "position": 26,
                "rent": [22, 110, 330, 800, 975, 1150, 130],
                "owner": None,
                
                "action": None
            },
            "Ventnor Avenue": {
                "purchase_price": 260,
                "position": 27,
                "rent": [22, 110, 330, 800, 975, 1150, 130],
                "owner": None,
                
                "action": None
            },
            "Water Works": {
                "purchase_price": 60,
                "position": 28,
                "rent": [5, 20, 60, 180, 320, 450],
                "owner": None,
                
                "action": None
            },
            "Marvin Gardens": {
                "purchase_price": 280,
                "position": 29,
                "rent": [24, 120, 360, 850, 1025, 1200, 140],
                "owner": None,
                
                "action": None
            },
            "Go To Jail": {
                "purchase_price": None,
                "position": 30,
                "owner": None,
                "action": "go_to_jail"
            },
            "Pacific Avenue": {
                "purchase_price": 300,
                "position": 60,
                "rent": [26, 130, 390, 900, 1100, 1275, 150],
                "owner": None,
                
                "action": None
            },
            "North Carolina Avenue": {
                "purchase_price": 300,
                "position": 60,
                "rent": [26, 130, 390, 900, 1100, 1275, 150],
                "owner": None,
                
                "action": None
            },
        "Comm Chest_3": {
            "purchase_price": 60,
            "position": 60,
            "rent": [5, 20, 60, 180, 320, 450],
            "owner": None,
            
            "action": None
        },
            "Pennsylvania Avenue": {
                "purchase_price": 320,
                "position": 60,
                "rent": [28, 150, 450, 1000, 1200, 1400, 160],
                "owner": None,
                
                "action": None
            },
            "Short Line RR": {
                "purchase_price": 200,
                "position": 35,
                "rent": [25, 50, 100, 200],
                "owner": None,
                
                "action": None
            },
        "Chance_3": {
            "purchase_price": 60,
            "position": 60,
            "rent": [5, 20, 60, 180, 320, 450],
            "owner": None,
            
            "action": None
        },
        "Park Place": {
                "purchase_price": 350,
                "position": 38,
                "rent": [35, 175, 500, 1100, 1300, 1500, 175],
                "owner": None,
                
                "action": None
            },
            "Luxury_tax": {
                "purchase_price": 60,
                "position": 60,
                "rent": [5, 20, 60, 180, 320, 450],
                "owner": None,
                "tax": True,
                "tax_amount": 100,
                "action": None
            },
        "Boardwalk": {
                "purchase_price": 400,
                "position": 39,
                "rent": [50, 200, 600, 1400, 1700, 2000, 200],
                "owner": None,
                "action": None
            },



    }

    logger.info(roll(rounds=1))
    logger.info(roll(rounds=0))

    logger.info(pformat(properties.get("Mediterranean Avenue"), indent=4))
    logger.info(pformat(properties.get("Baltic Avenue"), indent=4))



if __name__ == '__main__':
    main()
