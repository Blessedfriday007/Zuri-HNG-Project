def computepay(hours, rate):
   #hours should not be greater than 40
   if hours >= 40:
      #calculate pay with time and a half for extra hours
      pay = 40 * rate + (hours - 40) * rate * 1.5
   else:
      pay = hours * rate
      return pay
   #prompting the user hours and rate per hour
   hours = input("Enter hours:")
   rate = input ("Enter rate:")
   #conveting the parameters/ strings to numbers
   hours =float(hours)
   rate =float(rate)
   #call the function you created above to compute the grosspay
   pay = computepay(hours, rate)
   #print the result
   print("pay:", pay)

      
      






