temp = 25

# Only if
if temp < 10:
    print("Very Cold")
print("End of if block ...")

    # If - else
if temp < 10:
    print("Very Cold")
else:
    print("Not that cold..")

        # if-elif ... else
if temp < 10:
    print("Very cold")
elif temp > 10 and temp <= 25:
    print("Moderate temperature")
elif temp > 20 and temp <= 35:    
    print("Its warm ...")
elif temp > 30 and temp <= 45:    
    print("It is hot outside...")
else:
    print("Unbearable Hot ...")    