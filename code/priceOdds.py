import random
from random import randrange, uniform

while True:
	print("what win nr ?.!!")
	try:
		str1 = int(input())
		#check = str1 + str1		
	except:
		ordernr = 0
		#cost = 0
		#backed = 0
		#backedl = 0
		#balance = 50
		#total = 0
		#solo = 0
		#solomio = 0
		#str1 = randrange(1,4)
# order number 
# Variables Name 
# bp0x0 0
	try:
		check = backedw
	except:
		print("How much for the Winning NFTS?")
		backedw= input()
		print("How much for the Losing NFTS?")
		backedl= float(input())
		balance = 50
		
	try:
		check = balancew
	except:
		balancew = 0
	if balancew > 0:
		balancew = balancew
		balancel = balancel
		cost= cost 
	else:	
		balancew = 0
	try:
		check = solo
	except:
		solo = 0
	if solo > 0:
		solo = solo
	else:	
		solo = 0
	
	try:
		check = total 
	except:
		total = 0
	if total> 0:
		total = total
	else:	
		total = 0
		
	try:
		check = solomio
	except:
		solomio = 0
	if total> 0:
		solomio = solomio
	else:	
		solomio = 0
		
	print(f'...{solo}sol...{solomio}...solmi...{total}tot...')
	ordernr = 0
	win_ch = 0
	while win_ch < 1:# < 33445555:	
		win_nr = randrange(0,2)
		# 1%=2%=4%=8%=16%=32%=64%
		#1%=2%=4%=8%=10%
		#=20%=30%=40%=50%
		#=60%=70%=80%=90%=
		#...0,2 is 1/2=50% 
		#...0,3 is 1/3=33%
		#...0,4 is 1/4=25%
		#...0,5 is 1/5=20%
		#...0,6 is 1/6=16%
		#...0,7 is 1/7=14%
		#...0,8 is 1/8=12,5%
		#...0,9 is 1/9=11%
		#...0,10 is 1/10=10%
		#...0,12 is 1/12=8.3%
		#...0,12 is 1/12.5=8%
		#...0,13 is 1/13=7.6%
		#...0,20 is 1/20=5%
		#...0,25 is 1/25=4%
		#...0,40 is 1/40=2.5%
		#...0,50 is 1/50=2%
		#...0,75 is 1/75=1.3%
		#...0,80 is 1/80=1.25%
		#...0,100 is 1/100=1%
		#print (win_nr) 
		ordernr += 1		
		if win_nr == 1:#int(str1):
		       #print("..WIN..")
		       win_ch = 1
		if win_ch > 0:
		   	solo += 1
		   	total += ordernr
		   	print(f' ...{solo}=Total Win...{total-solo}=Total Lose...')
		   	solomio = total / solo
		   	win10 = int(solo)*int(backedw)
		   	lose2 = total-solo
		   	lose02 = lose2 * backedl+0.2
		   	ramcost = total*0.2
		   	cost = win10+lose02+ramcost
		   	print(f'HIT at {ordernr} attempts...{total} Total Open...{solomio} cut Win%...')
		   	print(f'...{win10} WAX total For Player Win...')
		   	print(f'...{lose02} WAX total for Player Lose...')
		   	print(f'...BACKED COST:{win10+lose02}...')
		   	print(f'...RAM COST:{ramcost}...')
		   	print(f'...Total...{cost}...')
		   	#print(f'=balance {balance} - Total to Pay {cost}...')
		   	#print(f'=balance {balance-cost}...')
		   	
		   	packP = cost/total
		   	profit = total*packP-cost
		   	prof = total*packP-cost
		   	#print(f'...PACKAGE PRICE\nNo Profit:\n{packP}...')
		   	#print(f'...PACKAGE PRICE:\n10%...\n{packP*0.1+packP}...')
		   	#print(f'...PACKAGE PRICE:\n50%...\n{packP*0.5+packP}...\n')
		   	#try:
		   	#	print("How much for 1 Package?")
		   	#	price1= float(input())
		   	#except:
		   	#	price1 = randrange (1,10)
		   	#prof1 = total*price1-cost
		   	print(f'...if...Profit 0%...\nprice 1 Pack {round(packP,4)}\nTotalOpend {total}\n= profit-cost\n{total*packP} - {cost}\n= Raw Profit {total*packP-cost}...\n')
		   	#print(f'...{cost}Total Cost...')
		   	s = packP
		   	s10 = packP*0.1
		   	s1o = packP*0.1+packP
		   	s20 = packP*0.2
		   	s2o = packP*0.2+packP
		   	s30 = packP*0.3
		   	s3o = packP*0.3+packP
		   	s40 = packP*0.4
		   	s4o = packP*0.4+packP
		   	s50 = packP*0.5
		   	s5o = packP*0.5+packP
		   	s60 = packP*0.6
		   	s6o = packP*0.6+packP
		   	s70 = packP*0.7
		   	s7o = packP*0.7+packP
		   	s80 = packP*0.8
		   	s8o = packP*0.8+packP
		   	s90 = packP*0.9
		   	s9o = packP*0.9+packP
		   	s100 = packP*1
		   	s1oo = packP*1+packP
		   	s125 = packP*1.25
		   	s125o = packP*1.25+packP
		   	s150 = packP*1.5
		   	s150o = packP*1.5+packP
		   	s175= packP*1.75
		   	s175o = packP*1.75+packP
		   	s200 = packP*2
		   	s2oo = packP*2+packP
		   	s250 = packP*2.5
		   	s25oo = packP*2.5+packP
		   	print(f'...10%...>>>{round(s10*total,4)}...{s1o}')
		   	print(f'...20%...>>>{round(s20*total,4)}...{s2o}')
		   	print(f'...30%...>>>{round(s30*total,4)}...{s3o}')
		   	print(f'...40%...>>>{round(s40*total,4)}...{s4o}')
		   	print(f'...50%...>>>{round(s50*total,4)}...{s5o}')
		   	print(f'...60%...>>>{round(s60*total,4)}...{s6o}')
		   	print(f'...70%...>>>{round(s70*total,4)}...{s7o}')
		   	print(f'...80%...>>>{round(s80*total,4)}...{s8o}')
		   	print(f'...90%...>>>{round(s90*total,4)}...{s9o}')
		   	print(f'...100%...>>>{round(s100*total,4)}...{s1oo}')
		   	print(f'...125%...>>>{round(s125*total,4)}...{s125o}')
		   	print(f'...150%...>>>{round(s150*total,4)}...{s150o}')
		   	print(f'...175%...>>>{round(s175*total,4)}...{s175o}')
		   	print(f'...200%...>>>{round(s200*total,4)}...{s2oo}')
		   	print(f'...250%...>>>{round(s250*total,4)}...{s25oo}')
		   	#print("..WIN..")
		   	#print(f'if price...{price1}...{prof1}Total Profit...')
		   	#print("..WIN..")
		   	win_ch = 2

#win = total won
#lose = tota'l lost	        
#ram = total cost
#baked = total cost	
#price = 1 pack + 1 nfts = 0.2wax
        
