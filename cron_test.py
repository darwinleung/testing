import datetime

num_lines = sum(1 for line in open('cron_test.txt'))

with open('cron_test.txt', 'a') as f:
    f.write(str(num_lines+1)+" "+str(datetime.datetime.now())+"\n")

print('Success')