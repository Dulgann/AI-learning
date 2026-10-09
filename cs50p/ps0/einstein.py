#calculate the energi with the formula E=mc^2
#ask for the mass and print the result
def main():
    m = int(input('m: '))
    print(energy(m))
#calculate the J
def energy(m):
    c = 300000000

    return m*c**2
   
main()

