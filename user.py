
"""Module to generate random  users"""
import faker
import logging
from pathlib import Path
BASE_DIR =Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR/'user.log',level=logging.INFO)

fake= faker.Faker()

def user_number():
    """

    :return:
        int:n
    """

    n = 0
    while n==0:
        n=input("Combien Utilisateur aimerais génerer avec faker \u1770 :")
    try:
        numb=int(n)
    except ValueError:

        print("A number did must be a string \u4048 :")
    logging.info(f"Generating {n} number")
    return numb



def get_user():
    """generateba single user

    :return:
        str:user
    """
    logging.info("Generating user ")
    return f"{fake.first_name()}  {fake.last_name()}"

def get_users(n):
    """generate a list of users

    :param:
     n(int): Number of user to generate
    :return:
    list[str] :list of users
    """
    logging.info(f"Generating à list of {n} users .")
    for i in range(1,n):
        return  [get_user() for _ in range(n)]


if __name__ =="__main__":

    user = get_users(user_number())
    print(user)

