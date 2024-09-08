def pto(arr,size):
    x1 = 2
    x = 0
    y = 0
    setbit = 0
    for i in range(1,size):
        x1 = x1^arr[i]
        setbit= x1 ~(x1-1)
    for i in range(size):
        if(arr[i]&setbit):
            x = x^arr[i]
        else:
            y = y^arr[i]
    print("Two odd elements are",x,"&&",y,)
arr =[]
arr_size = int(input("Enter size of the arry"))
