
##### - integer check input - #####
def check_integer_input(number): # O(N)
    while True:
        try:
            user_input = int(input(number))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")



####### - Display Menu - #########

def displayMenu():
  

  print("Choose from the following :\n1. Add Matrices\n2. Check Rotation\n3. Invert Dictionary\n4. Convert Matrix to Dictionary\n5. Check Palindrome\n6. Search for an Element\n7. exit\n")

################### - START OF MATRIX SECTION - ###################

##### - Create Matrix - #####

def createMatrix(matrix,row_num,col_num,choice):#O(N^3)
    id_list=[] #for choice 4
    
    for row in range(row_num):#O(N)
        matrix.append([])
        for col in range(col_num):#O(N)
            if choice==4: # convert matrix case
                            
                print('Data of user  ' , col+1 , ' of row number ' , row+1)    

                id = check_integer_input('Enter user\'s id : ') 
                if id not in id_list: # if id not added before accept it and add it to list 
                    id_list.append(id)
                else:
                    while id in id_list:#O(N) 
                        id = check_integer_input('\n\nAlready found user\'s id before, try another : ')#if not in list ask the user to try another one
                    id_list.append(id)    

                               
                print('\n\nEnter data of the user of ID :', id,'\n\n')                
                first_name=input('Enter user\'s first name : ')
                last_name=input('Enter user\'s last name : ')
                job_title= input('Enter user\'s job title : ')
                company = input('Enter user\'s company : ')
                matrix[row].extend([id,first_name,last_name,job_title,company])# using extend method to access adding more than 1 element to a list or matrix
                
            else:
                print('Row number : ' , row+1)                
                print('Element number  ' , col+1 )               
                user_input = check_integer_input('Enter your element number element of the matrix :')
                matrix[row].append(user_input) 
                                  
    return matrix

##### - Addition of Matrix - #####   

def addMatrix(matrix1,matrix2):#O(N^2)
    m3 = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1))] for i in range(len(matrix1))]  
    print('\n\n',matrix1 , ' + ' , matrix2 , ' = ' , m3, end='\n\n')    


##### - Check Rotation - #####

def rotationMatrix(matrix1,matrix2): #O(N^2)
    matrix1_rt=[]
    if len(matrix1)==len(matrix2):#O(1)
        for i in range(len(matrix1)):#O(N)
            result=[row[i] for row in matrix1]#O(N)  #list comprehension to iterate and add the elements
            matrix1_rt.append(result)
        print('This is matrix1 reversed : ' ,matrix1_rt)
        if matrix1_rt == matrix2:

            return '\n\nMatrices are equal\n\n'
    
        else: 
 
            return '\n\nMatrices are not equal\n\n'    

    else:
        for i in range(len(matrix1)+1):  #O(N)
            result=[row[i] for row in matrix1]#O(N)  #list comprehension to iterate and add the elements
            matrix1_rt.append(result) 
        print('This is matrix1 reversed : ' ,matrix1_rt)
        if matrix1_rt == matrix2: # comparing matrix with another matrix O(N)

            return '\n\nMatrices are equal\n\n'

        else:  
            return '\n\nMatrices are not equal\n\n'

##### - Convert Matrix to Dictionary - #####

def convert_matrix(matrix):#O(N)
    result_dict = {}
    for row in matrix:#O(N)
        id_val, first_name, last_name, job_title,company = row
        print('\n\nthis is the row converted',row)
        result_dict[str(id_val)] = [
             first_name,
            last_name,
            job_title,
            company
        ]
    return result_dict

################## - END OF MATRIX SECTION - ################

############## - START OF Dictionary Code Section - ###################

    ##### - Create Dictionary - #####

def createDict(dict):#O(N)
    done_loop=False
    while done_loop==False:#O(N)
        key=input('Enter key (Once finished enter done as a key to create your dictionary) : ')
        if key!='done':
            value=input('Enter value : ')
            dict[key]=value
                       
        else:
            done_loop=True
    return dict            

##### - Reverse Dictionart - #####

def invert_dict(dict):#O(N)
    inverted_dict = {}
    for key, value in dict.items():#O(N)
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        
        else:
            inverted_dict[value].append(key)
    return inverted_dict

    ##### - END OF Dictionary Code Section - ######


##### - Check Plaindrome - #####

def palindrome_check(s):#O(N)
    
    if len(s)<=1:
        return '\n\nWord you entered is Palindrome\n\n'
    if s[0]==s[-1]:
        return palindrome_check(s[1:-1])#O(N)
    else:
        return '\n\nThe word you entered is not palindrome\n\n'
    
#####- Check for item in list - ######

def check_list(n,list):#O(N)
    check_num=False
    for i in range(len(list)):
        if list[i]==n:
            check_num=True
            return i
        if i ==len(list)-1 and check_num==False:
            i=-1
            return i
        


##### - Merge Sort Algo - #####

def mergeSort(list): #O(NlgN)
    if len(list) > 1:
    
        
        mid = len(list)//2
        list_left = list[:mid]
        list_right = list[mid:]
        # Sort the two halves
        mergeSort(list_left)
        mergeSort(list_right)
     
        
        i = j = k = 0

        while i < len(list_left) and j < len(list_right):
            if list_left[i] < list_right[j]:
                list[k] = list_left[i]
                i += 1
            else:
                list[k] = list_right[j]
                j += 1
            k += 1

        while i < len(list_left):
            list[k] = list_left[i]
            i += 1
            k += 1
        #in case of lenght of one list is smaller than another
        while j < len(list_right):
            list[k] = list_right[j]
            j += 1
            k += 1
##### - Main - #####

def main():#O(n^3)

    name=input('Hello ! Enter your first name : ').upper()

    print(f'\n======== Welcome {name} ! ========',end='\n\n')


    choice =0
    while choice!=7 :
        
        displayMenu()

        choice= check_integer_input('\nEnter your choice please :')

        if choice>=1 and choice<=7:

            match choice: 
                case 1:   # Case of Addition
                    print('Matrices addition :')
                    matrix1=[] # List A
                    matrix2=[] # List B
                    row_num=check_integer_input('Enter the number of rows : ')
                    col_num=check_integer_input('Enter the number of columns : ')
                    matrix1=createMatrix(matrix1,row_num,col_num,choice)#O(N^3)
                    matrix2=createMatrix(matrix2,row_num,col_num,choice)#O(N^3)
                    addMatrix(matrix1,matrix2)#O(N^2)
                case 2:   # Case of rotation
                    print('Matrices rotation check\n')
                    matrix1=[] # List A
                    matrix2=[] # List B
                    # Rows and columns for Matrix X
                    row_num_x=check_integer_input('Enter the number of rows in Matrix X: ')
                    col_num_x=check_integer_input('Enter the number of columns in Matrix X : ')
                    matrix1 = createMatrix(matrix1,row_num_x,col_num_x,choice)#O(N^3)
                    print('\n\nEnter you second matrix : ')
                    matrix2= createMatrix(matrix2,col_num_x,row_num_x,choice)#O(N^3)
                    print(matrix1 , '  ' , matrix2)
                    print(rotationMatrix(matrix1,matrix2))#O(N^2)
                case 3: # case of inverting dictionaries
                    dict={}
                    print('Invert Dictionaries\n')
                    result = createDict(dict)#O(N)
                    print(f'\n\n The dictionary you entered is : {result} , Let\'s invert it:\n\n')
                    inverted_dict = invert_dict(result)#O(N)
                    print(f'\n\n The inverted dictionary result is : {inverted_dict} \n\n') 
                case 4:# case of convetiong matrix to dictionaries
                    matrix1=[]
                    print('Conveting Matrix to Dictionary\n')
                    number_of_users=check_integer_input('Enter the number of users : ')
                    col_num=1
                    matrix = createMatrix(matrix1,number_of_users,col_num,choice)#O(N^3)
                    print('The matrix you created is: ',matrix)
                    result=convert_matrix(matrix)#O(N)
                    print('\n\nThe converted matrix result is the following dictionary : ',result,'\n\n')
                    matrix.clear()
                case 5:# case of checking palindrome
                    print('Checking a word if palindrome\n')
                    s = input('Enter a word to check if its a palindrome : ')
                    result = palindrome_check(s)#O(N)
                    print(result)
                    
                case 6: 
                    # case of finding a number
                    print('Find a Number in a list\n')
                    list=[]
                    n=0
                    while n!=-1:
                        n= check_integer_input('\nEnter your list items , enter -1 once done to exit :')
                        if n!=-1:
                            list.append(n)
                    print(list)
                    n = check_integer_input('Enter the number to check at which index it is if found in list : ')
                    result = check_list(n,list)#O(N)
                    
                    if result != -1:    
                        print('\n\nNumber is at index : ',result) 
                        mergeSort(list)#O(NlgN)
                        print('\n\nSorted list using merge sort : ',list)
                    else: 
                        print('Number not found in list ! ')    
                        
        else:
            print('\n\nNumber not found in MENU , choice must be between 1 and 7 \n\n')  




                
main()
