import datetime
import verify_user as verify_user

######## - Display Menus According to user start- #######################
def displayAdminMenu():
  
  print("\n\nChoose from the following :\n1. Display Statistics\n2. Book a Ticket\n3. Dsiplay All Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. exit\n")

def displayUserMenu():
  
  print("\n\nChoose from the following :\n1. Book a Ticket\n2. exit\n")
######## - Display Menus According to user end - #######################
##### - integer check input - #####
def check_integer_input(number): # O(N)
    while True :
        try:
            user_input = int(input(number))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

##### - Merge Sort - ############

def merge_sort(arr,option):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half,option)
    right_half = merge_sort(right_half,option)

    return merge(left_half, right_half,option)

def merge(left, right,option):
    merged_list = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        left_date = int(left[left_idx][option])
        right_date = int(right[right_idx][option])

        if left_date <= right_date:
            merged_list.append(left[left_idx])
            left_idx += 1
        else:
            merged_list.append(right[right_idx])
            right_idx += 1

    merged_list.extend(left[left_idx:])
    merged_list.extend(right[right_idx:])
    
    return merged_list
            
###### - BS Algorithm - ######

def binary_search(arr, low, high, x):
 

    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
   
        return 'ID not found in list'



####### - Upload tickets and events to corresponding lists and dictionaries - ########
def UploadTickets( tickets, events):
    with open('events_data.txt', 'r') as file:
        for line in file:
            ticket_data = line.strip().split(',')
            if len(ticket_data) < 5:
                continue
            ticket = {
                'ticket_id': ticket_data[0],
                'event_id': ticket_data[1],
                'username': ticket_data[2],
                'date': ticket_data[3],
                'priority': int(ticket_data[4])
            }
            event = {
                'ticket_id': ticket_data[0],
                'username': ticket_data[2],
                'date': ticket_data[3],
                'priority': int(ticket_data[4])
            }
            tickets.append(ticket)
            events.setdefault(ticket_data[1], []).append(event)

####### - Add Ids to a list - ########


def GetTicketsId(tickets_id):
     with open('events_data.txt', 'r') as file:
        for line in file:
            ticket_data = line.strip().split(',')
            if len(ticket_data) < 5:
                continue
            tickets_id.append(ticket_data[0])
        return tickets_id


###### -  Get Last Id - ########

def GetLastId(removed,tickets,next_id):
    if removed == True and next_id!=None:
        next_ticket_id = int(next_id[4:])
        return next_ticket_id
    else: 
        last_index = len(tickets)-1
        last_ticket_id =tickets[last_index]['ticket_id']
        last_ticket_id = int(last_ticket_id[4:])
        return last_ticket_id

def HighestTicketsNum(events):

    highest =0
    highest_key=''
    for key, value in events.items():
        if len(value)>highest:
            highest=len(value)
            highest_key=key
    return f'Event {highest_key} has the highest number of tickets {highest}'   

####### - Create Ticket - ########

def createTicket(removed,last_id,tickets,next_id,role):
    
    if removed == True and next_id!=None:
        current_id_num =next_id
        ticket_id = str('tick')+ str(current_id_num)
        event_id=input('Enter the event ID with deleted before id: ')
        username=input('Enter your name : ')
        current_date = str(datetime.date.today())
        current_date = current_date.replace('-','')
        priority=0
        ticket = {
                'ticket_id': ticket_id,
                'event_id': event_id,
                'username':username,
                'date': current_date,
                'priority': priority
            }
        print('Following ticket is added with deleted before id: ' , ticket)
        tickets.append(ticket)
        return removed==False,next_id==None
        

    else: 
        current_id_num =last_id + 1
        ticket_id = str('tick')+ str(current_id_num)
        event_id=input('Enter the event ID for new id ticket: ')
        username=input('Enter your name : ')
        current_date = str(datetime.date.today())
        current_date = current_date.replace('-','')
        priority=0
        ticket = {
                'ticket_id': ticket_id,
                'event_id': event_id,
                'username':username,
                'date': current_date,
                'priority': priority
            }
        tickets.append(ticket)
    if role=='user':    
        with open('events_data.txt', 'a')as t_db:
            ticket_data = f"{ticket_id},{event_id},{username},{current_date},{priority}\n"
            t_db.write(ticket_data)

    
def DisplayByDate(tickets):
    current_date = str(datetime.date.today())
    current_date = current_date.replace('-','')
    sorted_tickets=merge_sort(tickets,'date')
    print('\nEvents of today\'s date :\n')
    for ticket in sorted_tickets :
        if ticket['date']== current_date:
            print(ticket)
 
    tomorrow_date= int(current_date)+1

    print('\nEvents of tomorrow\'s date :\n')
    for ticket in sorted_tickets :
        if ticket['date']== str(tomorrow_date):
            print(ticket)
    print('\nUpcoming Events :\n')
    for ticket in sorted_tickets :
        if ticket['date']> current_date and ticket['date']!= str(tomorrow_date):
            print(ticket)
                      
def ChangePriority(tickets,tickets_id):
    ticket_id_to_change = input('Enter ticket ID : ')
    if ticket_id_to_change not in tickets_id:
        print(f"\nTicket ID '{ticket_id_to_change}' you entered is not found.\n")
    else:    
        desired_priority = check_integer_input('Enter the priority to update it : ')    

        for ticket in tickets:
            if ticket['ticket_id'] == ticket_id_to_change:
                ticket['priority']=desired_priority
                print(ticket)     

###### - delete ticket by id - #########
def DeleteTicket(tickets,tickets_id):
    next_id=''
    id_to_delete = input('Enter a valid ticket ID to delete : ')
    if id_to_delete not in tickets_id:
        print(f"\nTicket ID '{id_to_delete}' you entered is not found.\n")
    else:    
        for ticket in tickets:
           
            if ticket['ticket_id']==id_to_delete:
                tickets.remove(ticket)
                removed = True
                next_id=id_to_delete
                print('The following ticket has been removed : ',ticket)
                return removed,next_id

##### - Run Events - #######
def RunEvents (sorted_by_priority):
    today_event=[]
    current_date = str(datetime.date.today())
    current_date = current_date.replace('-','')
    for ticket in sorted_by_priority :
        if ticket['date']== current_date:
            today_event.append(ticket)
            sorted_by_priority.remove(ticket)
    tickets=sorted_by_priority         
    print(f'Today\s Events were : {today_event}\n\n\nRemaining Events are {sorted_by_priority}')
    return tickets        

def main():
    removed=False
    next_id=None
    attempts = 5
    tickets=[]
    events={}

    UploadTickets(tickets,events)

    choice=0
    print('\n\nWelcome to our Events ticketing system !\nplease enter your username and password to enter as an admin,\nelse just proceed with an empty values if user :')
    while attempts>0:
        username=input('\n\nEnter your admin username : ')
        password= input('\n\nEnter your username\'s password to proceed as admin : ')

        admin =verify_user.VerifyLogin(username,password,'users.txt')
        if username == 'admin' and admin==True:
            attempts=0
        elif username =='admin' and admin ==False:
            print(f'Enter a valid username and password , you have {attempts} remaining')
            attempts-=1
        else: 
            attempts=0
            admin=False    
 
    if admin==True:

        print('Signed in as Admin')
       
        
        
        while choice!=7:
            role='admin'
            displayAdminMenu()
            choice= check_integer_input('Enter your choice between 1 and 7 : ')
            if choice>=1 and choice<=7:
                match choice:
                    case 1:
                        print(HighestTicketsNum(events))  
                    case 2:
                        print(next_id)
                        if next_id == None:
                            last_id = GetLastId(removed,tickets,next_id)
                            createTicket(removed,last_id,tickets,next_id,role)
                        else:
                            last_id=None
                            next_id_num = GetLastId(removed,tickets,next_id)
                            removed,next_id=createTicket(removed,last_id,tickets,next_id_num,role)                                
                       
                    case 3:
                        DisplayByDate(tickets)
                    case 4:
                        tickets_id=[]
                        GetTicketsId(tickets_id) 
                        ChangePriority(tickets,tickets_id)
                    case 5:
                        tickets_id=[]
                        GetTicketsId(tickets_id)                   
                        removed,next_id =DeleteTicket(tickets,tickets_id)
                        print('this is next id: ',next_id)
                        print(removed)
                    case 6:
                        sorted_by_priority=merge_sort(tickets,'priority')
                        sorted_by_priority.reverse()
                        tickets=RunEvents(sorted_by_priority)

            else:
                print('\n Choice should be between 1 and 7 ')


    else:
        print('Signed in as User')
        role='user'
        while choice!=2:
            displayUserMenu()
            choice= check_integer_input('Enter your choice between 1 and 2 : ')
            if choice>=1 and choice<=7:
                match choice:
                    case 1:
                        print(next_id)
                        if next_id == None:
                            last_id = GetLastId(removed,tickets,next_id)
                            createTicket(removed,last_id,tickets,next_id,role)
                        else:
                            last_id=None
                            next_id_num = GetLastId(removed,tickets,next_id)
                            removed,next_id=createTicket(removed,last_id,tickets,next_id_num,role)    
            else:
                print('\n Choice should be between 1 and 2 ')  
        

main()        