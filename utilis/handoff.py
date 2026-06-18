from utilis.ticket_generator import generate_ticket

def handoff_to_human():

    ticket = generate_ticket()

    return f"""
Ticket ID: {ticket}

Status: OPEN
Priority: HIGH

Your request has been escalated to a human support agent.
A support representative will contact you shortly.
"""