## This program prints 5 cards using an API that simulates dealing a deck of cards
## Author: Francesca Ruberto

import requests

#Shuffle a new deck
url= ("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
response = requests.get(url)

# Get the deck id
deck = response.json()
deck_id = deck['deck']

# Draw 5 cards from the deck
draw_cards_url = "https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=5"
response = requests.get(url)
cards = response.json()

