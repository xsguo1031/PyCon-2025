# first scenario: compute the price of items 
def compute_price(number_of_items: int, price_for_item: float) -> float:
        if number_of_items > 9:
              print(number_of_items)
              return round(number_of_items * price_for_item*0.9, 2)
            #   return round(number_of_items * price_for_item*0.9, 3) 
           
        return number_of_items * price_for_item


# second scenario: improve the function to support retrieving prices form an external HTTP service 
import os
import requests

def compute_price_from_ext_server(number_of_items: int, item_id: int) -> float:
    server_id = os.environ.get("PRICE_HTTP_SERVER", "https://myownserver")
    result = requests.get(f'{server_id}/{item_id}')
    if result.status_code == 200:
        price = result.json()['price']
        return compute_price(number_of_items, price)

# third scenario: retrieve the price from a on-the-fly spawned HTTP server  
