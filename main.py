from controller.controller import run as controller
from database import init_db

def run():
    controller()

if __name__ == "__main__":
    run()