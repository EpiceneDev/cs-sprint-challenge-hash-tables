#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ht = {}
    route = [None] * length

    for ticket in range(length):
        if tickets[ticket].source == "NONE":
            route[0] = tickets[ticket].destination

        ht[tickets[ticket].source] = tickets[ticket].destination

    for ticket in range(length):
        if route[ticket-1]:
            route[ticket] = ht[route[ticket-1]]
            

    return route
