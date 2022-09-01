import os
folders = ["asset","css","js"]

projectName = input("Project Name: ")
html_files ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/index.css"/>

    <title>"""+projectName+"""</title>
</head>
<body>
    
        <script type="text/javascript" src="./js/index.js"></script>
</body>
</html>
"""
def CreateThePro(name):
        try:
                os.mkdir(name)
                for folder in folders:
                    os.mkdir(name+"/"+folder)
                open(name+"/js/index.js", "w")
                open(name+"/css/index.css", "w")
                with open(projectName+"/index.html", "w") as f:
                   f.write(html_files)
                try:   
                   os.system("code ./"+name)
                except:
                    print("Error in vscode")
        except:
            print("Project Name already exists: " + name)


CreateThePro(projectName)
