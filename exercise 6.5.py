Rivers={'Nile':'Egypt',
        'Amazon':'South America',
        'Ganga':'India',
        }
for name,value in Rivers.items():
    print(name+ " runs through " +value+".\n")
for name in Rivers:
    print(name)

for country in Rivers.values():
    print("\n"+country)
