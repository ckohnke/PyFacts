from googlevoice import Voice,util,settings
from googlevoice.util import input
from random import randint
import time

# import voice/lists
voice = Voice()
voice.login()
with open("num_cat.db") as f:
    nums_cat = f.readlines()
with open("num_pok.db") as f:
    nums_pok = f.readlines()
with open("num_gir.db") as f:
    nums_gir = f.readlines()
with open("num_sex.db") as f:
    nums_sex = f.readlines()
with open("cat.db") as f:
    fax_cat = f.readlines()
with open("pokemon.db") as f:
    fax_pok = f.readlines()
with open("giraffe.db") as f:
    fax_gir = f.readlines()
with open("sex.db") as f:
    fax_sex = f.readlines()

# Send the list a random fact each
def daily():
  for i in range(0,len(nums_cat)-1):
    voice.send_sms(nums_cat[i],fax_cat[randint(0,len(fax_cat)-1)])
    time.sleep(10)
  for i in range(0,len(nums_pok)-1):
    voice.send_sms(nums_pok[i],fax_pok[randint(0,len(fax_pok)-1)])
    time.sleep(10)
  for i in range(0,len(nums_gir)-1):
    voice.send_sms(nums_gir[i],fax_gir[randint(0,len(fax_gir)-1)])
    time.sleep(10)
  for i in range(0,len(nums_sex)-1):
    voice.send_sms(nums_sex[i],fax_sex[randint(0,len(fax_sex)-1)])
    time.sleep(10)

# Check inbox, respond to unread messages
def checkInbox():
  for message in voice.sms().messages:
      if not message.isRead:
          n = message.phoneNumber
          message.mark()
          if str(n) in str(nums_cat): # if in cat list
            voice.send_sms(n,fax_cat[randint(0,len(fax_cat)-1)])
          if str(n) in str(nums_pok): # if in pokemon list
            voice.send_sms(n,fax_pok[randint(0,len(fax_pok)-1)])
          if str(n) in str(nums_gir): # if in giraffe list
            voice.send_sms(n,fax_gir[randint(0,len(fax_gir)-1)])
          if str(n) in str(nums_sex): # if in giraffe list
            voice.send_sms(n,fax_sex[randint(0,len(fax_sex)-1)])
          if not str(n) in str(nums_cat) and not str(n) in str(nums_pok) and not str(n) in str(nums_gir) and not str(n) in str(nums_sex): # if in no list, default to cat
            voice.send_sms(n,fax_cat[randint(0,len(fax_cat)-1)])
          time.sleep(10)

def main():
  perdiem = 6.0 # facts/day for daily
  start = 86400.0/perdiem
  sinDay = start
  s = 10 # Sleep incrimentor (s)
  daily()
  while True:
    if sinDay < 100:
      daily()  # Send fact perdiem/day to number list
      sinDay = start
    time.sleep(s)
    sinDay = sinDay-s
    checkInbox()

if __name__ == "__main__":
    main()
