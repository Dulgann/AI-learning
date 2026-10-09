# replace :( and :) for 🙁 and 🙂

#ask for imput (text) and call convert
def main():
    text = input('How are you feeling? ')
    
    print(convert(text))
    


#replace the text :) and :( for emotes
def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text


#Call main
main()
