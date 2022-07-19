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
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Comm Chest_0": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Baltic Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Reading RR": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Oriental Avenue":  {
                    "purchase_price": 60,
                    "position": 60,
                    "rent": 60,
                    "owner": 60,
                    "tax": False,
                    "action": None
                },
            "Chance_0": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Vermont Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Connecticut Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Jail": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
        "St. Charles Place": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Electric Company": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Virginia Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },

            "Pennsylvania RR": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "St. James Place": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
        "Comm Chest_2": {
            "purchase_price": 60,
            "position": 60,
            "rent": 60,
            "owner": 60,
            "tax": False,
            "action": None
        },
            "Tennessee Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "New York Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Kentucky Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
        "Chance_2": {
            "purchase_price": 60,
            "position": 60,
            "rent": 60,
            "owner": 60,
            "tax": False,
            "action": None
        },
        "Indiana Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Illinois Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "B&O RR": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Atlantic Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Ventnor Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Water Works": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Marvin Gardens": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Pacific Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "North Carolina Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
        "Comm Chest_3": {
            "purchase_price": 60,
            "position": 60,
            "rent": 60,
            "owner": 60,
            "tax": False,
            "action": None
        },
            "Pennsylvania Avenue": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Short Line": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
        "Chance_3": {
            "purchase_price": 60,
            "position": 60,
            "rent": 60,
            "owner": 60,
            "tax": False,
            "action": None
        },

        "Park Place": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
            "Luxury_tax": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },
        "Boardwalk": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },

            "Income_Tax": {
                "purchase_price": 60,
                "position": 60,
                "rent": 60,
                "owner": 60,
                "tax": False,
                "action": None
            },


    }

    logger.info(roll(rounds=1))
    logger.info(roll(rounds=0))

    logger.info(pformat(properties.get("Mediterranean Avenue"), indent=4))
    logger.info(pformat(properties.get("Baltic Avenue"), indent=4))



if __name__ == '__main__':
    main()
