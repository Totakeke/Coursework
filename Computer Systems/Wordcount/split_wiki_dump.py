import os
import bz2
import sys

def split_xml(filename):
    ''' The function gets the filename of wiktionary.xml.bz2 file as  input and creates
    smallers chunks of it in a the diretory chunks
    '''
    chunk_size = 134217728 #128MB
    # Check and create chunk diretory
    if not os.path.exists("chunks"):
        os.mkdir("chunks")
    # Counters
    pagecount = 0
    filecount = 1
    #open chunkfile in write mode
    chunkname = lambda filecount: os.path.join("chunks","chunk-"+str(filecount)+".xml")
    chunkfile = open(chunkname(filecount), 'w+')
    # Read line by line
    bzfile = bz2.BZ2File(filename)
    buf_file = open('temp.xml','w+') # A temporary buffer file
    for line in bzfile:
        buf_file.write(line)
        # the </page> determines new wiki page
        if '</page>' in line:
            if chunkfile.tell() + buf_file.tell() >= chunk_size:
                #print chunkname() # For Debugging
                print 'Filename: ' + chunkname(filecount) + ', page count: ' + str(pagecount) + ', Total size: ' + str(os.stat(chunkname(filecount)).st_size/1048576) + ', # files: ' + str(filecount)
                chunkfile.close()
                pagecount = 0 # RESET pagecount
                filecount += 1 # increment filename           
                chunkfile = open(chunkname(filecount), 'w+')
            pagecount += 1
            buf_file.seek(0) 
            chunkfile.write(buf_file.read())
            buf_file.close()
            os.remove('temp.xml')
            buf_file = open('temp.xml','w+')
           
    try:
        chunkfile.close()
    except:
        print 'Files already close'

if __name__ == '__main__':
    # When the script is self run
    split_xml(sys.argv[1])
