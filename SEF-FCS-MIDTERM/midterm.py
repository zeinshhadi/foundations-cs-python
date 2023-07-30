
# In the following ticketing system , removed ID chosen by user is handled in  a way that the next ticket to be added after a deleted one will tkae the deleted id and dort the tickets by id

import datetime
import verify_user as verify_user
# -------------------------------------------------------Displaying Menus Section--------------------------------------------------------------------------------------------------------------#
######## - Display Menu to admin - #######################


def displayAdminMenu():

    print("\n\nChoose from the following :\n1. Display Statistics\n2. Book a Ticket\n3. Dsiplay All Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. exit\n")
######## - Display User to admin - #######################


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
##### - merge sort for sorting ID - ######


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

##### - Merge Sort - ############


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


############# - Add Ids to a list - #################
# The following function will alse open the file storing the data and gets only the first index after splitting using the comma delimiter which is the ticcket ID
# Then the ids will be stored in a global list defined in the main called tickets_id
# This list is used to handle the next ticket ID that will be added to the system,so this list will handle the already used ids

def GetTicketsId():
    with open('events_data.txt', 'r') as file:
        for line in file:
            ticket_data = line.strip().split(',')
            if len(ticket_data) < 5:
                continue
            tickets_id.append(ticket_data[0])
        return tickets_id


###### -  Get Last Id - ########
# The following function will get the last id of the tickets , bby this we handled that the next ticket to be added will have the (oldId +1) since ID is auto incrementing
# removed in parameters is a boolean inialized in the main function and used when a ticket is deleted.
# when deleted a ticket removed get a true to let the function know that we have a deleted ID that should be the next id added to the nxt ticket
# deleted_id is a global list inialized in main too where all deleted ticket's ID are stored in it , to make sure that the next ticket will be added will take an ID from this list
# By this we will handle the IDs and avoid duplication and protect the sequence of the IDs
# tickets is the list holding the tickets

def GetLastId(removed, tickets):  # O(1) // ALL of the function is using constants
    # in the case that we have a deleted ticket before , we handle its ID
    if removed == True and len(deleted_id) != 0:
        next_id = deleted_id[0]              # next_id is the id that will be added next to the net ticket will be equal to the fist index of the deleted_id list

        deleted_id.remove(deleted_id[0])     # The taken id which is in the first index then is removed from the deleted_id list to prevent duplication
        
        next_ticket_id = int(next_id[4:])    # The tickets id pattern is as dollows: tick100 , tick101, tick103,.. etc so in this line im taking a substring where
                                             # i remove the 'tick' part and store the number after it as an integer using concatination

        return next_ticket_id
    else: # this is the case where no deleted ids are found in the deleted id list 
        last_index = len(tickets)-1  #we get the last index of the tickets list which will be golding the last ticket id we have

        last_ticket_id = tickets[last_index]['ticket_id'] #We get the ticket ID of the last ticket 

        last_ticket_id = int(last_ticket_id[4:])    # The tickets id pattern is as dollows: tick100 , tick101, tick103,.. etc so in this line im taking a substring where
                                                    # i remove the 'tick' part and store the number after it as an integer using concatination

        return last_ticket_id


# -----------------------------------------------------------Choices chosen functions Section-----------------------------------------------------------------------------------------#

def HighestTicketsNum(tickets):
    event_dict = {}

    for ticket in tickets:
        event_id = ticket["event_id"]
        ticket_info = {}
        for key, value in ticket.items():
            if key != "event_id":
                ticket_info[key] = value

        if event_id in event_dict:
            event_dict[event_id].append(ticket_info)
        else:
            event_dict[event_id] = [ticket_info]

    highest = 0
    highest_key = ''
    for key, value in event_dict.items():
        if len(value) > highest:
            highest = len(value)
            highest_key = key
    return f'Event {highest_key} has the highest number of tickets {highest}'


####### - Create Ticket - ########

def createTicket(removed, last_id, tickets, next_id_num, role):

    if removed == True and next_id_num != 0:

        current_id_num = next_id_num

        ticket_id = str('tick') + str(current_id_num)
        event_id = input('Enter the event ID with deleted before id: ')
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
        tickets.append(ticket)
        sort_id(tickets)
        tickets_id.append(ticket['ticket_id'])

    else:
        current_id_num = last_id + 1
        ticket_id = str('tick') + str(current_id_num)
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
    if role == 'user':
        with open('events_data.txt', 'a')as t_db:
            ticket_data = f"{ticket_id},{event_id},{username},{current_date},{priority}\n"
            t_db.write(ticket_data)


def DisplayByDate(tickets):
    current_date = str(datetime.date.today())
    current_date = current_date.replace('-', '')
    sorted_tickets = merge_sort(tickets, 'date')
    print('\nEvents of today\'s date :\n')
    for ticket in sorted_tickets:
        if ticket['date'] == current_date:
            if ticket['ticket_id'] not in deleted_id:
                print(ticket)

    tomorrow_date = int(current_date)+1

    print('\nEvents of tomorrow\'s date :\n')
    for ticket in sorted_tickets:
        if ticket['date'] == str(tomorrow_date):
            print(ticket)
    print('\nUpcoming Events :\n')
    for ticket in sorted_tickets:
        if ticket['date'] > current_date and ticket['date'] != str(tomorrow_date):
            print(ticket)


def ChangePriority(tickets, tickets_id):
    ticket_id_to_change = input('Enter ticket ID : ')
    for i in range(len(tickets_id)):
        if tickets_id[i] == ticket_id_to_change:
            desired_priority = check_integer_input(
                'Enter the priority to update it : ')

            for ticket in tickets:
                if ticket['ticket_id'] == ticket_id_to_change:
                    ticket['priority'] = desired_priority
                    return print(ticket)

    else:
        return print(f"\nTicket ID '{ticket_id_to_change}' you entered is not found.\n")
###### - delete ticket by id - #########


def DeleteTicket(tickets):
    print('\n\nthis is ticket_id from function :', tickets_id)
    id_to_delete = input('Enter a valid ticket ID to delete: ')
    if id_to_delete == '':
        print('Invalid input. Ticket ID cannot be null.')

    for i in range(len(tickets_id)):
        if tickets_id[i] == id_to_delete:
            removed_ticket = None
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
                print('Error: Ticket with ID not found')
                return False

    print('ID not found in the list')
    return False


##### - Run Events - #######
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

                            createTicket(removed, last_id,
                                         tickets, deleted_id, role)

                        else:
                            removed = True
                            temp = None

                            next_id_num = GetLastId(
                                removed, tickets)
                            print('this is the deletedddddd : ', deleted_id)
                            print('this is next id num : ', next_id_num)
                            createTicket(removed, temp, tickets,
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
                            createTicket(removed, last_id,
                                         tickets, deleted_id, role)
            else:
                print('\n Choice should be between 1 and 2 ')


main()
