
# In the following ticketing system , removed ID chosen by user is handled in  a way that the next ticket to be added after a deleted one will tkae the deleted id and dort the tickets by id
# id in this poblem should be as follows tick then followed by number
import datetime
import verify_user as verify_user
# -------------------------------------------------------Displaying Menus Section--------------------------------------------------------------------------------------------------------------#
############################## - Display Menu to admin - #######################


def displayAdminMenu():

    print("\n\nChoose from the following :\n1. Display Statistics\n2. Book a Ticket\n3. Display All Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. exit\n")
############################ - Display User to admin - #######################


def displayUserMenu():

    print("\n\nChoose from the following :\n1. Book a Ticket\n2. exit\n")

# --------------------------------------------------Integer input check Section---------------------------------------------------------------------------------------------------------------------#

##### - integer check input - #####
# This function check if the user entered an integer when needed, if the user entered a string instead of an integer for example Try and catch will throw an exception to handle the error
# displaying a message of an Invalid input to user and asking him i re-enter an integer


def check_integer_input(number):  # O(N)
    while True:
        try:  # Here the user will enter the input and if it is True then the user_input is an integer and it will be accepted
            user_input = int(input(number))
            return user_input
        except ValueError:  # if user didn't enter an integer,ValueError will thrown,ValueError is a type which will check the value if integer in this case,if it is not it will thow the invalid input message in this case
            print("Invalid input. Please enter an integer.")

# ------------------------------------------------Algorithms Section----------------------------------------------------------------------------------------------------------------------#

################### - Binary Search Sort for id of ticket - #####################

def binary_search_by_id(tickets, target_id):#O(logN)
    left = 0
    right = len(tickets) - 1

    while left <= right:
        mid = (right+left) // 2
        mid_id = tickets[mid]['ticket_id']                  # Here we save the mid ticket id in mid_id variable ,example if mid is 5 : tickets[5]['ticket_id']

        if mid_id == target_id:                                 
            return mid
        elif mid_id < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return -1

################### - Merge Sort for id, date and priority - #####################


def merge_sort(arr, option): #O(NLogN)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half, option)
    right_half = merge_sort(right_half, option)

    return merge(left_half, right_half, option)


def merge(left, right, option):
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):                                             #we increment then right by 1
      
        left_side = left[left_index][option]                            # Any other option will do same but it cannot accpet a 'ticket_id' as an option to be passed 
        right_side = right[right_index][option]                             # so i had to make it as if and else 
        if left_side <= right_side:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])

    return merged_list

# ----------------------------------------------------Tickets uploading , getting ID and the last ID of the tickets section-------------------------------------------------------------------------------------------------------------#


####### - Upload tickets and events to corresponding lists and dictionaries - ########

# The following function takes tickets as parameter
# Open the events_data.txt file where the information is stored
# then it split each line each line takinf ',' as delimiter
# it stores then the data in a dictionary named ticket where each key has its own value then this dictionary is added the tickets list


def UploadTickets(tickets):  # TIME COMPLEXITY : O(N) // since open() returns a file object which is a pointer or Handle so no time complexity here only for the for loop inside

    # 1. With open is used to close the file after finishing from it. 2. file open as read since we used 'r'
    with open('events_data.txt', 'r') as file:
        for line in file:  # iterating through each line in file

            # 1. strip to remove any spaces from the start or the end of the line . 2. split to use ',' as delimieter and split our data
            ticket_data = line.strip().split(',')

            if len(ticket_data) < 5:  # In case a line has less than than the data needed which is 5 in this case we ignore the line by using continue
                continue
            

            ticket = {  # Storing our splitted data in a diciotnary according to each index of the data
                'ticket_id': ticket_data[0],
                'event_id': ticket_data[1],
                'username': ticket_data[2],
                'date': ticket_data[3],
                'priority': int(ticket_data[4])
            }
            # adding the dictionaries to the list named tickets
            tickets.append(ticket)



########################## -  Get Last Id - ############################
# The following function will get the last id of the tickets , bby this we handled that the next ticket to be added will have the (oldId +1) since ID is auto incrementing
# removed in parameters is a boolean inialized in the main function and used when a ticket is deleted.
# when deleted a ticket removed get a true to let the function know that we have a deleted ID that should be the next id added to the nxt ticket
# deleted_id is a global list inialized in main too where all deleted ticket's ID are stored in it , to make sure that the next ticket will be added will take an ID from this list
# By this we will handle the IDs and avoid duplication and protect the sequence of the IDs
# tickets is the list holding the tickets

def GetLastId(removed, tickets):  # O(N) // ALL of the function is using constants and we have else
    # in the case that we have a deleted ticket before , we handle its ID
    if removed == True and len(deleted_id) != 0:
        # next_id is the id that will be added next to the net ticket will be equal to the fist index of the deleted_id list
        next_id = deleted_id[0]

        # The taken id which is in the first index then is removed from the deleted_id list to prevent duplication
        deleted_id.remove(deleted_id[0])

        # The tickets id pattern is as dollows: tick100 , tick101, tick103,.. etc so in this line im taking a substring where
        next_ticket_id = int(next_id[4:])
        # i remove the 'tick' part and store the number after it as an integer using concatination

        return next_ticket_id

    else:                            # this is the case where no deleted ids are found in the deleted id list
        # we get the last index of the tickets list which will be golding the last ticket id we have
        last_index = len(tickets)-1

        # We get the ticket ID of the last ticket
        last_ticket_id = tickets[last_index]['ticket_id']

        # The tickets id pattern is as dollows: tick100 , tick101, tick103,.. etc so in this line im taking a substring where
        last_ticket_id = int(last_ticket_id[4:])
        # i remove the 'tick' part and store the number after it as an integer using concatination

        return last_ticket_id
# -----------------------------         --------------------Date Section---------------                 --------------------------#
############ -  get the date of today - ##########

# the following function displays the current date 



def current_date():#O(N)
    current_date = str(datetime.date.today())
    current_date = int(current_date.replace('-', ''))
    return current_date

######################### - Tomorrow date function - ########################
# the following function is built to handle the next day events
#by getting today's date then using the timedelta method from datetime library
#we add 1 day to today's date and gets next day 
#then the date is edited to be in the same sequence in the dates stored in the tickets list by removing dashes then we return this date

def GetTomorrowDate():#O(1)
    today = datetime.date.today()
    tdelta = datetime.timedelta(days=1)   # timedelta is considered here is 1 day that can be added or decremented ot other usages
    tomorrow_date = today + tdelta    # adding 1 day to today's date
    tomorrow_date = str(tomorrow_date)
    tomorrow_date=tomorrow_date.replace('-','')
    return tomorrow_date



############ -  user datew input + validity check - ##########

#this function asks user to input a valid date and displays an error in invalid copied from older assignment and edited to fit this test case

def event_date(): #O(N)
    today_date = current_date()

    dateValidity = False


    date = ''
    while (dateValidity != True):
        date = input('Enter a EVENT DATE formatted as YYYY-MM-DD and starting today\'s date , example (2023-09-08) must conatin 8 digits : ').strip()

        frontSlashCount = date.count('/')
        dashCount = date.count('-')
        if (frontSlashCount == 2 or dashCount== 2):  # Check if user entered complete date with 2 slashes or 2 dashes

            date = date.replace('-','/')  # replace '-' with '/' if user entered this option

            year,month,day = date.split(
                '/'
            )  # split the date to check if the value of day , month and year are valid and sotre each value to its corresponding variables respectively
            
            if not (day.isdigit() and month.isdigit() and year.isdigit()):  # Assure that the user entered only digits
                print("Invalid date format! Please enter the date in the format YYYY-MM-DD.")

            # Assure that the day, month, and year are within valid ranges
            elif int(day) >= 1 and int(day) <= 31 and int(month) > 1 and int(month) <= 12 and int(year) >= 2023:  #we check for validity 
               
                date = date.replace('/', '')
                date = int(date)
              
                if date < today_date:                                                               #check if the date is earlier than the current day we are in
                    print('Invalid date you can\'t reserve an event that passed before')
                else:
                   
                    return date
                       
            else:
                  
                print("Invalid date format , check the hint to add a valid date")
        else:
            print("Invalid date format, check the hint to add a valid date ")
            dateValidity = False


# -----------------------------         --------------------Choices chosen functions Section---------------                 --------------------------#

# The following function is for the first choice to display the event with the highest tickets
# To do so i inialized a dictionary named even_dict where take the even Ids from the tickets list in parameter as a key to the values
# and the values will be the tickets for each event
# then to each event id which is the key , we count the number of values which are the tickets for this event
# the event that has the highest number of values will be the highest event that has the highest number of tickets

def HighestTicketsNum(tickets): # O(n^2) is the worst case since we have 2 nested dependent loops
    event_dict = {}

    for ticket in tickets:  # first for loop is to enter a list of dictionaries named tickets that is passed to the function through parameter
                            # inside this list each dictionary will have an event id(ticker['event_id']) which will be stored in event_id
        event_id = ticket["event_id"]
        ticket_info = {}  # a dictionary to save the ticekt info except for event_id to be added to its corresponding event id key
        for key, value in ticket.items():  # iterating through each item in dict found in the tickets list
            if key != "event_id":  # if the key is not =  to 'event_id' we append the key and value to the ticket_info dict
                ticket_info[key] = value

        # if event id is already found in even_dictt we append the value(which is the ticket info) to the same eventId
        if event_id in event_dict:
            event_dict[event_id].append(ticket_info)
        else:
            # if event id is not found in event_dict we append a ney key holding event_id with its value in ticket_info
            event_dict[event_id] = [ticket_info]

    highest = 0
    highest_key = ''
    for key, value in event_dict.items():  # in this part we iterate events dict and see which event has the highest number of tickets as id and we store the number
        # of values in highest variable and print the key of event which is the id of it and the number of tickets
        if len(value) > highest:
            highest = len(value)
            highest_key = key
    return f'Event {highest_key} has the highest number of tickets {highest}'


########################## - Create Ticket - ###############################

# the following function is to create a new ticket as booking a ticket
# removed to check if there is any removed id before to reuse it again as discussed in above functions
# if no removed ids we take the last id in the tickets list and increment it by 1
# if removed true , the deleted id will e passed from main as parameter and stored in next_id_num
# role is to check for user changes to save, if admin nothing will be saved


def CreateTicket(removed, last_id, tickets, next_id_num, role):# O(NlgN) // since we have merge sort called to sort ids

    if removed == True and next_id_num != 0:  # case of deleted id
                                                # if nextid is greater than 0 we store it in current_id_num
        current_id_num = next_id_num

        # we add 'tick' before number then add the number of id concatenated wih str
        ticket_id = str('tick') + str(current_id_num)
        # user will fill the data here
        event_id = input('Enter the event ID with deleted before id: ')
        username = input('Enter your name : ')
        event_date_added=str(event_date())

        priority = 0
        ticket = {  # data added above will be stored in a ticket dictionary that will be appended after to list tickets
            'ticket_id': ticket_id,
            'event_id': event_id,
            'username': username,
            'date': event_date_added,
            'priority': priority
        }
        tickets.append(ticket)
        # O(NlgN)                                                    #calling sort_id nerge sort to sort tickets by IDs
        merge_sort(tickets, 'ticket_id')
        # appending the new id added to the tickets_id, discuused the use of this list before
        print('Following ticket is added : ', ticket)
    else:  # the case where no deleted id is found
        # we take the last id found past from getlastid function and increment it by 1
        current_id_num = last_id + 1
        # rest is same as discussed above
        ticket_id = str('tick') + str(current_id_num)
        event_id = input('Enter the event ID for new id ticket: ')
        username = input('Enter your name : ')
        event_date_added=str(event_date())

        priority = 0
        ticket = {
            'ticket_id': ticket_id,
            'event_id': event_id,
            'username': username,
            'date': event_date_added,
            'priority': priority
        }

        print('Following ticket is added : ', ticket)
        tickets.append(ticket)
    if role == 'user':  # if the role is user we save changes to file
        with open('events_data.txt', 'a')as t_db:
            ticket_data = f"{ticket_id},{event_id},{username},{event_date_added},{priority}\n"
            t_db.write(ticket_data)
############################# - Display Ticket sorted by date - ####################################


# this function will display the tickets sorted by date using the merge sort
# it takes tixkets only as parameter
# checks for the date if in 3 cases : Today , Tomorrow and upcoming
# today will display today's events
# #tomorrow will to todays date a 1 since date is concatinated with in and increased days by one which will be the last number
# upcoming will display all the rest evetns

def DisplayByDate(tickets):  # O(NlgN) since we have merge sort
    current_date = str(datetime.date.today())
    # get current date which is today's date
    current_date = current_date.replace('-', '')
    # sort tickets by date(note the second parameter 'date' sent is for merge sort's option) trying to make  it moregeneral and reusable in case of soring by priority
    sorted_tickets = merge_sort(tickets, 'date')
    print('\nEvents of today\'s date :\n')
    for ticket in sorted_tickets:  # in each of upcoming parts in this function we are iterating through tickets to display them accorfing to there dates
        if ticket['date'] == current_date:
            # checking if ticket is not deleted as a douible check then checking what is the date is equal to(current,tomorrow or upcoming)
            if ticket['ticket_id'] not in deleted_id:
                # before printing it
                print(ticket)

    print('\nEvents of tomorrow\'s date :\n')
    
    tomorrow_date = GetTomorrowDate() # we call GetTomorrowDate funtcion and store value in a varibale to check for date

    for ticket in sorted_tickets:
       
        if ticket['date'] == str(tomorrow_date):
            print(ticket)
    print('\nUpcoming Events :\n')
    for ticket in sorted_tickets:
        # if the date is not current nor equal to tomorrow print upcoming
        if ticket['date'] > current_date and ticket['date'] != str(tomorrow_date):
            print(ticket)

#################################### - Change ticket priority - ##################################
# following function changes the priority of a ticket by iterating through tickets list and asking the user to enter the desired ticket id he wants to change its priority
# the we check through a loop if the id of this ticket is found then the ticket is found
# then the user is asked to enter the new priority which will be updated though accessing it where the key is priority


def ChangePriority(tickets):  # O(N) // 1 loop 
    # Using check_integer_input to echeck for user input
    ticket_id_to_change = input('Enter ticket ID : ')
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id_to_change:
            desired_priority = check_integer_input(
                'Enter the priority to update it : ')
            # setting the new priority when the id matches the user id input
            ticket['priority'] = desired_priority
            return print(ticket)

    else:
        return print(f"\nTicket ID '{ticket_id_to_change}' you entered is not found.\n")
####################################### - delete ticket by id - ######################################


# the following functiion delete a ticket user chooses through entering id searching for it using binary search then removing it from list

def DeleteTicket(tickets):  # O(NlgN) since it has .remove
    # inializing a removed ticket variable as none to make it equal ticket if removed
    removed_ticket = None
    id_to_delete = input('Enter a valid ticket ID to delete: ')
    ticket_index = binary_search_by_id(tickets, id_to_delete)

    if ticket_index != -1:
        removed_ticket = tickets[ticket_index]

        tickets.remove(removed_ticket)
        if removed_ticket:
            deleted_id.append(id_to_delete)
            print(f'Ticket of ID {id_to_delete} is successfuly deleted ')
            return True

    else:
        print(f"User '{id_to_delete}' not found.")


############################ - Run Events - ####################################


def RunEvents(sorted_by_priority, tickets):  # O(N) handles a for loop

    today_date=current_date()
    for ticket in sorted_by_priority:  # iterating throught the priority sorted list of tickets recieved from main
        if ticket['date'] == str(today_date):
            # if date is equal to current date we print this ticcket then we remove it from tickets list
            print('\n\nthis ticket is running today and will be removed : ', ticket)
            tickets.remove(ticket)
            # removed id will be added to deleted id , to handle the next id added
            deleted_id.append(ticket['ticket_id'])
            # removed from tickets id

    return tickets


# -----------------------------------------------           Main Function                ----------------------------------------------------#
def main():#O(n^2) is the worst case when highest ticket is called
    removed = False #if an id is deleted removed will be true to use the deleted index as next id 
    attempts = 5
    tickets = [] #store all tickets we have 
    global deleted_id
    deleted_id = []   #store deleted ids to handle ticket ids if deleted

    UploadTickets(tickets)      # Uploading tickets from file to list 

    tickets = merge_sort(tickets, 'ticket_id') # sorting list using merge sort

    #using match case where it accetps choice to check what is the user choice
    choice = 0
    print('\n\nWelcome to our Events ticketing system !\nplease enter your username and password to enter as an admin,\nelse just proceed with an empty values if user :')
    #checking for user attempts and role
    # while attempts > 0:
    #     username = input('\n\nEnter your admin username : ')
    #     password = input(
    #         '\n\nEnter your username\'s password to proceed as admin : ')

    #     admin = verify_user.VerifyLogin(username, password, 'users.txt')
    #     if username == 'admin' and admin == True:
    #         attempts = 0
    #     elif username == 'admin' and admin == False:
    #         print(
    #             f'Enter a valid username and password , you have {attempts} remaining')
    #         attempts -= 1
    #     else:
    #         attempts = 0
    #         admin = False
    admin=True
    if admin == True:

        print('Signed in as Admin')

        while choice != 7:

            role = 'admin'
            displayAdminMenu()
            choice = check_integer_input(
                'Enter your choice between 1 and 7 : ')

            if choice >= 1 and choice <= 7:
                match choice:
                    case 1:

                        print(HighestTicketsNum(tickets)) #O(n^2)
                    case 2:
                        #in this case if we don't found a delegted id before added to deleted_id list we enter the id 
                        # and book a ticket that will increment the last id we have in list, in this case removed is False
                        if len(deleted_id) == 0:     
                            # we get the last id in tickets list and store in last_id using function 
                            last_id = GetLastId(removed, tickets) #O(N)  
                            

                            CreateTicket(removed, last_id,
                                         tickets, deleted_id, role) #O(NlgN)    #we create then by sending the following parameters 
                        # if removed is true then we the deleted_id to get the last id and user 
                        #if role is admin we exir without saving else if user we save

                        else:
                            #case where we have a deleted id , we sort the deleted_id list to keep the sequence 
                            #removed is set True to enter the id condition in the create Ticket  
                            deleted_id.sort()  # O(NlgN)
                            removed = True
                            temp = None                     #this temp is to send it to parameter instead of last_id since we didn't inialize it at this state
                            next_id_num = GetLastId(removed, tickets) #since removed is true so the GetLastId will be the lowest id found in deleted id list 

                            print('this is next id num : ', next_id_num)
                            CreateTicket(removed, temp, tickets,next_id_num, role)
                            removed = False #after finising removed set back to False to avoid mistakes
                            tickets = merge_sort(tickets, 'ticket_id') #sotirng tickets by id using merge sort 

                    case 3:

                        DisplayByDate(tickets)#O(N)
                    case 4:

                        ChangePriority(tickets)#O(N)

                    case 5:
                        removed = DeleteTicket(tickets)#O(NlgN)

                    case 6:
                        sorted_by_priority = merge_sort(tickets, 'priority')  #sort tickets by priority using merge sort
                        sorted_by_priority.reverse()  # reversing the ticket which will have the highest first since they have the bigger chance to attend event
                        tickets = RunEvents(sorted_by_priority, tickets)  # RunEvents the sorted by priority list and the lsit of ticket to remove events that run

            else:
                print('\n Choice should be between 1 and 7 ')

    else:
        
        # in case of user he'll be able to book a ticket same as admin , but since the in parameter is user then the txt file will update and ticket in it

        print('Signed in as User')
        role = 'user'
        while choice != 2:
            displayUserMenu()
            choice = check_integer_input(
                'Enter your choice between 1 and 2 : ')
            if choice >= 1 and choice <= 7:
                match choice:
                    case 1:
                        if len(deleted_id) == 0:
                            last_id = GetLastId(removed, tickets)
                            CreateTicket(removed, last_id,
                                         tickets, deleted_id, role)
            else:
                print('\n Choice should be between 1 and 2 ')


main()
