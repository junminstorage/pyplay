'''
Created on Mar 14, 2016

@author: junminliu
'''
import unittest

import dictutils as mapper

class TestDictUtils(unittest.TestCase):


    def test_getbyJsonPath(self):
        dic = {
               'spam':'eggs',
               'morefoo': [{
                        'bar':'soap',
                        'morebar': {
                                    'bacon' : {
                                               'bla':'balbla'
                                     }
                        }
                        },
                       'bla'
                ],
               'test': {'ert': 'et', 'test': {'test': 1}}   
           }
        path = 'morefoo.1.bar'
        self.assertEqual(mapper.getByJsonPath(dic, path), None)
        path = 'morefoo.0.bar'
        self.assertEqual(mapper.getByJsonPath(dic, path), 'soap')
        path = 'test.ert'
        self.assertEqual(mapper.getByJsonPath(dic, path), 'et')
        path = 'test.test.test'
        self.assertEqual(mapper.getByJsonPath(dic, path), 1)
    
    def test_mapByJsonPath(self):
        dic = {
               'spam':'eggs',
               'morefoo': {
                        'bar':'soap',
                        'morebar': {
                                    'bacon' : {
                                               'bla':'balbla'
                                     }
                        }
                },
               'test': {'ert': 'et', 'test': {'test': 1}}   
        }
        des = {}
        mapper.mapByJsonPath(dic, des, 'morefoo.morebar.bacon.bla', 'spam.des.df', [str.upper, str.split, '_'.join])
        self.assertEquals(des['spam']['des']['df'],  'BALBLA')
        des2 = {}
        mapper.mapByJsonPath(dic, des2, 'morefoo.morebar.bacon.non_exist', 'spam.des.df', [str.upper, str.split, '_'.join])
        self.assertEquals(des2['spam']['des']['df'],  None)
        
    def test_mapBy(self):
        
        def splitdash(astr):
            return astr.split('-')
        
        dic = {
           'spam':'eggs fdsf',
           'morefoo': {
               'bar':'soap',
               'morebar': {
                           'bacon' : {
                                       'bla':'bal-bla'
                                     }
                           }       
            },
            'test': {'ert': 'et'}  
           }
    
        mapping = {'morefoo.morebar.bacon.bla' : 
                   {'value':'spam.des.df', 'fns':[str.upper, splitdash, '_'.join]},
                   'morefoo.bar' : 'spam.de',
                   'spam' : {'value':'spam.ds', 'fns':[str.upper, str.split, '_'.join]}
                   }    
        
        des = mapper.mapBy(dic, mapping)
        
        self.assertEquals(des['spam']['de'],  'soap')
        self.assertEquals(des['spam']['des']['df'],  'BAL_BLA')
        self.assertEquals(des['spam']['ds'],  'EGGS_FDSF')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()