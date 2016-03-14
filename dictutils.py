'''
Created on Mar 13, 2016

@author: junminliu
'''

def mapBy(src={}, mapping={}):
    '''
    map src by a series of json path defined in the mapping dictionary
    '''
    des = {}
    for k,v in mapping.iteritems():
        if type(v) is dict:
            mapByJsonPath(src, des, k, v['value'], v['fns'])
        else:
            mapByJsonPath(src, des, k, v)  
    return des
        
def mapTo(src={}, des={}, mapping={}):
    '''
    map src to des dictionary by a series of json path defined in the mapping dictionary
    '''
    for k,v in mapping.iteritems():
        if type(v) is dict:
            mapByJsonPath(src, des, k, v['value'], v['fns'])
        else:
            mapByJsonPath(src, des, k, v)          

def mapByJsonPath(src, des, spath, dpath, fns = None):
    '''
    map src to des dictionary by json path
    '''
    srv = getByJsonPath(src, spath)
    
    elem = des
    try:
        xlist = dpath.split('.')
        length = len(xlist)
        '''
        loop through the path, initialize the dic if necessary
        '''
        for index in xrange(length-1):
            p = xlist[index] 
            if elem.get(p) is None:    
                elem[p] = {}
            elem = elem.get(p)
        if srv and fns and type(fns) is list:
            for fn in fns:
                srv = fn(srv)       
        elem[xlist[length-1]] = srv         
    except Exception as ex:
        print ex
        pass
    
    return elem


def mapListByJsonPath(src, des, spath, dpath, fns=None):
    '''
    map a list inside src dictionary to a list inside des By Json Path
    spath: xyz.abc.*.title
    dpath: klm.opq.*.name
    '''
    #go through src to find the first list element
    elem = src
    try:
        for x in spath.split("."):
            elem = elem.get(x)
            if type(elem) is list:
                break
    except Exception as ex:
        print ex
        return
    
    print elem
    
    #go through the dpath, initialize the des if necessary
    ele = des
    try:
        xlist = dpath.split('.')
        length = len(xlist)
        
        for index in xrange(length-1):
            p = xlist[index] 
            if p == '*':
                break
            if ele.get(p) is None:
                if index+1<length and xlist[index+1] == '*':
                    ele[p] = []
                else:    
                    ele[p] = {}
            ele = ele.get(p)
    except Exception as ex:
        print ex
        return
    
    print ele
    
    if type(elem) is not list or type(ele) is not list:
        print 'invalid input'
        return
    
    #convert each item in elem list to an item in ele
    length = len(elem)
    for index in xrange(length):
        val = getByJsonPath(src, spath.replace('*', str(index)))
        print val
        
        path = dpath.replace('*', str(index))
        el = des
        try:
            leng = len(path.split("."))
            counter = 0
            for x in path.split("."):
                counter = counter + 1
                print counter, leng
                if counter == leng:
                    print 'el {}'.format(el)
                    if val is not None and fns and type(fns) is list:
                        for fn in fns:
                            val = fn(val)
                    el[x] = val
                else:    
                    try:
                        x = int(x)
                    except ValueError:
                        pass
                    finally:
                        print 'x {} el type {}'.format(x, type(el))
                        try:
                            if el[x] is None:
                                el[x] = {}
                        except IndexError:
                            el.append({})    
                        el = el[x]    
        except Exception as ex:
            print ex
            pass
    
def getByJsonPath(dic, path):
    elem = dic
    try:
        for x in path.split("."):
            try:
                x = int(x)
                elem = elem[x]
            except ValueError:
                elem = elem.get(x)
    except:
        elem = None

    return elem
