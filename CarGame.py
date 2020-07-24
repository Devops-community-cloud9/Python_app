command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print (" Car is Allready Started ")
        else:
            started = True
            print (" Car Started")
    elif command == "stop":
        if not started:
            print("Car is Allready Stopped")
        else:
             started = False
             print ("Car Stoped ")

    elif command == "help":
        print (""""
start - to start the car 
stop - to stop the car 
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print ("Sorry I Dont Understand That ")




