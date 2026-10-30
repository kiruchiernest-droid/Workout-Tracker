def get_status(steps):
    if steps >= 10000:
        print("Exceeded")
    elif steps >= 8000:
        print("Hit target")
    else:
        print("Below target")

# call 
get_status(5000)
get_status(8500)
get_status(4000)
 

