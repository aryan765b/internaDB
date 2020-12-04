import urllib.request, json


addr = input("Enter the link shared to start the program: ")

def get_val(tag):
    with urllib.request.urlopen("{}get/{}".format(addr, tage.replace(".", '%20'))) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        try:
            return data[tag]
        except:
            return data['status']

def set_val(tag,val):
    with urllib.request.urlopen("{}setv/{}/{}".format(addr, tag.replace(" ","%20"), val.replace(" ","%20"))) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']


def create_tag(tag,val):
    with urllib.request.urlopen("{}create/{}/{}".format(addr, tag.replace(" ","%20"), val.replace(" ","%20"))) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']


def get_separatedw(tag,sepa):
    with urllib.request.urlopen("{}get_separeted/{}/{}".format(addr, tag.replace(" ",'%20'), sepa.replace(" ","%20"))) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data[tag]


def getlinenum(tag):
    with urllib.request.urlopen("{}getlinenumber/{}".format(addr, tag.replace(" ",'%20'))) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data[tag]


def crenge(tag,val):
    with urllib.request.urlopen("{}creange/{}/{}".format(addr, tag.replace(" ","%20"), val.replace(" ","%20"))) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']


def deltag(tag):
    with urllib.request.urlopen("{}delete_tag/{}".format(addr, tag.replace(" ","%20"))) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']


def istag(tag):
    with urllib.request.urlopen(addr+"istagr/"+tag.replace(" ","%20")) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data[f"{tag} existance"]


def deletealldata(password):
    with urllib.request.urlopen(addr+"deletealldata/"+password.replace(" ","%20")) as url:
        password = password.replace("%20"," ")
        data = json.loads(url.read().decode())
        return data['status']


def get_list(tag):
    with urllib.request.urlopen(addr+"get_list/"+tag.replace(" ",'%20')) as url:
        tag = tag.replace("%20"," ")
        data = json.loads(url.read().decode())
        try:
            return data["got"]
        except:
            return data['status']

print(get_list("ok google")[-1])
