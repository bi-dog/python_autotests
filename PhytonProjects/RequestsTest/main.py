import requests 

token = '1f7dfdb6a62e17a1c65a904d95445bf6'
host = 'https://pokemonbattle.me:9104'

answer = requests.post(f'{host}/pokemons', json =
                       {
                           "name": "two",
                           "photo": "https://dolnikov.ru/pokemons/albums/107.png"
                       }, headers= {'Content-type' : 'application/json', 'trainer_token': token})

print(answer.status_code)
print(answer.text)

if answer.status_code == 201:
    pokemon_id = answer.json()['id']

    change = requests.put(f'{host}/pokemons', json =
                        {              
      "pokemon_id": pokemon_id,
      "name": "mmmm",
      "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                        }, headers= {'Content-type' : 'application/json', 'trainer_token' : token})
    
    print(change.status_code)
    print(change.text)
    
    ball = requests.post(f'{host}/trainers/add_pokeball', json =
                       {
                           "pokemon_id": pokemon_id
                       }, headers= {'Content-type' : 'application/json', 'trainer_token' : token})
    
    print(ball.status_code)
    print(ball.text)