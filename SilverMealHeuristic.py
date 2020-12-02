#########################################################
# SILVER MEAL HEURISTIC (composed by Edward A. Silver & H.C. Meal)
# Heuristic for the dynamic lot-size model
#########################################################

# given demands for a given planning horizon;
# order-fixed costs;
# given inventory cost rate per unit per period;
# infinite capacities;

# question: When do I order how much taking into account fixed-order costs and inventory costs;

# criterion: The order amount in period tau is increased by the demand in period t,
#     if the average cost c(tau,t) are not larger than c(tau,t-1);

# c(tau,t) are the average costs per period whose demand is covered by the order in tau,
#     if this very order covers the demand until t;
#------------------------------------------------------------------------------------------------

# order-fixed costs:
s = 250
# inventory cost rate per unit per period:
l = 2
# demands:
d_t= [100,120,80,110,80,40,10]
# -----------------------------------------------------

def silvermeal(fixcost, inventory_cost, demands):
   tau = 1
   t = 1
   previous_cost = fixcost
   order_amounts = []
   T = len(demands) # planning horizon

   for i in range(T):
      order_amounts.append(0)
   quantity = 0

   while t <= T:
      var_cost = 0
      for r in range(tau,t+1):
         var_cost += inventory_cost*(r-tau)*demands[r-1]
      average_cost = (fixcost + var_cost)/(t-tau+1)

      if average_cost <= previous_cost: # increase -> order also for t in tau"
            previous_cost = average_cost
            quantity += demands[t-1]
            increase = True
      
      else: # do not increase -> order in period t
         order_amounts[tau-1] = quantity
         tau = t
         quantity = demands[t - 1]
         previous_cost = fixcost
         increase = False

      if t == T:
         order_amounts[tau - 1] = quantity
      t += 1

   return(order_amounts)

solution = silvermeal(s,l,d_t)

# Write solution
for i in range(len(solution)):
   print("Order amount in period",i+1, "is", solution[i])