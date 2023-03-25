class Party:

    def __init__(self):
        self.people = []


party = Party()
attending_persons = input()
while attending_persons != 'End':
    party.people.append(attending_persons)
    attending_persons = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")