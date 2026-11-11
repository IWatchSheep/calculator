# Algebra word problem index

One folder per problem, holding `<id>.py` (the problem, its steps, its answer and `compute(...)`) and `<id>.jpg` (a diagram of the problem).
**Ready** = a solver answers it today (`compute(...)` works); **Reference** = the problem and its steps are stored, no solver answers it yet.
Written by `operator_keys/make_algebra_word_problem_files.py`; the solver column comes from `algebra_word_problems/algebra_matcher/word_solver.py`.
One wording is stored once. Further numbers for that wording are a slider on the unknown, not another stored problem.

479 problems: 235 ready (220 word_solver, 15 number_puzzle), 244 reference.

## Age

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0001 | Wren is 4 times as old as Jamal. In 5 years, the sum of their ages will be 105. How old is each now? | Jamal is 19, Wren is 76 | Reference |  | `age/0001/` |
| 0002 | Wes is 13 years older than Theo. The sum of their ages is 85. How old is each? | Theo is 36, Wes is 49 | Ready | sum_difference | `age/0002/` |
| 0003 | Ben is 8 years older than Sam. 32 years ago, Ben was twice as old as Sam. How old is each now? | Sam is 40, Ben is 48 | Reference |  | `age/0003/` |
| 0004 | Dana is 2 times as old as Aiden. In 6 years, the sum of their ages will be 33. How old is each now? | Aiden is 7, Dana is 14 | Reference |  | `age/0004/` |
| 0005 | Uma is 3 times as old as Yusuf. In 10 years, the sum of their ages will be 68. How old is each now? | Yusuf is 12, Uma is 36 | Reference |  | `age/0005/` |
| 0006 | Hiro is 2 years older than Maya. The sum of their ages is 24. How old is each? | Maya is 11, Hiro is 13 | Ready | sum_difference | `age/0006/` |
| 0007 | Noah is 3 times as old as Ava. In 3 years, the sum of their ages will be 82. How old is each now? | Ava is 19, Noah is 57 | Reference |  | `age/0007/` |
| 0008 | Emeka is 5 years older than Yara. The sum of their ages is 67. How old is each? | Yara is 31, Emeka is 36 | Ready | sum_difference | `age/0008/` |
| 0009 | Maya is 30 years older than Yara. The sum of their ages is 40. How old is each? | Yara is 5, Maya is 35 | Ready | sum_difference | `age/0009/` |

## Average

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0010 | The mean of 4 numbers is 41. 3 of them are 56, 32, 17. What is the missing number? | 59 | Reference |  | `average/0010/` |
| 0011 | Ava scored 87, 71, 73, 89, 97 on 5 tests. What score is needed on the next test to average 86? | 99 | Ready | average_needed | `average/0011/` |
| 0013 | Oscar scored 93, 81, 67, 64 on 4 tests. What score is needed on the next test to average 79? | 90 | Ready | average_needed | `average/0013/` |
| 0014 | Tara scored 94, 77, 83, 85, 92, 73 on 6 tests. What score is needed on the next test to average 86? | 98 | Ready | average_needed | `average/0014/` |
| 0015 | The mean of 5 numbers is 36. 4 of them are 18, 50, 34, 36. What is the missing number? | 42 | Reference |  | `average/0015/` |
| 0016 | Mateo scored 60, 94, 80, 60, 98, 62 on 6 tests. What score is needed on the next test to average 76? | 78 | Ready | average_needed | `average/0016/` |
| 0018 | Maya scored 62, 75, 94 on 3 tests. What score is needed on the next test to average 79? | 85 | Ready | average_needed | `average/0018/` |

## Average (weighted)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0019 | Class A has 13 students averaging 75. Class B averages 93. Together the classes average 84. How many students are in class B? | 13 students | Ready | archive_average_weighted_1 | `average_weighted/0019/` |
| 0020 | A course grade is 75% coursework and 25% final exam. Elena has a coursework average of 96. What final exam score gives an overall grade of 86? | 56 | Reference |  | `average_weighted/0020/` |
| 0021 | A course grade is 60% coursework and 40% final exam. Gus has a coursework average of 79. What final exam score gives an overall grade of 85? | 94 | Reference |  | `average_weighted/0021/` |
| 0024 | A course grade is 60% coursework and 40% final exam. Rhea has a coursework average of 80. What final exam score gives an overall grade of 88? | 100 | Reference |  | `average_weighted/0024/` |
| 0025 | A course grade is 60% coursework and 40% final exam. Ivan has a coursework average of 97. What final exam score gives an overall grade of 85? | 67 | Reference |  | `average_weighted/0025/` |
| 0028 | A course grade is 70% coursework and 30% final exam. Lena has a coursework average of 87. What final exam score gives an overall grade of 81? | 67 | Reference |  | `average_weighted/0028/` |

## Break-even

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0029 | Electric utility plan A costs $38.00 plus $0.15 per kWh. Plan B costs $26.50 plus $0.20 per kWh. For how many kWhs do they cost the same? | 230 kWhs | Reference |  | `break_even/0029/` |
| 0030 | Service A has a $160 sign-up fee and costs $5/month. Service B has no fee and costs $15/month. After how many months is the total cost the same? | 16 months | Ready | archive_break_even_1 | `break_even/0030/` |
| 0031 | Job A pays $1000 a month plus 2% commission. Job B pays $490 a month plus 5% commission. At what monthly sales total do both pay the same? | $17,000.00 | Reference |  | `break_even/0031/` |
| 0032 | A food truck pays $350 in daily costs, and each meal costs $1 in ingredients. Meals sell for $8. How many meals a day cover the costs? | 50 meals | Reference |  | `break_even/0032/` |
| 0033 | Buying a pressure washer costs $500. Renting one costs $50 once plus $50 per use. After how many uses does renting cost the same as buying? | 9 uses | Reference |  | `break_even/0033/` |
| 0035 | Car rental A costs $15.00 plus $0.25 per mile. Plan B costs $4.50 plus $0.40 per mile. For how many miles do they cost the same? | 70 miles | Ready | archive_break_even_2 | `break_even/0035/` |
| 0036 | It costs $250 to set up a print run plus $15 per poster. Posters sell for $17 each. How many must be sold to break even? | 125 posters | Reference |  | `break_even/0036/` |
| 0037 | Buying a carpet cleaner costs $550. Renting one costs $25 once plus $15 per use. After how many uses does renting cost the same as buying? | 35 uses | Reference |  | `break_even/0037/` |
| 0040 | Buying a kayak costs $475. Renting costs $25 per use. After how many uses would renting cost the same as buying? | 19 uses | Reference |  | `break_even/0040/` |
| 0042 | Phone plan A costs $20.00 plus $0.10 per minute. Plan B costs $3.00 plus $0.15 per minute. For how many minutes do they cost the same? | 340 minutes | Reference |  | `break_even/0042/` |
| 0047 | Buying a pressure washer costs $1275. Renting costs $25 per use. After how many uses would renting cost the same as buying? | 51 uses | Reference |  | `break_even/0047/` |

## Clock

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0053 | At what time between 1:00 and 2:00 are the hour and minute hands of a clock exactly together? | 60/11 ≈ 5.45 minutes after 1:00 | Reference |  | `clock/0053/` |

## Coins

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0057 | Pablo has 45 coins, all nickels and quarters, worth $7.45 in total. How many of each coin are there? | 19 nickels and 26 quarters | Reference |  | `coins/0057/` |
| 0058 | A jar has quarters, dimes, and nickels worth $2.65. There are 4 more dimes than quarters and twice as many nickels as quarters. How many of each coin? | 5 quarters, 9 dimes, 10 nickels | Reference |  | `coins/0058/` |
| 0059 | Theo has 37 coins, all nickels and quarters, worth $2.85 in total. How many of each coin are there? | 32 nickels and 5 quarters | Reference |  | `coins/0059/` |
| 0062 | Xena has 42 coins, all dimes and quarters, worth $6.15 in total. How many of each coin are there? | 29 dimes and 13 quarters | Reference |  | `coins/0062/` |
| 0064 | Yusuf has 79 coins, all nickels and quarters, worth $11.95 in total. How many of each coin are there? | 39 nickels and 40 quarters | Reference |  | `coins/0064/` |
| 0065 | Oscar has 30 coins, all dimes and quarters, worth $3.45 in total. How many of each coin are there? | 27 dimes and 3 quarters | Reference |  | `coins/0065/` |

## Consecutive integers

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0067 | Of three consecutive even integers, the sum of the smallest and largest is 8. Find all three. | 2, 4, 6 | Ready | archive_consecutive_integers_1 | `consecutive_integers/0067/` |
| 0068 | The average of 5 consecutive integers is 50. What is the smallest? | 48 (the integers are 48 to 52) | Reference |  | `consecutive_integers/0068/` |
| 0069 | Three consecutive integers are such that 3 times the smallest is 4 more than the largest. Find the integers. | 3, 4, 5 | Ready | archive_consecutive_integers_2 | `consecutive_integers/0069/` |
| 0070 | The sum of 3 consecutive integers is 120. What are the integers? | 39, 40, 41 | Ready | consecutive | `consecutive_integers/0070/` |
| 0074 | The sum of 4 consecutive odd integers is 160. What are the integers? | 37, 39, 41, 43 | Ready | consecutive | `consecutive_integers/0074/` |
| 0078 | Three consecutive integers are such that 3 times the smallest is 8 less than the largest. Find the integers. | -3, -2, -1 | Reference |  | `consecutive_integers/0078/` |
| 0084 | The sum of 4 consecutive even integers is 244. What are the integers? | 58, 60, 62, 64 | Ready | consecutive | `consecutive_integers/0084/` |

## Current / wind

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0086 | A boat travels 34 km downstream in 2 hours and 35 km upstream in 5 hours. Find the speed of the boat in still water and the speed of the current. | Boat 12 km/h, current 5 km/h | Ready | still_water_current | `current_wind/0086/` |
| 0087 | A plane flies 540 miles with the wind in 3 hours. Flying back against the same wind takes 4.5 hours. Find the plane's speed in still air and the wind speed. | Plane 150 mph, wind 30 mph | Reference |  | `current_wind/0087/` |
| 0088 | A boat travels 38 km downstream in 2 hours and 3 km upstream in 1 hour. Find the speed of the boat in still water and the speed of the current. | Boat 11 km/h, current 8 km/h | Ready | still_water_current | `current_wind/0088/` |

## Digits

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0095 | In a two-digit number, the units digit is 3 times the tens digit. The number is 27 more than the sum of its digits. Find the number. | 39 | Reference |  | `digits/0095/` |
| 0096 | The digits of a two-digit number add up to 11. When the digits are reversed, the new number is 63 less than the original. Find the original number. | 92 | Reference |  | `digits/0096/` |
| 0098 | The digits of a two-digit number add up to 12. When the digits are reversed, the new number is 18 more than the original. Find the original number. | 57 | Reference |  | `digits/0098/` |

## Direct variation

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0105 | A spring stretches 2.5 cm under a 20 N force. Stretch varies directly with force. How far will it stretch under 40 N? | 5 cm | Ready | proportion | `direct_variation/0105/` |
| 0106 | Pay varies directly with hours worked. Kira earns $900.00 for 40 hours. How much for 42 hours? | $945.00 | Ready | proportion | `direct_variation/0106/` |
| 0108 | Pay varies directly with hours worked. Priya earns $450.00 for 30 hours. How much for 6 hours? | $90.00 | Ready | proportion | `direct_variation/0108/` |
| 0109 | Pay varies directly with hours worked. Xena earns $536.25 for 33 hours. How much for 11 hours? | $178.75 | Ready | proportion | `direct_variation/0109/` |
| 0112 | Pay varies directly with hours worked. Dev earns $229.50 for 17 hours. How much for 17 hours? | $229.50 | Ready | proportion | `direct_variation/0112/` |

## Distance (average speed)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0115 | Kofi drove 1 hour at 30 mph and then some hours at 55 mph. The average speed for the whole trip was 50 mph. How long was the second part? | 4 hours | Reference |  | `distance_average_speed/0115/` |
| 0116 | A car goes from A to B at 60 km/h. How fast must it return so that the average speed for the round trip is 30 km/h? | 20 km/h | Ready | archive_distance_average_speed_1 | `distance_average_speed/0116/` |
| 0117 | Aiden drove 2 hours at 60 mph and then some hours at 45 mph. The average speed for the whole trip was 55 mph. How long was the second part? | 1 hour | Reference |  | `distance_average_speed/0117/` |
| 0120 | Lena drove 2 hours at 30 mph and then some hours at 75 mph. The average speed for the whole trip was 45 mph. How long was the second part? | 1 hour | Reference |  | `distance_average_speed/0120/` |
| 0121 | Emeka drove 1 hour at 50 mph and then some hours at 45 mph. The average speed for the whole trip was 46 mph. How long was the second part? | 4 hours | Reference |  | `distance_average_speed/0121/` |
| 0124 | Sofia drove 3 hours at 60 mph and then some hours at 75 mph. The average speed for the whole trip was 66 mph. How long was the second part? | 2 hours | Reference |  | `distance_average_speed/0124/` |

## Distance (catch-up)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0125 | Two runners start together on a 400 m track, one at 5 m/s and the other at 7 m/s. After how many seconds does the faster one lap the slower one? | 200 seconds | Ready | archive_distance_catch_up_1 | `distance_catch_up/0125/` |
| 0126 | Caleb leaves at 39 mph. 2 hours later, Aiden follows the same route at 63 mph. How long after Aiden leaves will Aiden catch up? | 3.25 hours | Ready | catch_up | `distance_catch_up/0126/` |
| 0128 | Rosa leaves at 39 mph. 1 hour later, Dev follows the same route at 45 mph. How long after Dev leaves will Dev catch up? | 6.5 hours | Ready | catch_up | `distance_catch_up/0128/` |
| 0130 | Jamal leaves at 38 mph. 1 hour later, Nia follows the same route at 57 mph. How long after Nia leaves will Nia catch up? | 2 hours | Ready | catch_up | `distance_catch_up/0130/` |
| 0132 | Maya leaves at 38 mph. 3 hours later, Omar follows the same route at 50 mph. How long after Omar leaves will Omar catch up? | 9.5 hours | Ready | catch_up | `distance_catch_up/0132/` |
| 0134 | Sofia leaves at 47 mph. 3 hours later, Mateo follows the same route at 59 mph. How long after Mateo leaves will Mateo catch up? | 11.75 hours | Ready | catch_up | `distance_catch_up/0134/` |

## Distance (opposite directions)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0135 | Omar and Lena leave the same town at the same time, driving in opposite directions at 30 mph and 36 mph. After how many hours will they be 165 miles apart? | 2.5 hours | Ready | opposite_directions | `distance_opposite_directions/0135/` |
| 0136 | Zoe and Sam leave the same town at the same time, driving in opposite directions at 31 mph and 34 mph. After how many hours will they be 260 miles apart? | 4 hours | Ready | opposite_directions | `distance_opposite_directions/0136/` |
| 0137 | Kira and Wes leave the same town at the same time, driving in opposite directions at 55 mph and 57 mph. After how many hours will they be 112 miles apart? | 1 hour | Ready | opposite_directions | `distance_opposite_directions/0137/` |
| 0138 | Umar and Tara leave the same town at the same time, driving in opposite directions at 43 mph and 55 mph. After how many hours will they be 98 miles apart? | 1 hour | Ready | opposite_directions | `distance_opposite_directions/0138/` |
| 0139 | Kofi and Emeka leave the same town at the same time, driving in opposite directions at 49 mph and 51 mph. After how many hours will they be 300 miles apart? | 3 hours | Ready | opposite_directions | `distance_opposite_directions/0139/` |

## Distance (round trip)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0140 | Tara drove to a lake at 45 mph and returned on the same road at 36 mph. The round trip took 8 hours. How far is the lake? | 160 miles | Reference |  | `distance_round_trip/0140/` |
| 0141 | A cyclist rides 225 km to a town and returns 5 km/h faster. The whole trip takes 9.5 hours. How fast was the outbound ride? | 45 km/h | Ready | archive_distance_round_trip_1 | `distance_round_trip/0141/` |
| 0142 | Bea drove to a lake at 60 mph and returned on the same road at 30 mph. The round trip took 10 hours. How far is the lake? | 200 miles | Reference |  | `distance_round_trip/0142/` |
| 0143 | A cyclist rides 60 km to a town and returns 15 km/h faster. The whole trip takes 10/3 hours. How fast was the outbound ride? | 30 km/h | Reference |  | `distance_round_trip/0143/` |
| 0144 | Kofi drove to a lake at 40 mph and returned on the same road at 20 mph. The round trip took 6 hours. How far is the lake? | 80 miles | Reference |  | `distance_round_trip/0144/` |
| 0146 | Isla drove to a lake at 45 mph and returned on the same road at 30 mph. The round trip took 2 hours. How far is the lake? | 36 miles | Reference |  | `distance_round_trip/0146/` |
| 0148 | Aiden drove to a lake at 30 mph and returned on the same road at 20 mph. The round trip took 5 hours. How far is the lake? | 60 miles | Reference |  | `distance_round_trip/0148/` |

## Distance (toward each other)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0149 | Carla and Jamal live 391 miles apart. Carla drives toward Jamal at 67 mph. 1 hour later, Jamal starts driving toward Carla at 41 mph. How long after Jamal leaves do they meet? | 3 hours | Reference |  | `distance_toward_each_other/0149/` |
| 0150 | Two trains start 142 miles apart and travel toward each other at 38 mph and 33 mph. When will they meet? | 2 hours | Ready | toward_each_other | `distance_toward_each_other/0150/` |
| 0151 | Two cyclists are 198 km apart and ride toward each other at 64 km/h and 35 km/h. How long until they meet? | 2 hours | Ready | toward_each_other | `distance_toward_each_other/0151/` |
| 0152 | Emeka and Quinn live 362 miles apart. Emeka drives toward Quinn at 58 mph. 2 hours later, Quinn starts driving toward Emeka at 65 mph. How long after Quinn leaves do they meet? | 2 hours | Reference |  | `distance_toward_each_other/0152/` |
| 0154 | Yusuf and Theo live 618 miles apart. Yusuf drives toward Theo at 59 mph. 2 hours later, Theo starts driving toward Yusuf at 66 mph. How long after Theo leaves do they meet? | 4 hours | Reference |  | `distance_toward_each_other/0154/` |
| 0156 | Carla and Zane live 370 miles apart. Carla drives toward Zane at 58 mph. 1 hour later, Zane starts driving toward Carla at 46 mph. How long after Zane leaves do they meet? | 3 hours | Reference |  | `distance_toward_each_other/0156/` |
| 0157 | Victor and Aiden live 327 miles apart. Victor drives toward Aiden at 63 mph. 1 hour later, Aiden starts driving toward Victor at 69 mph. How long after Aiden leaves do they meet? | 2 hours | Reference |  | `distance_toward_each_other/0157/` |

## Distance (two legs)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0159 | Pablo walked at 4 km/h and then rode a bus at 40 km/h. The whole trip was 13 km and took 1 hours. How long was the walk? | 0.75 h walking, 0.25 h on the bus | Reference |  | `distance_two_legs/0159/` |
| 0160 | Lena walked at 5 km/h and then rode a bus at 36 km/h. The whole trip was 38.5 km and took 1.5 hours. How long was the walk? | 0.5 h walking, 1 h on the bus | Reference |  | `distance_two_legs/0160/` |
| 0161 | Quinn walked at 3 km/h and then rode a bus at 30 km/h. The whole trip was 10.5 km and took 1.25 hours. How long was the walk? | 1 h walking, 0.25 h on the bus | Reference |  | `distance_two_legs/0161/` |
| 0162 | Hana walked at 5 km/h and then rode a bus at 24 km/h. The whole trip was 39.75 km and took 2.25 hours. How long was the walk? | 0.75 h walking, 1.5 h on the bus | Reference |  | `distance_two_legs/0162/` |
| 0163 | Kira walked at 5 km/h and then rode a bus at 24 km/h. The whole trip was 38.5 km and took 2 hours. How long was the walk? | 0.5 h walking, 1.5 h on the bus | Reference |  | `distance_two_legs/0163/` |

## Exponential

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0164 | A substance has a half-life of 2 years. How long until 200 g decays to 25 g? | 6 years | Ready | periodic_growth | `exponential/0164/` |
| 0165 | A bacteria culture starts with 1000 cells and doubles every 20 minutes. When will it reach 4,000 cells? | 40 minutes | Ready | periodic_growth | `exponential/0165/` |
| 0166 | A rumor spreads so that the number of people who have heard it triples every 5 days. It starts with 50 people. When will 450 people have heard it? | 10 days | Ready | periodic_growth | `exponential/0166/` |
| 0169 | A bacteria culture starts with 300 cells and doubles every 4 hours. When will it reach 4,800 cells? | 16 hours | Ready | periodic_growth | `exponential/0169/` |

## Formula

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0178 | Using distance = speed × time, how long does it take to travel 160 km at 40 km/h? | 4 hours | Ready | distance_speed_time | `formula/0178/` |
| 0179 | Using v = u + at, how long does it take an object to go from 0 m/s to 30 m/s with acceleration 5 m/s²? | 6 seconds | Ready | kinematics_time | `formula/0179/` |
| 0180 | Solve P = 2l + 2w for w when P = 70 and l = 27. | 8 | Reference |  | `formula/0180/` |
| 0181 | Using V = IR, find the current when the voltage is 12 V and the resistance is 4 Ω. | 3 A | Ready | archive_formula_1 | `formula/0181/` |
| 0182 | At what Celsius temperature is the Fahrenheit reading exactly 2 times the Celsius reading? (F = (9/5)C + 32) | 160°C (320°F) | Reference |  | `formula/0182/` |
| 0183 | An object has a mass of 16.2 g and a density of 2.7 g/cm³. Using density = mass/volume, find its volume. | 6 cm³ | Ready | archive_formula_2 | `formula/0183/` |
| 0184 | On a seesaw, weight × distance from the pivot must be equal on both sides. Jade (69 kg) sits 3 m from the pivot. How far from the pivot must Theo (36 kg) sit to balance? | 5.75 m | Reference |  | `formula/0184/` |
| 0188 | Using F = (9/5)C + 32, what Celsius temperature equals 113°F? | 45°C | Reference |  | `formula/0188/` |
| 0189 | On a seesaw, weight × distance from the pivot must be equal on both sides. Yara (36 kg) sits 6 m from the pivot. How far from the pivot must Priya (54 kg) sit to balance? | 4 m | Reference |  | `formula/0189/` |
| 0195 | On a seesaw, weight × distance from the pivot must be equal on both sides. Sofia (66 kg) sits 6 m from the pivot. How far from the pivot must Mateo (22 kg) sit to balance? | 18 m | Reference |  | `formula/0195/` |
| 0203 | On a seesaw, weight × distance from the pivot must be equal on both sides. Ivan (35 kg) sits 1 m from the pivot. How far from the pivot must Pablo (70 kg) sit to balance? | 0.5 m | Reference |  | `formula/0203/` |
| 0204 | Using V = IR, find the resistance (in ohms) when the voltage is 50 V and the current is 5 A. | 10 Ω | Ready | archive_formula_3 | `formula/0204/` |
| 0206 | On a seesaw, weight × distance from the pivot must be equal on both sides. Sam (30 kg) sits 3 m from the pivot. How far from the pivot must Sofia (72 kg) sit to balance? | 1.25 m | Reference |  | `formula/0206/` |

## Fractions

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0210 | Maya spent 1/6 of their money on a game and then 1/5 of what was left on lunch, leaving $360. How much did they start with? | $540 | Reference |  | `fractions/0210/` |
| 0211 | A puzzle: a man spent 1/6 of his life as a boy, 1/12 more as a youth, and 1/7 more before marrying. 5 years later a son was born, who lived 1/2 as long as his father. The father died 4 years after the son. How long did the father live? | 84 years | Reference |  | `fractions/0211/` |
| 0212 | A gas tank is 1/2 full. Adding 1 gallons fills it to 2/3. How much does the tank hold? | 6 | Reference |  | `fractions/0212/` |
| 0213 | Sofia read 1/5 of a book on Monday and 1/4 of the remaining pages on Tuesday. 108 pages are left. How many pages does the book have? | 180 pages | Reference |  | `fractions/0213/` |
| 0214 | A tank is 2/5 full. After 200 liters are added, it is 9/10 full. What is the tank's capacity? | 400 | Reference |  | `fractions/0214/` |
| 0215 | Gus spent 1/4 of their money on a game and then 1/3 of what was left on lunch, leaving $60. How much did they start with? | $120 | Reference |  | `fractions/0215/` |
| 0216 | Omar read 1/5 of a book on Monday and 1/4 of the remaining pages on Tuesday. 252 pages are left. How many pages does the book have? | 420 pages | Reference |  | `fractions/0216/` |
| 0217 | Sam read 1/5 of a book on Monday and 1/2 of the remaining pages on Tuesday. 52 pages are left. How many pages does the book have? | 130 pages | Reference |  | `fractions/0217/` |
| 0218 | Yara spent 1/2 of their money on a game and then 1/3 of what was left on lunch, leaving $20. How much did they start with? | $60 | Reference |  | `fractions/0218/` |
| 0220 | Uma spent 1/4 of their money on a game and then 1/5 of what was left on lunch, leaving $60. How much did they start with? | $100 | Reference |  | `fractions/0220/` |
| 0221 | Isla read 1/3 of a book on Monday and 1/2 of the remaining pages on Tuesday. 12 pages are left. How many pages does the book have? | 36 pages | Reference |  | `fractions/0221/` |
| 0223 | Aiden spent 1/3 of their money on a game and then 1/2 of what was left on lunch, leaving $34. How much did they start with? | $102 | Reference |  | `fractions/0223/` |

## Geometry (Pythagorean)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0224 | A rectangular field is 4 m long. A diagonal path across it is 5 m long. How wide is the field? | 3 m | Reference |  | `geometry_pythagorean/0224/` |
| 0225 | A 10 ft ladder leans against a wall with its foot 6 ft from the wall. How high up the wall does it reach? | 8 ft | Reference |  | `geometry_pythagorean/0225/` |
| 0226 | One leg of a right triangle is 23 cm longer than the other. The hypotenuse is 37 cm. Find the legs. | 12 and 35 | Reference |  | `geometry_pythagorean/0226/` |
| 0228 | A rectangular TV screen is 12 in tall with a diagonal of 20 in. How wide is it? | 16 in | Reference |  | `geometry_pythagorean/0228/` |
| 0229 | The hypotenuse of a right triangle is 29 in, and one leg is 1 in longer than the other leg. How long are the legs? | 20 and 21 | Reference |  | `geometry_pythagorean/0229/` |
| 0231 | A 29 m support wire runs from the top of a pole to a stake 20 m from the pole's base. How tall is the pole? | 21 m | Reference |  | `geometry_pythagorean/0231/` |
| 0234 | A ramp is 41 ft long and covers a horizontal distance of 9 ft; how high does it rise? | 40 ft | Reference |  | `geometry_pythagorean/0234/` |

## Geometry (angles)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0237 | The angles of a triangle are in the ratio 3:5:7. Find each angle. | 36°, 60°, 84° | Ready | triangle_ratio | `geometry_angles/0237/` |
| 0238 | Where two lines cross, opposite angles are (2x + 4)° and (5x − 110)°. Find the angle. | x = 38; each angle is 80° | Ready | opposite_angles_equal | `geometry_angles/0238/` |
| 0239 | Two parallel lines are cut by a transversal. A pair of alternate exterior angles measure (2x + 24)° and (1x + 49)°. Find x and the angle. | x = 25; each angle is 74° | Ready | transversal_equal_angles | `geometry_angles/0239/` |
| 0240 | Two angles are complementary. One angle is 12 less than 5 times the other. Find both angles. | 17° and 73° | Ready | complementary_supplementary | `geometry_angles/0240/` |
| 0241 | Two angles form a linear pair. One measures (4x + 29)° and the other (1x + 41)°. Find both angles. | x = 22; the angles are 117° and 63° | Reference |  | `geometry_angles/0241/` |
| 0242 | In an isosceles triangle, the vertex angle is 18° more than each base angle. Find all three angles. | 54°, 54°, 72° | Ready | archive_geometry_angles_1 | `geometry_angles/0242/` |
| 0243 | In a triangle, the second angle is 3 times the first, and the third angle is 75 more than the first. Find all three angles. | 21°, 63°, 96° | Ready | archive_geometry_angles_2 | `geometry_angles/0243/` |
| 0244 | An exterior angle of a triangle measures (3x + 22)°. The two remote interior angles measure (2x + 21)° and (3x − 33)°. Find x and the exterior angle. | x = 17; exterior angle = 73° | Reference |  | `geometry_angles/0244/` |
| 0249 | Two angles are complementary. One angle is 20 more than 4 times the other. Find both angles. | 14° and 76° | Ready | complementary_supplementary | `geometry_angles/0249/` |
| 0251 | Angles A and B lie on a straight line. A = (1x − 2)° and B = (2x + 104)°. What are A and B? | x = 26; the angles are 24° and 156° | Reference |  | `geometry_angles/0251/` |
| 0252 | Where two lines cross, opposite angles are (3x − 10)° and (6x − 118)°. Find the angle. | x = 36; each angle is 98° | Ready | opposite_angles_equal | `geometry_angles/0252/` |
| 0253 | Two vertical angles measure (6x − 13)° and (4x + 17)°. Find x and the angle measure. | x = 15; each angle is 77° | Reference |  | `geometry_angles/0253/` |
| 0254 | Angles A and B lie on a straight line. A = (1x + 2)° and B = (3x + 138)°. What are A and B? | x = 10; the angles are 12° and 168° | Reference |  | `geometry_angles/0254/` |
| 0256 | In an isosceles triangle, the vertex angle is 12° less than each base angle. Find all three angles. | 64°, 64°, 52° | Reference |  | `geometry_angles/0256/` |
| 0257 | Two parallel lines are cut by a transversal. A pair of corresponding angles measure (4x + 4)° and (6x − 54)°. Find x and the angle. | x = 29; each angle is 120° | Ready | transversal_equal_angles | `geometry_angles/0257/` |
| 0262 | Two angles form a linear pair. One measures (3x + 18)° and the other (4x − 69)°. Find both angles. | x = 33; the angles are 117° and 63° | Reference |  | `geometry_angles/0262/` |
| 0263 | Two angles are supplementary. One angle is 6 less than 5 times the other. Find both angles. | 31° and 149° | Ready | complementary_supplementary | `geometry_angles/0263/` |
| 0265 | Where two lines cross, opposite angles are (6x + 7)° and (3x + 31)°. Find the angle. | x = 8; each angle is 55° | Ready | opposite_angles_equal | `geometry_angles/0265/` |
| 0270 | Angles A and B lie on a straight line. A = (4x − 2)° and B = (1x − 18)°. What are A and B? | x = 40; the angles are 158° and 22° | Reference |  | `geometry_angles/0270/` |
| 0273 | Two parallel lines are cut by a transversal. A pair of alternate interior angles measure (2x + 1)° and (1x + 33)°. Find x and the angle. | x = 32; each angle is 65° | Ready | transversal_equal_angles | `geometry_angles/0273/` |

## Geometry (area)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0274 | If each side of a square is increased by 2 cm, its area increases by 92 cm². Find the original side length. | 22 cm | Reference |  | `geometry_area/0274/` |
| 0275 | A rectangle's length is twice its width. If the length is decreased by 6 m and the width increased by 4 m, the area stays the same. Find the original dimensions. | Width 12 m, length 24 m | Reference |  | `geometry_area/0275/` |
| 0276 | A trapezoid has parallel sides of 7 cm and 29 cm and an area of 270 cm². Find its height. | 15 cm | Ready | archive_geometry_area_1 | `geometry_area/0276/` |
| 0277 | A triangle has an area of 60 m² and a height of 3 m. How long is its base? | 40 m | Ready | archive_geometry_area_2 | `geometry_area/0277/` |

## Geometry (perimeter)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0292 | Each side of a square is (1x + 1) cm. The perimeter is 116 cm. Find x and the side length. | x = 28; side = 29 cm | Reference |  | `geometry_perimeter/0292/` |
| 0293 | A window is a rectangle 17 ft tall topped by an equilateral triangle. The triangle's sides equal the rectangle's width. The outside perimeter is 91 ft. How wide is the window? | 19 ft | Ready | archive_geometry_perimeter_1 | `geometry_perimeter/0293/` |
| 0298 | Each side of a square is (4x − 6) cm. The perimeter is 88 cm. Find x and the side length. | x = 7; side = 22 cm | Reference |  | `geometry_perimeter/0298/` |

## Geometry (polygons)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0300 | Each interior angle of a regular polygon measures 150°. How many sides does the polygon have? | 12 sides | Ready | archive_geometry_polygons_1 | `geometry_polygons/0300/` |
| 0301 | The interior angles of a polygon add up to 720°. How many sides does it have? | 6 sides | Ready | polygon_angle_sum | `geometry_polygons/0301/` |
| 0302 | Each exterior angle of a regular polygon is 120°. How many sides does it have? | 3 sides | Ready | archive_geometry_polygons_2 | `geometry_polygons/0302/` |

## Geometry (quadratic)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0309 | A rectangle has a perimeter of 40 ft and an area of 36 ft². Find its length and width. | 18 ft by 2 ft | Ready | rectangle_from_perimeter_area | `geometry_quadratic/0309/` |
| 0310 | A farmer has 48 m of fencing to build a rectangular pen against a barn wall (no fence on the wall side). The pen must have an area of 216 m². What dimensions work? | Two answers: 18 m × 12 m, or 6 m × 36 m | Reference |  | `geometry_quadratic/0310/` |
| 0311 | Squares of side x are cut from each corner of a 29 cm by 21 cm sheet, and the sides are folded up to make an open box. The base of the box has area 209 cm². Find x. | 5 cm | Reference |  | `geometry_quadratic/0311/` |
| 0312 | A rectangle's length is 12 m more than its width, and its area is 640 m². Find the dimensions. | Width 20 m, length 32 m | Ready | archive_geometry_quadratic_1 | `geometry_quadratic/0312/` |
| 0313 | A 19 ft by 19 ft garden has a path of uniform width around it. The path's area is 168 ft². How wide is the path? | 2 ft | Reference |  | `geometry_quadratic/0313/` |
| 0314 | The height of a triangle is 9 cm more than its base. The area is 243 cm². Find the base and height. | Base 18 cm, height 27 cm | Ready | archive_geometry_quadratic_2 | `geometry_quadratic/0314/` |
| 0315 | A 18 in × 15 in photo is surrounded by a frame of uniform width. The framed picture covers 418 in². How wide is the frame? | 2 in | Ready | archive_geometry_quadratic_3 | `geometry_quadratic/0315/` |

## Geometry (rectangle)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0341 | The length of a rectangle is 3 less than 3 times its width. The perimeter is 178 cm. Find the dimensions. | Width 23 cm, length 66 cm | Reference |  | `geometry_rectangle/0341/` |
| 0342 | The length of a rectangle is 2 more than its width. The perimeter is 132 cm. Find the dimensions. | Width 32 cm, length 34 cm | Reference |  | `geometry_rectangle/0342/` |
| 0344 | The length of a rectangle is 5 more than 3 times its width. The perimeter is 170 cm. Find the dimensions. | Width 20 cm, length 65 cm | Reference |  | `geometry_rectangle/0344/` |

## Geometry (triangle)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0346 | Each of the two equal sides of an isosceles triangle is 2 cm longer than the base. The perimeter is 52 cm. Find the side lengths. | Base 16 cm, equal sides 18 cm | Ready | archive_geometry_triangle_1 | `geometry_triangle/0346/` |
| 0347 | A triangle's second side is 11 in longer than the first, and its third side is 5 in less than twice the first. If the perimeter is 122 in, how long is each side? | 29 in, 40 in, 53 in | Reference |  | `geometry_triangle/0347/` |
| 0353 | The sides of a triangle are x, x + 8, and 2x − 3 inches long. The perimeter is 89 inches. Find each side. | 21 in, 29 in, 39 in | Reference |  | `geometry_triangle/0353/` |

## Geometry (volume)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0355 | A rectangular box is 16 in long and 5 in wide. Its volume is 320 in³. How tall is it? | 4 in | Ready | archive_geometry_volume_1 | `geometry_volume/0355/` |
| 0356 | An aquarium 16 dm long and 4 dm wide holds 384 dm³ of water when full. How deep is it? | 6 dm | Reference |  | `geometry_volume/0356/` |

## Inequality

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0359 | A school dance costs $303 to run. Tickets are $8. How many tickets must be sold for a profit of at least $2200? | 313 tickets | Ready | least_for_profit | `inequality/0359/` |
| 0360 | An elevator holds at most 1200 lb. A 200 lb worker is loading 60 lb boxes. How many boxes can go up with the worker in one trip? | 16 boxes | Ready | most_that_fits | `inequality/0360/` |
| 0361 | The temperature is 26°F and falling 3°F per hour. For how many whole hours will it stay at or above 1°F? | 8 hours | Ready | temperature_whole_hours | `inequality/0361/` |
| 0362 | Elena has $160 and saves $40 a week. What is the fewest weeks needed to have at least $670? | 13 weeks | Reference |  | `inequality/0362/` |
| 0363 | Hana has $157 to spend. There is a $25 entry fee, and T-shirts cost $12.00 each. What is the most T-shirts that can be bought? | 11 T-shirts | Ready | most_you_can_buy | `inequality/0363/` |
| 0364 | Plan A costs $21 plus $0.10 per minute. Plan B costs $33 plus $0.03 per minute. What is the fewest whole minutes for which Plan B is cheaper? | 172 minutes | Reference |  | `inequality/0364/` |
| 0365 | A rectangular garden is 40 ft long, and there is at most 109 ft of fencing. What is the greatest whole-number width possible? | 14 ft | Reference |  | `inequality/0365/` |
| 0366 | Isla's test scores are 94, 64. What is the lowest score on the next test that gives an average of at least 85? | 97 | Reference |  | `inequality/0366/` |
| 0367 | A salesperson earns $400 a week plus 12% of sales. What is the least (whole-dollar) amount of sales needed to earn at least $1500? | $9,167.00 | Reference |  | `inequality/0367/` |
| 0370 | Isla has $10 and saves $15 a week. What is the fewest weeks needed to have at least $920? | 61 weeks | Reference |  | `inequality/0370/` |
| 0372 | Gus has $136 to spend. There is a $8 entry fee, and bags of mulch cost $12.00 each. What is the most bags of mulch that can be bought? | 10 bags of mulch | Ready | most_you_can_buy | `inequality/0372/` |
| 0373 | Lena's test scores are 81, 88, 63, 78, 85. What is the lowest score on the next test that gives an average of at least 80? | 85 | Reference |  | `inequality/0373/` |
| 0378 | Jade has $110 and saves $40 a week. What is the fewest weeks needed to have at least $510? | 10 weeks | Reference |  | `inequality/0378/` |
| 0379 | Emeka's test scores are 92, 93, 72, 74, 93. What is the lowest score on the next test that gives an average of at least 85? | 86 | Reference |  | `inequality/0379/` |
| 0382 | Emeka has $113 to spend. There is a $10 entry fee, and T-shirts cost $6.00 each. What is the most T-shirts that can be bought? | 17 T-shirts | Ready | most_you_can_buy | `inequality/0382/` |
| 0386 | Lena's test scores are 93, 83, 85. What is the lowest score on the next test that gives an average of at least 88? | 91 | Reference |  | `inequality/0386/` |
| 0388 | Wes has $138 to spend. There is a $8 entry fee, and bags of mulch cost $12.00 each. What is the most bags of mulch that can be bought? | 10 bags of mulch | Ready | most_you_can_buy | `inequality/0388/` |
| 0392 | The temperature is 16°F and falling 3°F per hour. For how many whole hours will it stay at or above -8°F? | 8 hours | Ready | temperature_whole_hours | `inequality/0392/` |
| 0394 | Ivan has $70 and saves $20 a week. What is the fewest weeks needed to have at least $670? | 30 weeks | Reference |  | `inequality/0394/` |
| 0397 | Gus's test scores are 61, 80, 75, 64. What is the lowest score on the next test that gives an average of at least 75? | 95 | Reference |  | `inequality/0397/` |

## Inverse variation

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0401 | 12 workers can build a wall in 10 days. At the same rate, how many days would 3 workers take? | 40 days | Ready | archive_inverse_variation_1 | `inverse_variation/0401/` |
| 0402 | A gear with 24 teeth turning at 40 rpm drives a gear with 20 teeth. Teeth × rpm is the same for both gears. How fast does the second gear turn? | 48 rpm | Ready | archive_inverse_variation_2 | `inverse_variation/0402/` |
| 0403 | At 72 km/h a trip takes 5 hours. Time varies inversely with speed. How long would it take at 90 km/h? | 4 hours | Ready | archive_inverse_variation_3 | `inverse_variation/0403/` |

## Joint variation

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0415 | 6 workers working 10 hours a day finish a job in 5 days. How many days would 4 workers working 5 hours a day take? | 15 days | Ready | archive_joint_variation_1 | `joint_variation/0415/` |

## Linear cost

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0420 | A venue charges $100 plus $15 per guest. The total was $865. How many guests came? | 51 guests | Ready | fixed_plus_rate | `linear_cost/0420/` |
| 0421 | A gym charges a $50 joining fee and $30 per month. Carla has paid $470 in total. How many months has Carla been a member? | 14 months | Ready | fixed_plus_rate | `linear_cost/0421/` |
| 0422 | Yara works two jobs paying $16/h and $22/h. Last month 61 hours were worked in total, earning $1156. How many hours were worked at the $16 job? | 31 hours at $16, 30 hours at $22 | Ready | two_prices_known_count | `linear_cost/0422/` |
| 0423 | A phone plan costs $50 a month and includes 5 GB of data. Each extra GB costs $5. The bill was $90. How much data was used? | 13 GB | Ready | plan_with_included | `linear_cost/0423/` |
| 0424 | Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120. How many extra chores were done? | 10 chores | Ready | base_plus_extra_over_time | `linear_cost/0424/` |
| 0425 | Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $46.00. How many notebooks were bought? | 14 notebooks | Ready | price_minus_coupon | `linear_cost/0425/` |
| 0426 | A plumber charges a $80 call-out fee plus $85 per hour. The bill was $250.00. How long did the job take? | 2 hours | Ready | fixed_plus_rate | `linear_cost/0426/` |
| 0427 | Bowling costs $5.50 per game plus $4.00 for shoe rental. Uma spent $9.50. How many games were bowled? | 1 game | Reference |  | `linear_cost/0427/` |
| 0428 | An electric bill is $20 per month plus $0.18 per kWh. This month's bill is $189.20. How many kWh were used? | 940 kWh | Ready | archive_linear_cost_1 | `linear_cost/0428/` |
| 0429 | A parking garage charges $5 for the first hour and $2.00 for each additional hour. A driver paid $11.00. How many hours did they park? | 4 hours | Ready | archive_linear_cost_2 | `linear_cost/0429/` |
| 0430 | A taxi charges $3.50 plus $1.50 per mile. A ride costs $39.50. How many miles was the ride? | 24 miles | Ready | fixed_plus_rate | `linear_cost/0430/` |
| 0431 | A rental car costs $45 per day plus $0.50 per mile. A 2-day rental cost $185.00. How many miles were driven? | 190 miles | Reference |  | `linear_cost/0431/` |
| 0432 | Sam earns $20/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $950.00. How many overtime hours were worked? | 5 overtime hours (45 hours total) | Reference |  | `linear_cost/0432/` |
| 0433 | Umar works two jobs paying $18/h and $20/h. Last month 53 hours were worked in total, earning $1010. How many hours were worked at the $18 job? | 25 hours at $18, 28 hours at $20 | Ready | two_prices_known_count | `linear_cost/0433/` |
| 0435 | Zane gets $10 allowance a week plus $3 for each extra chore. Over 8 weeks that came to $92. How many extra chores were done? | 4 chores | Ready | base_plus_extra_over_time | `linear_cost/0435/` |
| 0441 | Bags of chips cost $7.50 each. With a $10 coupon, Kira paid $12.50. How many bags of chips were bought? | 3 bags of chips | Ready | price_minus_coupon | `linear_cost/0441/` |
| 0442 | Pablo earns $16/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $832.00. How many overtime hours were worked? | 8 overtime hours (48 hours total) | Reference |  | `linear_cost/0442/` |
| 0443 | A gym charges a $100 joining fee and $15 per month. Caleb has paid $145 in total. How many months has Caleb been a member? | 3 months | Ready | fixed_plus_rate | `linear_cost/0443/` |
| 0445 | Bowling costs $6.00 per game plus $4.00 for shoe rental. Nia spent $22.00. How many games were bowled? | 3 games | Reference |  | `linear_cost/0445/` |
| 0447 | Bowling costs $6.00 per game plus $3.00 for shoe rental. Theo spent $9.00. How many games were bowled? | 1 game | Reference |  | `linear_cost/0447/` |
| 0448 | Priya earns $12/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $552.00. How many overtime hours were worked? | 4 overtime hours (44 hours total) | Reference |  | `linear_cost/0448/` |
| 0450 | Leo gets $8 allowance a week plus $4 for each extra chore. Over 6 weeks that came to $64. How many extra chores were done? | 4 chores | Ready | base_plus_extra_over_time | `linear_cost/0450/` |
| 0453 | Notebooks cost $4.50 each. With a $10 coupon, Bea paid $8.00. How many notebooks were bought? | 4 notebooks | Reference |  | `linear_cost/0453/` |
| 0454 | Pablo works two jobs paying $12/h and $17/h. Last month 21 hours were worked in total, earning $297. How many hours were worked at the $12 job? | 12 hours at $12, 9 hours at $17 | Ready | two_prices_known_count | `linear_cost/0454/` |
| 0456 | A gym charges a $50 joining fee and $25 per month. Uma has paid $325 in total. How many months has Uma been a member? | 11 months | Ready | fixed_plus_rate | `linear_cost/0456/` |
| 0459 | Notebooks cost $3.50 each. With a $2 coupon, Dev paid $33.00. How many notebooks were bought? | 10 notebooks | Ready | price_minus_coupon | `linear_cost/0459/` |
| 0462 | Bowling costs $7.00 per game plus $4.00 for shoe rental. Wren spent $39.00. How many games were bowled? | 5 games | Reference |  | `linear_cost/0462/` |
| 0464 | Caleb earns $18/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $801.00. How many overtime hours were worked? | 3 overtime hours (43 hours total) | Reference |  | `linear_cost/0464/` |
| 0465 | Ava gets $8 allowance a week plus $3 for each extra chore. Over 6 weeks that came to $78. How many extra chores were done? | 10 chores | Ready | base_plus_extra_over_time | `linear_cost/0465/` |
| 0466 | Ivan works two jobs paying $14/h and $17/h. Last month 24 hours were worked in total, earning $363. How many hours were worked at the $14 job? | 15 hours at $14, 9 hours at $17 | Ready | two_prices_known_count | `linear_cost/0466/` |
| 0469 | A gym charges a $100 joining fee and $30 per month. Wren has paid $190 in total. How many months has Wren been a member? | 3 months | Ready | fixed_plus_rate | `linear_cost/0469/` |
| 0473 | Rosa gets $5 allowance a week plus $3 for each extra chore. Over 6 weeks that came to $54. How many extra chores were done? | 8 chores | Ready | base_plus_extra_over_time | `linear_cost/0473/` |
| 0475 | Jamal earns $16/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $808.00. How many overtime hours were worked? | 7 overtime hours (47 hours total) | Reference |  | `linear_cost/0475/` |
| 0476 | A gym charges a $99 joining fee and $15 per month. Dana has paid $219 in total. How many months has Dana been a member? | 8 months | Ready | fixed_plus_rate | `linear_cost/0476/` |
| 0477 | Bags of chips cost $4.00 each. With a $10 coupon, Wren paid $10.00. How many bags of chips were bought? | 5 bags of chips | Ready | price_minus_coupon | `linear_cost/0477/` |

## Linear model

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0480 | Town A has 18,000 people and grows by 2000 a year. Town B has 63,000 people and shrinks by 500 a year. In how many years will they be equal? | 18 years | Ready | two_changing_equal | `linear_model/0480/` |
| 0481 | A pool holds 9,300 L and drains at 50 L per minute. After how many minutes will 500 L remain? | 176 minutes | Ready | drain_or_fill | `linear_model/0481/` |
| 0482 | For a taxi ride, 4 miles cost $46 and 11 miles cost $88. The cost is linear: C = m·x + b. Find m and b, then how many miles cost $136. | m = 6, b = 22; 19 miles | Ready | line_from_two_points | `linear_model/0482/` |
| 0483 | Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week. After how many weeks will they be the same height? | 7.5 weeks | Ready | two_changing_equal | `linear_model/0483/` |
| 0484 | A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days? | 53 pages per day | Ready | pages_per_day | `linear_model/0484/` |
| 0485 | One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour. When will they be the same height? | 4.5 hours | Ready | two_candles_equal | `linear_model/0485/` |
| 0486 | Sound travels about 343 m/s, so d = 343t. A storm is 2744 m away. How many seconds after the lightning flash will the thunder be heard? | 8 seconds | Reference |  | `linear_model/0486/` |
| 0487 | A tractor bought for $23,000.00 loses $1,600.00 in value each year. After how many years will it be worth $16,600.00? | 4 years | Ready | archive_linear_model_1 | `linear_model/0487/` |
| 0488 | A club has raised $10 so far. At its bake sale it charges $5 per box of cookies. How many more boxes must it sell to reach its $130 goal? | 24 | Ready | archive_linear_model_2 | `linear_model/0488/` |
| 0489 | A hot-air balloon at 5500 ft descends 650 ft per minute. Another at 1300 ft rises 400 ft per minute. When are they at the same height? | 4 minutes | Ready | archive_linear_model_3 | `linear_model/0489/` |
| 0490 | A phone at 90% battery loses 5% per hour. After how many hours will it be at 20%? | 14 hours | Ready | archive_linear_model_4 | `linear_model/0490/` |
| 0509 | A club has raised $30 so far. At its car wash it charges $12 per car. How many more cars must it sell to reach its $486 goal? | 38 | Reference |  | `linear_model/0509/` |
| 0513 | A delivery van bought for $22,000.00 loses $3,800.00 in value each year. After how many years will it be worth $6,800.00? | 4 years | Reference |  | `linear_model/0513/` |
| 0522 | For a plumber's bill, 5 hours cost $107 and 7 hours cost $121. The cost is linear: C = m·x + b. Find m and b, then how many hours cost $142. | m = 7, b = 72; 10 hours | Ready | line_from_two_points | `linear_model/0522/` |

## Mixture

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0532 | How many pounds of coffee worth $10/lb must be added to 14 lb of coffee worth $8/lb to make a mix worth $9/lb? | 14 lb | Ready | add_to_blend | `mixture/0532/` |
| 0533 | How many liters of a 25% juice drink must be mixed with a 50% juice drink to make 100 liters of a 39% juice drink? | 44 L of the 25% and 56 L of the 50% | Ready | two_solution_mix | `mixture/0533/` |
| 0534 | One alloy is 25% nickel and another is 75% nickel. How many kilograms of each are needed to make 25 kg of an alloy that is 31% nickel? | 22 kg of 25%, 3 kg of 75% | Ready | two_solution_mix | `mixture/0534/` |
| 0535 | How much water must be added to 4 L of a 30% salt solution to make it 5% salt? | 20 L | Reference |  | `mixture/0535/` |
| 0536 | A 30 L tank of 6% salt water is left to evaporate until it is 15% salt. How much water evaporates? | 18 L | Reference |  | `mixture/0536/` |
| 0537 | 50 lb of a blend of coffee beans selling for $13.60/lb is made from coffee beans costing $8/lb and $15/lb. How many pounds of each are used? | 10 lb at $8 and 40 lb at $15 | Ready | price_blend | `mixture/0537/` |
| 0538 | How many liters of pure antifreeze must be added to 4 L of a 30% antifreeze mix to get a 80% mix? | 10 L | Reference |  | `mixture/0538/` |
| 0539 | A 20-liter radiator holds a 50% antifreeze mix. How much must be drained and replaced with pure antifreeze to raise it to 70%? | 8 L | Reference |  | `mixture/0539/` |
| 0541 | A 6 L batch of 80% juice concentrate is diluted with water to 12% juice. How much water is added? | 34 L | Reference |  | `mixture/0541/` |
| 0544 | One alloy is 10% silver and another is 50% silver. How many kilograms of each are needed to make 20 kg of an alloy that is 16% silver? | 17 kg of 10%, 3 kg of 50% | Ready | two_solution_mix | `mixture/0544/` |
| 0545 | 40 lb of a blend of candy selling for $13.60/lb is made from candy costing $8/lb and $24/lb. How many pounds of each are used? | 26 lb at $8 and 14 lb at $24 | Ready | price_blend | `mixture/0545/` |
| 0547 | How many liters of a 60% acid solution must be mixed with a 70% acid solution to make 40 liters of a 65% acid solution? | 20 L of the 60% and 20 L of the 70% | Ready | two_solution_mix | `mixture/0547/` |
| 0555 | How many pounds of raisins worth $12/lb must be added to 4 lb of raisins worth $8/lb to make a mix worth $11/lb? | 12 lb | Ready | add_to_blend | `mixture/0555/` |
| 0558 | How many pounds of peanuts worth $12/lb must be added to 12 lb of peanuts worth $6/lb to make a mix worth $9/lb? | 12 lb | Ready | add_to_blend | `mixture/0558/` |
| 0561 | How many liters of a 50% alcohol solution must be mixed with a 60% alcohol solution to make 30 liters of a 54% alcohol solution? | 18 L of the 50% and 12 L of the 60% | Ready | two_solution_mix | `mixture/0561/` |
| 0562 | 50 lb of a blend of nuts selling for $10.20/lb is made from nuts costing $10/lb and $20/lb. How many pounds of each are used? | 49 lb at $10 and 1 lb at $20 | Ready | price_blend | `mixture/0562/` |
| 0566 | One alloy is 10% copper and another is 90% copper. How many kilograms of each are needed to make 20 kg of an alloy that is 54% copper? | 9 kg of 10%, 11 kg of 90% | Ready | two_solution_mix | `mixture/0566/` |

## Number puzzle

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0570 | 6 times the difference of a number and 6 is 174. What is the number? | 35 | Ready | number_puzzle | `number_puzzle/0570/` |
| 0571 | The second of three numbers is 3 times the first. The third is 8 more than the second. Their sum is 176. Find the numbers. | 24, 72, 80 | Reference |  | `number_puzzle/0571/` |
| 0572 | Tara has 3 more than 4 times as many stamps as Aiden. Together they have 38 stamps. How many does each have? | Aiden: 7, Tara: 31 | Reference |  | `number_puzzle/0572/` |
| 0573 | If you divide a number by 7 and add 1, you get -3. What was the number? | -28 | Ready | number_puzzle | `number_puzzle/0573/` |
| 0574 | Five times a number, decreased by 19, is 106. Find the number. | 25 | Ready | number_puzzle | `number_puzzle/0574/` |
| 0575 | One-fourth of a number plus one-half of the same number is 48. Find the number. | 64 | Ready | number_puzzle | `number_puzzle/0575/` |
| 0576 | Aiden has 3 times as much money as Fatima. After Aiden gives Fatima $43, they have the same amount. How much did each have at first? | Fatima $43, Aiden $129 | Reference |  | `number_puzzle/0576/` |
| 0577 | 1/2 of a number plus 27 is 39. Find the number. | 24 | Ready | number_puzzle | `number_puzzle/0577/` |
| 0578 | 6 times a number minus 4 equals 5 times the number plus 6. Find the number. | 10 | Ready | number_puzzle | `number_puzzle/0578/` |
| 0579 | Grace has 4 times as much money as Nia. After Grace gives Nia $42, they have the same amount. How much did each have at first? | Nia $28, Grace $112 | Reference |  | `number_puzzle/0579/` |
| 0581 | One-third of a number is 4 more than one-fifth of it. Find the number. | 30 | Ready | number_puzzle | `number_puzzle/0581/` |
| 0582 | A number divided by 9, then increased by 9, gives 10. Find the number. | 9 | Ready | number_puzzle | `number_puzzle/0582/` |
| 0584 | When 4 is subtracted from a number and the result is multiplied by 5, the answer is 60. Find the number. | 16 | Ready | number_puzzle | `number_puzzle/0584/` |
| 0585 | Grace has 9 more than 4 times as many stamps as Uma. Together they have 139 stamps. How many does each have? | Uma: 26, Grace: 113 | Reference |  | `number_puzzle/0585/` |
| 0586 | 9 times a number, increased by 31, is 229. Find the number. | 22 | Ready | number_puzzle | `number_puzzle/0586/` |
| 0591 | Wren has 3 times as much money as Sam. After Wren gives Sam $15, they have the same amount. How much did each have at first? | Sam $15, Wren $45 | Reference |  | `number_puzzle/0591/` |
| 0594 | Caleb has 12 more than 3 times as many stamps as Bea. Together they have 88 stamps. How many does each have? | Bea: 19, Caleb: 69 | Reference |  | `number_puzzle/0594/` |
| 0596 | One-fourth of a number is 2 more than one-fifth of it. Find the number. | 40 | Ready | number_puzzle | `number_puzzle/0596/` |
| 0597 | Ben has 3 times as much money as Dev. After Ben gives Dev $38, they have the same amount. How much did each have at first? | Dev $38, Ben $114 | Reference |  | `number_puzzle/0597/` |
| 0600 | Isla has 5 more than 2 times as many stamps as Caleb. Together they have 26 stamps. How many does each have? | Caleb: 7, Isla: 19 | Reference |  | `number_puzzle/0600/` |
| 0603 | If you divide a number by 5 and add 10, you get 26. What was the number? | 80 | Ready | number_puzzle | `number_puzzle/0603/` |
| 0604 | Four times a number, increased by 1, is 117. Find the number. | 29 | Ready | number_puzzle | `number_puzzle/0604/` |
| 0607 | Victor has 2 times as much money as Yara. After Victor gives Yara $25, they have the same amount. How much did each have at first? | Yara $50, Victor $100 | Reference |  | `number_puzzle/0607/` |
| 0608 | 6 times the difference of a number and 11 is -108. What is the number? | -7 | Ready | number_puzzle | `number_puzzle/0608/` |
| 0610 | 9 times a number, decreased by 11, is 205. Find the number. | 24 | Ready | number_puzzle | `number_puzzle/0610/` |
| 0611 | Maya has 5 more than 4 times as many stamps as Ben. Together they have 285 stamps. How many does each have? | Ben: 56, Maya: 229 | Reference |  | `number_puzzle/0611/` |

## Percent

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0612 | A coat is marked 40% off, and then an extra 10% is taken off the sale price. The final price is $464.40. What was the original price? | $860.00 | Ready | two_discounts | `percent/0612/` |
| 0613 | A test has 20 questions. Jamal scored 65%. How many questions were answered correctly? | 13 questions | Ready | percent_of_count | `percent/0613/` |
| 0614 | A town's population changed from 2500 to 4000. What was the percent change? | +60% (increase) | Ready | percent_change_between | `percent/0614/` |
| 0615 | After adding a 20% tip, a dinner bill came to $195.18. What was the bill before the tip? | $162.65 | Ready | percent_change | `percent/0615/` |
| 0616 | In a two-candidate election, the winner got 58% of the votes and won by 3392 votes. How many votes were cast? | 21,200 votes | Ready | election_margin | `percent/0616/` |
| 0617 | After a 2% raise, Mateo's salary is $77,520.00. What was the salary before the raise? | $76,000.00 | Ready | percent_change | `percent/0617/` |
| 0618 | Yara spent 75% of a paycheck on rent and had $280 left. How much was the paycheck? | $1120 | Ready | percent_spent_left | `percent/0618/` |
| 0619 | The total cost of an item including 7.5% sales tax is $46.87. What was the price before tax? | $43.60 | Ready | percent_change | `percent/0619/` |
| 0620 | What percent of 95 is 114? | 120% | Ready | archive_percent_1 | `percent/0620/` |
| 0621 | 3 is 30% of what number? | 10 | Reference |  | `percent/0621/` |
| 0622 | After a 20% discount, a backpack costs $20.00. What was the original price? | $25.00 | Ready | percent_change | `percent/0622/` |
| 0623 | 9 friends split a restaurant bill equally, including a 25% tip. Each paid $175.00. What was the bill before the tip? | $1,260.00 | Reference |  | `percent/0623/` |
| 0624 | 20% of the students in a club are boys. There are 136 girls. How many students are in the club? | 170 students | Reference |  | `percent/0624/` |
| 0625 | A stock's price rose 10% one month and then fell 40% the next, ending at $580.80. What was the starting price? | $880.00 | Reference |  | `percent/0625/` |
| 0629 | Rhea spent 40% of a paycheck on rent and had $192 left. How much was the paycheck? | $320 | Ready | percent_spent_left | `percent/0629/` |
| 0631 | After a 2% raise, Kira's salary is $55,080.00. What was the salary before the raise? | $54,000.00 | Ready | percent_change | `percent/0631/` |
| 0633 | A test has 20 questions. Isla scored 65%. How many questions were answered correctly? | 13 questions | Ready | percent_of_count | `percent/0633/` |
| 0637 | After a 40% discount, a lamp costs $27.00. What was the original price? | $45.00 | Ready | percent_change | `percent/0637/` |
| 0644 | 30 out of 150 students passed. What percent passed? | 20% | Ready | archive_percent_2 | `percent/0644/` |
| 0645 | After a 5% raise, Fatima's salary is $69,300.00. What was the salary before the raise? | $66,000.00 | Ready | percent_change | `percent/0645/` |
| 0647 | A test has 40 questions. Pablo scored 95%. How many questions were answered correctly? | 38 questions | Ready | percent_of_count | `percent/0647/` |
| 0650 | Kira spent 60% of a paycheck on rent and had $424 left. How much was the paycheck? | $1060 | Ready | percent_spent_left | `percent/0650/` |
| 0651 | After a 10% discount, a coffee maker costs $22.50. What was the original price? | $25.00 | Ready | percent_change | `percent/0651/` |
| 0653 | A group paid $243.95 for lunch, which included a 25% tip. How much was the meal itself? | $195.16 | Ready | percent_change | `percent/0653/` |
| 0656 | A test has 80 questions. Theo scored 95%. How many questions were answered correctly? | 76 questions | Ready | percent_of_count | `percent/0656/` |
| 0659 | After a 25% discount, a bicycle costs $258.75. What was the original price? | $345.00 | Ready | percent_change | `percent/0659/` |
| 0663 | After a 5% raise, Hiro's salary is $93,450.00. What was the salary before the raise? | $89,000.00 | Ready | percent_change | `percent/0663/` |
| 0666 | Mateo spent 25% of a paycheck on rent and had $435 left. How much was the paycheck? | $580 | Ready | percent_spent_left | `percent/0666/` |
| 0670 | A test has 80 questions. Gus scored 70%. How many questions were answered correctly? | 56 questions | Ready | percent_of_count | `percent/0670/` |

## Percent (commission)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0677 | Theo earns a weekly base pay of $400 plus 2% commission on sales. One week the total pay was $560.00. What were the sales? | $8,000.00 | Reference |  | `percent_commission/0677/` |
| 0678 | Isla earns a weekly base pay of $750 plus 6% commission on sales. One week the total pay was $2,670.00. What were the sales? | $32,000.00 | Reference |  | `percent_commission/0678/` |
| 0679 | A salesperson gets $750 per week plus 5% of everything they sell. To earn $1,625.00 in a week, how much must they sell? | $17,500.00 | Reference |  | `percent_commission/0679/` |
| 0681 | Nia earns a weekly base pay of $500 plus 15% commission on sales. One week the total pay was $2,900.00. What were the sales? | $16,000.00 | Reference |  | `percent_commission/0681/` |

## Percent (markup)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0682 | After a 75% markup, a watch is priced at $1,347.50. What was the wholesale cost? | $770.00 | Ready | percent_change | `percent_markup/0682/` |
| 0683 | A store marks up a jacket by 25% and sells it for $425.00. What did the store pay for it? | $340.00 | Ready | percent_change | `percent_markup/0683/` |
| 0684 | After a 100% markup, a phone case is priced at $590.00. What was the wholesale cost? | $295.00 | Ready | percent_change | `percent_markup/0684/` |
| 0685 | A store marks up a rug by 50% and sells it for $127.50. What did the store pay for it? | $85.00 | Ready | percent_change | `percent_markup/0685/` |

## Profit

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0686 | A candle shop has fixed costs of $2000. Each item costs $2 to make and sells for $17. How many items must be sold to make a profit of $9775? | 785 items | Ready | archive_profit_1 | `profit/0686/` |
| 0689 | A T-shirt business has fixed costs of $100. Each item costs $2 to make and sells for $8. How many items must be sold to make a profit of $452? | 92 items | Reference |  | `profit/0689/` |
| 0690 | A bakery stall has fixed costs of $750. Each item costs $2 to make and sells for $4. How many items must be sold to make a profit of $302? | 526 items | Reference |  | `profit/0690/` |

## Proportion

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0691 | A model car is built at a 1:50 scale. The real car is 50 cm long. How long is the model? | 1 | Reference |  | `proportion/0691/` |
| 0692 | A lawn needs 4 kg of fertilizer per 25 m². How much is needed for 400 m²? | 64 kg | Ready | proportion | `proportion/0692/` |
| 0693 | A shade of green uses blue and yellow paint in the ratio 2:3. If 6 L of blue is used, how much yellow is needed? | 9 L | Ready | ratio_split | `proportion/0693/` |
| 0694 | A recipe uses 0.5 cups of flour for 4 servings. How many cups are needed for 8 servings? | 1 cup | Ready | proportion | `proportion/0694/` |
| 0695 | Suppose 1 dollar buys 1.25 units of a foreign currency. How many dollars do you need to get 1875 units? | $1,500.00 | Ready | proportion | `proportion/0695/` |
| 0696 | A cookie recipe needs 4 eggs for 24 cookies. How many eggs for 60 cookies? | 10 eggs | Ready | proportion | `proportion/0696/` |
| 0697 | On a map, 1 cm represents 20 km. Two cities are 380 km apart. How far apart are they on the map? | 19 cm | Reference |  | `proportion/0697/` |
| 0711 | A recipe uses 1.5 cups of sugar for 3 servings. How many cups are needed for 10 servings? | 5 cups | Ready | proportion | `proportion/0711/` |
| 0716 | A recipe uses 1 cups of rice for 6 servings. How many cups are needed for 15 servings? | 2.5 cups | Ready | proportion | `proportion/0716/` |
| 0722 | A recipe uses 0.75 cups of milk for 6 servings. How many cups are needed for 5 servings? | 5/8 cups | Ready | proportion | `proportion/0722/` |

## Proportion (similar triangles)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0725 | A 5 ft person casts a 2 ft shadow. At the same time a tree casts a 30 ft shadow. How tall is the tree? | 75 | Ready | archive_proportion_similar_triangles_1 | `proportion_similar_triangles/0725/` |
| 0726 | At noon a 6 m post casts a 10 m shadow, and a building nearby casts a 150 m shadow. How tall is the building? | 90 | Reference |  | `proportion_similar_triangles/0726/` |

## Quadratic

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0729 | The square of a positive number is 48 more than 2 times the number. Find the number. | 8 | Reference |  | `quadratic/0729/` |
| 0730 | The sum of the squares of two consecutive positive integers is 85. Find the integers. | 6 and 7 | Reference |  | `quadratic/0730/` |
| 0731 | The square of a positive number plus 16 times the number equals 720. Find the number. | 20 | Reference |  | `quadratic/0731/` |
| 0732 | A polygon has 5 diagonals. Using D = n(n − 3)/2, how many sides does it have? | 5 sides | Reference |  | `quadratic/0732/` |
| 0733 | The product of two consecutive positive integers is 12. Find the integers. | 3 and 4 | Ready | consecutive_product | `quadratic/0733/` |
| 0734 | Two numbers add up to 56 and multiply to 780. What are they? | 26 and 30 | Reference |  | `quadratic/0734/` |
| 0736 | The sum of two numbers is 43 and their product is 456. Find the numbers. | 19 and 24 | Reference |  | `quadratic/0736/` |
| 0741 | The product of two consecutive positive even integers is 224. Find the integers. | 14 and 16 | Ready | consecutive_product | `quadratic/0741/` |
| 0753 | The product of two consecutive positive odd integers is 35. Find the integers. | 5 and 7 | Ready | consecutive_product | `quadratic/0753/` |

## Quadratic (counting)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0755 | At a party everyone shook hands with everyone else exactly once, for 10 handshakes. How many people were there? | 5 | Reference |  | `quadratic_counting/0755/` |
| 0757 | In a round-robin tournament each team plays every other team once, for 45 games. How many teams are there? | 10 | Reference |  | `quadratic_counting/0757/` |

## Quadratic (projectile)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0759 | A rocket is launched upward from a height of 96 ft at 16 ft/s. Its height is h = −16t² + 16t + 96. After how many seconds does it hit the ground? | 3 seconds | Reference |  | `quadratic_projectile/0759/` |
| 0762 | A rock is launched upward from a height of 16 ft at 24 ft/s. Its height is h = −16t² + 24t + 16. After how many seconds does it hit the ground? | 2 seconds | Reference |  | `quadratic_projectile/0762/` |
| 0763 | A stone is launched upward from a height of 32 ft at 124 ft/s. Its height is h = −16t² + 124t + 32. After how many seconds does it hit the ground? | 8 seconds | Reference |  | `quadratic_projectile/0763/` |

## Quadratic (sequences)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0764 | How many consecutive whole numbers, starting from 1, must be added to get a sum of 1326? (Use 1 + 2 + … + n = n(n + 1)/2.) | 51 numbers (1 through 51) | Reference |  | `quadratic_sequences/0764/` |
| 0765 | A stack of cans has 1 can in the top row, and each row below has 1 more than the row above. The stack has 15 cans in total. How many rows are there? | 5 rows | Reference |  | `quadratic_sequences/0765/` |
| 0766 | A stack of cans has 8 cans in the top row, and each row below has 2 more than the row above. The stack has 260 cans in total. How many rows are there? | 13 rows | Reference |  | `quadratic_sequences/0766/` |

## Rate

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0774 | A car travels 364 miles on 13 gallons of gas. At this rate, how many gallons are needed for 392 miles? | 14 gallons | Ready | proportion | `rate/0774/` |

## Ratio

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0779 | The ratio of boys to girls in a class is 3:8. After 4 more girls join, the ratio becomes 1:3. How many students were there originally? | 44 students (12 boys, 32 girls) | Ready | class_ratio_after_join | `ratio/0779/` |
| 0780 | An estate of $64,500.00 is split among three heirs. Wes gets 2 times as much as Nia, and Noah gets $6,500.00 more than Nia. How much does each receive? | Wes $29,000.00, Nia $14,500.00, Noah $21,000.00 | Reference |  | `ratio/0780/` |
| 0781 | A mix uses cement, sand, and gravel in the ratio 8:4:5. The total is 204 kg. How much of each is used? | 96, 48, 60 kg | Reference |  | `ratio/0781/` |
| 0782 | The ratio of Yusuf's marbles to Dev's is 3:5. After Yusuf gives Dev 12 marbles, the ratio is 1:7. How many did each have at first? | Yusuf 18, Dev 30 | Reference |  | `ratio/0782/` |
| 0783 | Sofia and Pablo invested in a business in the ratio 2:1. They share a profit of $22,500.00 in the same ratio. How much does each get? | Sofia $15,000.00, Pablo $7,500.00 | Reference |  | `ratio/0783/` |
| 0784 | A 10 m rope is cut into two pieces in the ratio 1:4. How long is each piece? | 2 m and 8 m | Reference |  | `ratio/0784/` |
| 0785 | A 105 cm board is cut into two pieces. One piece is 7 cm longer than the other. How long is each piece? | 49 cm and 56 cm | Ready | sum_difference | `ratio/0785/` |
| 0786 | A mix uses flour, sugar, and butter in the ratio 2:4:5. The total is 88 g. How much of each is used? | 16, 32, 40 g | Reference |  | `ratio/0786/` |
| 0787 | The ratio of Hana's marbles to Maya's is 1:1. After Hana gives Maya 23 marbles, the ratio is 1:3. How many did each have at first? | Hana 46, Maya 46 | Reference |  | `ratio/0787/` |
| 0790 | An estate of $92,000.00 is split among three heirs. Finn gets 3 times as much as Sam, and Ben gets $2,000.00 more than Sam. How much does each receive? | Finn $54,000.00, Sam $18,000.00, Ben $20,000.00 | Reference |  | `ratio/0790/` |
| 0792 | Caleb and Quinn invested in a business in the ratio 6:4. They share a profit of $82,500.00 in the same ratio. How much does each get? | Caleb $49,500.00, Quinn $33,000.00 | Reference |  | `ratio/0792/` |
| 0793 | The ratio of Ben's marbles to Carla's is 3:5. After Ben gives Carla 16 marbles, the ratio is 1:7. How many did each have at first? | Ben 24, Carla 40 | Reference |  | `ratio/0793/` |
| 0794 | Finn and Jade invested in a business in the ratio 4:2. They share a profit of $10,500.00 in the same ratio. How much does each get? | Finn $7,000.00, Jade $3,500.00 | Reference |  | `ratio/0794/` |
| 0799 | An estate of $71,000.00 is split among three heirs. Jamal gets 3 times as much as Maya, and Noah gets $6,000.00 more than Maya. How much does each receive? | Jamal $39,000.00, Maya $13,000.00, Noah $19,000.00 | Reference |  | `ratio/0799/` |
| 0802 | The ratio of Yusuf's marbles to Zane's is 5:6. After Yusuf gives Zane 18 marbles, the ratio is 2:9. How many did each have at first? | Yusuf 30, Zane 36 | Reference |  | `ratio/0802/` |
| 0804 | An estate of $31,500.00 is split among three heirs. Xena gets 3 times as much as Dana, and Finn gets $9,000.00 more than Dana. How much does each receive? | Xena $13,500.00, Dana $4,500.00, Finn $13,500.00 | Reference |  | `ratio/0804/` |
| 0805 | Aiden and Quinn invested in a business in the ratio 1:3. They share a profit of $10,000.00 in the same ratio. How much does each get? | Aiden $2,500.00, Quinn $7,500.00 | Reference |  | `ratio/0805/` |
| 0808 | A mix uses red, blue, and yellow paint in the ratio 7:4:2. The total is 390 mL. How much of each is used? | 210, 120, 60 mL | Reference |  | `ratio/0808/` |
| 0809 | The ratio of Gus's marbles to Kira's is 6:5. After Gus gives Kira 16 marbles, the ratio is 4:7. How many did each have at first? | Gus 48, Kira 40 | Reference |  | `ratio/0809/` |
| 0810 | An estate of $88,500.00 is split among three heirs. Theo gets 3 times as much as Kira, and Umar gets $1,000.00 more than Kira. How much does each receive? | Theo $52,500.00, Kira $17,500.00, Umar $18,500.00 | Reference |  | `ratio/0810/` |
| 0811 | Zane and Wes invested in a business in the ratio 5:2. They share a profit of $50,750.00 in the same ratio. How much does each get? | Zane $36,250.00, Wes $14,500.00 | Reference |  | `ratio/0811/` |

## Rational equation

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0812 | A field trip costs $350 for the bus plus $15 admission per student. The bus cost is shared equally, and each student pays $32.50 in total. How many students went? | 20 students | Ready | shared_fixed_cost | `rational_equation/0812/` |
| 0813 | A plane flies 1590 miles with a 40 mph tailwind in the same time it flies 1350 miles into the same wind as a headwind. What is the plane's speed in still air? | 490 mph | Ready | wind_same_time | `rational_equation/0813/` |
| 0814 | The denominator of a fraction is 2 more than the numerator. If 4 is added to both, the fraction becomes 7/8. Find the original fraction. | 10/12 | Reference |  | `rational_equation/0814/` |
| 0815 | A number plus its reciprocal equals 2.5. Find the number. | 2 or 1/2 | Reference |  | `rational_equation/0815/` |
| 0816 | A group shares a $42 rental equally. If 2 more people join, each pays $5.60 less. How many people are in the group originally? | 3 people | Ready | archive_rational_equation_1 | `rational_equation/0816/` |
| 0817 | A truck travels 96 miles in the same time a car travels 138 miles. The car is 14 mph faster. Find both speeds. | Truck 32 mph, car 46 mph | Ready | archive_rational_equation_2 | `rational_equation/0817/` |
| 0818 | A boat goes 52 km upstream in the same time it goes 132 km downstream. Its speed in still water is 23 km/h. What is the speed of the current? | 10 km/h | Ready | archive_rational_equation_3 | `rational_equation/0818/` |
| 0819 | Jogging a route at 10 km/h takes 2.8 hours longer than cycling it at 24 km/h. How long is the route? | 48 km | Ready | archive_rational_equation_4 | `rational_equation/0819/` |
| 0821 | Jogging a route at 8 km/h takes 10/3 hours longer than cycling it at 18 km/h. How long is the route? | 48 km | Reference |  | `rational_equation/0821/` |
| 0847 | A number plus its reciprocal equals 10/3. Find the number. | 3 or 1/3 | Reference |  | `rational_equation/0847/` |

## Savings

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0848 | Ben has $150 saved and adds $25 each week. Ava has $310 saved and adds $15 each week. After how many weeks will they have the same amount? | 16 weeks (each will have $550) | Ready | savings_equal | `savings/0848/` |
| 0849 | Ben has $70 and saves $15 per week to buy a laptop that costs $220. How many weeks until there is enough? | 10 weeks | Reference |  | `savings/0849/` |
| 0850 | Victor has $0 saved and adds $25 each week. Kira has $180 saved and adds $10 each week. After how many weeks will they have the same amount? | 12 weeks (each will have $300) | Ready | savings_equal | `savings/0850/` |
| 0851 | Noah has $270 and saves $15 per week to buy a guitar that costs $630. How many weeks until there is enough? | 24 weeks | Reference |  | `savings/0851/` |
| 0852 | Jamal has $60 and saves $20 per week to buy a game console that costs $320. How many weeks until there is enough? | 13 weeks | Reference |  | `savings/0852/` |
| 0853 | Yusuf has $350 saved and adds $25 each week. Umar has $630 saved and adds $20 each week. After how many weeks will they have the same amount? | 56 weeks (each will have $1750) | Ready | savings_equal | `savings/0853/` |
| 0854 | Lena has $0 and saves $30 per week to buy a guitar that costs $750. How many weeks until there is enough? | 25 weeks | Reference |  | `savings/0854/` |
| 0855 | Rhea has $330 saved and adds $15 each week. Jamal has $440 saved and adds $10 each week. After how many weeks will they have the same amount? | 22 weeks (each will have $660) | Ready | savings_equal | `savings/0855/` |
| 0856 | Finn has $50 and saves $15 per week to buy concert tickets that costs $320. How many weeks until there is enough? | 18 weeks | Reference |  | `savings/0856/` |

## Sequences

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0857 | A theater has 29 seats in the first row and each row has 5 more seats than the row before. Which row has 209 seats? | Row 37 | Ready | archive_sequences_1 | `sequences/0857/` |
| 0860 | A savings jar holds $15 in week 1 and grows by $6 each week. In which week does it hold $63? | Week 9 | Reference |  | `sequences/0860/` |

## Simple interest

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0862 | Dev has $18,000.00 invested at 3%. How much more must be invested at 9% so that the total earns 6% overall? | $18,000.00 | Reference |  | `simple_interest/0862/` |
| 0863 | Quinn invests $31,000.00, part at 2% and the rest at 3% simple annual interest. After one year the total interest is $770.00. How much was invested at each rate? | $16,000.00 at 2% and $15,000.00 at 3% | Ready | two_rate_interest | `simple_interest/0863/` |
| 0864 | $16,500.00 is split between two accounts paying 6% and 4% simple interest. Both accounts earn the same interest in a year. How much is in each? | $6,600.00 at 6%, $9,900.00 at 4% | Reference |  | `simple_interest/0864/` |
| 0865 | How many years will it take $2,000.00 to earn $480.00 in simple interest at 4% per year? | 6 years | Reference |  | `simple_interest/0865/` |
| 0867 | Victor invests $20,500.00, part at 5% and the rest at 7% simple annual interest. After one year the total interest is $1,055.00. How much was invested at each rate? | $19,000.00 at 5% and $1,500.00 at 7% | Ready | two_rate_interest | `simple_interest/0867/` |
| 0869 | Emeka has $6,000.00 invested at 2%. How much more must be invested at 8% so that the total earns 5% overall? | $6,000.00 | Reference |  | `simple_interest/0869/` |
| 0871 | Yusuf has $19,000.00 invested at 4%. How much more must be invested at 9% so that the total earns 7% overall? | $28,500.00 | Reference |  | `simple_interest/0871/` |
| 0872 | Kofi invests $30,500.00, part at 2% and the rest at 4% simple annual interest. After one year the total interest is $830.00. How much was invested at each rate? | $19,500.00 at 2% and $11,000.00 at 4% | Ready | two_rate_interest | `simple_interest/0872/` |
| 0874 | $15,000.00 earns $5,400.00 in simple interest over 9 years. What is the annual interest rate? | 4% | Ready | archive_simple_interest_1 | `simple_interest/0874/` |
| 0875 | Dana invests $13,500.00, part at 2% and the rest at 5% simple annual interest. After one year the total interest is $450.00. How much was invested at each rate? | $7,500.00 at 2% and $6,000.00 at 5% | Ready | two_rate_interest | `simple_interest/0875/` |
| 0876 | Wren has $16,000.00 invested at 4%. How much more must be invested at 9% so that the total earns 7% overall? | $24,000.00 | Reference |  | `simple_interest/0876/` |
| 0880 | Tara has $1,500.00 invested at 2%. How much more must be invested at 7% so that the total earns 6% overall? | $6,000.00 | Reference |  | `simple_interest/0880/` |
| 0881 | Mateo invests $40,000.00, part at 2% and the rest at 8% simple annual interest. After one year the total interest is $2,000.00. How much was invested at each rate? | $20,000.00 at 2% and $20,000.00 at 8% | Ready | two_rate_interest | `simple_interest/0881/` |

## System of equations

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0882 | A basketball team scored 92 points from 40 field goals, all 2-pointers and 3-pointers. How many of each? | 28 two-pointers, 12 three-pointers | Ready | two_scores | `system_of_equations/0882/` |
| 0883 | Noah bought 30 stamps, some at 55¢ and some at 70¢, for $19.65. How many of each? | 9 at 55¢, 21 at 70¢ | Ready | two_prices_known_count | `system_of_equations/0883/` |
| 0884 | 1 burgers and 3 fries cost $43.00. 5 burgers and 1 fries cost $65.90. Find the price of one of each. | burgers: $11.05 each, fries: $10.65 each | Ready | two_purchases | `system_of_equations/0884/` |
| 0885 | Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is each now? | Jade 75, Emeka 15 | Ready | ages_later_multiple | `system_of_equations/0885/` |
| 0886 | A shop sold 31 kg of two teas, one at $5/kg and one at $12/kg, for $239. How many kg of each? | 19 kg at $5, 12 kg at $12 | Ready | two_prices_known_count | `system_of_equations/0886/` |
| 0887 | A concert sold 628 tickets: lawn seats at $30 and reserved seats at $50. Ticket sales totaled $21,500. How many of each were sold? | 495 lawn, 133 reserved | Ready | two_priced_items | `system_of_equations/0887/` |
| 0888 | Two numbers x and y satisfy −4x − 3y = 9 and 5x − 3y = -18. Find x and y. | x = -3, y = 1 | Reference |  | `system_of_equations/0888/` |
| 0889 | The perimeter of a rectangle is 70 m and its length is 7 m more than its width. Find the length and width. | 21 m by 14 m | Reference |  | `system_of_equations/0889/` |
| 0890 | A farm packed 924 eggs into 41 cartons, using cartons of 12 and cartons of 30. All cartons were full. How many of each? | 17 of 12, 24 of 30 | Reference |  | `system_of_equations/0890/` |
| 0891 | A banquet hall seats 104 guests at 17 tables. Some tables seat 4 and the others seat 8. How many of each kind are there? | 8 tables of 4, 9 tables of 8 | Reference |  | `system_of_equations/0891/` |
| 0892 | The sum of two numbers is 126 and their difference is 100. Find the numbers. | 113 and 13 | Ready | sum_difference | `system_of_equations/0892/` |
| 0893 | A lot has motorcycles and cars. There are 113 vehicles and 344 wheels. How many of each are there? | 54 motorcycles and 59 cars | Reference |  | `system_of_equations/0893/` |
| 0894 | A test has 50 questions. Each correct answer earns 4 points and each wrong answer loses 1. Gus answered every question and scored 180. How many were correct? | 46 correct, 4 wrong | Reference |  | `system_of_equations/0894/` |
| 0895 | A camp rents 13 canoes for 32 campers, filling every seat. Some canoes hold 2 people and the rest hold 4. How many of each were rented? | 10 2-person and 3 4-person | Reference |  | `system_of_equations/0895/` |
| 0896 | A cash drawer has 38 bills, all $10 and $20 bills, totaling $490. How many of each? | 27 $10 bills and 11 $20 bills | Reference |  | `system_of_equations/0896/` |
| 0900 | A lot has bicycles and tricycles. There are 112 vehicles and 277 wheels. How many of each are there? | 59 bicycles and 53 tricycles | Reference |  | `system_of_equations/0900/` |
| 0901 | Zane bought 24 stamps, some at 44¢ and some at 63¢, for $12.27. How many of each? | 15 at 44¢, 9 at 63¢ | Ready | two_prices_known_count | `system_of_equations/0901/` |
| 0902 | A camp rents 16 paddle boats for 74 campers, filling every seat. Some paddle boats hold 4 people and the rest hold 6. How many of each were rented? | 11 4-person and 5 6-person | Reference |  | `system_of_equations/0902/` |
| 0904 | Vera is 5 times as old as Xena. In 18 years, Vera will be 3 times as old as Xena. How old is each now? | Vera 90, Xena 18 | Ready | ages_later_multiple | `system_of_equations/0904/` |
| 0908 | 2 coffees and 5 muffins cost $33.85. 3 coffees and 5 muffins cost $37.90. Find the price of one of each. | coffees: $4.05 each, muffins: $5.15 each | Ready | two_purchases | `system_of_equations/0908/` |
| 0910 | Two numbers x and y satisfy 4x + 5y = -41 and −2x − 3y = 25. Find x and y. | x = 1, y = -9 | Reference |  | `system_of_equations/0910/` |
| 0911 | A test has 50 questions. Each correct answer earns 3 points and each wrong answer loses 1. Priya answered every question and scored 90. How many were correct? | 35 correct, 15 wrong | Reference |  | `system_of_equations/0911/` |
| 0912 | Two numbers x and y satisfy 3x + 5y = 22 and 3x + 4y = 20. Find x and y. | x = 4, y = 2 | Reference |  | `system_of_equations/0912/` |
| 0920 | A farm has chickens and pigs. There are 48 heads and 138 legs. How many of each are there? | 27 chickens and 21 pigs | Ready | heads_and_feet | `system_of_equations/0920/` |
| 0921 | 1 notebooks and 6 pens cost $32.85. 1 notebooks and 3 pens cost $19.20. Find the price of one of each. | notebooks: $5.55 each, pens: $4.55 each | Ready | two_purchases | `system_of_equations/0921/` |
| 0923 | Kofi bought 36 stamps, some at 55¢ and some at 70¢, for $21.30. How many of each? | 26 at 55¢, 10 at 70¢ | Ready | two_prices_known_count | `system_of_equations/0923/` |
| 0924 | Hiro is 5 times as old as Xena. In 2 years, Hiro will be 4 times as old as Xena. How old is each now? | Hiro 30, Xena 6 | Ready | ages_later_multiple | `system_of_equations/0924/` |
| 0925 | A test has 30 questions. Each correct answer earns 5 points and each wrong answer loses 2. Zoe answered every question and scored 52. How many were correct? | 16 correct, 14 wrong | Reference |  | `system_of_equations/0925/` |
| 0928 | Two numbers x and y satisfy −x + 3y = 3 and 5x − 2y = -41. Find x and y. | x = -9, y = -2 | Reference |  | `system_of_equations/0928/` |
| 0931 | Kira is 4 times as old as Ava. In 8 years, Kira will be 2 times as old as Ava. How old is each now? | Kira 16, Ava 4 | Ready | ages_later_multiple | `system_of_equations/0931/` |
| 0932 | A farm has spiders and beetles. There are 17 bugs and 110 legs. How many of each are there? | 4 spiders and 13 beetles | Reference |  | `system_of_equations/0932/` |
| 0936 | A test has 50 questions. Each correct answer earns 4 points and each wrong answer loses 1. Noah answered every question and scored 75. How many were correct? | 25 correct, 25 wrong | Reference |  | `system_of_equations/0936/` |
| 0941 | Omar bought 39 stamps, some at 50¢ and some at 75¢, for $23.00. How many of each? | 25 at 50¢, 14 at 75¢ | Ready | two_prices_known_count | `system_of_equations/0941/` |
| 0942 | Gus bought 40 stamps, some at 44¢ and some at 63¢, for $21.97. How many of each? | 17 at 44¢, 23 at 63¢ | Ready | two_prices_known_count | `system_of_equations/0942/` |

## System of equations (3 variables)

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0950 | An apple, a banana, and a cherry cup cost $4.05 together. Two apples and a banana cost $3.40. A banana and two cherry cups cost $4.70. Find each price. | apple $1.10, banana $1.20, cherry cup $1.75 | Reference |  | `system_of_equations_3_variables/0950/` |
| 0951 | Three numbers add up to 21. The first plus the second is 10, and the second plus the third is 12. Find all three. | 9, 1, 11 | Reference |  | `system_of_equations_3_variables/0951/` |

## Tickets

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0959 | Adult tickets to a movie screening cost $12 and child tickets cost $6. 167 tickets were sold for a total of $1404. How many of each were sold? | 67 adult and 100 child tickets | Ready | archive_tickets_1 | `tickets/0959/` |
| 0960 | Adult tickets to a museum cost $10 and child tickets cost $4. 599 tickets were sold for a total of $4196. How many of each were sold? | 300 adult and 299 child tickets | Reference |  | `tickets/0960/` |
| 0962 | Adult tickets to a concert cost $15 and child tickets cost $4. 225 tickets were sold for a total of $1967. How many of each were sold? | 97 adult and 128 child tickets | Reference |  | `tickets/0962/` |

## Work rate

| Id | Problem | Answer | Status | Solver | Folder |
|---|---|---|---|---|---|
| 0964 | Two typists type 55 and 35 words per minute. Working together, how long will they take to type 1440 words? | 16 minutes | Ready | two_rates_one_pile | `work_rate/0964/` |
| 0965 | Rosa can assemble the shelves in 15 hours. Fatima can do it in 3 hours. How long will it take them working together? | 2.5 hours (2.50 h) | Ready | work_together | `work_rate/0965/` |
| 0966 | Pipe A fills a pool in 4 hours, pipe B in 5 hours, and a drain empties it in 20 hours. With all three open, how long does it take to fill the pool? | 2.5 hours | Ready | pipes_and_drain | `work_rate/0966/` |
| 0967 | A new machine works 2 times as fast as an old one. Together they finish an order in 3 hours. How long would the old machine take alone? | 9 hours (new machine: 4.5 hours) | Ready | archive_work_rate_1 | `work_rate/0967/` |
| 0968 | Gus, Rosa, and Bea can each paint a room alone in 12, 30, and 3 hours. How long will it take all three together? | 20/9 hours | Reference |  | `work_rate/0968/` |
| 0969 | An inlet pipe fills a tank in 5 hours. A drain empties it in 6 hours. If both are open, how long does it take to fill the empty tank? | 30 hours | Ready | archive_work_rate_2 | `work_rate/0969/` |
| 0970 | Working together, Rhea and Emeka can finish a job in 4 hours. Rhea alone takes 12 hours. How long would Emeka take alone? | 6 hours | Reference |  | `work_rate/0970/` |
| 0971 | Sam can do a job in 4 hours and Hana can do it in 8 hours. Sam works alone for 2 hours, then Hana joins. How much longer will it take to finish? | 4/3 more hours | Reference |  | `work_rate/0971/` |
| 0972 | Working together, Noah and Victor can finish a job in 6 hours. Noah alone takes 12 hours. How long would Victor take alone? | 12 hours | Reference |  | `work_rate/0972/` |
| 0974 | Grace can do a job in 5 hours and Isla can do it in 15 hours. Grace works alone for 2 hours, then Isla joins. How much longer will it take to finish? | 2.25 more hours | Reference |  | `work_rate/0974/` |
| 0976 | Lena can paint a fence in 5 hours. Ava can do it in 10 hours. How long will it take them working together? | 10/3 hours (3.33 h) | Ready | work_together | `work_rate/0976/` |
| 0978 | Quinn, Jamal, and Sam can each paint a room alone in 24, 20, and 30 hours. How long will it take all three together? | 8 hours | Reference |  | `work_rate/0978/` |
| 0980 | Rhea can do a job in 4 hours and Carla can do it in 12 hours. Rhea works alone for 2 hours, then Carla joins. How much longer will it take to finish? | 1.5 more hours | Reference |  | `work_rate/0980/` |
| 0983 | Bea can mow a lawn in 12 hours. Yara can do it in 18 hours. How long will it take them working together? | 7.2 hours (7.20 h) | Ready | work_together | `work_rate/0983/` |
| 0986 | Aiden, Lena, and Yara can each paint a room alone in 8, 30, and 20 hours. How long will it take all three together? | 4.8 hours | Reference |  | `work_rate/0986/` |
| 0987 | Working together, Gus and Sam can finish a job in 3 hours. Gus alone takes 6 hours. How long would Sam take alone? | 6 hours | Reference |  | `work_rate/0987/` |
| 0990 | Sofia, Grace, and Sam can each paint a room alone in 24, 15, and 10 hours. How long will it take all three together? | 4.8 hours | Reference |  | `work_rate/0990/` |
| 0991 | Vera can do a job in 4 hours and Zane can do it in 12 hours. Vera works alone for 1 hour, then Zane joins. How much longer will it take to finish? | 2.25 more hours | Reference |  | `work_rate/0991/` |
| 0992 | Maya can wash the cars in 10 hours. Kira can do it in 20 hours. How long will it take them working together? | 20/3 hours (6.67 h) | Ready | work_together | `work_rate/0992/` |
| 0995 | Working together, Hiro and Nia can finish a job in 3 hours. Hiro alone takes 4 hours. How long would Nia take alone? | 12 hours | Reference |  | `work_rate/0995/` |
| 0997 | Working together, Omar and Fatima can finish a job in 3 hours. Omar alone takes 12 hours. How long would Fatima take alone? | 4 hours | Reference |  | `work_rate/0997/` |
| 0998 | Grace, Uma, and Omar can each paint a room alone in 10, 30, and 24 hours. How long will it take all three together? | 40/7 hours | Reference |  | `work_rate/0998/` |
| 0999 | Dana can clean the house in 15 hours. Priya can do it in 10 hours. How long will it take them working together? | 6 hours | Ready | work_together | `work_rate/0999/` |
| 1000 | Dev can do a job in 12 hours and Pablo can do it in 3 hours. Dev works alone for 1 hour, then Pablo joins. How much longer will it take to finish? | 2.2 more hours | Reference |  | `work_rate/1000/` |
