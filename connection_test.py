from pyModbusTCP.client import ModbusClient
from pymodbus.client import ModbusTcpClient
import numpy as np
import time 

conn = ModbusTcpClient(host="172.20.32.38",port=502)
print(conn.connect())
while True:
    time.sleep(1)
    print(conn.write_register(26,0, 2))
    print(conn.write_register(24,8000, 2))
