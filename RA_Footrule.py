# -*- coding: utf-8 -*- #

import math
from RankAggregation import RankAggregation


##  The RA_Footrule class handles the Footrule method for Rank Aggregation.
#   This class inherits from the RankAggregation class, and implements the rank() function. 
#   The Footrule Optimal Aggregation algorithm is a good approximation of the Kemeny optimal aggregation, that can be computed in polynomial time.
#   \cite Dwork:2001 .
class RA_Footrule(RankAggregation):
	
	## \fn rank 
	#  The rank function uses the Footrule Optimal Aggregation algorithm to compute a new ranked list for the query object.
	#  \param tp_param Represent a value N, where N indicates that we are interested in the first N elements in the final rank (top-N).
	#  \return A ranked list with the same structure as the ls_data attribute (a list of dictionaries, each dictionary with three keys ('sim','id','rank')).
	def rank(self,*tp_param):
		ls_finalRank = []
		auxDict = dict()
		j = math.ceil(len(self.ls_data)/2.0)
		n = tp_param[0]
		int_pos = 1

		for i in range(len(self.ls_data[0])):
			# This loop runs for each element in the rank
			
			for rankedlist in self.ls_data:
				# This loop runs for each ranked list
		
				if not rankedlist[i].get('id') in auxDict.keys() and not rankedlist[i].get('id') in ls_finalRank:
					# The element is neither in the subset of known elements nor in the final rank. It consists of an element not considered yet.
					# The element starts with a vote.
					auxDict[rankedlist[i].get('id')] = 1
					
				elif rankedlist[i].get('id') in auxDict.keys():
					# The element receives one more vote.
					auxDict[rankedlist[i].get('id')] += 1
					
					# Check if the element has the necessary number of votes.
					if auxDict[rankedlist[i].get('id')] == j:
						# The element is inserted in the next position available in the final rank
						ls_finalRank.append({ 'rank':int_pos, 'id':rankedlist[i].get('id'), 'sim':None })
						
						# For the context of geocodind, in wich we are interested only on the first element of the rank, we interrupt the run when achieve the second element.
						# The code allows to break the execution when reaches the top-n elements
						# In this case, the first element is the query, because we are using the development set.
						if len(ls_finalRank) == n:
							return ls_finalRank
							
						int_pos += 1						
						del auxDict[rankedlist[i].get('id')]
						
		return ls_finalRank
	