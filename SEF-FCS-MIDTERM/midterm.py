import datetime
import verify_user as verify_user


##### - integer check input - #####
def check_integer_input(number): # O(N)
    while True:
        try:
            user_input = int(input(number))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

######## - Display Menus According to user start- #######################
def displayAdminMenu():
  
  print("\n\nChoose from the following :\n1. Display Statistics\n2. Book a Ticket\n3. Dsiplay All Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. exit\n")

def displayUserMenu():
  
  print("\n\nChoose from the following :\n1. Display Statistics\n2. Book a Ticket\n")
######## - Display Menus According to user end - #######################


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

def GetLastId(removed,tickets):
    if removed == True:
        pass
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

def createTicket(removed,last_id):
    
    if removed == True:
        pass
    else: 
        current_id_num =last_id + 1
        ticket_id = str('tick')+ str(current_id_num)
        event_id='ev008'
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
        
    with open('events_data.txt', 'a')as t_db:
        ticket_data = f"{ticket_id},{event_id},{username},{current_date},{priority}\n"
        t_db.write(ticket_data)

    
def DisplayByDate(tickets):
    current_date = str(datetime.date.today())
    current_date = current_date.replace('-','')
    print('\nEvents of today\'s date :\n')

    for ticket in tickets :
        if ticket['date']== current_date:
            print(ticket)
 
    tomorrow_date= int(current_date)+1

    print('\nEvents of tomorrow\'s date :\n')
    for ticket in tickets :
        if ticket['date']== str(tomorrow_date):
            print(ticket)
    print('\nUpcoming Events :\n')
    for ticket in tickets :
        if ticket['date']> current_date and ticket['date']!= str(tomorrow_date):
            print(ticket)
                      
def ChangePriority(tickets,tickets_id):
    ticket_id_to_change = input('Enter ticket ID : ')
    if ticket_id_to_change not in tickets_id:
        print(f"\nTicket ID '{ticket_id_to_change}' you entered is not found.\n")
    else:    
        desired_priority = check_integer_input('Enter the priority to update it : ')    

        with open('events_data.txt', 'r') as file:
            lines = file.readlines()
        print()    

        for i, line in enumerate(lines):


            ticket_id, event_id, username,date, priority = line.strip().split(',')
            if ticket_id == ticket_id_to_change:
                lines[i] = f"{ticket_id},{event_id},{username},{date},{desired_priority}\n"
                break


        with open('events_data.txt', 'w') as file:
            file.writelines(lines)

        for ticket in tickets:
            if ticket['ticket_id'] == ticket_id_to_change:
                ticket['priority']=desired_priority
                print(ticket)        


                             
def main():
    removed=False
    global tickets
    tickets=[]
    events={}

    
    UploadTickets(tickets,events)



    choice=0
    print('\n\nWelcome to our Events ticketing system !\nplease enter your username and password to enter as an admin,\nelse just proceed with an empty values if user :')

    username=input('\n\nEnter your admin username : ')
    password= input('\n\nEnter your username\'s password to proceed as admin : ')
    
    admin =verify_user.VerifyLogin(username,password,'users.txt')
    admin=True
    if admin==True:

        print('Signed in as Admin')
        displayAdminMenu()
        
        
        while choice!=7:
            choice= check_integer_input('Enter your choice between 1 and 7 : ')
            if choice>=1 and choice<=7:
                match choice:
                    case 1:
                        print(HighestTicketsNum(events))  
                    case 2:
                        last_id = GetLastId(removed,tickets)
                        createTicket(removed,last_id)
                       
                    case 3: 
                        DisplayByDate(tickets)
                    case 4:
                        tickets_id=[]
                        GetTicketsId(tickets_id) 
                        ChangePriority(tickets,tickets_id)
            else:
                print('\n Choice should be between 1 and 7 ')


    else:
        
        displayUserMenu()    
        

main()        