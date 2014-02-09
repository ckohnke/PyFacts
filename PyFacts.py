from googlevoice import Voice,util,settings
from googlevoice.util import input
from random import randint
import time

# import voice/lists
voice = Voice()
voice.login()
with open("number.db") as f:
    nums = f.readlines()
with open("pokemon.db") as f:
    fax_pok = f.readlines()

# Send the list a random fact each
def daily():
  for i in range(0,len(nums)-1):
    voice.send_sms(nums[0],fax_pok[randint(0,len(fax_pok)-1)])

# Check inbox, respond to unread messages
def checkInbox():
  for message in voice.inbox().messages:
      if not message.isRead:
          n = message.phoneNumber
          message.mark()
          voice.send_sms(n,fax_pok[randint(0,len(fax_pok)-1)])

def main():
  perdiem = 5 # facts/day for daily
  start = 86400/perdiem
  sinDay = start
  s = 5 # Sleep incrimentor (s)
  while True:
    if sinDay < 0:
      daily()  # Send fact perdiem/day to number list
      sinDay = start
    time.sleep(s)
    sinDay = sinDay-s
    checkInbox()

if __name__ == "__main__":
    main()
