import dropbox
class Transferdata:
    def __init__(self,accesstoken):
       self.accesstoken=accesstoken

    def uploadfile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        with open(filefrom,'rb') as f:
            dbx.files_upload(f.read(),fileto)
def main():
    accesstoken='nxfu-ttBwOIAAAAAAAAAAQVl0ngpCGeKxTHrYV3q4DWQ1KrRaFg1Nq_ASE1wpzvZ'
    transferdata=Transferdata(accesstoken)

    filefrom=input("Enter the file path to transfer")
    fileto=input("Enter the full path to upload to dropbox")
    transferdata.uploadfile(filefrom,fileto)
    print("file has been moved")
main()                   