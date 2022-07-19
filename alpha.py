from random import randrange, choice
import logging
logging.basicConfig(level=logging.INFO)

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')


def roll(rounds):
    dice = randrange(2, 12)
    speed_die = choice(['bus', 'mr', 1, 2, 3, 'mr'])
    if rounds > 0:
        return [dice, speed_die]
    return dice

def get_property(position):
    ...

def get_user_balance(user):
    ...


def main():
    properties = {
        "Mediterranean Avenue",
        "Baltic Avenue",
        "Reading RR",
        "Oriental Avenue",
        "Vermont Avenue",
        "Connecticut Avenue",
        "St. Charles Place",
        "Electric Company",
        "States Avenue",
        "Virginia Avenue",
        "Pennsylvania RR",
        "St. James Place",
        "Tennessee Avenue",
        "New York Avenue",
        "Kentucky Avenue",
        "Indiana Avenue",
        "Illinois Avenue",
        "B&O RR",
        "Atlantic Avenue",
        "Ventnor Avenue",
        "Water Works",
        "Marvin Gardens",
        "Pacific Avenue",
        "North Carolina Avenue",
        "Pennsylvania Avenue",
        "Short Line",
        "Park Place",
        "Boardwalk"
    }

    print(roll(rounds=1))
    print(roll(rounds=0))

if __name__ == '__main__':
    main()
