from django.shortcuts import render
#from .models import Question
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
import pandas as pd

def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 'Home Page'}
    return render(request, 'polls/index.html', context)

import csv
from django.http import HttpResponse

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="CSVtesting.csv"'

    writer = csv.writer(response)
#    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Week Index','Year','Location Name', 'Pad Type','Week Start Date','Week End Date','week of year Original','Pad Requirement Count', 'Total Orders Count','LinearFeet','Rolls','Pad to be Ordered'])
    df_raw = pd.read_csv("C:/Users/Divya Mereddy/OneDrive - United Installs, LLC/Python Scripts/DataSets/Sprint2/Pad_Counts_Perweek.csv",index_col=0)
#    print(df_raw)
    for LAB,ROW  in df_raw.iterrows():
        writer.writerow([LAB,ROW['year'],ROW['Location_Name'],ROW['Pad_Type'],ROW['WeekStartDate'],ROW['WeekEndDate'],ROW['weekofyear_Original'],ROW['Pad_Requirement_Count'],ROW['PO#'],ROW['LinearFeet'],ROW['Rolls'],ROW['Order_quantity_perweeok']])
#        print(LAB,ROW[['Store #','Pad Type']])
#        writer.writerow(LAB)
#        context = {'response': response}
#    return render(request, 'polls/index.html', context)
    return response
#    return  HttpResponse('Please find attached pad requirement for next weeks')
def some_view1(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Pad_Counts.csv"'

    writer = csv.writer(response)
#    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Location Name','Name_Of_Pad','Current_Quantity', 'Ordered_Quantity','Required_Quantity','Pad_Count_To_Be_Ordered'])
    df_raw = pd.read_csv("C:/Users/Divya Mereddy/OneDrive - United Installs, LLC/Python Scripts/DataSets/Pad_Counts.csv",index_col=0)
#    print('Check',df_raw)
    df_raw=df_raw.fillna(0)
    for LAB,ROW  in df_raw.iterrows():
        writer.writerow([LAB,ROW['Name_Of_Pad'],ROW['Current_Quantity'],ROW['Ordered_Quantity'],ROW['Required_Quantity'],ROW['Pad_Count_To_Be_Ordered']])
#       print(LAB,ROW)
#        writer.writerow(LAB)
#        context = {'response': response}
#    return render(request, 'polls/index.html', context)
    return response
