# -*- coding: utf-8 -*- #

from RankAggregation import RankAggregation


# The RA_Reciprocal class handles the Reciprocal Rank Fusion algorithm for 
# Rank Aggregation. 
# This class inherits from the RankAggregation class, and implements the 
# rank() function. 
# The Reciprocal Rank Fusion (RRF) algorithm is a simple method for 
# combining the document rankings from multiple IR systems. 
# It uses the rank information for computing a similarity score between 
# the query object and another one.
# \cite Cormack:2009 . 
class RkReciprocal(RankAggregation):

    # \fn rank 
    # The rank function uses the RRF algorithm to compute a new ranked 
    # list for the query object.
    # \param tp_param Is a constant that mitigates the impact of high 
    # rankings by outlier systems.
    # \return A ranked list with the same structure as the ls_data attribute 
    # (a list of dictionaries, each dictionary with three keys 
    # ('sim','id','rank')).
    def rank(self, tp_param = 60):
        
        if tp_param < 0:
            raise ValueError("tp_param must be greater than or equal to zero.")
            
        dc_map = {}
        
        # Initialize map of ranks from first ranked list
        for dc_i in self.ls_data[0]:
            dc_map.update({dc_i.get('id'):1.0/(tp_param + dc_i.get('rank'))})
            
        # Computes RRF count
        for i in range(1, self.int_numRanks):
            for dc_i in self.ls_data[i]:
                dc_map[dc_i.get('id')] += 1.0/(tp_param + dc_i.get('rank')) 
                
        max_count = max(dc_map.values())
        
        # Sorting objects by using RRF count
        dc_map = \
            sorted(dc_map.items(), key=lambda dc_map: dc_map[1], reverse=True)
        
        ls_finalRank = []
        
        # The new similarity is the normalized RRF count.
        for i in range(len(dc_map)):
            final_count = dc_map[i][1]/float(max_count)
            ls_finalRank.append(
                {'id': dc_map[i][0],'rank': i+1, 'sim': final_count})

        return ls_finalRank
