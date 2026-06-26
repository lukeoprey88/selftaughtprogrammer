#1
with open("hello_world.py", 'r') as f:
    print(f.read())

#2
nameOfUser = input('What is your name?')
with open("name.txt", 'w') as f:
    f.write(nameOfUser)
#3
filmLists = [
    [
        "Top Gun", "Risky Business", "Minority Report"
    ],
    [
        "Titanic", "The Revenant", "Inception"
    ],
    [
        "Training Day", "Man on Fire", "Flight"
    ]
]
import csv
with open("films.csv", 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    for filmGroup in filmLists:
        w.writerow(filmGroup)
        ''' Superfluous code as array could be written directly
        addFilm = []
        for film in filmGroup:
            addFilm.append(film)
        print(addFilm)
        w.writerow(addFilm)
        '''
        
        

        