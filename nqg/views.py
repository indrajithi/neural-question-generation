from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import NameForm
from .forms import UploadFileForm

import re
import os

def handle_uploaded_file(f):
    with open('input.txt', 'wb+') as inptfile:
        for chunk in f.chunks():
            inptfile.write(chunk)  
    try:
        open('gendata/snt.txt','w').close()
        open('gendata/par.txt','w').close()

    except Exception as e:
        print("Error in clearning data from 'gendata': No data cleared:")

    with open('input.txt','r') as infile:
        for line in infile:
            if line == '\n':
                pass

            
            par = ""
            snt = ""

            par =  re.sub(r'[^\x00-\x7F]+',' ', line) 

            if par[-1] != '\n':
                par = par + '\n'

            snt =  par.replace(".",".\n")
            snt = snt.replace("\n ", "\n")
            if snt[-1] == '\n':
                snt = snt[:-1]

            n = snt.count('\n') 
            
                
            with open('gendata/snt.txt','a') as f_snt:
                f_snt.writelines(snt)
            with open('gendata/par.txt', 'a') as f_par:
                for i in range(n):
                    f_par.writelines(par)

        os.system('./script.sh')

        quest_out = []
        with open('gendata/quest.txt', 'r') as f_par:
            for line in f_par:
                quest_out.append(line) 


        return quest_out



def index(request):
    form = NameForm()
    print("index workig.........................................................................")
    return HttpResponse(render(request,'input.html',{'form': form}))


def genrate_files(in_txt):

    try:
        open('gendata/snt.txt','w').close()
        open('gendata/par.txt','w').close()

    except Exception as e:
        print("Error in clearning data from 'gendata': No data cleared:")


    for line in in_txt.split('\n'):
        if line in ('\n',' '):
            pass

        if line[-1] != '.':
            line = line +'.'
        
        par = ""
        snt = ""

        par =  re.sub(r'[^\x00-\x7F]+',' ', line) 

        if par[-1] != '\n':
            par = par + '\n'

        snt =  par.replace(".",".\n")
        snt = snt.replace("\n ", "\n")
        if snt[-1] == '\n':
            snt = snt[:-1]

        n = snt.count('\n') 
        
            
        with open('gendata/snt.txt','a') as f_snt:
            f_snt.writelines(snt)
        with open('gendata/par.txt', 'a') as f_par:
            for i in range(n):
                f_par.writelines(par)



def get_name_par(request):
    # if this is a POST request we need to process the form data
    newform = NameForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        genrate_files(form['textin'].value())
        print(os.system('./script2.sh'))

        quest_out = []
        with open('gendata/quest.txt', 'r') as f_par:
            for line in f_par:
                quest_out.append(line) 


        return render(request, 'output2.html', {'questions': quest_out,'paragraph': form['textin'].value()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        uploadform =  UploadFileForm()


    return HttpResponse(render(request,'input2.html',{'form': newform,'uploadform': uploadform}))

def get_name(request):
    # if this is a POST request we need to process the form data
    newform = NameForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        genrate_files(form['textin'].value())
        print(os.system('./script.sh'))

        quest_out = []
        with open('gendata/quest.txt', 'r') as f_par:
            for line in f_par:
                quest_out.append(line) 


        return render(request, 'output.html', {'questions': quest_out,'paragraph': form['textin'].value()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        uploadform =  UploadFileForm()
       

    return HttpResponse(render(request,'input.html',{'form': newform,'uploadform': uploadform}))

def upload_fle(request):


    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            quest_out = handle_uploaded_file(request.FILES['file'])

            with open('gendata/snt.txt','r') as file:
                file_content = file.read()     

            return HttpResponse(render(request, 'output.html', {'questions': quest_out ,'paragraph': file_content}))
    else:

        form = UploadFileForm()
    return HttpResponseRedirect('/nqg')
