
# In the following ticketing system , removed ID chosen by user is handled in  a way that the next ticket to be added after a deleted one will tkae the deleted id and dort the tickets by id

import datetime
import verify_user as verify_user
# -------------------------------------------------------Displaying Menus Section--------------------------------------------------------------------------------------------------------------#
############################## - Display Menu to admin - #######################


def displayAdminMenu():

    print("\n\nChoose from the following :\n1. Display Statistics\n2. Book a Ticket\n3. Dsiplay All Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. exit\n")
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

# ------------------------------------------------Merge Sort Algorithms Section----------------------------------------------------------------------------------------------------------------------#
################# - merge sort for sorting ID - ################


def sort_id(tickets):
    if len(tickets) <= 1:
        return tickets

    mid = len(tickets) // 2
    left_half_id = tickets[:mid]
    right_half_id = tickets[mid:]

    left_half_id = sort_id(left_half_id)
    right_half_id = sort_id(right_half_id)

    return sort_merge_id(left_half_id, right_half_id)


def sort_merge_id(left, right):
    merged_list_id = []
    left_index_id, right_index_id = 0, 0

    while left_index_id < len(left) and right_index_id < len(right):
        if left[left_index_id]["ticket_id"] < right[right_index_id]["ticket_id"]:
            merged_list_id.append(left[left_index_id])
            left_index_id += 1
        else:
            merged_list_id.append(right[right_index_id])
            right_index_id += 1

    merged_list_id.extend(left[left_index_id:])
    merged_list_id.extend(right[right_index_id:])
    return merged_list_id

################### - Merge Sort for date and priority - #####################


def merge_sort(arr, option):
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
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        left_side = int(left[left_idx][option])
        right_side = int(right[right_idx][option])

        if left_side <= right_side:
            merged_list.append(left[left_idx])
            left_idx += 1
        else:
            merged_list.append(right[right_idx])
            right_idx += 1

    merged_list.extend(left[left_idx:])
    merged_list.extend(right[right_idx:])

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


############################# - Add Ids to a list - #########################################
# The following function will alse open the file storing the data and gets only the first index after splitting using the comma delimiter which is the ticcket ID
# Then the ids will be stored in a global list defined in the main called tickets_id
# This list is used to handle the next ticket ID that will be added to the system,so this list will handle the already used ids

def GetTicketsId():#O(N) // since it holds a for loop
    with open('events_data.txt', 'r') as file:
        for line in file:
            ticket_data = line.strip().split(',')
            if len(ticket_data) < 5:
                continue
            tickets_id.append(ticket_data[0])
        return tickets_id


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
        next_id = deleted_id[0]              # next_id is the id that will be added next to the net ticket will be equal to the fist index of the deleted_id list

        deleted_id.remove(deleted_id[0])     # The taken id which is in the first index then is removed from the deleted_id list to prevent duplication

        next_ticket_id = int(next_id[4:])    # The tickets id pattern is as dollows: tick100 , tick101, tick103,.. etc so in this line im taking a substring where
                                             # i remove the 'tick' part and store the number after it as an integer using concatination

        return next_ticket_id
    
    else:                            # this is the case where no deleted ids are found in the deleted id list 
        last_index = len(tickets)-1  #we get the last index of the tickets list which will be golding the last ticket id we have

        last_ticket_id = tickets[last_index]['ticket_id'] #We get the ticket ID of the last ticket 

        last_ticket_id = int(last_ticket_id[4:])    # The tickets id pattern is as dollows: tick100 , tick101, tick103,.. etc so in this line im taking a substring where
                                                    # i remove the 'tick' part and store the number after it as an integer using concatination

        return last_ticket_id


# -----------------------------------------------------------Choices chosen functions Section-----------------------------------------------------------------------------------------#

# The following function is for the first choice to display the event with the highest tickets 
# To do so i inialized a dictionary named even_dict where take the even Ids from the tickets list in parameter as a key to the values
#and the values will be the tickets for each event 
#then to each event id which is the key , we count the number of values which are the tickets for this event
#the event that has the highest number of values will be the highest event that has the highest number of tickets

def HighestTicketsNum(tickets): # O(n^2) is the worst case since we have 2 nested dependent loops
    event_dict = {}

    for ticket in tickets:                    #first for loop is to enter a list of dictionaries named tickets that is passed to the function through parameter
        event_id = ticket["event_id"]         # inside this list each dictionary will have an event id(ticker['event_id']) which will be stored in event_id
        ticket_info = {}                      #a dictionary to save the ticekt info except for event_id to be added to its corresponding event id key
        for key, value in ticket.items():     #iterating through each item in dict found in the tickets list
            if key != "event_id":             #if the key is not =  to 'event_id' we append the key and value to the ticket_info dict
                ticket_info[key] = value

        if event_id in event_dict:                          #if event id is already found in even_dictt we append the value(which is the ticket info) to the same eventId
            event_dict[event_id].append(ticket_info)
        else:
            event_dict[event_id] = [ticket_info]            #if event id is not found in event_dict we append a ney key holding event_id with its value in ticket_info

    highest = 0 
    highest_key = ''
    for key, value in event_dict.items():                   #in this part we iterate events dict and see which event has the highest number of tickets as id and we store the number
        if len(value) > highest:                            # of values in highest variable and print the key of event which is the id of it and the number of tickets 
            highest = len(value)
            highest_key = key
    return f'Event {highest_key} has the highest number of tickets {highest}'


########################## - Create Ticket - ###############################

#the following function is to create a new ticket as booking a ticket 
#removed to check if there is any removed id before to reuse it again as discussed in above functions 
#if no removed ids we take the last id in the tickets list and increment it by 1
#if removed true , the deleted id will e passed from main as parameter and stored in next_id_num
#role is to check for user changes to save, if admin nothing will be saved

def CreateTicket(removed, last_id, tickets, next_id_num, role):#O(NlgN) // since we have merge sort called

    if removed == True and next_id_num != 0:        #case of deleted id 

        current_id_num = next_id_num                #if nextid is greater than 0 we store it in current_id_num

        ticket_id = str('tick') + str(current_id_num)                       #we add 'tick' before number then add the number of id concatenated wih str
        event_id = input('Enter the event ID with deleted before id: ')     #user will fill the data here
        username = input('Enter your name : ')
        current_date = str(datetime.date.today())
        current_date = current_date.replace('-', '')
        priority = 0
        ticket = {                                                          #data added above will be stored in a ticket dictionary that will be appended after to list tickets
            'ticket_id': ticket_id,
            'event_id': event_id,
            'username': username,
            'date': current_date,
            'priority': priority
        }
        tickets.append(ticket)
        sort_id(tickets)#O(NlgN)                                                    #calling sort_id nerge sort to sort tickets by IDs
        tickets_id.append(ticket['ticket_id'])                              #appending the new id added to the tickets_id, discuused the use of this list before
        print('Following ticket is added : ', ticket)
    else:                                                                   #the case where no deleted id is found
        current_id_num = last_id + 1                                        # we take the last id found past from getlastid function and increment it by 1
        ticket_id = str('tick') + str(current_id_num)                       #rest is same as discussed above
        event_id = input('Enter the event ID for new id ticket: ')  
        username = input('Enter your name : ')
        current_date = str(datetime.date.today())
        current_date = current_date.replace('-', '')
        priority = 0
        ticket = {
            'ticket_id': ticket_id,
            'event_id': event_id,
            'username': username,
            'date': current_date,
            'priority': priority
        }
        tickets_id.append(ticket['ticket_id'])
        print('Following ticket is added : ', ticket)
        tickets.append(ticket)
    if role == 'user':                                                      #if the role is user we save changes to file
        with open('events_data.txt', 'a')as t_db:
            ticket_data = f"{ticket_id},{event_id},{username},{current_date},{priority}\n"
            t_db.write(ticket_data)
############################# - Display Ticket sorted by date - ######################################


#this function will display the tickets sorted by date using the merge sort 
#it takes tixkets only as parameter
#checks for the date if in 3 cases : Today , Tomorrow and upcoming
#today will display today's events 
# #tomorrow will to todays date a 1 since date is concatinated with in and increased days by one which will be the last number
#upcoming will display all the rest evetns


def DisplayByDate(tickets):#O(N) since independent For loops
    current_date = str(datetime.date.today())
    current_date = current_date.replace('-', '')       #get current date which is today's date
    sorted_tickets = merge_sort(tickets, 'date')       #sort tickets by date(note the second parameter 'date' sent is for merge sort's option) trying to make  it moregeneral and reusable in case of soring by priority
    print('\nEvents of today\'s date :\n')             
    for ticket in sorted_tickets:                           #in each of upcoming parts in this function we are iterating through tickets to display them accorfing to there dates
        if ticket['date'] == current_date:
            if ticket['ticket_id'] not in deleted_id:       #checking if ticket is not deleted as a douible check then checking what is the date is equal to(current,tomorrow or upcoming)
                print(ticket)                               # before printing it

    tomorrow_date = int(current_date)+1

    print('\nEvents of tomorrow\'s date :\n')
    for ticket in sorted_tickets:
        if ticket['date'] == str(tomorrow_date):
            print(ticket)
    print('\nUpcoming Events :\n')
    for ticket in sorted_tickets:
        if ticket['date'] > current_date and ticket['date'] != str(tomorrow_date):  #if the date is not current nor equal to tomorrow print upcoming 
            print(ticket)

#################################### - Change ticket priority - ##################################
#following function changes the priority of a ticket by iterating through tickets list and asking the user to enter the desired ticket id he wants to change its priority
#the we check through a loop if the id of this ticket is found then the ticket is found
#then the user is asked to enter the new priority which will be updated though accessing it where the key is priority


def ChangePriority(tickets):#O(N) // 2 dependent loops O(N) each
    ticket_id_to_change = input('Enter ticket ID : ') # Using check_integer_input to echeck for user input              
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id_to_change:
            desired_priority = check_integer_input('Enter the priority to update it : ') 
            ticket['priority'] = desired_priority           #setting the new priority when the id matches the user id input
            return print(ticket)
        
    else:
        return print(f"\nTicket ID '{ticket_id_to_change}' you entered is not found.\n")
####################################### - delete ticket by id - ######################################


# the following functiion delete a ticket user chooses through entering id

def DeleteTicket(tickets):#O(N) 1 loop
    removed_ticket = None
    print('\n\nthis is ticket_id from function :', tickets_id)
    id_to_delete = input('Enter a valid ticket ID to delete: ')         
    for ticket in tickets:
        if ticket['ticket_id'] == id_to_delete:
            removed_ticket = ticket
            tickets.remove(ticket)
            break
    if removed_ticket:
        tickets_id.remove(id_to_delete)
        deleted_id.append(str(id_to_delete))
        print('The following ticket has been removed:', removed_ticket)
        return True
    else:
        print('ID not found in the list')
        return False

############################ - Run Events - ####################################
def RunEvents(sorted_by_priority, deleted_id):
    today_event = []
    current_date = str(datetime.date.today())
    current_date = current_date.replace('-', '')
    size = len(sorted_by_priority)-1
    while size > 0:
        for ticket in sorted_by_priority:
            if ticket['date'] == current_date:
                print('\n\nthis ticket is today and will be removed : ', ticket)
                today_event.append(ticket)
                deleted_id.append(ticket['ticket_id'])
                deleted_id.sort()
                tickets_id.remove(ticket['ticket_id'])
                sorted_by_priority.remove(ticket)

        size -= 1

    return sorted_by_priority, deleted_id


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main():
    removed = False
    next_id = None
    attempts = 5
    tickets = []

    global deleted_id
    deleted_id = []
    global tickets_id
    tickets_id = []
    UploadTickets(tickets)
    tickets = sort_id(tickets)
    GetTicketsId()
    choice = 0
    print('\n\nWelcome to our Events ticketing system !\nplease enter your username and password to enter as an admin,\nelse just proceed with an empty values if user :')
    while attempts > 0:
        username = input('\n\nEnter your admin username : ')
        password = input(
            '\n\nEnter your username\'s password to proceed as admin : ')

        admin = verify_user.VerifyLogin(username, password, 'users.txt')
        if username == 'admin' and admin == True:
            attempts = 0
        elif username == 'admin' and admin == False:
            print(
                f'Enter a valid username and password , you have {attempts} remaining')
            attempts -= 1
        else:
            attempts = 0
            admin = False
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

                        print(HighestTicketsNum(tickets))
                    case 2:

                        if len(deleted_id) == 0:

                            last_id = GetLastId(removed, tickets)

                            CreateTicket(removed, last_id,
                                         tickets, deleted_id, role)

                        else:
                            removed = True
                            temp = None

                            next_id_num = GetLastId(
                                removed, tickets)
                            print('this is the deletedddddd : ', deleted_id)
                            print('this is next id num : ', next_id_num)
                            CreateTicket(removed, temp, tickets,
                                         next_id_num, role)
                            removed = False
                            tickets = sort_id(tickets)

                            print('\n\nsorted tickets  :\n', tickets)

                    case 3:

                        DisplayByDate(tickets)
                    case 4:

                        ChangePriority(tickets, tickets_id)

                    case 5:
                        removed = DeleteTicket(tickets)
                        deleted_id.sort()
                    case 6:
                        sorted_by_priority = merge_sort(tickets, 'priority')
                        sorted_by_priority.reverse()
                        tickets, deleted_id = RunEvents(
                            sorted_by_priority, deleted_id)
                        print('\n\ntickets ramining after running events : ', tickets)

            else:
                print('\n Choice should be between 1 and 7 ')

    else:
        print('Signed in as User')
        role = 'user'
        while choice != 2:
            displayUserMenu()
            choice = check_integer_input(
                'Enter your choice between 1 and 2 : ')
            if choice >= 1 and choice <= 7:
                match choice:
                    case 1:
                        print(next_id)
                        if len(deleted_id) == 0:
                            last_id = GetLastId(removed, tickets, deleted_id)
                            CreateTicket(removed, last_id,
                                         tickets, deleted_id, role)
            else:
                print('\n Choice should be between 1 and 2 ')


main()
