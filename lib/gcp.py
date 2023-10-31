# Connection to GCP
import os
from dotenv import load_dotenv
import pandas as pd
from google.cloud import bigquery

load_dotenv()


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "movie-grader-394211-4edbebb0a607.json"
TABLE_NAME = os.getenv('TABLE_NAME')

# def bq_client(credentials_path):
#     # return bigquery.Client()
#     return bigquery.Client.from_service_account_json(credentials_path)


def client():
    return bigquery.Client()

def basic_query_job(client):

    QUERY = (
        'SELECT * from {TABLE_NAME}'
    )
    job = client.query(QUERY)
    final_job = job.result().to_dataframe()
    return final_job


def user_login(client, email: str, password: str)->int:
    QUERY = (
        f"""SELECT email, password FROM {TABLE_NAME} WHERE email = '{email}' and password = '{password}'"""
    )
    job = client.query(QUERY)
    login_job = job.result().to_dataframe()
    user_in_database =  len(login_job)
    QUERY = f"""UPDATE {TABLE_NAME} SET logged_in = True WHERE email = '{email}' and password = '{password}'"""
    job = client.query(QUERY)
    result = job.result()
    return user_in_database


# User Signup should also include a function to make sure there are no matching accounts
def user_signup(client, first_name: str, last_name: str, handle: str, email: str, dob: str, phone_prefix: str, phone_number: str, ethnicity: str, race: str, gender: str, gender_identity: str, sexual_orientation: str, political_party: str, password: str):
    existing_user = user_exists(client, email)
    if not existing_user:
        QUERY = f"""
        INSERT INTO {TABLE_NAME} VALUES (GENERATE_UUID(), '{first_name}', '{last_name}',
        '{handle}', '{email}', '{password}', '{ethnicity}', '{race}', '{gender}', '{gender_identity}', '{sexual_orientation}', '{dob}', 
        '{phone_prefix}', '{phone_number}', '{political_party}', {True})
        """
        job = client.query(QUERY)
        result = job.result()
        # return result
        return 'Signup Successful!'
    else:
        return 'User Already Exists'

def user_exists(client, email):
    QUERY = f"""SELECT * FROM {TABLE_NAME} WHERE email = '{email}'"""
    job = client.query(QUERY)
    result_len = len(job.result().to_dataframe())
    return True if result_len > 0 else False

if __name__ == '__main__':
    c = client()    
    # print(query_job(c))
    # print(user_login(c, 'drue@email.com', 'drue_pass123v'))
    print(user_signup(c, 'Albus', 'Dumbledore', 'elderWand', 'dd@email.com', '10-4-1213', '1', '892-343-4233', 'Prefer Not to Disclose', 'Prefer Not to Disclose', 'Prefer Not to Disclose', 'Prefer Not to Disclose', 'Prefer Not to Disclose', 'Prefer Not to Disclose', 'dd_pass123'))  
    # print(user_exists(c, 'drue@email.com'))
    print('Done')