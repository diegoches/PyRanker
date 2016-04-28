#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# # \authors Diego Chávez Escalante 
# # \authors Jael Louis Zela Ruiz
# # \authors Kelly Lopes
# # \authors Luís Augusto Martins Pereira
# # \authors Miriã Rafante Bernardino
# # \authors Ramon Pires

from RankAggregation import RankAggregation
import  operator

##  The RA_CombMIN class handles the CombMIN algorithm for Rank Aggregation.
#   This class inherits from the RankAggregation class, and implements the rank() function. 
#   The CombMIN algorithm get the minimum similarity of each object in the ranked lists, and then it order them in descending order.
#   \cite Fox:1994 .
class RA_CombMIN(RankAggregation):

	## \fn rank 
	#  The rank function uses the CombMIN algorithm to compute a new ranked list for the query object.
	#  \param tp_param The CombMIN algorithm does not use any hyper-parameter.
	#  \return A ranked list with the same structure as the ls_data attribute (a list of dictionaries, each dictionary with three keys ('sim','id','rank')).
	def rank(self,*tp_param):
		
		int_tam=len(self.ls_data[0]);
		int_rnk=len(self.ls_data);
		
		dc_tmp={};
		
		# Get the minimum similarity for each object.
		for i in range(0,int_rnk):
			for j in range(0,int_tam):
				str_name=self.ls_data[i][j].get('id');
				flo_sim=self.ls_data[i][j].get('sim');
				if dc_tmp.has_key(str_name)==False :
					dc_tmp[str_name]=flo_sim;
				else:
					if(flo_sim<dc_tmp[str_name]):
						dc_tmp[str_name]=flo_sim;
		
		# Orders a list of the objects by its new similarity.
		ls_sor=sorted(dc_tmp.iteritems(),key=operator.itemgetter(1),reverse=True);
		
		ls_ra=[];
		
		# Maps the new rank in the output format.
		for i in range(0,int_tam):
			dc_tp={'sim':ls_sor[i][1],'id':ls_sor[i][0],'rank':i+1}
			ls_ra.append(dc_tp);
		
		return ls_ra;
		
	



