# pyplay
collection of useful python utilities, e.g. json path-based object mapper for dictionary and list

---
## mapByJsonPath(src, des, spath, dpath, fns, default=None)
 <pre>
given two dictionary and json path, map one to the other
 src: source dictionary
 des: destination dictionary
 spath: source json path
 dpath: destination json path
 fns: list of functions to transform the source value
 default: default value if source value is None
 
 Usage:
  import dictutils as mapper
  mapper.mapByJsonPath(dic, des, 'morefoo.morebar.bacon.bla', 'spam.des.df', [str.upper, str.split, '_'.join])
 </pre>
 
## getByJsonPath(src, path)
<pre>
given a dictionary and json path, return the value
 src: source dictionary
 path: json path
</pre> 

## mapListByJsonPath(src, des, spath, dpath, fns=None):
 <pre>
 Map a list inside dictionary to a list in another dictionary
  src: source dictionary
  des: destination dictionary
  spath: source json path
  dpath: destination json path
  fns: list of functions to transform the source value 
 </pre>

## mapTo(src, des, mapping)
<pre>
given two dictionary and a dictionary contains key-value pairs of json path, map one to the other
 src: source dictionary
 des: destination dictionary
 mapping: a dictionary contains k-v pairs of source json path and destination json path
 
 Usage:
  import dictutils as mapper
  mapper.mapTo(dic, des, {'morefoo.morebar.bacon.bla': {'value':'spam.des.df', 'fns': [str.upper, str.split, '_'.join], 'default': 'FUND_MANAGER'})
 </pre>
