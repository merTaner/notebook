import re

def is_valid_uid(uid):
  return re.match(r'^(?!.*(.).*\1)(?=(.*[\d]){3,}.*)((?=(.*[A-Z]){2,}.*))([a-zA-Z0-9]{10})$', uid)


if __name__ == '__main__':
    for _ in range(int(input())):
       uid = input()

       if is_valid_uid(uid):
          print('Valid')
       else:
          print('Invalid')
