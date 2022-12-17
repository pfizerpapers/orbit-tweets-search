from django.shortcuts import render
from .forms import FullSearchForm
from .scripts import formatDates,getTweetsFullArchive,exportExcelFile
from django.contrib import messages
# Create your views here.
def index(request):
    if(request.method == 'POST'):
        form = FullSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['Query']
            lang = form.cleaned_data['Lang']
            print(lang)
            date1 = form.cleaned_data['Date1']
            date2 = form.cleaned_data['Date2']            
            fromDate, toDate = formatDates(date1,date2)
            
            df_output = getTweetsFullArchive(query,lang, fromDate, toDate)
            
            if df_output.empty:
                print('a consulta não retornou nenhum registro!')   
                messages.add_message(request, messages.WARNING, 'A consulta não retornou nenhum registro')             
            else:                
                res = exportExcelFile(df_output)
                return res
    else:
        form = FullSearchForm()
    
    return render(request, 'fullsearch.html', {"form": form})
    
