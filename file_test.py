def enter_point_and_comment():
    while True:
        print( "Please enter a value between 1 to 5" )
        point = input()
        if point.isdecimal():
            if 1 <= int(point) <= 5:
                print( "Enter your comments" )
                comment = input()
                post =  f'Points: {point} Comments: {comment}'
                file = open("data.txt", "a")
                file.write( f'{ post } \n' )
                file.close()
                break
                    
def print_results_so_far():
    print( "Results so far" )
    file = open("data.txt", "r")
    print(file.read())
    file.close()

while True:
    print( "Please select the process you would like to carry out from the following \n 1: Enter your rating points and comments \n 2: Check the results so far \n 3: Exit" )
    point = input()
    if point.isdecimal():
        if int(point) == 1:
            enter_point_and_comment()
        elif int(point) == 2:
            print_results_so_far()
        elif int(point) == 3:
            print( "Exit" )
            break
        else:
            print( "Please enter 1 to 3" )
    else:
        print( "Please enter 1 to 3" )
        
