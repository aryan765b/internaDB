import urllib.request, json 
addr = input("enter the link shared to start the progtram")
def get_val(tag):
    with urllib.request.urlopen(addr+"get/"+tag.replace(" ",'%20')) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        try:
            return data[tag]
        except:
            return data['status']
# print(get_val("ok%20google"))
def set_val(tag,val):
    with urllib.request.urlopen(addr+"setv/"+tag.replace(" ","%20")+"/"+val.replace(" ","%20")) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']
# print(set_val("ok google","hello google"))
def create_tag(tag,val):
    with urllib.request.urlopen(addr+"create/"+tag.replace(" ","%20")+"/"+val.replace(" ","%20")) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']
def get_separatedw(tag,sepa):
    with urllib.request.urlopen(addr+"get_separeted/"+tag.replace(" ",'%20')+"/"+sepa.replace(" ","%20")) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data[tag]
# print(get_separatedw("tag"," is "))
def getlinenum(tag):
    with urllib.request.urlopen(addr+"getlinenumber/"+tag.replace(" ",'%20')) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data[tag]
# print(getlinenum("ag"))
def crenge(tag,val):
    with urllib.request.urlopen(addr+"creange/"+tag.replace(" ","%20")+"/"+val.replace(" ","%20")) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']
# print(crenge("ag","ij"))
def deltag(tag):
    with urllib.request.urlopen(addr+"delete_tag/"+tag.replace(" ","%20")) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']
# print(deltag("ok google"))
# crenge("ok google","hi")
def istag(tag):
    with urllib.request.urlopen(addr+"istagr/"+tag.replace(" ","%20")) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data[f"{tag} existance"]
# print(istag("ok google"))
def deletealldata(password):
    with urllib.request.urlopen(addr+"deletealldata/"+password.replace(" ","%20")) as url:
        password = password.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']
# print(deletealldata("2007"))
def get_list(tag):
    with urllib.request.urlopen(addr+"get_list/"+tag.replace(" ",'%20')) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        try:
            return data["got"]
        except:
            return data['status']
# print(get_val("ok%20google"))
# create_tag("ok google","[1,2.0,'3','hello']")
print(get_list("ok google")[-1])
