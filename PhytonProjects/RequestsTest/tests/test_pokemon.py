import requests
import pytest

token = '1f7dfdb6a62e17a1c65a904d95445bf6'
host = 'https://pokemonbattle.me:9104'

def test_status_code():
 gettrainer = requests.get(f'{host}/trainers', 
                              params= {'trainer_id' : 4244})

 assert gettrainer.status_code == 200

def test_name():
 body = requests.get(f'{host}/trainers', 
                     params= {'trainer_id' : 4244})
 
 assert body.json()['trainer_name'] == 'bidawg'

