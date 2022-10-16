import  colorama
from colorama import Fore


print("Hello!! Welcome to One and Zero")
print( "Here is a guide to help you ' How to Start '")
print("step1. Create an Ad\n Step2. Select Category for Your Ad\n Step3. Choose Price and Duration for your Ad\n Step4. Select Platform to place your Ad\n Step5. Submit\n")

print("Select your Ad Category\n Press 1 for Beauty Things\n Press 2 for Gaming Things\n Press 3 for Software Product\n Press 4 for Electronics Product\n Press 5 for Sports Product\n Press 6 for Home Essentials\n Press 7 for Food Items\n Press 8 to Go Back\n Press 0 to Exit\n")

Category = int(input("Press Your Category Number : "))
if 1 <= Category <= 7:
      if Category == 1:
            print("You Selected Beauty Things")
      elif Category == 2:
            print("You Selected Gaming Things")
      elif Category == 3:
            print("You Selected Software Product")
      elif Category == 4:
            print("You Selected Electronics Product")
      elif Category == 5:
            print("You Selected Sports Product")
      elif Category == 6:
            print("You Selected Home Essentials")
      else:
            print("You Selected Food Items")


else:
      print("Enter a number from 1 to 7")
      exit()

print("Enter Your CPV and CPC in Paisa")
CPC = float(input("Enter Your CPV"))
CPV = float(input("Enter Your CPC"))

if CPC > 0 and CPV > 0 :
      print("Your CPC IS ", CPC)
      print("Your CPV IS ", CPV)
else :
      print("Your CPC and CPV should be greater than 0 Paisa ")
      exit()

def choice():
      print("Would you like to continue with your CPC and CPV ?")
      Price = input("Type yes or no : ").lower()
      if Price == "yes":
            platform()
      elif Price == "no":
            exit()
      else:
            choice()

def platform():
      if 1<= CPV <= 9 and 1 <= CPC <= 5 :
            if Category == 1 or 2 or 5:
                  print("You should go with Email Ads\n Email impressions as well as sales will be good \n") #less risk average sales
            else:
                  print("You should go with Other Site Ads\n your impression will be avarage but sales will be more\n ") # affiliate as Other site

      elif 1 <= CPV <= 19 and 6 <= CPC <= 12:
            if Category == 1 or 2 or 5:
                  print("You should go with Facebook Ads\n you will get good views and sales\n ") #little risk but more gain

            else:
                  print("You should go with Email and Other Site Ads and you should give few promotion coupons to attract people \n") # good gain with little risk

      elif 20 <= CPV <= 40 and 13<= CPC <= 25:
            if Category == 1 or 2 or 5:
                  print("You should go with Facebook Ads and other site Ads to get good views with sales\n and your impressions on facebook and othersite will also be good \n")

            else :
                  print("you should go with youtube Ads or Email Ads to increase views and sales ")

      elif 41 <= CPV <= 58 and 26 <= CPC <= 50 :
            print("You should go with Google Ads , the best place to increase your click rate to achieve your sales .")


      else:
            print("You should go with Google Ads Facebook Ads and Other Site Ads , CTR and Views will help you to increase sales at peak ")

choice()

print(Fore.YELLOW + "Code for Digital Marketing by Team 'One and Zero' ")

