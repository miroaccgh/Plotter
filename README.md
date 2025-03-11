# TDD Methodology and Syntax
## Stages
1. Red:
    Write a test that fails for the code has nto been written
    Get the code to succeed the test
2. Green:
    Test is succesful
3. Refactor:
    Refactor the code to be pythonic andcomplient with the conventions

## Basic test syntax
``` Python
def test_functionality():
    # Arrange: instanciate class
    client = Client()
    client.open_connection()
    # Act: perform functionality
    result = client.read_from_server()
    # Assert: Validate result from act, which results in a success or failed test (red or green)
    assert result != None
    # Destroy: Close connections/remove files used or created from test
    client.close_connection()
```