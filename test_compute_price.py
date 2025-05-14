# Auto testing 
# A utility function to compute price for an e-commerce 

# import importlib
# import importlib.metadata
# import sys


# # test if the packages are installed and have the right version
# REQUIREMENTS = {
#     "pytest": None,
#     "pytest-cov": None,
#     "pytest-httpserver": None,
#     "requests": None,
#     "mutmut": "2.5.1",
# }

# def check_packages():
#     all_good = True

#     for package, required_version in REQUIREMENTS.items():
#         try:
#             # Check if module can be imported
#             importlib.import_module(package.replace("-", "_"))

#             # Get installed version
#             installed_version = importlib.metadata.version(package)

#             if required_version and installed_version != required_version:
#                 print(f"[FAIL] {package} version mismatch: {installed_version} (required: {required_version})")
#                 all_good = False
#             else:
#                 print(f"[OK]   {package} {installed_version}")

#         except ModuleNotFoundError:
#             print(f"[FAIL] {package} not installed")
#             all_good = False
#         except importlib.metadata.PackageNotFoundError:
#             print(f"[FAIL] {package} metadata not found (possibly not installed properly)")
#             all_good = False

#     return all_good

# if __name__ == "__main__":
#     if not check_packages():
#         sys.exit(1)

# write a function that computes the price given the item price, the number of items and apply a fixed discuount if qunatity is greater than X
from price import compute_price 
import unittest   

class TestComputePriceCase(unittest.TestCase):
    def assert_price_semantic(self, price:float):
        price_as_str = str(price)
        integer_part, floating_part = price_as_str.split(".")
        assert len(integer_part) < 3


    def test_compute_price(self):
        # given 
        number_of_items = 10
        price_for_item =5.0
        # when 
        price = compute_price(number_of_items, price_for_item)
        # then 
        assert price is not None
        assert price == 45.0
        self.assert_price_semantic(price)

    def test_compute_price_with_discount(self):
        # given 
        number_of_items = 10
        price_for_item = 1.0
        # when 
        price = compute_price(number_of_items, price_for_item)
        # then 
        assert price is not None
        assert price == 9.0
        self.assert_price_semantic(price)


    def test_compute_with_floating_bug(self):
        price = compute_price(11,9.99)
        assert price is not None
        self.assert_price_semantic(price)



if __name__ == "__main__":
    unittest.main()
    
test_compute_price()



