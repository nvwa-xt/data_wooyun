def getCodeStr(result):
    #gb2312
    try:
        myResult=result.decode('gb2312').encode('gbk','ignore')
        return myResult
    except:
        pass
    #utf-8
    try:
        myResult=result.decode('utf-8').encode('gbk','ignore')
        return myResult
    except:
            pass
 
    #unicode
    try:
        myResult=result.encode('gbk','ignore')
        return myResult
    except:
        pass
    #gbk
    try:
        myResult=result.decode('gbk').encode('gbk','ignore')
        return myResult
    except:
        pass
    #big5
    try:
        myResult=result.decode('big5').encode('gbk','ignore')
        return myResult
    except:
        pass
