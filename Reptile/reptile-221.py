import requests
def main():
    '''url='http://www.4399dmw.com/search/dh-7-0-0-0-0-{}-0/'
    url_list=[]
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    # url_list.append(url.format(i))#print(url_list)

    proxies={'HTTP':'121.232.148.223:9000'}  #加载代理
    url=url.format(1)'''
    '''for i in range(14):
        url_change=url.format(i)
        print(url_change)'''
    '''print(url)
    resp=requests.get(url=url,headers=headers,proxies=proxies)
    with open('a'+'.txt','wb+') as f:
            f.write(resp.content)'''


    url='http://sqlilabs.njhack.xyz/Less-20/index.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    data={"uname":"admin","passwd":"admin"}
    session=requests.session()
    session.post(url=url, headers=headers, data=data) #此时已经有cookie在里面
    #resp=session.post(url=url,headers=headers,data=data)
    res=session.get(url,headers=headers)
    print(res.content.decode("utf-8"))

if __name__=="__main__":
    main()