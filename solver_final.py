#!/usr/biN//env python3

import sys
import math
import itertools

from common import print_solution, read_input


def distance(city1, city2):
   return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)



def solve(cities):
   N = len(cities)
   cities_a = []
   cities_b = []
   cities_c = []
   cities_d = []
   cities_e = []
   cities_f = []
   cities_g = []
   cities_h = []

   dist = [[0] * N for i in range(N)]
   for i in range(N):
       for j in range(N):
           dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

   current_city = 0
   unvisited_cities = set(range(1, N))


   def distance_from_current_city(to):
       return dist[current_city][to]

   mostfar_city = max(unvisited_cities, key=distance_from_current_city)
   max_distance = distance_from_current_city(mostfar_city)

   maxX_city = max(cities, key = (lambda city: city[0]))
   maxY_city = max(cities, key = (lambda city: city[1]))

   maxX = maxX_city[0]
   maxY = maxY_city[1]


   def search_centercity(cities):
       leastdistance = maxX
       for i in range(N):
           newdistance = math.sqrt((650 - cities[i][0]) ** 2 + (350 - cities[i][1]) ** 2)
           if newdistance < leastdistance:
               leastdistance = newdistance
               centercity = i
       return centercity

   current_city = search_centercity(cities)
   solution = [current_city]

   for i in range(0, N):
       if i == current_city:
           pass
       elif (cities[i][0] <= maxX/4.0) and (cities[i][1] <= maxY/2.0):
           cities_a.append(i)
       elif (cities[i][0] <= maxX/2.0) and (cities[i][1] <= maxY/2.0):
           cities_b.append(i)
       elif (cities[i][0] <= 3*maxX/4.0) and (cities[i][1] <= maxY/2.0):
           cities_c.append(i)
       elif (cities[i][1] <= maxY/2.0):
           cities_d.append(i)
       elif (cities[i][0] <= maxX/4.0):
           cities_e.append(i)
       elif (cities[i][0] <= maxX/2.0):
           cities_f.append(i)
       elif (cities[i][0] <= 3*maxX/4.0):
           cities_g.append(i)
       else: cities_h.append(i)


   while cities_b:
       next_city = min(cities_b, key=distance_from_current_city)
       cities_b.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   while cities_a:
       next_city = min(cities_a, key=distance_from_current_city)
       cities_a.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   while cities_e:
       next_city = min(cities_e, key=distance_from_current_city)
       cities_e.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   while cities_f:
       next_city = min(cities_f, key=distance_from_current_city)
       cities_f.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   while cities_g:
       next_city = min(cities_g, key=distance_from_current_city)
       cities_g.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   while cities_h:
       next_city = min(cities_h, key=distance_from_current_city)
       cities_h.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   while cities_d:
       next_city = min(cities_d, key=distance_from_current_city)
       cities_d.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   while cities_c:
       next_city = min(cities_c, key=distance_from_current_city)
       cities_c.remove(next_city)
       solution.append(next_city)
       current_city = next_city

   def two_opt(cities):
       total = 0
       distanceA = 0
       distanceB = 0
       while True:
           #print cities
           count = 0
           for i in range(0,N-2):
               for j in range(i+2, N):
                   if j==N-1:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[0]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[0]]
                   else:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]
                   if distanceB < distanceA:
                       cities[i+1], cities[j] = cities[j], cities[i+1]
                       count += 1
           total += count
           if count < 1:
               break

       return cities

   def two_opt_div(cities):
       total = 0
       distanceA = 0
       distanceB = 0
       m = N
       while True:
           count = 0
           for i in range(0,N//4-2):
               for j in range(i+2, N//4):
                   if j==N-1:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[0]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[0]]
                   else:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]
                   if distanceB < distanceA:
                       cities[i+1], cities[j] = cities[j], cities[i+1]
                       count += 1
           total += count
           #print"count"
           #print count
           if count < 1:
               break

       while True:
           count = 0
           for i in range(N//4,2*N//4-2):
               for j in range(i+2, 2*N//4):
                   if j==N-1:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[0]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[0]]
                   else:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]
                   if distanceB < distanceA:
                       cities[i+1], cities[j] = cities[j], cities[i+1]
                       count += 1
           total += count
           #print"count"
           #print count
           if count < 1:
               break
       while True:
           count = 0
           for i in range(2*N//4,3*N//4-2):
               for j in range(i+2, 3*N//4):
                   if j==N-1:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[0]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[0]]
                   else:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]
                   if distanceB < distanceA:
                       cities[i+1], cities[j] = cities[j], cities[i+1]
                       count += 1
           total += count
           #print"count"
           #print count
           if count < 4:
               break
       while True:
           count = 0
           for i in range(3*N//4,N-2):
               for j in range(i+2, N):
                   if j==N-1:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[0]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[0]]
                   else:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]
                   if distanceB < distanceA:
                       cities[i+1], cities[j] = cities[j], cities[i+1]
                       count += 1
           total += count
           #print"count"
           #print count
           if count < 1:
               break

       return cities


   def three_opt(cities):
       total = 0
       distanceA = 0
       distanceB = 0
       while True:
           count = 0
           for i in range(N-5):
               if dist[solution[i]][solution[i+2]] + dist[solution[i+1]][solution[i+4]] + dist[solution[i+3]][solution[i+5]] < dist[solution[i]][solution[i+1]] + dist[solution[i+2]][solution[i+3]] + dist[solution[i+4]][solution[i+5]]:
                   cities[i+1], cities[i+2] = cities[i+2], cities[i+1]
                   cities[i+3], cities[i+4] = cities[i+4], cities[i+3]
                   count += 1

               elif dist[solution[i]][solution[i+4]] + dist[solution[i+2]][solution[i+5]] + dist[solution[i+1]][solution[i+3]] < dist[solution[i]][solution[i+1]] + dist[solution[i+2]][solution[i+3]] + dist[solution[i+4]][solution[i+5]]:
                   cities[i+1], cities[i+4] = cities[i+4], cities[i+1]
                   cities[i+3], cities[i+5] = cities[i+5], cities[i+3]
                   count += 1

               elif dist[solution[i]][solution[i+4]] + dist[solution[i+1]][solution[i+2]] + dist[solution[i+3]][solution[i+5]] < dist[solution[i]][solution[i+1]] + dist[solution[i+2]][solution[i+3]] + dist[solution[i+4]][solution[i+5]]:
                   cities[i+1], cities[i+4] = cities[i+4], cities[i+1]
                   cities[i+3], cities[i+1] = cities[i+1], cities[i+3]
                   count += 1

               elif dist[solution[i]][solution[i+5]] + dist[solution[i+3]][solution[i+4]] + dist[solution[i+1]][solution[i+2]] < dist[solution[i]][solution[i+1]] + dist[solution[i+2]][solution[i+3]] + dist[solution[i+4]][solution[i+5]]:
                   cities[i+1], cities[i+5] = cities[i+5], cities[i+1]
                   cities[i+2], cities[i+4] = cities[i+4], cities[i+2]
                   count += 1
           total += count
           if count < 1:
               break

       return cities

   def two_opt_div_half(cities):
       total = 0
       distanceA = 0
       distanceB = 0
       m = N
       while True:
           count = 0
           for i in range(0,N//2-2):
               for j in range(i+2, N//2):
                   if j==N-1:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[0]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[0]]
                   else:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]
                   if distanceB < distanceA:
                       cities[i+1], cities[j] = cities[j], cities[i+1]
                       count += 1
           total += count
           #print"count"
           #print count
           if count < 1:
               break

       while True:
           count = 0
           for i in range(N//2,N-2):
               for j in range(i+2, N):
                   if j==N-1:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[0]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[0]]
                   else:
                       distanceA = dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]]
                       distanceB = dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]
                   if distanceB < distanceA:
                       cities[i+1], cities[j] = cities[j], cities[i+1]
                       count += 1
           total += count
           #print"count"
           #print count
           if count < 1:
               break
       return cities



   def or_opt(cities, divnumber):
       total = 0
       for i in range(1, divnumber+1):
           for j in range(0+(i-1)*N//divnumber, i*N//divnumber):
               while True:
                   count = 0
                   #print j
                   length = i*N//divnumber
                   #print length
                   pre_city1 = j-1
                   post_city1 = j+1
                   if pre_city1 < 0: pre_city1 = divnumber-1
                   if post_city1 == length: post_city1 = 0
                   for k in range(length):
                       #print k
                       #print post_city1
                       post_city2 = k+1
                       if post_city2 == length: post_city2 = 0
                       if k != j and post_city2 != j:
                           if dist[solution[pre_city1]][solution[post_city1]] + dist[solution[k]][solution[j]] + dist[solution[j]][solution[post_city2]] < dist[solution[pre_city1]][solution[j]] + dist[solution[j]][solution[post_city1]] + dist[solution[k]][solution[post_city2]]:
                               p = solution[j]
                               if post_city1 == 0:
                                   solution.pop()
                               else:
                                   solution[j:post_city1] = []

                               if j < k:
                                   solution[k:k] = [p]
                               else:
                                   solution[post_city2:post_city2] = [p]
                               count += 1
                               #print solution

                   total += count
                   #print count
                   if count < 1:
                       break
       return cities


   solution = two_opt_div(solution)
   #solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)
   solution = two_opt_div(solution)
   #solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)

   solution = two_opt_div(solution)
   #solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)

   return solution


if __name__ == '__main__':
   assert len(sys.argv) > 1
   solution = solve(read_input(sys.argv[1]))
   print_solution(solution)
