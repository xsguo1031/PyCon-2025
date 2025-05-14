# # second scenario: improve the function to support retrieving prices form an external HTTP service 

# from unittest.mock import patch, MagicMock, Mock
# from price import compute_price_from_ext_server 
# import requests
# class TestComputePriceFromServerCase():
#     @patch('requests.get')
#     def test_compute_price_from_ext_server(self, mock_request_get: MagicMock):
#         #given 
#         result = Mock(status_code=200)
#         mock_request_get.return_value = result
#         result.json.return_value = dict(price = 1.0)


#         number_of_items = 5
#         item_id = 1   
#         price = compute_price_from_ext_server(number_of_items = 5,item_id = 1)
#         assert price == 5.0

#         mock_request_get.assert_called_once_with('https://myownserver/1')
    

# result = requests.get('https://priceserver.com/1')


# second scenario: improve the function to support retrieving prices from an external HTTP service 




from unittest.mock import patch, MagicMock, Mock
from price import compute_price_from_ext_server 
import requests

class TestComputePriceFromServerCase:
    @patch('requests.get')
    def test_compute_price_from_ext_server(self, mock_request_get: MagicMock):
        # given 
        result = Mock(status_code=200)
        mock_request_get.return_value = result
        result.json.return_value = dict(price=1.0)

        number_of_items = 5
        item_id = 1   
        
        # when
        price = compute_price_from_ext_server(number_of_items=5, item_id=1)
        
        # then
        assert price == 5.0
        mock_request_get.assert_called_once_with('https://myownserver/1')
