# -*- coding: utf-8 -*- #

from rank_structures.rank_list import RankList
from rank_structures.rank import Rank


# The RankAggregation class is a built-in type that works as a general 
# interface for all rank aggregation algorithms.
# The RankAggregation class has two attributes. The ranked lists and the
# number of ranked lists.  
# Every Rank Aggregation method has to inheritance this class and implements 
# the rank(self, ls_param) function.  
# \var ls_data The ranked lists are a list of lists where each element is a 
# dictionary with three keys: 'id', 'sim' and 'rank'. 
# The value for the key 'id' is the object's identifier; 
# the value of 'sim' is the related similarity to each object in the current 
# ranked list; the value of 'rank' is just the object's position in the 
# ranked list.
# \var int_numRanks The number of ranked lists.
class RankAggregation(object):

    def __init__(self):
        self.rank_list = RankList()
        self.aggregated_rank = Rank()

    # \fn rank
    # This function is the one that accomplish the Rank Aggregation algorithm.
    # It has to be implemented by all the classes that inherit from this class.
    # \param tp_param is a tuple of hyper-parameters from the
    # specific algorithm. In the case that the algorithm does not have
    # hyper-parameters, tp_param would be empty.
    def rank(self, *tp_param):
        raise NotImplementedError("Please Implement this method")
    
    # \fn __list_id
    # This method returns the ids of a given ranked list.
    # \param ls_rankedList is a list of dictionaries with three
    # keys ('id','sim','rank').
    # \return a list of strings with the ids of the objects in the ranked list.
    def __list_id(self, ls_rankedList):
        
        ls_ids = []
        for var in ls_rankedList:
            ls_ids.append(var.get('id'))
                
        return ls_ids
        
    # \fn __intersection_id
    # This method intersects the ranked lists in the ls_data attribute.
    # \return a single list of ids.
    def __intersection_id(self):
        
        ls_itrsec = self.__list_id(self.ls_data[0])
        
        for i in xrange(1, self.int_num_ranks):
            ls_tmp = self.__list_id(self.ls_data[i])                
            ls_itrsec = list(set(ls_itrsec).intersection(ls_tmp))
        
        return ls_itrsec

    # \fn __union_id
    # This method makes the union of the ranked lists in the ls_data attribute.
    # \return a single list of ids.
    def __union_id(self):
        
        ls_union = self.__list_id(self.ls_data[0])
        
        for i in xrange(1, self.int_num_ranks):
            ls_tmp = self.__list_id(self.ls_data[i])                
            ls_union = list(set(ls_union).union(ls_tmp))
        
        return ls_union
    
    # \fn __resize_data
    # This method resizes the ranked lists in the ls_data attribute,
    # according to a defined percentage.
    # \param flo_perc is the percentage to be used for the resize procedure,
    # it has to be between 0 and 1.
    def __resize_data(self, flo_perc):
        
        self.size = int(round(len(self.ls_data[0]) * flo_perc))
        for i in xrange(self.int_num_ranks):
            self.ls_data[i] = self.ls_data[i][:self.size]
            
    # \fn set_percentage_intersection
    #  This method modifies the ls_data attribute, by intersecting just a
    # percentage of the objects in each ranked list.
    # \param flo_perc is the percentage to be used for the resize procedure,
    # it has to be between 0 and 1.
    def set_percentage_intersection(self, flo_perc):
        
        if flo_perc == 1.0:
            self.size = len(self.ls_data[0])
            
        else:
            self.__resize_data(flo_perc)
            ls_itrsec = self.__intersection_id()
            if len(ls_itrsec) == 0:
                raise Exception("There is not intersection between "
                                "the ranked lists with this percentage.")
            
            for i in xrange(self.int_num_ranks):
                current_list_id = self.__list_id(self.ls_data[i])
                ls_id = list(set(current_list_id).difference(ls_itrsec))
                ls_tmp = self.ls_data[i] 
                
                for str_id in ls_id:
                    for dc_j in ls_tmp:
                        
                        if dc_j.get('id') == str_id:
                            self.ls_data[i].remove(dc_j)
                            break
                    ls_tmp = self.ls_data[i]
                    
                k = 1
                for dc_i in self.ls_data[i]:
                    dc_i['rank'] = k
                    k += 1
            
            self.size = len(self.ls_data[0])
        
    # \fn set_percentage_union
    # This method modifies the ls_data attribute, by making the union of
    # just a percentage of the objects in each ranked list.
    # \param flo_perc is the percentage to be used for the resize procedure,
    # it has to be between 0 and 1.
    def set_percentage_union(self, flo_perc):
        
        if flo_perc == 1.0:
            self.size = len(self.ls_data[0])
        
        else:
            ls_data_cpy = list(self.ls_data)
            
            self.__resize_data(flo_perc)
            ls_union = self.__union_id()
            
            for i in xrange(self.int_num_ranks):
                current_list_id = self.__list_id(self.ls_data[i])
                ls_id = list(set(ls_union).difference(current_list_id))

                for str_id in ls_id:
                    for dc_j in ls_data_cpy[i]:
                        
                        if dc_j.get('id') == str_id:
                            self.ls_data[i].append(dc_j)
                            break
            
            self.size = len(self.ls_data[0])
