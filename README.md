# pyplay
a collection of useful python utils 

- getByJsonPath
  given a dictionary and json path, return the value
  
- mapByJsonPath
  given two dictionary and json path, map one to the other

  <pre>
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
  </pre>
  
- mapListByJsonPath
  given two list inside two distionary, map one to the other based on json path
