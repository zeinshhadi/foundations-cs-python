def VerifyLogin(username,password,filepath):
    try:
        password = password+"\n"

        with open(filepath,'r') as file:


            lines=file.readlines()

            for line in lines:

                fields = line.split(',')
           
                if(fields[0]==username and fields[1]==password):

                    return True
                
    except Exception:

        print(Exception)      

    return False
