def city_country(city,country,population=0):
    message=city+","+country
    if population:
        message+= '-population '+str(population)
    return message
                 
