from src.mqtt.mqtt_client import MqttClient

def test_connect():
    """
    This test tests that an object of the MqttClient can connect to the broker.
    """
    # Arrange
    client = MqttClient
    # Act
    client.connect()
    connected = client.is_connected
    # Destroy
    client.disconnect()
    # Assert
    assert connected == True

def test_disconnect():
    pass

def test_create_topic():
    pass

def test_read():
    pass

def test_write():
    pass