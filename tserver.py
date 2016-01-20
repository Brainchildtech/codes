import socket
Host='127.0.0.1'
       

port=8000
      
     
     

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,port))
s.listen(2)

print "server started."	 
    
   
while True:
	conn,addr=s.accept()
 
	print 'connected by', addr


        data=conn.recv(1024)
        print 'received:',repr(data)
        reply=raw_input("Reply: ")
        conn.sendall(reply)
conn.close
