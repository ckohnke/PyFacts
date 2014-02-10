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
with open("cat.db") as f:
    fax_cat = f.readlines()
with open("pokemon.db") as f:
    fax_pok = f.readlines()

# Send the list a random fact each
def daily():
  for i in range(0,len(nums_cat)-1):
    voice.send_sms(nums_cat[i],fax_cat[randint(0,len(fax_cat)-1)])
  for i in range(0,len(nums_pok)-1):
    voice.send_sms(nums_pok[i],fax_pok[randint(0,len(fax_pok)-1)])

# Check inbox, respond to unread messages
def checkInbox():
  for message in voice.sms().messages:
      if not message.isRead:
          n = message.phoneNumber
          message.mark()
          if str(n) in str(nums_cat):
            voice.send_sms(n,fax_cat[randint(0,len(fax_cat)-1)])
          if str(n) in str(nums_pok):
            voice.send_sms(n,fax_pok[randint(0,len(fax_pok)-1)])
          if not str(n) in str(nums_cat) and not str(n) in str(nums_pok):
            voice.send_sms(n,fax_cat[randint(0,len(fax_cat)-1)])
          time.sleep(5)

def main():
  perdiem = 3 # facts/day for daily
  start = 86400/perdiem
  sinDay = start
  s = 5 # Sleep incrimentor (s)
  #daily()
  while True:
    if sinDay < 0:
      daily()  # Send fact perdiem/day to number list
      sinDay = start
    time.sleep(s)
    sinDay = sinDay-s
    checkInbox()

if __name__ == "__main__":
    main()
