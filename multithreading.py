import threading, time
print("Start of program.")

def takeANap():
    time.sleep(3)
    print("Wake up!")

threadObj = threading.Thread(target=takeANap) #we create a new thread object and pass it the function takeANap
threadObj.start()

print("End of program")
