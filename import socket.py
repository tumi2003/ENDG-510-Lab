import socket
import pandas as pd 
# in case of error, install pnadas using: pip install pandas
# Create an empty Pandas DataFrame
df = pd.DataFrame(columns=['Temp', 'Humd', 'Label']) 
# Label: 1 means valid, means invalid
# next create a socket object
s = socket.socket()
print ("Socket successfully created")
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345
# Next bind to the portwe have not typed any ip in the ip field instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")

c,addr = s.accept()
print('Got connection from', addr)

i = 1000 
while i>=0:
    client = c.recv(1024)
    data= client.decode()
    temp= data.split(" ")[0]
    hum= data.split(" ")[1]
    new_data= {
        'Temp':temp,
        'Humd': hum,
        'Label': 1
    }
    df = df._append(new_data, ignore_index=True)
    print(data)
    i= i-1
c.close()
df.to_csv('data.csv', index= False)

