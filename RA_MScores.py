#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# # \authors Diego Chávez Escalante 
# # \authors Jael Louis Zela Ruiz
# # \authors Kelly Lopes
# # \authors Luís Augusto Martins Pereira
# # \authors Miriã Rafante Bernardino
# # \authors Ramon Pires

from RankAggregation import RankAggregation
import math

##  The RA_MScores class handles the Multiplication scores (MS) method for Rank Aggregation.
#   This class inherits from the RankAggregation class, and implements the rank() function. 
#   The Multiplication Scores algorithm works by multiplying the different similarity scores, high scores are propagated to the others, leading to high aggregated values. The similarity multiplication can be seen as the computation of the probability of two objects be similar.
#   \cite Pedronette:14 .
class RA_MScores(RankAggregation):
	
	## \fn rank 
	#  The rank function uses the Multiplication Scores algorithm to compute a new ranked list for the query object.
	#  \param tp_param The Multiplication Scores algorithm does not use any hyper-parameter.
	#  \return A ranked list with the same structure as the ls_data attribute (a list of dictionaries, each dictionary with three keys ('sim','id','rank')).
	def rank(self,*tp_param):
	
		dc_map = {}
		
		#initialize map of similarities from first ranked list
		for dc_i in self.ls_data[0]:
			dc_map.update({dc_i.get('id'):(dc_i.get('sim') + 1)})
					
		#Multiplication scores
		for i in range(1, self.int_numRanks):
			for dc_i in self.ls_data[i]:
				dc_map[dc_i.get('id')] *= dc_i.get('sim') + 1
		
		#m root of scores
		for str_id in dc_map.iterkeys():
			dc_map[str_id] = math.pow(dc_map[str_id],1.0/self.int_numRanks)/float(self.int_numRanks) 	
		
		max_count = max(dc_map.values())
		
		#Sorting objects by using scores
		dc_map = sorted(dc_map.items(), key=lambda dc_map: dc_map[1],reverse=True)
		
		ls_finalRank = []
		
		#The new similarity is the normalized scores.	
		for i in range(len(dc_map)):
			final_count = dc_map[i][1]/float(max_count)
			ls_finalRank.append({'id':dc_map[i][0],'rank':i+1,'sim':final_count})
		
		return ls_finalRank
		