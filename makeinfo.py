from sys import argv
from pyPdf import PdfFileReader
from os import path

filename = argv[1]

document = PdfFileReader(file(filename, "rb"))
pages = document.getNumPages()

with open(filename+".info", 'w') as out:
    out.write("""import json

    def UpdateInfo():
        global FileName, FileList, PageCount
        global DocumentTitle
        global Pcurrent, Pnext, Tcurrent, Tnext, InitialPage
        global RTrunning, RTrestart, StartTime, PageEnterTime, CurrentTime

        io = open('"""+path.dirname(filename)+"""./json.txt', 'w')
        json.dump(({"page_count": PageCount, "current_page": Pcurrent, "previous_page": Pnext, "start_time": StartTime, "pageenter_time": PageEnterTime, "current_time": CurrentTime, "notes": PageProps[Pcurrent]['notes']}), io)
        io.close()

    PageProps = {
    """)

    for i in range(1,pages + 1):
        if i < pages:
            out.write("\t"+str(i)+": {\n\t\t'transition': None,\n\t\t'overview': True,\n\t\t'notes': '',\n\t\t'OnEnter': UpdateInfo\n\t},\n")
        else:
            out.write("\t"+str(i)+": {\n\t\t'transition': None,\n\t\t'overview': True,\n\t\t'notes': '',\n\t\t'OnEnter': UpdateInfo\n\t}\n}")