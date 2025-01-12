import sys
import time
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from io import BytesIO
import urllib
from datetime import datetime, timedelta
# import streamlit as st
import docx

def main():

    # st.balloons()
    # st.title('Welcome🙏🏻')
    # st.header('Simply Ayurveda presents🌿')
    # st.subheader('Dainika Almanac🗓️')
    today = datetime.today()
    date1 = today.strftime("%d/%m/%Y")
    tomorrow = today + timedelta(1)
    formatted_date = tomorrow.strftime("%d/%m/%Y")
    # formatted_date = datetime.today().strftime("%d/%m/%Y")
    # st.write(f"Today's Almanac📝: {formatted_date}")
    
    nakshatras = ["Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishtha", "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"]
    
    tithidinas = {"Pratipada": "1",
                  "Dwitiya":"2",
                  "Tritiya":"3",
                  "Chaturthi":"4",
                  "Panchami":"5",
                  "Shashthi":"6",
                  "Saptami":"7",
                  "Ashtami":"8",
                  "Navami":"9",
                  "Dashami":"10",
                  "Ekadashi":"11",
                  "Dwadashi":"12",
                  "Trayodashi":"13",
                  "Chaturdashi":"14",
                  "Purnima":"Full moon",
                  "Amavasya":"New moon"}
    
    chakravara = {"Sunday":"Manipura, Sahasrara",
                  "Monday":"Svadishtana, Ajna",
                  "Tuesday":"Manipura",
                  "Wednesday":"Anahata, Vishudha",
                  "Thursday":"Vishudha, Ajna",
                  "Friday":"Svadishtana, Anahata, Ajna",
                  "Saturday":"Mooladhara"}
    
    docfile = "https://docs.google.com/document/d/1xwy3aN2VSTTAw0Z7chr36PELaf8a4Mv0Gy2snZ0YAas/export?format=docx"
    response = requests.get(docfile)
    with open("temp.docx", "wb") as temp_file:
        temp_file.write(response.content)
    doc = docx.Document("temp.docx")
    fullText = []
    for para in doc.paragraphs:
        lines = para.text.splitlines()  # Split paragraph into lines
        fullText.extend(lines)
    
    sheet_url = "https://docs.google.com/spreadsheets/d/1W_CG0CD7j7yFBB5W8DDdLSA2dyztyAQ9Pn03RPcAbyY/export?format=csv"
    response = requests.get(sheet_url)
    df = pd.read_csv(BytesIO(response.content))
    df.to_csv('sudhakalavishakala.csv', index = False)
    dd = pd.read_csv('sudhakalavishakala.csv')
    
    page=requests.get('https://www.drikpanchang.com/panchang/day-panchang.html?geoname-id=1277333&date='+formatted_date)
    
    soup=BeautifulSoup(page.text,'html.parser')
    #res = dd.loc[df['Date'] == date1]
    l12 = soup.find('div',class_='dpPHeaderRightContent')
    a1 = {}
    a1['Weekday'] = l12.span.text
    l1 = soup.find('h2',class_='dpPageShortTitle')
    a={}
    a['Date'] = l1.text
    
    page1=requests.get('https://www.drikpanchang.com/malayalam/panchangam/malayalam-day-panchangam.html?geoname-id=1277333&date='+formatted_date)
    
    soup1=BeautifulSoup(page1.text,'html.parser')
    kollamera_element = soup1.find('div', text=lambda t: 'Kollam Era' in t if t else False)
    l121 = soup1.find('div',class_='dpPHeaderLeftTitle')
    kollamdate = l121.text

    page2=requests.get('https://www.drikpanchang.com/kannada/panchangam/kannada-day-panchangam.html?geoname-id=1277333&date='+formatted_date)
    
    soup2=BeautifulSoup(page2.text,'html.parser')
    masa_element = soup2.find('div',class_='dpPHeaderLeftTitle')
    Masa = masa_element.text
    # print(Masa)
    Kollamera = kollamdate+", "+kollamera_element.text[:4]
    # print(Kollamera)
    l13 = soup.find('div',class_='dpPHeaderEventList')
    c={}
    c['Significance'] = l13.text.replace("\xa0","")
    l2 = soup.find('div',class_='dpSunriseMoonriseCardWrapper').find_all('div',class_='dpTableCell')
    d={}
    for i,j in zip(range(0,len(l2), 4), range(1, len(l2),4)):
      if l2[i].text!='' and l2[i].text!=' ':
        temp = l2[i].text
        d[temp] = l2[j].text.replace("ⓘ","")
      else:
        d[temp] = d[temp] + " " + l2[j].text.replace("ⓘ","")
    f={}
    for i,j in zip(range(2,len(l2), 4), range(3, len(l2),4)):
      if l2[i].text!='' and l2[i].text!=' ':
        temp = l2[i].text
        f[temp] = l2[j].text.replace("ⓘ","")
      else:
        f[temp] = f[temp] + " " + l2[j].text.replace("ⓘ","")
    l3 = soup.find('div',class_='dpCorePanchangCardWrapper').find_all('div',class_='dpTableCell')
    e={}
    for i,j in zip(range(0,len(l3), 4), range(1, len(l3),4)):
      if l3[i].text!='' and l3[i].text!=' ':
        temp = l3[i].text
        e[temp] = l3[j].text.replace("ⓘ","")
      else:
        e[temp] = e[temp] + " " + l3[j].text.replace("ⓘ","")
    g={}
    for i,j in zip(range(2,len(l3), 4), range(3, len(l3),4)):
      if l3[i].text!='' and l3[i].text!=' ':
        temp = l3[i].text
        g[temp] = l3[j].text.replace("ⓘ","")
      else:
        g[temp] = g[temp] + " " + l3[j].text.replace("ⓘ","")
    l4 = soup.find('div',class_='dpLunarDateCardWrapper').find_all('div',class_='dpTableCell')
    h={}
    for i,j in zip(range(0,len(l4), 4), range(1, len(l4),4)):
      if l4[i].text!='' and l4[i].text!=' ':
        temp = l4[i].text
        h[temp] = l4[j].text.replace("ⓘ","")
      else:
        h[temp] = h[temp] + " " + l4[j].text.replace("ⓘ","")
    k={}
    for i,j in zip(range(2,len(l4), 4), range(3, len(l4),4)):
      if l4[i].text!='' and l4[i].text!=' ':
        temp = l4[i].text
        k[temp] = l4[j].text.replace("ⓘ","")
      else:
        k[temp] = k[temp] + " " + l4[j].text.replace("ⓘ","")
    l5 = soup.find('div',class_='dpRashiNakshatraCardWrapper').find_all('div',class_='dpTableCell')
    l={}
    for i,j in zip(range(0,len(l5), 4), range(1, len(l5),4)):
      if l5[i].text!='' and l5[i].text!=' ':
        temp = l5[i].text
        l[temp] = l5[j].text.replace("ⓘ","")
      else:
        l[temp] = l[temp] + " " + l5[j].text.replace("ⓘ","")
    m={}
    for i,j in zip(range(2,len(l5), 4), range(3, len(l5),4)):
      if l5[i].text!='' and l5[i].text!=' ':
        temp = l5[i].text
        m[temp] = l5[j].text.replace("ⓘ","")
      else:
        m[temp] = m[temp] + " " + l5[j].text.replace("ⓘ","")
    l6 = soup.find('div',class_='dpAyanaRituCardWrapper').find_all('div',class_='dpTableCell')
    n={}
    for i,j in zip(range(0,len(l6), 4), range(1, len(l6),4)):
      if l6[i].text!='' and l6[i].text!=' ':
        temp = l6[i].text
        n[temp] = l6[j].text.replace("ⓘ","")
      else:
        n[temp] = n[temp] + " " + l6[j].text.replace("ⓘ","")
    o={}
    for i,j in zip(range(2,len(l6), 4), range(3, len(l6),4)):
      if l6[i].text!='' and l6[i].text!=' ':
        temp = l6[i].text
        o[temp] = l6[j].text.replace("ⓘ","")
      else:
        o[temp] = o[temp] + " " + l6[j].text.replace("ⓘ","")
    l7 = soup.find('div',class_='dpAuspiciousCardWrapper').find_all('div',class_='dpTableCell')
    p={}
    for i,j in zip(range(0,len(l7), 4), range(1, len(l7),4)):
      if l7[i].text!='' and l7[i].text!=' ':
        temp = l7[i].text
        p[temp] = l7[j].text.replace("ⓘ","")
      else:
        p[temp] = p[temp] + " " + l7[j].text.replace("ⓘ","")
    q={}
    for i,j in zip(range(2,len(l7), 4), range(3, len(l7),4)):
      if l7[i].text!='' and l7[i].text!=' ':
        temp = l7[i].text
        q[temp] = l7[j].text.replace("ⓘ","")
      else:
        q[temp] = q[temp] + " " + l7[j].text.replace("ⓘ","")
    l8 = soup.find('div',class_='dpInauspiciousCardWrapper').find_all('div',class_='dpTableCell')
    r={}
    for i,j in zip(range(0,len(l8), 4), range(1, len(l8),4)):
      if l8[i].text!='' and l8[i].text!=' ':
        temp = l8[i].text
        r[temp] = l8[j].text.replace("ⓘ","")
      else:
        r[temp] = r[temp] + " " + l8[j].text.replace("ⓘ","")
    s={}
    for i,j in zip(range(2,len(l8), 4), range(3, len(l8),4)):
      if l8[i].text!='' and l8[i].text!=' ':
        temp = l8[i].text
        s[temp] = l8[j].text.replace("ⓘ","")
      else:
        s[temp] = s[temp] + " " + l8[j].text.replace("ⓘ","")
    l9 = soup.find('div',class_='dpTamilYogaCardWrapper').find_all('div',class_='dpTableCell')
    t={}
    for i,j in zip(range(0,len(l9), 4), range(1, len(l9),4)):
      if l9[i].text!='' and l9[i].text!=' ':
        temp = l9[i].text
        t[temp] = l9[j].text.replace("ⓘ","")
      else:
        t[temp] = t[temp] + " " + l9[j].text.replace("ⓘ","")
    u={}
    for i,j in zip(range(2,len(l9), 4), range(3, len(l9),4)):
      if l9[i].text!='' and l9[i].text!=' ':
        temp = l9[i].text
        u[temp] = l9[j].text.replace("ⓘ","")
      else:
        u[temp] = u[temp] + " " + l9[j].text.replace("ⓘ","")
    l10 = soup.find('div',class_='dpNivasaShoolaCardWrapper').find_all('div',class_='dpTableCell')
    v={}
    for i,j in zip(range(0,len(l10), 4), range(1, len(l10),4)):
      if l10[i].text!='' and l10[i].text!=' ':
        temp = l10[i].text
        v[temp] = l10[j].text.replace("ⓘ","")
      else:
        v[temp] = v[temp] + " " + l10[j].text.replace("ⓘ","")
    w={}
    for i,j in zip(range(2,len(l10), 4), range(3, len(l10),4)):
      if l10[i].text!='' and l10[i].text!=' ':
        temp = l10[i].text
        w[temp] = l10[j].text.replace("ⓘ","")
      else:
        w[temp] = w[temp] + " " + l10[j].text.replace("ⓘ","")
    l11 = soup.find('div',class_='dpCalendarEpochCardWrapper').find_all('div',class_='dpTableCell')
    x={}
    for i,j in zip(range(0,len(l11), 4), range(1, len(l11),4)):
      if l11[i].text!='' and l11[i].text!=' ':
        temp = l11[i].text
        x[temp] = l11[j].text.replace("ⓘ","")
      else:
        x[temp] = x[temp] + " " + l11[j].text.replace("ⓘ","")
    y={}
    for i,j in zip(range(2,len(l11), 4), range(3, len(l11),4)):
      if l11[i].text!='' and l11[i].text!=' ':
        temp = l11[i].text
        y[temp] = l11[j].text.replace("ⓘ","")
      else:
        y[temp] = y[temp] + " " + l11[j].text.replace("ⓘ","")
    
    nakshatrabodypart = ""
    for naksh in nakshatras:
      if naksh in g['Nakshatra']:
        for nakshbody in range(len(fullText)):
          if naksh in fullText[nakshbody]:
            nakshatrabodypart = nakshatrabodypart + fullText[nakshbody][1:] + "\n"
    
    paksha_element = soup.find('div', text=lambda t: 'Paksha' in t if t else False)
    
    # Extract the text if the element exists
    thithi_value = paksha_element.get_text(strip=True).split(',')[1][1:] if paksha_element else 'Not Found'
    paksha_value = paksha_element.get_text(strip=True).split(',')[0][:-7] if paksha_element else 'Not Found'
    
    res = dd.loc[dd['Paksha'] == paksha_value]
    res = res.loc[res['Tithi'] == tithidinas[thithi_value]]
    
    for key in tithidinas:
      if key == thithi_value:
        Sudhakalainwomen = res['Sudhakala in Stri'].values[0]
        Sudhakalainmen = res['Sudhakala in Purusha'].values[0]
        Vishakalainwomen = res['Vishakala in Stri'].values[0]
        Vishakalainmen = res['Vishakala in Purusha'].values[0]
    # Sudhakalainwomen = ""#res['Sudhakala in women'].values[0]
    # Sudhakalainmen = ""#res['Sudhakala in men'].values[0]
    # Vishakalainwomen = ""#res['Vishakala in women'].values[0]
    # Vishakalainmen = ""#res['Vishakala in men'].values[0]
    Chakrabasedonvasara = chakravara[a1['Weekday']]
    Bodypartbasedonnakshatra = nakshatrabodypart
    Date=a['Date']
    Weekday=a1['Weekday']
    Sunrise=d['Sunrise']
    Sunset=f['Sunset']
    Moonrise=d['Moonrise']
    Moonset=f['Moonset']
    Samvatsara=h['Shaka Samvat']
    Ayana=n['Drik Ayana']
    Ritu=n['Drik Ritu']
    Masa=Masa
    Kollamera=Kollamera
    Paksha=e['Paksha']
    Tithi=e['Tithi']
    Vasara=e['Weekday']
    Nakshatra=g['Nakshatra']
    Sunsign=l['Sunsign']
    Moonsign=l['Moonsign']
    Brahmamuhurta=p['Brahma Muhurta']
    Pratahsandhya=q['Pratah Sandhya']
    Abhijitmuhurta=p['Abhijit']
    Saayamsandhya=q['Sayahna Sandhya']
    Rahukalam=r['Rahu Kalam']
    Yamaganda=s['Yamaganda']
    Gulikaikaalam=r['Gulikai Kalam']
    Significance=c['Significance']
    Sudhakalainwomen=Sudhakalainwomen
    Sudhakalainmen=Sudhakalainmen
    Vishakalainwomen=Vishakalainwomen
    Vishakalainmen=Vishakalainmen
    Chakrabasedonvasara=Chakrabasedonvasara
    Bodypartbasedonnakshatra=Bodypartbasedonnakshatra
    message = """
Simply Ayurveda - Dainika Vaidya Almanac

✨ Suprabhatam ✨

{Date}
{Weekday}

☀️ Sunrise – {Sunrise}
🌇 Sunset – {Sunset}
🌒 Moonrise – {Moonrise}
🌃 Moonset – {Moonset}

Samvatsara – {Samvatsara}
Ayana - {Ayana}
Ritu – {Ritu}
Masa - {Masa}
Kollam era – {Kollamera}
Paksha – {Paksha}
Tithi – {Tithi}
Vasara – {Vasara}
Nakshatra – {Nakshatra}
Sunsign – {Sunsign}
Moonsign – {Moonsign}

✨ Auspicious hours -✨
🪷 Brahma muhurta – {Brahmamuhurta}
🌼 Pratah sandhya – {Pratahsandhya}
🌸 Abhijit muhurta – {Abhijitmuhurta}
🌼 Saayam sandhya – {Saayamsandhya}

🛑 Hours to be careful around
❌Rahu kalam – {Rahukalam}
‼️Yama ganda – {Yamaganda}
💊Gulikai Kaalam – {Gulikaikaalam}

Significance – {Significance}

🩺✡️ Medicoastrological significance -
Sudhakala in women – {Sudhakalainwomen}🚺
Sudhakala in men – {Sudhakalainmen}🚹
Vishakala in women – {Vishakalainwomen}🦳
Vishakala in men – {Vishakalainmen}🧔🏻‍♂
Chakra based on vasara – {Chakrabasedonvasara}

Body of Kala Purusha according to Nakshatra –

{Bodypartbasedonnakshatra}
Have we missed anything important?
Message Simply Ayurveda on WhatsApp. https://wa.me/message/DTX6RK5L6HE3B1
Subscribe to our YouTube channel - https://youtube.com/c/SimplyAyurveda
    """
    msg = message.format(Date=Date, Weekday=Weekday, Sunrise=Sunrise, Sunset=Sunset, Moonrise=Moonrise, Moonset=Moonset, Samvatsara=Samvatsara, Ayana=Ayana, Ritu=Ritu, Masa=Masa, Kollamera=Kollamera, Paksha=Paksha, Tithi=Tithi, Vasara=Vasara, Nakshatra=Nakshatra, Sunsign=Sunsign, Moonsign=Moonsign, Brahmamuhurta=Brahmamuhurta, Pratahsandhya=Pratahsandhya, Abhijitmuhurta=Abhijitmuhurta, Saayamsandhya=Saayamsandhya, Rahukalam=Rahukalam, Yamaganda=Yamaganda, Gulikaikaalam=Gulikaikaalam, Significance=Significance, Sudhakalainwomen=Sudhakalainwomen, Sudhakalainmen=Sudhakalainmen, Vishakalainwomen=Vishakalainwomen, Vishakalainmen=Vishakalainmen, Chakrabasedonvasara=Chakrabasedonvasara, Bodypartbasedonnakshatra=Bodypartbasedonnakshatra)
    print(msg)
    #st.code(msg)
    #st.write(dd)
    
    TELEGRAM_BOT_TOKEN = "7965698138:AAHvzdIZbZH9Uu9k8wmBevSev14iLwEgEAo"
    TELEGRAM_CHAT_ID = "-4741545165"
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    
    response = requests.post(url, json=payload)
    
    msg2 = """
For Admin purposes only 🛠: You can check the Almanac for any date of your choice by clicking on the following link:-
https://almac2.streamlit.app
    """
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg2, "parse_mode": "Markdown"}
    
    response = requests.post(url, json=payload)
    # if response.status_code == 200:
    #   st.success("Message sent to Telegram!")
    # else:
    #   st.error("Failed to send message.")

if __name__ == "__main__":
    main()
