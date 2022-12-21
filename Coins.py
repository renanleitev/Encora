# Save the code to Coins.py file and run with the command "py -u Coins.py" (Windows) or "python3 -u Coins.py" (Linux)
# The function below will show all the possible results for a given number of coins 
# amount = number of coins
def makeChange(amount):
  # Showing the value of each coin (quarters, dimes, nickels and pennies)
  coins = [25, 10, 5, 1]
  # Final set (to show all possible results)
  final = set()
  # Loop through the coins to show all possible coins (nested loop), to the most value (quarter) to lowest value (pennies)
  # Each "for" represents a type of coin and the maximum value that can be reached, according to the "amount" variable
  # P.S: +1 = to compensate the final range
  for quarters in range (0,int(amount/coins[0])+1):
    for dimes in range(0,int((amount-coins[0]*quarters)/coins[1])+1):
      for nickels in range(0,int((amount-coins[0]*quarters-coins[1]*dimes)/coins[2])+1):
        # Pennies don't need to loop "for" (it is the lowest value == 1)
        pennies=amount-coins[0]*quarters-coins[1]*dimes-coins[2]*nickels
        # Temporarily stores the result of the loop
        result = (quarters, dimes, nickels, pennies)
        # Append the temporary result into the final set
        final.add(result)
  # Returns the set
  return final
# Output the set on terminal
print(makeChange(12))
# Output the type == set
print(type(makeChange(12)))
