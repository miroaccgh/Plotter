import paho.mqtt.client as paho
from paho import mqtt
from dotenv import load_dotenv
import os
from typing import Literal
import time
import json


class MqttClient:
    connectionTypes: Literal["signal_creation", "scope_creation", "signal_session", "scope_session"]
    def __init__(self, connection_type, topics, subscribe):
        self._connected = False
        self._subscribed = None
        self._connection_type = connection_type
        self._client_id = self.connection_type + str(int(time.time()))
        self._topics = topics
        self._subscribe = subscribe
        load_dotenv()
        self._env = {
            "username": os.getenv("BROKER_USERNAME"),
            "password": os.getenv("BROKER_PASSWORD"),
            "url": os.getenv("BROKER_URL"),
            "port": int(os.getenv("BROKER_PORT"))
        }
        self._client = paho.Client(client_id=self.client_id, userdata=None, protocol=paho.MQTTv5)
        self.set_callbacks()

    @property
    def is_connected(self) -> bool:
        return self._connected

    def set_callbacks(self):
        def on_subscribe(client, userdata, mid, granted_qos, properties=None):
            print(f"{self._client_id} subscribed to {self._topics}")
            self._subscribed = True

        def on_message(client, userdata, msg):
            msg_object = json.loads(msg.payload.decode("utf-8"))
            if msg_object["meta"]["topic"] == "meta/emergency_button" and msg_object["msg"]["isPressed"]:
                print(f"{self._connection_type} acknowledged emergency button state True")
                return {"EB_pressed": True}
            print(f"{self._connection_type} received {msg.payload.decode('utf-8')} on {self._topics}")
            return msg

        self.client.on_subscribe = on_subscribe
        self.client.on_message = on_message
    
    def connect(self):
        def on_connect(client, userdata, flags, rc, properties=None, ):
            print(f"{self._connection_type} connected to {self.env['url']}")
            self._connected = True

        self._client.on_connect = on_connect
        self._client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        self._client.username_pw_set(self.env["username"], self.env["password"])
        self._client.connect(self.env["url"], self.env["port"])
    
    def disconnect():
        pass

    def create_topic():
        pass

    def read():
        pass

    def write():
        pass