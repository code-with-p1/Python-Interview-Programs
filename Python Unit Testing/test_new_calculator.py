import unittest
from new_calculator import NewCalculator


class TestNewCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.cls = NewCalculator()

    def test_addition(self):
        self.assertEqual(self.cls.addition(5,5), 10)

if __name__ == "__main__":
    unittest.main()

'''

1. **Run a single test script**:
   ```sh
   python -m unittest tests/test_app.py
   ```

2. **Run all tests in a directory**:
   ```sh
   python -m unittest discover -s tests
   ```

3. **Run a specific test case**:
   ```sh
   python -m unittest tests.test_app.TestLogin.test_login_success
   ```

4. **Run tests with a specific pattern**:
   ```sh
   python -m unittest discover -s tests -p "test_*.py"
   ```

5. **Run tests verbosely**:
   ```sh
   python -m unittest -v tests/test_app.py
   ```

6. **Run all tests in a directory with verbose output**:
   ```sh
   python -m unittest discover -s tests -p "test_*.py" -v
   ```


'''