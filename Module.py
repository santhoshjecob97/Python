class classmultiple():
    
    def Subfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in List:
            print(temp)
            
    def oddeven():
        num=int(input("Enter the number:"))
        if(num%2==1):
            print(num,"is odd number")
        else:
            print(num,"is Even Number")

    def eligible():
        gender = input("Your Gender is: ")
        age = int(input("Your Age is: "))
        
        if gender == 'male':
            if age >= 21:
                print("eligible")
            else:
                print("not eligible")
        elif gender == 'female':
            if age >= 18:
                print("eligible")
            else:
                print("not eligible")
        else:
            print('invalid input data')

    def percentage():
            s1 = int(input("Subject1 = "))
            s2 = int(input("Subject2 = "))
            s3 = int(input("Subject3 = "))
            s4 = int(input("Subject4 = "))
            s5 = int(input("Subject5 = "))
            Total = s1 + s2 + s3 + s4 + s5
            print("Total : ", Total)
            Percent = (Total / 500) * 100
            print("Percentage :",Percent)

    def triangle():
         Height=int(input("Height:"))
         breath=int(input("Breath:"))
         print("Area formula: (Height*Breath)/2")
         print("Area of Triangle: ",(Height*breath)/2)
         Height1=int(input("Height1:"))
         Height2=int(input("Height2:"))
         breath=int(input("Breath:"))
         print("Perimeter formula: Height1+Height2+Breath")
         print("Perimeter of Triangle: ",Height1+Height2+breath)