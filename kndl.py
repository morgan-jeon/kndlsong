import requests

loginUrl = "https://kndl.kr/login"
commitUrl = "https://kndl.kr/kndl"

def login(id: str, pw: str, requ):
    param = {'id':id,'pw':pw}
    req = requ.post(loginUrl,headers={'referrer':'https://kndl.kr/login','Content-Type':'application/x-www-form-urlencoded'},data=param)
    # print(req.text)
    # print(req.cookies.get_dict())
    # print(req.headers)

def commitSong(song:str,artist:str,id:str,requ):
    songDict = {'youtube': id,'song': song,'singer':artist,'request': '3번째로부탁한다.'}
    req2 = requ.post(commitUrl,headers={'referrer':'https://kndl.kr/kndl','Content-Type':'application/x-www-form-urlencoded'},data=songDict)
    if "신청이 완료되었습니다." in req2.text:
        print("Complete")
    elif "이미 신청하셨습니다." in req2.text:
        print("Already Used")
    else:
        print("Error")
    # print(req2.cookies.get_dict())
    # print(req2.headers)
    
def routine(id, pw, youtubeid, song, artist):
    requ = requests.session()
    login(id, pw,requ)
    commitSong(song,artist,youtubeid,requ)

if __name__=="__main__":
    comdict = [
        {'id':'01097370653','pw':'k09280303','yt':'WNp_XLCOTBw'},
        {'id':'01074311015','pw':'1015','yt':'xOSmS2VEjpQ'}
        ]
    for c in comdict:
        routine(c['id'],c['pw'],c['yt'],'','')
