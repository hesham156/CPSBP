import os
folders = ["asset","css","js"]

projectName = input("Project Name: ")
def html_files(proname) :
 return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/index.css"/>

    <title>"""+proname+"""</title>
</head>
<body>
    
        <script type="text/javascript" src="./js/index.js"></script>
</body>
</html>
"""
def createFile(path):
    return open(path,"w")
def errormsg(msg):
    print(msg)
def CreateThePro(name):
    if os.path.exists(name):
       errormsg("Project Name already exists: " + name)
       Name = input("Project Name: ")
       CreateThePro(Name)

    else:
                os.mkdir(name)
                for folder in folders:
                    os.mkdir(name+"/"+folder)
                createFile(name+"/js/index.js")
                createFile(name+"/css/index.css")
                with createFile(name+"/index.html") as f:
                   f.write(html_files(name))
                try:   
                   os.system("code ./"+name)
                except:
                    errormsg("Error in vscode")
 

CreateThePro(projectName)
