import time
import sys
import requests
import pandas as pd
from io import BytesIO
import urllib
from datetime import datetime, timedelta
import docx

def main():
    response = requests.get("https://docs.google.com/spreadsheets/d/1h2rVBV6X2gNg4hRNVFT26DoW-cbOnHEesF2oz9wipDo/export?format=csv")
    df = pd.read_csv(BytesIO(response.content))
    df.to_csv('almanac1.csv', index = False)
    dd = pd.read_csv('almanac1.csv')
    today = datetime.today()
    tomorrow = today + timedelta(1)
    formatted_date = tomorrow.strftime("%d-%m-%Y")
    res = dd.loc[df['Date'] == formatted_date]
    Date=res['Date'].values[0]
    Weekday=res['Weekday'].values[0]
    Sunrise=res['Sunrise'].values[0]
    Sunset=res['Sunset'].values[0]
    Moonrise=res['Moonrise'].values[0]
    Moonset=res['Moonset'].values[0]
    Samvatsara=res['Samvatsara'].values[0]
    Ayana=res['Ayana'].values[0]
    Ritu=res['Rtu'].values[0]
    Masa=res['Masa'].values[0]
    Kollamera=res['Kollam era'].values[0]
    Paksha=res['Paksha'].values[0]
    Tithi=res['Tithi'].values[0]
    Vasara=res['Vasara'].values[0]
    Nakshatra=res['Nakshatra'].values[0]
    Sunsign=res['Sunsign'].values[0]
    Moonsign=res['Moonsign'].values[0]
    Brahmamuhurta=res['Brahma muhurta'].values[0]
    Pratahsandhya=res['Pratah sandhya'].values[0]
    Abhijitmuhurta=res['Abhijit muhurta'].values[0]
    Saayamsandhya=res['Saayam sandhya'].values[0]
    Rahukalam=res['Rahu kalam'].values[0]
    Yamaganda=res['Yama ganda'].values[0]
    Gulikaikaalam=res['Gulikai Kaalam'].values[0]
    Significance=res['Significance'].values[0]
    Sudhakalainmen=res['Sudhakala in Purusha'].values[0]
    Vishakalainmen=res['Vishakala in Purusha'].values[0]
    Sudhakalainwomen=res['Sudhakala in Stri'].values[0]
    Vishakalainwomen=res['Vishakala in Stri'].values[0]
    Chakrabasedonvasara=res['Chakra based on vasara'].values[0]
    Bodypartbasedonnakshatra=res['The Body of Kal Purusha by Nakshatra'].values[0]
    
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

🦶 Body of Kala Purusha according to Nakshatra –

{Bodypartbasedonnakshatra}
Have we missed anything important?
Message Simply Ayurveda on WhatsApp. https://wa.me/message/DTX6RK5L6HE3B1
Subscribe to our YouTube channel - https://youtube.com/c/SimplyAyurveda
    """
    msg = message.format(Date=Date, Weekday=Weekday, Sunrise=Sunrise, Sunset=Sunset, Moonrise=Moonrise, Moonset=Moonset, Samvatsara=Samvatsara, Ayana=Ayana, Ritu=Ritu, Masa=Masa, Kollamera=Kollamera, Paksha=Paksha, Tithi=Tithi, Vasara=Vasara, Nakshatra=Nakshatra, Sunsign=Sunsign, Moonsign=Moonsign, Brahmamuhurta=Brahmamuhurta, Pratahsandhya=Pratahsandhya, Abhijitmuhurta=Abhijitmuhurta, Saayamsandhya=Saayamsandhya, Rahukalam=Rahukalam, Yamaganda=Yamaganda, Gulikaikaalam=Gulikaikaalam, Significance=Significance, Sudhakalainwomen=Sudhakalainwomen, Sudhakalainmen=Sudhakalainmen, Vishakalainwomen=Vishakalainwomen, Vishakalainmen=Vishakalainmen, Chakrabasedonvasara=Chakrabasedonvasara, Bodypartbasedonnakshatra=Bodypartbasedonnakshatra)
    # print(msg)
    
    TELEGRAM_BOT_TOKEN = "7965698138:AAHvzdIZbZH9Uu9k8wmBevSev14iLwEgEAo"
    TELEGRAM_CHAT_ID = "-4741545165"
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    
    response = requests.post(url, json=payload)
    
    time.sleep(10)
    
    msg2 = """
For Admin purposes only 🛠: You can check the Almanac for any date of your choice by clicking on the following link:-
https://almac2.streamlit.app
    """
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg2, "parse_mode": "Markdown"}
    
    response = requests.post(url, json=payload)

if __name__ == "__main__":
    main()
