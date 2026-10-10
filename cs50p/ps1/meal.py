
#ask what time is it and return the answer
def main():
    time = input('What time is it? ').strip()
    hours = convert(time)
    if 7.00 <= hours <= 8.00:
        print('breakfast time')
    elif 12.00 <= hours <=  13.00:
        print('lunch time')
    elif 18.00 <= hours <= 19.00:
        print('dinner time')

#convert a time like “7:30” into hours as a float (7.5)
def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60   

if __name__ == "__main__":
    main()  