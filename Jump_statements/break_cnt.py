#Continue:Used when you wanr to skip a particular condition , Control is given to next iteration
#Break:Used when you want to terminate a loop at a certain condition and come out of the loop,it terminates the existing loop


#continue
print("using continue statement")
for i in range(1,11):
    if(i==3 or i==5):
        continue
    else:
        print(i)


#break
print("\nUsing break staement")
for i in range(1,11):
    if(i>=7):
        break
    else:
        print(i)