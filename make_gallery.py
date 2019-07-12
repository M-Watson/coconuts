import os

head = '''
<head>
</head>

'''


startdir = './'  #Starting Directory

with open("output.html",'w') as f:
    f.write("{}".format(head))
    f.close()

subfolders = [f.path for f in os.scandir(startdir) if f.is_dir() ]
master_file_list = []

#Writes out a header and 3 images for preview
for folder in subfolders:
    with open("output.html",'a') as f:
        #f.write("<h1>{}</h1>\n<ul>".format(folder))
        f.write("<h1>{}</h1>\n".format(folder))
        f.close()
    file_list = [f.path for f in os.scandir(folder)]
    i = 0
    for file in file_list:
        file_name = '{}'.format(file)
        file_name.replace(".\\","/")
        master_file_list.append(file_name)
        if i < 3:
            i+=1
            with open('output.html','a') as f:
                # IF I WANT LIST -  f.write("<li><img src=\"{}\" height=100px/></li>\n".format(file_name))
                f.write("<a href = \"individuals\\{}.html\"><img src=\"{}\" style=\"height:40%;max-width:30%; \"/></a>\n".format(folder,file_name))
                f.close()
        else:
            break

    for folder in subfolders:
        with open("individuals/{}.html".format(folder),'w') as f:
            individ_head = '''
            <head>
            <style>

            input[type="checkbox"][id^="cb"] {
              display: none;
            }

            label {
              border: 1px solid #fff;
              cursor: pointer;
              -webkit-touch-callout: none;
              -webkit-user-select: none;
              -khtml-user-select: none;
              -moz-user-select: none;
              -ms-user-select: none;
              user-select: none;
            }

            label::before {
              background-color: white;
              color: white;
              content: " ";
              transition-duration: 0.4s;
              transform: scale(0);
            }

            label img {
              height: 30%;
              transition-duration: 0.2s;
              transform-origin: 50% 50%;
            }

            :checked+label {
              border-color: white;
            }

            :checked+label::before {
              background-color: grey;
              transform: scale(1);
            }

            :checked+label img {
              height:90%;
              box-shadow: 0 0 5px #333;

              margin-top:10%;
              margin-left:10%;

            }
            </style>
            </head>
            '''
            f.write(individ_head)
            f.close()
        with open("individuals/{}.html".format(folder),'a') as f:
            #f.write("<h1>{}</h1>\n<ul>".format(folder))
            f.write("<h1>{}</h1>\n<div style=\"width:80%;margin-left:10%;\">".format(folder))
            f.close()
        file_list = [f.path for f in os.scandir(folder)]
        file_index = 0
        for file in file_list:
            file_index +=1
            file_name = '..\\{}'.format(file)
            file_name.replace(".\\","/")
            master_file_list.append(file_name)
            with open("individuals/{}.html".format(folder),'a') as f:
                # IF I WANT LIST -  f.write("<li><img src=\"{}\" height=100px/></li>\n".format(file_name))
                indiv_output = '''
                <input type="checkbox" id="cb{}" />
                    <label for="cb{}"><img src="{}" /></label>

                  '''.format(file_index,file_index,file_name)
                f.write(indiv_output)
                f.close()
        with open("individuals/{}.html".format(folder),'a') as f:
            #f.write("<h1>{}</h1>\n<ul>".format(folder))
            f.write("</div>")
            f.close()
