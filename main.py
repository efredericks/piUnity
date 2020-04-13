import socket
from sense_hat import SenseHat

# Initialize sense hat
sh = SenseHat()
sh.set_imu_config(False, True, False)



backlog = 1
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 50001))
s.listen(backlog)

try:
  print("I'm waiting...")
  client, address = s.accept()

  while True:
    data = client.recv(size)
    if data:
      print(str(data))

    gyro = sh.get_gyroscope()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
 
    

except:
  print("Closing socket")
  client.close()
  s.close()
