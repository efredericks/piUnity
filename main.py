import socket
import time
import json
from sense_hat import SenseHat

# Initialize sense hat
sh = SenseHat()
sh.set_imu_config(False, True, False)

IP_ADDR = "192.168.1.18"
IP_PORT = 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  try:
    gyro = sh.get_gyroscope()
    #txData = '{"pitch":' + str(gyro['pitch']) + ',"roll":' + str(gyro['roll']) + ',"yaw":' + str(gyro['yaw']) + '}'
    
    txData = "{pitch};{roll};{yaw}".format(**gyro)
    print("Sending [{0}] to [{1}:{2}]".format(txData, IP_ADDR, IP_PORT))
    sock.sendto(bytes(txData, "utf-8"), (IP_ADDR, IP_PORT))
    #time.sleep(1)

  except Exception as e:
    print("Error: {0}".format(e))
    sock.close()
    break


"""
backlog = 1
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 50001))
s.listen(backlog)

while True:
  try:
    client, address = s.accept()
    bytes_received = client.recv(size)

    gyro = sh.get_gyroscope()
    txData = "{pitch};{roll};{yaw}".format(**gyro)
    client.send(txData.encode())
    time.sleep(1)
  except Exception as e:
    print("Error: {0}".format(e))
    client.close()
    break

"""
"""
try:
  print("I'm waiting...")
  client, address = s.accept()

  while True:
    data = client.recv(size)
    if data:
      print(str(data))

    gyro = sh.get_gyroscope()
    txData = "{pitch};{roll};{yaw}".format(**gyro)
    print(txData)
    client.sendall(txData)#txData);
    #print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro))
 
    

except:
  print("Closing socket")
  client.close()
  s.close()
"""
