import re
html = input('the html to validate:')


def isValidHtml(_html):
    balise = re.compile(r'<[^>]+>')
    balise = balise.findall(html)
    tmp = []
    ouvert = 0
    j=0
    for i in balise:
        j+=1
        i=str.removeprefix(i,"<")
        i=str.removesuffix(i,">")
        if not str.startswith(i,'/'):
            if i in tmp:
                ouvert +=1
                tmp.append(i)
            else:
                tmp.append(i)
                ouvert +=1
        else:
            i = str.removeprefix(i,"/")
            print(i)
            if i not in tmp:
                return False
            elif i in tmp and (len(tmp)%2 !=0 or len(tmp)==1) and len(balise) != j:
                return False
            else:
                tmp.append(i)
                ouvert-=1
    if ouvert == 0:
        return True
    else:
        return False
            


print(isValidHtml(html))