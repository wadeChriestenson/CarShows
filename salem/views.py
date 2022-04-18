from django.shortcuts import render, redirect
import plotly.graph_objects as go
from plotly.offline import plot
from datetime import date



# Create your views here.
from salem.forms import setupMeetInfo


def dataInput(request):
    import psycopg2
    conn = psycopg2.connect(
        host="<Default>",
        database="<Default>",
        user="<Default>",
        password="<Default>")
    cur = conn.cursor()
    # execute a statement
    print('Connected PostgreSQL')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = setupMeetInfo(request.POST)
        lat = form['latitude'].value()
        long = form['longitude'].value()
        hostName = form['host_name'].value()
        meetPlace = form['meet_place'].value()
        meetAddress = form['meet_address'].value()
        meetDescription = form['meet_description'].value()
        meetDate = form['meet_date'].value()
        startTime = form['start_time'].value()
        endTime = form['end_time'].value()
        enthusiastType = form['enthusiast_type'].value()
        latitude = lat
        longitude = long

        meetinfo = """INSERT INTO salem_meetinfo(
            latitude,
            longitude,
            host_name,
            meet_place,
            meet_address,
            meet_description,
            meet_date,
            start_time,
            end_time,
            enthusiast_type)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        meet = (
            latitude,
            longitude,
            hostName,
            meetPlace,
            meetAddress,
            meetDescription,
            meetDate,
            startTime,
            endTime,
            enthusiastType)
        cur.execute(meetinfo, meet)
        conn.commit()
        # close communication with the database
        cur.close()
        conn.close()
        response = redirect('/')
        return response


def carMeet(request):
    import psycopg2
    today = date.today()
    d1 = today.strftime("%Y%m%d")
    print(d1)
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    print(year,'-',month,'-',day)
    conn = psycopg2.connect(
        host="<Default>",
        database="<Default>",
        user="<Default>",
        password="<Default>")
    cur = conn.cursor()
    # execute a statement
    type = """SELECT meet_date FROM salem_meetinfo"""
    cur.execute(type)
    types = cur.fetchall()
    for x in types:
        print(x)
    print('Connected PostgreSQL')
    getMeets = f"""SELECT * 
    FROM salem_meetinfo 
    ORDER BY meet_date"""
    cur.execute(getMeets)
    meets = cur.fetchall()
    allMeetsMaps = []
    allMeetsMeta = []
    for x in meets:
        # print(x)

        mapbox_access_token = '<Default>'

        meet_meta = {
            'latitude': x[1],
            'longitude': x[2],
            'locationName': x[4],
            'address': x[5],
            'hostName': x[3],
            'date': x[7],
            'startTime': x[8],
            'endTime': x[9],
            'type': x[10],
            'desc': x[6]
        }

        meet = go.Figure(go.Scattermapbox(
            lat=[meet_meta['latitude']],
            lon=[meet_meta['longitude']],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=25
            ),
            text=meet_meta['locationName'],
        ))

        meet.update_layout(
            autosize=True,
            hovermode='closest',
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=5,
                center=dict(
                    lat=meet_meta['latitude'],
                    lon=meet_meta['longitude']
                ),
                pitch=0,
                zoom=14,
                style='streets',
            ),
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0,
                # pad=4
            ),
        )

        allMeetsMeta.append(meet_meta)

        allMeetsMaps.append(plot(meet,
                                 output_type='div',
                                 include_plotlyjs=False))
        # print(allMeetsMaps)

    cur.close()
    conn.close()
    return render(request, 'carmeets.html', {
        'meet_Map': allMeetsMaps,
        'meet_Info': allMeetsMeta,
    })


def setup(request):
    from .forms import setupMeetInfo
    setupMeetInfo = setupMeetInfo()
    return render(request, 'setup.html', {'form': setupMeetInfo})


def aboutus(request):
    aboutus = 'This site is dedicated to helping ' \
              'car enthusiast organize and manage local, safe and respectable ' \
              'car meets. We are decicated to keep the car culture respectable in the community. ' \
              'By giving the enthusiast a place to organize and plan ahead of time. '
    email = 'mailto:salemcarmeet@gmail.com'
    return render(request, 'aboutus.html', {'aboutus': aboutus, 'email': email})


def disclaimer(request):
    return render(request, 'disclaimer.html')
