#git status
#aby zapisać 2 korki:
#1 git add[nazwa pliku] 
#2 git commit + -m[wiadomość]
#git log - historia commitów
#git push origin main

#git checkout - pozwala na przełączanie się miedzy branchami

from flask import Flask

app = Flask(__name__)

if __name__=="__main__":
    app.run(port=8080)