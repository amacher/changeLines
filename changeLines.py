import os

#where to read files from, replace 'C:...' with our path
directory = r'C:...'
#where to save the files, replace 'C:...' with our path
saveTo = 'C:...'

###Create Directory if doesn't exist
isDir = os.path.isdir(saveTo)
if isDir == False:
    os.mkdir(saveTo)
    print('Dir. Created')

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        with open(os.path.join(directory, filename)) as f:
            lines = f.readlines()

##PROCESS THE COPY
        with open(os.path.join(saveTo, filename), 'w', encoding="utf-8") as f:
            for line in lines:
                #Replace whole copyright line to include the code to auto update the year
                if line.startswith('<div class="column2"><p>&copy;1996 My Awesome Company</p>'):
                    line = '<div class="column2"><p>Copyright &copy; <script>document.write(new Date().getFullYear())</script> My Awesome Company LLC</p>'
                elif '<div class="column1"><p>123 E. Awesome St., This Town' in line:
                    line = '<div class="column1"><p><a href="http://www.myawesomeco.com">My Awesome Company LLC</a></p>\n<p>123 E. Awesome St., This Town' 
                elif '<p>(123) 456-7890</p>' in line:
                    line = line + '<p><a href = "mailto: awesome@myawesomeco.com">email us</a></p>'
                #Replaces the old name to the new name; keeping to last in case it throws off other lines like the copyright
                elif 'My Awesome Company' in line:
                    line = line.replace('My Awesome Company', 'My Awesome Company LLC')
                #Change the kids page links to internet page
                elif '"kids.html"' in line:
                    line = line.replace('"kids.html"','"internet.html"')
                    line = line.replace('Kids Corner','Internet')
                f.write(line)
    #add extensions to anything you want to do a straight copy over; if you try for all, it will try to copy hidden files and fail
    elif filename.endswith((".css", ".js")):
        with open(os.path.join(directory, filename)) as f:
            lines = f.readlines()
        with open(os.path.join(saveTo, filename), 'w', encoding="utf-8") as f:
            for line in lines:
                f.write(line)  