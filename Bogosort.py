import random
import time
import multiprocessing
repeat = True
numvld = False
trdvld = False
repeats = 1
time1 = 0
time2 = 0
core_count = multiprocessing.cpu_count()

num = int(input("How many numbers?: "))

if num <= 0:
    while numvld == False:
        num = int(input("Error: Invalid Number, please choose another: "))
        if num <= 0:
            num = int(input("Error: Invalid Number, please choose another: "))
        else:
            numvld = True

list = random.sample(range(-999999,999999), num)
list2 = random.sample(range(-999999,999999), num)
list3 = random.sample(range(-999999,999999), num)
list4 = random.sample(range(-999999,999999), num)
list5 = random.sample(range(-999999,999999), num)
list6 = random.sample(range(-999999,999999), num)
list7 = random.sample(range(-999999,999999), num)
list8 = random.sample(range(-999999,999999), num)
list9 = random.sample(range(-999999,999999), num)
list10 = random.sample(range(-999999,999999), num)
list11 = random.sample(range(-999999,999999), num)
list12 = random.sample(range(-999999,999999), num)

def Main(list): 
    shuffle = 0
    sorted = True
    while sorted == True:
        sorted = False
        for index in range(0,len(list)-1):
            if list[index] > list[index +1]:
                sorted = True
                random.shuffle(list)
    print(list)

def Main2(list2): 
    shuffle = 0
    sorted2 = True
    while sorted2 == True:
        sorted2 = False
        for index2 in range(0,len(list2)-1):
            if list2[index2] > list2[index2 +1]:
                sorted2 = True
                random.shuffle(list2)
    print(list2)

def Main3(list3): 
    shuffle = 0
    sorted3 = True
    while sorted3 == True:
        sorted3 = False
        for index3 in range(0,len(list3)-1):
            if list3[index3] > list3[index3 +1]:
                sorted3 = True
                random.shuffle(list3)
    print(list3)

def Main4(list4): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list4)-1):
            if list4[index4] > list4[index4 +1]:
                sorted4 = True
                random.shuffle(list4)
    print(list4)

def Main5(list5): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list5)-1):
            if list5[index4] > list5[index4 +1]:
                sorted4 = True
                random.shuffle(list5)
    print(list5)

def Main6(list6): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list6)-1):
            if list6[index4] > list6[index4 +1]:
                sorted4 = True
    print(list6)

def Main7(list7): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list7)-1):
            if list7[index4] > list7[index4 +1]:
                sorted4 = True
                random.shuffle(list7)
    print(list7)

def Main8(list8): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list5)-1):
            if list8[index4] > list8[index4 +1]:
                sorted4 = True
                random.shuffle(list8)
    print(list8)

def Main9(list9): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list5)-1):
            if list9[index4] > list9[index4 +1]:
                sorted4 = True
                random.shuffle(list9)
    print(list9)

def Main10(list10): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list10)-1):
            if list10[index4] > list10[index4 +1]:
                sorted4 = True
                random.shuffle(list10)
    print(list10)

def Main11(list11): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list11)-1):
            if list11[index4] > list11[index4 +1]:
                sorted4 = True
                random.shuffle(list11)
    print(list11)

def Main12(list12): 
    shuffle = 0
    sorted4 = True
    while sorted4 == True:
        sorted4 = False
        for index4 in range(0,len(list12)-1):
            if list12[index4] > list12[index4 +1]:
                sorted4 = True
                random.shuffle(list12)
    print(list12)

print("CPU Cores:", core_count)
threads = int(input("How many threads?: "))

if threads <= 0 or threads > 12:
        while trdvld == False:
            threads = int(input("Error: Invalid Number, please choose another: "))
            if threads <= 0 or threads > 12:
                threads = int(input("Error: Invalid Number, please choose another: "))
            else:
                trdvld = True


while repeat == True:
    repeat = False
    if threads == 1:
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t1.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            repeats += 1

    elif threads == 2:
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t1.start()
        t2.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            repeats += 1

    elif threads == 3:
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t1.start()
        t2.start()
        t3.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            repeats += 1

    elif threads == 4:    
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main(list2))
        t3 = multiprocessing.Process(target = Main(list3))
        t4 = multiprocessing.Process(target = Main(list4))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            repeats += 1

    elif threads == 5:  
        time1 = time.time() 
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            repeats += 1
        
    elif threads == 6: 
        time1 = time.time()  
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t6 = multiprocessing.Process(target = Main6(list6))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            list6 = random.sample(range(-999999,999999), num)
            repeats += 1
        
    elif threads == 7:
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t6 = multiprocessing.Process(target = Main6(list6))
        t7 = multiprocessing.Process(target = Main7(list7))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            list6 = random.sample(range(-999999,999999), num)
            list7 = random.sample(range(-999999,999999), num)
            repeats += 1
        
    elif threads == 8:
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t6 = multiprocessing.Process(target = Main6(list6))
        t7 = multiprocessing.Process(target = Main7(list7))
        t8 = multiprocessing.Process(target = Main8(list8))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            list6 = random.sample(range(-999999,999999), num)
            list7 = random.sample(range(-999999,999999), num)
            list8 = random.sample(range(-999999,999999), num)
            repeats += 1
        
    elif threads == 9:
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t6 = multiprocessing.Process(target = Main6(list6))
        t7 = multiprocessing.Process(target = Main7(list7))
        t8 = multiprocessing.Process(target = Main8(list8))
        t9 = multiprocessing.Process(target = Main9(list9))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            list6 = random.sample(range(-999999,999999), num)
            list7 = random.sample(range(-999999,999999), num)
            list8 = random.sample(range(-999999,999999), num)
            list9 = random.sample(range(-999999,999999), num)
            repeats += 1
        
    elif threads == 10:
        time1 = time.time()
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t6 = multiprocessing.Process(target = Main6(list6))
        t7 = multiprocessing.Process(target = Main7(list7))
        t8 = multiprocessing.Process(target = Main8(list8))
        t9 = multiprocessing.Process(target = Main9(list9))
        t10 = multiprocessing.Process(target = Main10(list10))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            list6 = random.sample(range(-999999,999999), num)
            list7 = random.sample(range(-999999,999999), num)
            list8 = random.sample(range(-999999,999999), num)
            list9 = random.sample(range(-999999,999999), num)
            list10 = random.sample(range(-999999,999999), num)
            repeats += 1
        
    elif threads == 11: 
        time1 - time.time()   
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t6 = multiprocessing.Process(target = Main6(list6))
        t7 = multiprocessing.Process(target = Main7(list7))
        t8 = multiprocessing.Process(target = Main8(list8))
        t9 = multiprocessing.Process(target = Main9(list9))
        t10 = multiprocessing.Process(target = Main10(list10))
        t11 = multiprocessing.Process(target = Main11(list11))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            list6 = random.sample(range(-999999,999999), num)
            list7 = random.sample(range(-999999,999999), num)
            list8 = random.sample(range(-999999,999999), num)
            list9 = random.sample(range(-999999,999999), num)
            list10 = random.sample(range(-999999,999999), num)
            list11 = random.sample(range(-999999,999999), num)
            repeats += 1
        
    elif threads == 12:   
        time1 = time.time() 
        t1 = multiprocessing.Process(target = Main(list))
        t2 = multiprocessing.Process(target = Main2(list2))
        t3 = multiprocessing.Process(target = Main3(list3))
        t4 = multiprocessing.Process(target = Main4(list4))
        t5 = multiprocessing.Process(target = Main5(list5))
        t6 = multiprocessing.Process(target = Main6(list6))
        t7 = multiprocessing.Process(target = Main7(list7))
        t8 = multiprocessing.Process(target = Main8(list8))
        t9 = multiprocessing.Process(target = Main9(list9))
        t10 = multiprocessing.Process(target = Main10(list10))
        t11 = multiprocessing.Process(target = Main11(list11))
        t12 = multiprocessing.Process(target = Main12(list12))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        time2 = time.time()
        print(time2 - time1)
        repeat_choice = input("Repeat? (Y/N): ")
        if repeat_choice.lower() == "y":
            repeat = True
            list = random.sample(range(-999999,999999), num)
            list2 = random.sample(range(-999999,999999), num)
            list3 = random.sample(range(-999999,999999), num)
            list4 = random.sample(range(-999999,999999), num)
            list5 = random.sample(range(-999999,999999), num)
            list6 = random.sample(range(-999999,999999), num)
            list7 = random.sample(range(-999999,999999), num)
            list8 = random.sample(range(-999999,999999), num)
            list9 = random.sample(range(-999999,999999), num)
            list10 = random.sample(range(-999999,999999), num)
            list11 = random.sample(range(-999999,999999), num)
            list12 = random.sample(range(-999999,999999), num)
            repeats += 1

if repeats == 1:
    print("Looped 1 time.")
elif repeats > 1:
    print("Looped", repeats, "times.")