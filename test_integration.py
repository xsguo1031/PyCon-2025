from pytest_httpserver import httpserver
from price import compute_price_from_ext_server
from pytest import fixture 
import os 
@fixture 
def item_id():
    yield 1 

@ fixture
def env_vars(httpserver, monkeypatch, item_id):
    monkeypatch.setenv("PRICE_HTTP-SERVER", f"http://localhost:{httpserver.port}")
    httpserver.expect_request(f"/{item_id}").respond_with_json({"price":5.0})
    
class TestIntegrationComputePriceCase:
    def test_compute_price_with_real_server(self, env_vars, item_id):
        # given 
        # item_id = "1"
        # os.environ["PRICE_HTTP_SERVER"] = f"http://localhost:{httpserver.port}"
        # server_id = os.environ.get("PRICE_HTTP_SERVER")
        # httpserver.expect_request(f"/{item_id}").respond_with_json({"price":5.0})
        # when 
        price = compute_price_from_ext_server(5, item_id)
        assert price == 25.0
        pass
