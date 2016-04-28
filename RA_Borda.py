#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# # \authors Diego Chávez Escalante 
# # \authors Jael Louis Zela Ruiz
# # \authors Kelly Lopes
# # \authors Luís Augusto Martins Pereira
# # \authors Miriã Rafante Bernardino
# # \authors Ramon Pires

from RankAggregation import RankAggregation

##  The RA_Borda class handles the Borda algorithm for Rank Aggregation.
#   This class inherits from the RankAggregation class, and implements the rank() function. 
#   The Borda algorithm sums for each object its currents positions in each ranked list, and then it order them in ascending order.
#   \cite Young:74 .
class RA_Borda(RankAggregation):

	## \fn rank 
	#  The rank function uses the Borda algorithm to compute a new ranked list for the query object.
	#  \param tp_param The Borda algorithm does not use any hyper-parameter.
	#  \return A ranked list with the same structure as the ls_data attribute (a list of dictionaries, each dictionary with three keys ('sim','id','rank')).
	def rank(self,*tp_param):
	
		dc_map = {}
		
		#initialize map of ranks from first ranked list.
		for dc_i in self.ls_data[0]:
			dc_map.update({dc_i.get('id'):dc_i.get('rank')})
			
		#Computes Borda count.
		for i in range(1, self.int_numRanks):
			for dc_i in self.ls_data[i]:
				dc_map[dc_i.get('id')] += dc_i.get('rank') 
			
		max_count = max(dc_map.values())
		
		#Sorting objects by using Borda count.
		dc_map = sorted(dc_map.items(), key=lambda dc_map: dc_map[1])
		
		ls_finalRank = []
		
		#The new similarity is the normalized Borda count.	
		for i in range(len(dc_map)):
			final_count = 1 - dc_map[i][1]/float(max_count)
			ls_finalRank.append({'id':dc_map[i][0],'rank':i+1,'sim':final_count})
		
		return ls_finalRank
		
