#!/usr/bin/env python3

import sys
import math
import itertools

from common import print_solution, read_input


def distance(city1, city2):
   return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)



def solve(cities):
   N = len(cities)

   areas = [[] for i in range(16)]

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

   maxX = 1500
   maxY = 700


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
       elif (cities[i][0] <= maxX/4.0) and (cities[i][1] <= maxY/4.0):
           areas[2].append(i)
       elif (cities[i][0] <= 2*maxX/4.0) and (cities[i][1] <= maxY/4.0):
           areas[1].append(i)
       elif (cities[i][0] <= 3*maxX/4.0) and (cities[i][1] <= maxY/4.0):
           areas[14].append(i)
       elif (cities[i][1] <= maxY/4.0):
           areas[13].append(i)
       elif (cities[i][0] <= maxX/4.0) and (cities[i][1] <= 2*maxY/4.0):
           areas[3].append(i)
       elif (cities[i][0] <= 2*maxX/4.0) and (cities[i][1] <= 2*maxY/4.0):
           areas[0].append(i)
       elif (cities[i][0] <= 3*maxX/4.0) and (cities[i][1] <= 2*maxY/4.0):
           areas[15].append(i)
       elif (cities[i][1] <= 2*maxY/4.0):
           areas[12].append(i)
       elif (cities[i][0] <= maxX/4.0) and (cities[i][1] <= 3*maxY/4.0):
           areas[4].append(i)
       elif (cities[i][0] <= 2*maxX/4.0) and (cities[i][1] <= 3*maxY/4.0):
           areas[7].append(i)
       elif (cities[i][0] <= 3*maxX/4.0) and (cities[i][1] <= 3*maxY/4.0):
           areas[8].append(i)
       elif (cities[i][1] <= 3*maxY/4.0):
           areas[11].append(i)
       elif (cities[i][0] <= maxX/4.0):
           areas[5].append(i)
       elif (cities[i][0] <= 2*maxX/4.0):
           areas[6].append(i)
       elif (cities[i][0] <= 3*maxX/4.0):
            areas[9].append(i)
       else:
           areas[10].append(i)

   def search_in_area(area):
       while area:
           next_city = min(area, key = distance_from_current_city)
           area.remove(next_city)
           solution.append(next_city)
           current_city = next_city

   for i in range(0,16):
       search_in_area(areas[i])



   def two_opt(cities):
       total = 0
       distanceA = 0
       distanceB = 0
       while True:
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
           print"count"
           print count
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
           for i in range(0,N/4-2):
               for j in range(i+2, N/4):
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
           print"count"
           print count
           if count < 1:
               break

       while True:
           count = 0
           for i in range(N/4,2*N/4-2):
               for j in range(i+2, 2*N/4):
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
           print"count"
           print count
           if count < 1:
               break
       while True:
           count = 0
           for i in range(2*N/4,3*N/4-2):
               for j in range(i+2, 3*N/4):
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
           print"count"
           print count
           if count < 1:
               break
       while True:
           count = 0
           for i in range(3*N/4,N-2):
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
           print"count"
           print count
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
           for i in range(0,N/2-2):
               for j in range(i+2, N/2):
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
           print"count"
           print count
           if count < 1:
               break

       while True:
           count = 0
           for i in range(N/2,N-2):
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
           print"count"
           print count
           if count < 1:
               break
       return cities


   def three_opt(cities):
       total = 0
       while True:
           count = 0
           for i in range(N-4):
               for j in range(i+2, N-2):
                   for k in range(j+2, N):
                       if k == N-1:
                           post_citiy3 = 0
                       else:
                           post_citiy3 = k+1
                       if i != 0 or j != 0 or k != 0:
                           if dist[cities[i]][cities[k]] + dist[cities[j+1]][cities[i+1]] + dist[cities[post_citiy3]][cities[j]] < dist[cities[i]][cities[i+1]] + dist[cities[j]][cities[j+1]] + dist[cities[k]][cities[post_citiy3]]:
                               cities[i+1], cities[k] = cities[k], cities[i+1]
                               cities[j], cities[i+1] = cities[i+1], cities[j]
                               count += 1
                           elif dist[cities[j+1]][cities[i]] + dist[cities[k]][cities[j]] + dist[cities[post_citiy3]][cities[i+1]] < dist[cities[i]][cities[i+1]] + dist[cities[j]][cities[j+1]] + dist[cities[k]][cities[post_citiy3]]:
                               cities[i+1], cities[j+1] = cities[j+1], cities[i+1]
                               cities[k], cities[i+1] = cities[i+1], cities[k]
                               count += 1
                           elif dist[cities[j]][cities[post_citiy3]] + dist[cities[i]][cities[j+1]] + dist[cities[k]][cities[i+1]] < dist[cities[i]][cities[i+1]] + dist[cities[j]][cities[j+1]] + dist[cities[k]][cities[post_citiy3]]:
                               cities[i], cities[j] = cities[j], cities[i]
                               cities[post_citiy3], cities[i+1] = cities[i+1], cities[post_citiy3]
                               count += 1
                           elif dist[cities[i]][cities[j]] + dist[cities[j+1]][cities[post_citiy3]] + dist[cities[k]][cities[i+1]] < dist[cities[i]][cities[i+1]] + dist[cities[j]][cities[j+1]] + dist[cities[k]][cities[post_citiy3]]:
                               cities[i+1], cities[j] = cities[j], cities[i+1]
                               cities[i+1], cities[post_citiy3] = cities[post_citiy3], cities[i+1]
                               count += 1

           total += count
           print cities
           print"count"
           print count
           if count < 10000000000:
               break

       return cities

   def or_opt(cities, divnumber):
       total = 0
       for i in xrange(1, divnumber+1):
           for j in xrange(0+(i-1)*N/divnumber, i*N/divnumber):
               while True:
                   count = 0
                   #print j
                   length = i*N/divnumber
                   #print length
                   pre_city1 = j-1
                   post_city1 = j+1
                   if pre_city1 < 0: pre_city1 = divnumber-1
                   if post_city1 == length: post_city1 = 0
                   for k in xrange(length):
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
                               print solution
                               if j < k:
                                   solution[k:k] = [p]
                               else:
                                   solution[post_city2:post_city2] = [p]
                               count += 1
                               print solution

                   total += count
                   print count
                   if count < 1:
                       break
       return cities


   solution = two_opt_div(solution)
   solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)
   solution = two_opt_div(solution)
   solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)

   solution = two_opt_div(solution)
   solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)

   solution = two_opt_div(solution)
   solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)
   solution = two_opt_div(solution)
   solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)

   solution = two_opt_div(solution)
   solution = two_opt_div_half(solution)

   solution = or_opt(solution, 1)
   #solution = three_opt(solution)

   solution = two_opt_div_half(solution)
   return solution


if __name__ == '__main__':
   assert len(sys.argv) > 1
   solution = solve(read_input(sys.argv[1]))
   print_solution(solution)
