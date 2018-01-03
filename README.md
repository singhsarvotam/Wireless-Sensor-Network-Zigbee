# Wireless Sensor Network 

Objective
----------
To send data from a coordinator on one machine using xctu to a router attached on another machine.
Using python code we successfully extracted the data from the xbee frame. 
We create a tcp packet and send it from one machine to another.

Projects
--------
Chat application and Wireless Doorbell System.
The Xbee's are detected and configured using XCTU as the Coordinator and the Router nodes. Configuration is also possible using terminal applications like Cool Term for Mac and Tera Term for Windows. The Xbee with the C symbol is configured as the coordinator node and the other as the router node. 

The chat app was tested using two ways:

Two 'cool term' terminals on one Macintosh machine. One terminal was attached to the router node (arduino/xbee setup). The screenshot of the usbmodem1411 shows the terminal screen of the router. And the other screenshot of the usbserial port shows the terminal of the coordinator node. 

We then had an arduino/ xbee setup on two separate machines, Mac and Windows and we used two seperate terminal applications. Cool Term and Tera Term to test the communication between the two nodes. 


For the wireless doorbell application we uploaded a 'button input' program, on one arduino, written in C and a 'buzzer output' program written in C was uploaded onto the other arduino. These arduinos were attached on separate machines to upload the programs. The xbee used with the buzzer is configured as the router and the xbee used with the button input is configured as the coordinator. Now that these steps are complete, as soon as we power up our equipment our Wireless Doorbell System will work without any configuration required. These programs and configurations are permanently (can be modified) written on the arduino boards and the xbees. 

Please find attached the Movie/ Video we have made for the entire working of the Wireless Doorbell Application. 
Please find attached screenshots for reference.
