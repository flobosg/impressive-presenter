from sys import argv
from pyPdf import PdfFileReader
from os import path

filename = argv[1]

document = PdfFileReader(file(filename, "rb"))
pages = document.getNumPages()

with open(filename+".info", 'w') as out:
    path = path.dirname(filename)
    if path:
        path = path + '/'
    out.write("""import json

def UpdateInfo():
    global FileName, FileList, PageCount
    global DocumentTitle
    global Pcurrent, Pnext, Tcurrent, Tnext, InitialPage
    global RTrunning, RTrestart, StartTime, PageEnterTime, CurrentTime

    with open('"""+path+"""json.txt', 'w') as io:
        json.dump(({"page_count": PageCount, "current_page": Pcurrent, "previous_page": Pnext, "start_time": StartTime, "pageenter_time": PageEnterTime, "current_time": CurrentTime, "notes": PageProps[Pcurrent]['notes']}), io)

PageProps = {
""")

    for i in range(1,pages + 1):
        if i < pages:
            out.write("    "+str(i)+": {\n        'transition': None,\n        'overview': True,\n        'notes': '',\n        'OnEnter': UpdateInfo\n    },\n")
        else:
            out.write("    "+str(i)+": {\n        'transition': None,\n        'overview': True,\n        'notes': '',\n        'OnEnter': UpdateInfo\n    }\n}")
