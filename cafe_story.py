#-------- Historie om et kafébesøk --------#
print("Velkommen til vår kaféhistorie!")
# Karakterer
karakterer = {
    "Anna": {"rolle": "kunde", "favoritt_drikke": "latte"},
    "Ben": {"rolle": "barista", "favoritt_drikke": "espresso"},
}
# Setting
kafe_navn = "Kaffehjørnet"          
kafe_beskrivelse = "En koselig kafé med et variert utvalg av kaffe og kaker." 
# Historie
historie = f"""
Det var en gang en kafé som het {kafe_navn}. {kafe_beskrivelse}
En dag kom {karakterer["Anna"]["rolle"]} Anna inn for å bestille sin favorittdrikk, {karakterer["Anna"]["favoritt_drikke"]}.
Baristaen, {karakterer["Ben"]["rolle"]} Ben, laget en perfekt {karakterer["Ben"]["favoritt_drikke"]} til henne.
Sammen delte de historier om livet, drømmer og selvfølgelig, kaffe.
Det ble starten på et vakkert vennskap.
"""
print(historie)
# Avslutning
print("Takk for at du fulgte med på kaféhistorien vår!")
#-------- End of cafe_story.py --------#