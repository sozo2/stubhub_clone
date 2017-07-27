#imports venue seating maps

def printVenueName():
    venues=Venue.objects.all() 
    for venue in venues:
        print venue.title,",", venue.id
    return venues.first()

imglocations=[[1,	'www.theatreinchicago.com/images/seat/privatebank-theatre-seating-chart.jpg'],[2,	'cadillacpalacetheatre.com/wp-content/uploads/2014/11/cadillac_palace_theatre.gif'],[3,	'I.gse.io/gse_media/images/000/005/467/1380658049-courtyard-theater.jpg?p=1'],[4,	'chicago.whitesox.mlb.com/cws/images/ticketing/y2013/525x469_seating_chart.gif'],[5,'seatics.tickettransaction.com/OrientalTheatre-FordCenterforthePerfArts_Endstage-IntZone-2015-05-20_2015-08-05_1044_SVGC_tn.gif'],[6,'luck.s3.amazonaws.com/venue/243.gif'],[7,'sites.google.com/site/bullsseats/chicago-bulls-seating-chart/Chicago%20Bulls%20Seating%20Chart%20for%20United%20Center.jpg?attredirects=0'],[8,	's1.ticketm.net/tm/en-us/tmimages/venue/maps/arz/64749s.gif'],[10,'blog.tickpick.com/wp-content/uploads/2015/09/The-Chicago-Theatre-Seating-Chart.png'],[11,'static.ticketutils.com/Charts/IA/f208b16a-3e63-460f-9734-67b94349ee2f/WB/3_0_0.jpg'],[14,	'www.cubsseatingchart.com/wp-content/uploads/Chicago-Cubs-Seating-Chart-for-Wrigley-Field.jpg']]

for x in imglocations:
    currVen=Venue.objects.get(id=x[0])
    currVen.seating_map = x[1]
    currVen.save()