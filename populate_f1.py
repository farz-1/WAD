import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1.settings')
django.setup()

from for1.models import *
import news_api


def populate():

    driver_list = [
        {'name': 'Lewis Hamilton', 'DOB': '07/01/1985', 'height': '1.74m', 'weight': '73kg',
         'nationality': 'British', 'driverNumber': 44, 'seasonsWon': 7, 'podiumsWon': 182,
         'constructor': 'Mercedes'},
        {'name': 'George Russell', 'DOB': '15/02/1998', 'height': '1.85m', 'weight': '70kg',
         'nationality': 'British', 'driverNumber': 63, 'seasonsWon': 0, 'podiumsWon': 1,
         'constructor': 'Mercedes'},
        {'name': 'Max Verstappen', 'DOB': '30/09/1997', 'height': '1.81m', 'weight': '72kg',
         'nationality': 'Belgian-Dutch', 'driverNumber': '1', 'seasonsWon': 1, 'podiumsWon': 60,
         'constructor': 'Red Bull'},
        {'name': 'Sergio Perez', 'DOB': '26/01/1990', 'height': '1.73m', 'weight': '63kg',
         'nationality': 'Mexican', 'driverNumber': 11, 'seasonsWon': 0, 'podiumsWon': 15,
         'constructor': 'Red Bull'},
        {'name': 'Lando Norris', 'DOB': '13/11/1999', 'height': '1.7m', 'weight': '66kg',
         'nationality': 'British', 'driverNumber': 4, 'seasonsWon': 0, 'podiumsWon': 5,
         'constructor': 'McLaren'},
        {'name': 'Daniel Ricciardo', 'DOB': '01/07/1989', 'height': '1.8m', 'weight': '72kg',
         'nationality': 'Australian', 'driverNumber': 3, 'seasonsWon': 0, 'podiumsWon': 32,
         'constructor': 'McLaren'},
        {'name': 'Carlos Sainz', 'DOB': '01/09/1994', 'height': '1.78m', 'weight': '64kg',
         'nationality': 'Spanish', 'driverNumber': 3, 'seasonsWon': 0, 'podiumsWon': 6,
         'constructor': 'Ferrari'},
        {'name': 'Charles Leclerc', 'DOB': '16/10/1997', 'height': '1.8m', 'weight': '69kg',
         'nationality': 'Monocan', 'driverNumber': 16, 'seasonsWon': 0, 'podiumsWon': 13,
         'constructor': 'Ferrari'},
        {'name': 'Fernando Alonso', 'DOB': '29/07/1981', 'height': '1.71m', 'weight': '68kg',
         'nationality': 'Spanish', 'driverNumber': 14, 'seasonsWon': 2, 'podiumsWon': 98,
         'constructor': 'Alpine'},
        {'name': 'Esteban Ocon', 'DOB': '17/09/1996', 'height': '1.86m', 'weight': '66kg',
         'nationality': 'French', 'driverNumber': 31, 'seasonsWon': 0, 'podiumsWon': 2,
         'constructor': 'Alpine'},
        {'name': 'Pierre Gasly', 'DOB': '07/02/1996', 'height': '1.77m', 'weight': '70kg',
         'nationality': 'French', 'driverNumber': 10, 'seasonsWon': 0, 'podiumsWon': 3,
         'constructor': 'AlphaTauri'},
        {'name': 'Yuki Tsunoda', 'DOB': '11/05/2000', 'height': '1.59m', 'weight': '54kg',
         'nationality': 'Japanese', 'driverNumber': 22, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'AlphaTauri'},
        {'name': 'Sebastian Vettel', 'DOB': '3/07/1987', 'height': '1.75m', 'weight': '62kg',
         'nationality': 'German', 'driverNumber': 5, 'seasonsWon': 4, 'podiumsWon': 122,
         'constructor': 'Aston Martin'},
        {'name': 'Lance Stroll', 'DOB': '29/10/1998', 'height': '1.82m', 'weight': '70kg',
         'nationality': 'Canadian', 'driverNumber': 18, 'seasonsWon': 0, 'podiumsWon': 3,
         'constructor': 'Aston Martin'},
        {'name': 'Alexander Albon', 'DOB': '23/03/1996', 'height': '1.86m', 'weight': '73kg',
         'nationality': 'Thai', 'driverNumber': 23, 'seasonsWon': 0, 'podiumsWon': 2,
         'constructor': 'Williams'},
        {'name': 'Nicholas Latifi', 'DOB': '29/07/1995', 'height': '1.85m', 'weight': '73kg',
         'nationality': 'Canadian', 'driverNumber': 6, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'Williams'},
        {'name': 'Mick Schumacher', 'DOB': '22/03/1999', 'height': '1.77m', 'weight': '67kg',
         'nationality': 'German', 'driverNumber': 47, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'Haas'},
        {'name': 'Kevin Magnussen', 'DOB': '05/10/1992', 'height': '1.74m', 'weight': '68kg',
         'nationality': 'Danish', 'driverNumber': 20, 'seasonsWon': 0, 'podiumsWon': 1,
         'constructor': 'Haas'},
        {'name': 'Valtteri Bottas', 'DOB': '28/08/1989', 'height': '1.73m', 'weight': '69kg',
         'nationality': 'Finnish', 'driverNumber': 77, 'seasonsWon': 0, 'podiumsWon': 67,
         'constructor': 'Alfa Romeo'},
        {'name': 'Guanyu Zhou', 'DOB': '30/05/1999', 'height': '1.75m',
         'weight': '63kg', 'nationality': 'Chinese', 'driverNumber': 24, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'Alfa Romeo'},
        {'name': 'Nico Hulkenberg', 'DOB': '19/08/1987', 'height': '1.84m',
         'weight': '78kg', 'nationality': 'German', 'driverNumber': 27, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'Aston Martin'}]

    constructor_list = [
        {'name': 'Mercedes', 'teamPrincipal': 'Totto Wolff', 'nationality': 'German',
         'yearsActive': 68, 'raceEngineer': 'Peter Bonnington', 'about':"Mercedes-Benz, a brand of the Mercedes-Benz Group, has been involved in Formula One as both team owner and engine manufacturer for various periods since 1954. The Mercedes-AMG Petronas F1 Team, which is based in Brackley, England,and possesses a German licence,is as of 2022 majority owned by the Mercedes-Benz Group with Toto Wolff having a significant shareholding. Mercedes-branded teams are often referred to by the nickname, the 'Silver Arrows'. An announcement was made in December 2020 that Ineos planned to take a one third equal ownership stake alongside the Mercedes-Benz Group and Wolff; as of December 2021, this had not yet been completed. Before the Second World War, Mercedes-Benz competed in the European Championship, winning three titles. The marque debuted in Formula One in 1954. After winning their first race at the 1954 French Grand Prix, driver Juan Manuel Fangio won another three Grands Prix to win the 1954 Drivers' Championship and repeated this success in 1955. Despite winning two Drivers' Championships, Mercedes-Benz withdrew from motor racing after 1955 in response to the 1955 Le Mans disaster. Mercedes returned to Formula One in 1994 as an engine manufacturer in association with Ilmor, a British independent high-performance autosport engineering company, which developed their engines. The company won one constructors' title and three drivers' titles in a works partnership with McLaren which lasted until 2009."},
        {'name': 'Red Bull', 'teamPrincipal': 'Christian Horner', 'nationality': 'Austrian',
         'yearsActive': 17, 'raceEngineer': 'Gianpiero Lambiase','about':"Red Bull Racing came into existence late in 2004 with ambitions to challenge for race victories and world championship titles. Christian Horner was appointed team principal soon after and has guided the development of the team ever since. This was not the work of a moment. Over the next four seasons, solid foundations were laid. The team recruited in both quantity and quality, steadily expanding until it was capable of going toe-to-toe with the most illustrious names in racing. The team finished comfortably mid-table in 2005 and 2006. The initial driver line-up mixed youth and experience: David Coulthard provided the latter, while Christian Klien, Vitantonio Liuzzi and Robert Doornbos were the former. DC scored our first podium, finishing third at the 2006 Monaco Grand Prix. For 2007, Mark Webber came onboard to join DC. The team finished fifth that year but dropped back to seventh again in 2008, although everything was going to change in 2009. David Coulthard retired at the end of 2008 to be replaced by Sebastian Vettel. Sebs arrival coincided with a major reset in the sports aerodynamic regulations. The new rules gave the technical team the chance to shine. With the RB5, they produced a winner: Vettel took Red Bull Racings first victory, leading home Webber in a 1-2 finish at the Chinese Grand Prix. The car would win five more times in 2009, including Webbers debut F1 victory at the Nürburgring. The team finished second in the Constructors Championship but, perhaps more significantly, it won the final three races of the season. Strong in-season development is a hallmark of the team, the origin story of which largely begins here. History was made in 2010. Driving the RB6, Webber and Vettel were title contenders from the start. Their consistent podium finishes secured the Constructors Championship at the penultimate round in Brazil. Both drivers went to the final race in Abu Dhabi with a shot at the Drivers crown. Vettel emerged triumphant, winning the race to become the sports youngest ever World Champion. A record that still stands."},
        {'name': 'McLaren', 'teamPrincipal': 'Zak Brown', 'nationality': 'British',
         'yearsActive': 56, 'raceEngineer': 'William Joseph','about':"McLaren Racing Limited is a British motor racing team based at the McLaren Technology Centre in Woking, Surrey, England. McLaren is best known as a Formula One constructor, the second oldest active team, and the second most successful Formula One team after Ferrari, having won 183 races, 12 Drivers' Championships and 8 Constructors' Championships. McLaren also has a history of competing in American open wheel racing, as both an entrant and a chassis constructor, and has won the Canadian-American Challenge Cup (Can-Am) sports car racing championship. The team is a subsidiary of the McLaren Group, which owns a majority of the team. Founded in 1963 by New Zealander Bruce McLaren, the team won its first Grand Prix at the 1968 Belgian Grand Prix, but their greatest initial success was in Can-Am, which they dominated from 1967 to 1971. Further American triumph followed, with Indianapolis 500 wins in McLaren cars for Mark Donohue in 1972 and Johnny Rutherford in 1974 and 1976. After Bruce McLaren died in a testing accident in 1970, Teddy Mayer took over and led the team to their first Formula One Constructors' Championship in 1974, with Emerson Fittipaldi and James Hunt winning the Drivers' Championship in 1974 and 1976 respectively. 1974 also marked the start of a long-standing sponsorship by the Marlboro cigarette brand. In 1981, McLaren merged with Ron Dennis' Project Four Racing; Dennis took over as team principal, and shortly afterwards organised a buyout of the original McLaren shareholders to take full control of the team. This began the team's most successful era; with Porsche and Honda engines, Niki Lauda, Alain Prost, and Ayrton Senna won seven Drivers' Championships between them and the team took six Constructors' Championships. The combination of Prost and Senna was particularly dominant—together they won all but one race in 1988—but later their rivalry soured and Prost left for Ferrari. Fellow English team Williams offered the most consistent challenge during this period, the two winning every constructors' title between 1984 and 1994. By the mid-1990s, Honda had withdrawn from Formula One, Senna had moved to Williams, and the team went three seasons without a win. With Mercedes-Benz engines, West sponsorship, and former Williams designer Adrian Newey, further championships came in 1998 and 1999 with driver Mika Häkkinen, and during the 2000s the team were consistent front-runners, with driver Lewis Hamilton taking their latest title in 2008. Ron Dennis retired as McLaren team principal in 2009, handing over to long-time McLaren employee Martin Whitmarsh. At the end of 2013, after the team's worst season since 2004, Whitmarsh was ousted. McLaren announced in 2013 that they would be using Honda engines from 2015 onwards, replacing Mercedes-Benz. The team raced as McLaren Honda for the first time since 1992 at the 2015 Australian Grand Prix. In September 2017, McLaren announced they had agreed on an engine supply with Renault from 2018 to 2020. McLaren is using Mercedes-Benz engines from the 2021 season until at least 2024."},
        {'name': 'Ferrari', 'teamPrincipal': 'Mattia Binotto', 'nationality': 'Italian',
         'yearsActive': 72, 'raceEngineer': 'Riccardo Adami','about':"Scuderia Ferrari was founded by Enzo Ferrari in 1929 to enter amateur drivers in various races,though Ferrari himself had raced in CMN (Costruzioni Maccaniche Nazionali) and Alfa Romeo cars before that date. The idea came about on the night of 16 November at a dinner in Bologna, where Ferrari solicited financial help from textile heirs Augusto and Alfredo Caniato and wealthy amateur racer Mario Tadini. He then gathered a team which at its peak included over forty drivers, most of whom raced in various Alfa Romeo 8C cars; Ferrari himself continued racing, with moderate success, until the birth of his first son Dino in 1932. The well-known prancing horse blazon first appeared at the 1932 Spa 24 Hours in Belgium on a two-car team of Alfa Romeo 8C 2300 Spiders, which finished first and second. Scuderia Ferrari is the racing division of luxury Italian auto manufacturer Ferrari and the racing team that competes in Formula One racing. The team is also nicknamed 'The Prancing Horse', in reference to their logo. It is the oldest surviving and most successful Formula One team, having competed in every world championship since the 1950 Formula One season.The team was founded by Enzo Ferrari, initially to race cars produced by Alfa Romeo, though by 1947 Ferrari had begun building its own cars. Among its important achievements outside Formula One are winning the World Sportscar Championship, 24 Hours of Le Mans, 24 Hours of Spa, 24 Hours of Daytona, 12 Hours of Sebring, Bathurst 12 Hour, races for Grand tourer cars and racing on road courses of the Targa Florio, the Mille Miglia and the Carrera Panamericana. The team is also known for its passionate support base, known as the tifosi. The Italian Grand Prix at Monza is regarded as the team's home race. As a constructor, Ferrari has a record 16 Constructors' Championships, the last of which was won in 2008. Alberto Ascari, Juan Manuel Fangio, Mike Hawthorn, Phil Hill, John Surtees, Niki Lauda, Jody Scheckter, Michael Schumacher and Kimi Räikkönen have won a record 15 Drivers' Championships for the team. Since Räikkönen's title in 2007 the team narrowly lost out on the 2008 drivers' title with Felipe Massa and the 2010 and 2012 drivers' titles with Fernando Alonso. The 2020 Tuscan Grand Prix marked Ferrari's 1000th Grand Prix in Formula One. Michael Schumacher is the team's most successful driver. Joining the team in 1996 and departing in 2006, he won five consecutive drivers' titles and 72 Grands Prix for the team. His titles came consecutively between 2000 and 2004, and the team won consecutive constructors' titles between 1999 and 2004; this was the team's most successful period. The team's 2022 drivers are Charles Leclerc and Carlos Sainz Jr. Scuderia Ferrari was founded by Enzo Ferrari in 1929 to enter amateur drivers in various races,though Ferrari himself had raced in CMN (Costruzioni Maccaniche Nazionali) and Alfa Romeo cars before that date. The idea came about on the night of 16 November at a dinner in Bologna, where Ferrari solicited financial help from textile heirs Augusto and Alfredo Caniato and wealthy amateur racer Mario Tadini. He then gathered a team which at its peak included over forty drivers, most of whom raced in various Alfa Romeo 8C cars; Ferrari himself continued racing, with moderate success, until the birth of his first son Dino in 1932. The well-known prancing horse blazon first appeared at the 1932 Spa 24 Hours in Belgium on a two-car team of Alfa Romeo 8C 2300 Spiders, which finished first and second."},
        {'name': 'Alpine', 'teamPrincipal': 'Otmar Szafnauer', 'nationality': 'French', 'yearsActive': 1,
         'raceEngineer': 'Karel Loos','about':"Alpine F1 Team, competing as BWT Alpine F1 Team is a Formula One constructor which made its debut at the start of the 2021 Formula One World Championship. Formerly named Renault F1 Team and owned by the French automotive company Groupe Renault, the team was rebranded for 2021 to promote Renault's sports car brand, Alpine, and continues to serve as Renault's works team. The chassis and managerial side of the team is based in Enstone, Oxfordshire, England, and the engine side of the team is based in Viry-Châtillon, a suburb of Paris, France. The team entity has a long history, first competing in Formula One in 1981 as Toleman, when the team was based in Witney, England.In 1986, following its purchase by Benetton Group, it was renamed and competed as Benetton. As Benetton, it won the 1995 Constructors' Championship and its driver, Michael Schumacher, won two Drivers' Championships in 1994 and 1995. Prior to the 1992 season it moved to its current location in Enstone, UK. By the 2000 season, Renault had purchased the team (for the first time), and by the 2002 season its name was changed to Renault F1 Team, and it was racing as Renault. Renault won the Constructors' Championship in 2005 and 2006 and its driver, Fernando Alonso won the Drivers' Championships in the same two years. In 2011, Lotus Cars came on board as a sponsor, and the team's name changed to Lotus Renault GP, though still racing as just 'Renault' for that season. By 2012, Genii Capital had a majority stake in the team, and from 2012 until 2015 the team's name was Lotus F1 Team, after its branding partner, and it raced as 'Lotus'. At the end of 2015, Renault had taken over the team for a second time, renaming it to Renault Sport Formula One Team.The team raced as 'Renault' again, from 2016, and continued as such until the end of the 2020 season.When discussing the history of the organisation as a whole rather than those of specific constructors it has operated, the colloquialism 'Team Enstone' is generally used.The team operates in a 17,000 m2 (180,000 sq ft) facility on a 17-acre site in Enstone. The involvement of the sportscar manufacturer Automobiles Alpine in Formula One can be traced back to 1968, when the Alpine A350 Grand Prix car was built, powered by a Gordini V8 engine. However, after initial testing with Mauro Bianchi at Zandvoort, the project was ended when it was found that the engine produced around 300 horsepower (220 kW) compared to the Cosworth V8 engines' 400.In 1975, the company produced the Alpine A500 prototype to test a 1.5 L V6 turbo engine for the Renault factory team which would eventually début in 1977. In September 2020, Groupe Renault announced their intention to use 'Alpine' as their works team's new name going forward to promote the Alpine marque, and thus the team is set to become known as the 'Alpine F1 Team' whilst retiring the 'Renault F1 Team' moniker after five years."},
        {'name': 'AlphaTauri', 'teamPrincipal': 'Franz Tost', 'nationality': 'Italian', 'yearsActive': 18,
         'raceEngineer': 'Pierre Hamelin','about':"Scuderia AlphaTauri, or simply AlphaTauri, is an Italian Formula One racing team and constructor. It is one of two Formula One constructors owned by Austrian beverage company Red Bull, the other being Red Bull Racing. The constructor was rebranded for the 2020 Formula One World Championship from 'Toro Rosso' to 'AlphaTauri' in order to promote the AlphaTauri fashion brand.According to Franz Tost and Helmut Marko, Scuderia AlphaTauri is no longer the junior team but the sister team to Red Bull Racing. In September 2019, Toro Rosso announced their intention to change their naming rights for the 2020 championship.It was announced on 1 December 2019 that the team had selected 'AlphaTauri' as their new moniker to promote parent company Red Bull's fashion label of the same name by purchasing Toro Rosso's naming rights. Thus, they became Scuderia AlphaTauri and retired the Scuderia Toro Rosso moniker after fourteen years .The team's involvement in Formula One can be traced back to the 1985 season when they first competed as Minardi. The team has been owned by Red Bull GmbH since the 2006 season. AlphaTauri had Daniil Kvyat and Pierre Gasly drive for them in their debut season.The team remained with the Honda engine, being the team's engine partner since the 2018 season.Sérgio Sette Câmara, Sébastien Buemi, and Jüri Vips were signed as the team's test drivers. The team achieved its first podium finish and race victory under the AlphaTauri name at the 2020 Italian Grand Prix, which also marked Pierre Gasly's first race victory and the first win for a French Formula One driver since Olivier Panis won the 1996 Monaco Grand Prix 24 years prior. AlphaTauri ended the year in 7th place on 107 points, 75 for Gasly and 32 for Kvyat."},
        {'name': 'Aston Martin', 'teamPrincipal': 'Lawrence Stroll', 'nationality': 'British',
         'yearsActive': 63, 'raceEngineer': 'Ben Michell','about':"Aston Martin is a British car manufacturer that has participated in Formula One in various forms. The company first participated in Formula One during the 1959 season where they debuted the DBR4 chassis using their own engine but it failed to score any points. They continued to perform poorly through the 1960 season, once again failing to score any points. As a result, Aston Martin decided to leave Formula One after 1960. A commercial rebranding of Racing Point F1 Team resulted in the team's return as Aston Martin in 2021, although it competes using Mercedes power units. The team, owned by Lawrence Stroll, has Sebastian Vettel and Lance Stroll as their race drivers. Aston Martin first entered Formula One with the DBR4, their first open-wheel racing car. The DBR4 was first built and tested in 1957 but did not make its Formula One debut until 1959. This delay was caused by the company prioritising the development of the DBR1 sports car, which went on to win the 1959 24 Hours of Le Mans. By the DBR4's world championship debut at the Dutch Grand Prix, it had become outdated and struggled for pace against its competitors, with Carroll Shelby and Roy Salvadori qualifying 10th and 13th respectively out of 15.Salvadori retired from the race in the early laps with an engine failure, with Shelby's car suffering the same fate later in the race. The team's next entry came at the British Grand Prix where Salvadori was surprised by qualifying in 2nd place.Early in the race, one of Shelby's ignition magnetos failed, harming his car's pace. The second magneto failed late in the race, causing his retirement. Salvadori could only hold on to 6th place, narrowly missing out on a points finish.At the Portuguese Grand Prix, both cars avoided issues to finish 6th and 8th but still failed to score points.Aston Martin's final entry of the season was the Italian Grand Prix where both cars continued to struggle, qualifying only 17th and 19th. During the race, Salvadori had run as high as 7th before suffering an engine failure whilst Shelby came home to finish 10th.The car was significantly outdated by its rivals and failed to score any points."},
        {'name': 'Williams', 'teamPrincipal': 'Jost Capito', 'nationality': 'British', 'yearsActive': 44,
         'raceEngineer': 'Paul Williams','about':"Williams Grand Prix Engineering Limited, currently racing in Formula One as Williams Racing, is a British Formula One motor racing team and constructor. It was founded by former team owner Frank Williams and automotive engineer Patrick Head. The team was formed in 1977 after Frank Williams's earlier unsuccessful F1 operation: Frank Williams Racing Cars which later became Wolf–Williams Racing in 1976. All of Williams F1 chassis are called 'FW' then a number, the FW being the initials of team co-founder and original owner, Frank Williams. The team's first race was the 1977 Spanish Grand Prix, where the new team ran a March chassis for Patrick Nève. Williams started manufacturing its own cars the following year, and Switzerland's Clay Regazzoni won Williams's first race at the 1979 British Grand Prix. At the 1997 British Grand Prix, Canadian Jacques Villeneuve scored the team's 100th race victory, making Williams one of only four teams in Formula One, alongside Ferrari, fellow British team McLaren, and Mercedes to win 100 races. Williams won nine Constructors' Championships between 1980 and 1997. This stood as a record until Ferrari surpassed it in 2000. Drivers for Williams have included Australia's Alan Jones; Finland's Keke Rosberg; Britain's Nigel Mansell, Damon Hill, David Coulthard and Jenson Button; Colombia's Juan Pablo Montoya; France's Alain Prost; Brazil's Nelson Piquet and Ayrton Senna; Italy's Ricardo Patrese; and Canada's Jacques Villeneuve. Each of these drivers, with the exception of Senna, Patrese, Coulthard, Montoya and Button, have won one Drivers' title with the team. Of those who have won the championship with Williams, only Jones, Rosberg and Villeneuve actually defended their title while still with the team. Piquet moved to Lotus after winning the 1987 championship, Mansell moved to the American-based Indy Cars after winning the 1992 championship, Prost retired from racing after his 4th World Championship in 1993, while Hill moved to Arrows after winning in 1996. No driver who has won a drivers' title with Williams has managed to again win a title with another team.Williams have worked with many engine manufacturers, most successfully with Renault, winning five of their nine Constructors' titles with the French company. Along with Ferrari, McLaren, Benetton and Renault, Williams is one of a group of five teams that won every Constructors' Championship between 1979 and 2008 and every Drivers' Championship from 1984 to 2008.Williams F1 also has business interests beyond Formula One racing. Based in Grove, Oxfordshire, England, Williams has established Williams Advanced Engineering and Williams Hybrid Power which take technology originally developed for Formula One and adapt it for commercial applications. In April 2014, Williams Hybrid Power were sold to GKN. Williams Advanced Engineering had a technology centre in Qatar until it was closed in 2014."},
        {'name': 'Haas', 'teamPrincipal': 'Guenther Steiner', 'nationality': 'American', 'yearsActive': 8,
         'raceEngineer': 'Ayao Komatsu','about':"Haas Formula LLC,competing as Haas F1 Team, is an American Formula One racing team established by NASCAR Cup Series team co-owner Gene Haas in April 2014. The team originally intended to make its debut at the start of the 2015 season but later elected to postpone their entry until the 2016 season.The team principal for the Haas F1 team is Guenther Steiner. The team is headquartered in Kannapolis, North Carolina, United States – 31 mi (50 km) from Charlotte – alongside sister team and NASCAR entrant Stewart-Haas Racing, though the two teams are separate entities. The team also established a forward base in Banbury, England, for the purpose of turning cars around between races during the European part of the calendar. Haas was the first American constructor to submit an F1 entry after the failed US F1 project in 2010, and it is the first American constructor to compete since the unrelated Haas Lola outfit raced in the 1985 and 1986 seasons. The Haas Lola team was owned by former McLaren boss Teddy Mayer and Carl Haas, who was not related to Gene Haas. Following the collapse of Marussia F1 during the 2014 season and the auctioning of their assets, Haas purchased the team's Banbury headquarters to serve as a forward base for their operations. Unrestricted by testing regulations until the time the team actually entered Formula One, Haas shook its new car down in December 2015 ahead of official pre-season testing at Barcelona in early 2016.[14] Haas approached Italian manufacturer Dallara to build their chassis, with a power unit supplied by Ferrari.Former Jaguar and Red Bull Racing technical director Guenther Steiner is the team principal.Haas confirmed its new car had passed the mandatory FIA crash tests in January 2016."},
        {'name': 'Alfa Romeo', 'teamPrincipal': 'Frédéric Vasseur', 'nationality': 'Italian',
         'yearsActive': 72, 'raceEngineer': 'Ruth Buscombe','about':"Italian motor manufacturer Alfa Romeo has participated many times in Formula One. It currently participates as Alfa Romeo F1 Team Orlen while being operated by Sauber Motorsport AG. The brand has competed in motor racing as both a constructor and engine supplier sporadically between 1950 and 1987, and later as a commercial partner since 2015. The company's works drivers won the first two World Drivers' Championships in the pre-war Alfetta: Nino Farina in 1950 and Juan Manuel Fangio in 1951. Following these successes, Alfa Romeo withdrew from Formula One. During the 1960s, although the company had no official presence in the top tier of motorsport several Formula One teams used independently developed Alfa Romeo engines to power their cars. In the early 1970s, Alfa provided Formula One support for their works driver Andrea de Adamich, supplying adapted versions of their 3-litre V8 engine from the Alfa Romeo Tipo 33/3 sports car to power Adamich's McLaren (1970) and March (1971) entries. None of these engine combinations scored championship points. In the mid-1970s, Alfa engineer Carlo Chiti designed a flat-12 engine to replace the T33 V8, which achieved some success in taking the 1975 World Sportscar Championship. Bernie Ecclestone, then owner of the Brabham Formula One team, persuaded Alfa Romeo to supply this engine free for the 1976 Formula One season. Although the Brabham-Alfa Romeo's first season was relatively modest, during the 1977 and 1978 World Championships their cars took 14 podium finishes, including two race victories for Niki Lauda. The company's sporting department, Autodelta, returned as the works team in 1979. This second period as a constructor was less successful than the first. Between the company's return and its withdrawal as a constructor at the end of 1985, Alfa works drivers did not win a race and the team never finished higher than sixth in the World Constructors' Championship. The team's engines were also supplied to Osella from 1983 to 1987, but they scored only two World Championship points during this period. The Alfa Romeo logo returned to Formula One in 2015, appearing on the Scuderia Ferrari cars. In late 2017, Alfa Romeo announced that they were to become title sponsors for Sauber from 2018, and had entered into a technical and commercial partnership with the team. Alfa Romeo returned to the sport when Sauber was renamed at the beginning of 2019."}]

    car_list = [
        {'model': 'Mercedes-AMG W13 E Performance', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,658lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Mercedes'},
        {'model': 'Red Bull Racing RB18', 'horsepower': '740bhp', 'engine': 'HRC 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Red Bull'},
        {'model': 'McLaren MCL36 Mercedes', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'McLaren'},
        {'model': 'Ferrari SF-75', 'horsepower': '740bhp', 'engine': 'Tipo 066/7 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Ferrari'},
        {'model': 'Alpine A522 Renault', 'horsepower': '740bhp', 'engine': 'Renault E22 90º V6',
         'weight': '1,753lbs', 'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Alpine'},
        {'model': 'AlphaTauri AT03', 'horsepower': '740bhp', 'engine': 'HRC 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'AlphaTauri'},
        {'model': 'Aston Martin AMR22 Mercedes', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Aston Martin'},
        {'model': 'Williams FW44 Mercedes', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Williams'},
        {'model': 'Haas VF-22 Ferrari', 'horsepower': '740bhp', 'engine': 'Ferrari Tipo 066/7 90º V6',
         'weight': '1,753lbs', 'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Haas'},
        {'model': 'Alfa Romeo Racing C42 Ferrari', 'horsepower': '740bhp',
         'engine': 'Ferrari Tipo 066/7 90º V6', 'weight': '1,753lbs', 'gearbox': 'Paddle Operated 8 speed Automatic',
         'constructor': 'Alfa Romeo'}]

    race_list = [
        {'location': 'Bahrain - Sakhir', 'trackLength': '5.412km', 'date': '18/03-20/03', 'laps': 57,
         'time': '15:00-17:00'},
        {'location': 'Saudi Arabia - Jeddah', 'trackLength': '6.174km', 'date': '25/03-27/03', 'laps': 50,
         'time': '18:00-20:00'},
        {'location': 'Australia - Melbourne', 'trackLength': '5.303km', 'date': '08/04-10/04', 'laps': 58,
         'time': '06:00-08:00'},
        {'location': 'Italy - Imola', 'trackLength': '5.793km', 'date': '22/04-24/04', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'United States - Miami', 'trackLength': '5.410km', 'date': '06/05-/08/05', 'laps': 57,
         'time': '08:30-22:30'},
        {'location': 'Spain - Catalunya', 'trackLength': '4.655km', 'date': '20/05-22/05', 'laps': 66,
         'time': '14:00-16:00'},
        {'location': 'Monaco - Monaco', 'trackLength': '3.337km', 'date': '27/05-29/05', 'laps': 78,
         'time': '14:00-16:00'},
        {'location': 'Azerbaijan - Baku', 'trackLength': '6.003km', 'date': '10/06/-12/06', 'laps': 51,
         'time': '12:00-14:00'},
        {'location': 'Canada - Montreal', 'trackLength': '4.361km', 'date': '17/06-19/06', 'laps': 70,
         'time': '19:00-21:00'},
        {'location': 'Great Britain - Baku', 'trackLength': '6.003km', 'date': '10/06-12/06', 'laps': 51,
         'time': '12:00-14:00'},
        {'location': 'Great Britain - Silverstone', 'trackLength': '5.891km', 'date': '01/07-03/07',
         'laps': 52, 'time': '15:00-17:00'},
        {'location': 'Austria - Spielberg', 'trackLength': '	4.318km', 'date': '10/07-tbc/07', 'laps': 71,
         'time': '14:00-16:00'},
        {'location': 'France - Le Castellet', 'trackLength': '5.842km', 'date': '22/07-24/07', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'Hungary - Mogyoród', 'trackLength': '4.381km', 'date': '29/07-31/07', 'laps': 70,
         'time': '14:00-16:00'},
        {'location': 'Belgium - Spa', 'trackLength': '7.004km', 'date': '26/08-28/08', 'laps': 44,
         'time': '14:00-16:00'},
        {'location': 'Netherlands - Zandvoort', 'trackLength': '4.259km', 'date': '02/09-04/09', 'laps': 72,
         'time': '14:00-16:00'},
        {'location': 'Italy - Monza', 'trackLength': '5.793km', 'date': '09/09-11/09', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'Singapore - Marina Bay', 'trackLength': '5.063km', 'date': '30/09-02/10',
         'laps': 61, 'time': '13:00-15:00'},
        {'location': 'Japan - Suzuka', 'trackLength': '5.807km', 'date': '07/10-09/10', 'laps': 53,
         'time': '06:00-08:00'},
        {'location': 'United States - Austin', 'trackLength': '5.513km', 'date': '21/10-23/10', 'laps': 56,
         'time': '20:00-22:00'},
        {'location': 'Mexico - Mexico City', 'trackLength': '4.304km', 'date': '28/10-30/10', 'laps': 71,
         'time': '20:00-22:00'},
        {'location': 'Brazi - São Paulo', 'trackLength': '4.309km', 'date': '11/11-13/11', 'laps': 71,
         'time': '20:00-22:00'},
        {'location': 'Abu Dhabi - United Arab Emirates', 'trackLength': '5.554km', 'date': '18/11-20/11', 'laps': 55,
         'time': '13:00-15:00'}]

    user_list = [
        {'username': 'Adam', 'password': 'tempy', 'favCar': 'Mercedes-AMG W13 E Performance', 'favTeam': 'Mercedes',
         'favDriver': 'Lewis Hamilton', 'aboutMe': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
         'picture': ''},
        {'username': 'Dave', 'password': 'test1', 'favCar': 'Red Bull Racing RB18', 'favTeam': 'Red Bull',
         'favDriver': 'Max Verstappen', 'aboutMe': 'Proin lectus nulla, condimentum nec mollis quis.', 'picture': ''},
        {'username': 'Lauren', 'password': 'drowssap', 'favCar': 'McLaren MCL36 Mercedes', 'favTeam': 'McLaren',
         'favDriver': 'Lando Norris', 'aboutMe': 'Pellentesque posuere justo tortor.', 'picture': ''},
        {'username': 'Meghan', 'password': 'sdea_$23-12FR%', 'favCar': 'Aston Martin AMR22 Mercedes',
         'favTeam': 'Aston Martin', 'favDriver': 'Sebastian Vettel', 'aboutMe': 'Donec euismod rutrum mauris.',
         'picture': ''},
        {'username': 'Steve', 'password': 'EFWJ!"£435_23jsd-=', 'favCar': 'Haas VF-22 Ferrari', 'favTeam': 'Haas',
         'favDriver': 'Mick Schumacher', 'aboutMe': 'Curabitur commodo nec enim in vestibulum.', 'picture': ''}]

    driver_rating_list = [
        {'driverID': 'Lewis Hamilton', 'userID': 'Adam', 'overallRating': '4', 'personality': '2',
         'aggressiveness': '5', 'awareness': '5', 'experience': '5', 'starts': '4', 'pace': '4', 'racecraft': '3'},
        {'driverID': 'Lando Norris', 'userID': 'Dave', 'overallRating': '3', 'personality': '3', 'aggressiveness': '4',
         'awareness': '4', 'experience': '2', 'starts': '4', 'pace': '2', 'racecraft': '3'},
        {'driverID': 'Nico Hulkenberg', 'userID': 'Lauren', 'overallRating': '3', 'personality': '5',
         'aggressiveness': '2', 'awareness': '3', 'experience': '5', 'starts': '3', 'pace': '2', 'racecraft': '4'},
        {'driverID': 'Lewis Hamilton', 'userID': 'Meghan', 'overallRating': '2', 'personality': '2',
         'aggressiveness': '3', 'awareness': '1', 'experience': '5', 'starts': '2', 'pace': '3', 'racecraft': '1'},
        {'driverID': 'Max Verstappen', 'userID': 'Steve', 'overallRating': '4', 'personality': '2',
         'aggressiveness': '5', 'awareness': '5', 'experience': '3', 'starts': '4', 'pace': '5', 'racecraft': '3'}]

    car_rating_list = [
        {'carID': 'Haas VF-22 Ferrari', 'userID': 'Adam', 'overallRating': '4', 'speed': '4', 'aerodynamics': '3',
         'aesthetics': '2', 'braking': '4', 'engine': '4'},
        {'carID': 'Mercedes-AMG W13 E Performance', 'userID': 'Dave', 'overallRating': '2', 'speed': '2',
         'aerodynamics': '4', 'aesthetics': '3', 'braking': '2', 'engine': '1'},
        {'carID': 'Red Bull Racing RB18', 'userID': 'Lauren', 'overallRating': '5', 'speed': '5', 'aerodynamics': '3',
         'aesthetics': '4', 'braking': '4', 'engine': '5'},
        {'carID': 'Haas VF-22 Ferrari', 'userID': 'Meghan', 'overallRating': '3', 'speed': '4', 'aerodynamics': '2',
         'aesthetics': '1', 'braking': '2', 'engine': '3'},
        {'carID': 'McLaren MCL36 Mercedes', 'userID': 'Steve', 'overallRating': '2', 'speed': '3', 'aerodynamics': '2',
         'aesthetics': '3', 'braking': '2', 'engine': '1'}]

    constructor_rating_list = [
        {'constructorID': 'Mercedes', 'userID': 'Adam', 'overallRating': '4', 'teamPrinciple': '4', 'raceStrategy': '5',
         'pitStop': '3'},
        {'constructorID': 'Mclaren', 'userID': 'Dave', 'overallRating': '3', 'teamPrinciple': '3', 'raceStrategy': '4',
         'pitStop': '2'},
        {'constructorID': 'Haas', 'userID': 'Lauren', 'overallRating': '4', 'teamPrinciple': '4', 'raceStrategy': '2',
         'pitStop': '2'},
        {'constructorID': 'Mercedes', 'userID': 'Meghan', 'overallRating': '2', 'teamPrinciple': '1',
         'raceStrategy': '4', 'pitStop': '3'},
        {'constructorID': 'Ferrari', 'userID': 'Steve', 'overallRating': '5', 'teamPrinciple': '4', 'raceStrategy': '2',
         'pitStop': '3'}]

    for i in constructor_list:
        add_constructor(i['name'], i['teamPrincipal'], i['nationality'], i['yearsActive'], i['raceEngineer'],i['about'])

    for i in driver_list:
        add_driver(i['name'], i['DOB'], i['height'], i['weight'], i['nationality'], i['driverNumber'],
                   i['seasonsWon'], i['podiumsWon'], i['constructor'])

    for i in car_list:
        add_car(i['model'], i['horsepower'], i['engine'], i['weight'], i['gearbox'], i['constructor'])

    for i in race_list:
        add_race(i['location'], i['trackLength'], i['date'], i['laps'], i['time'])


def add_driver(name, DOB, height, weight, nationality, driverNum, seasonsWon, podiumsWon, constructor):
    record = Driver.objects.get_or_create(name=name, DOB=DOB, height=height, weight=weight,
                                          nationality=nationality, driverNumber=driverNum, seasonsWon=seasonsWon,
                                          podiumsWon=podiumsWon,
                                          constructor=Constructor.objects.get(name=constructor))[0]
    record.save()
    print("Driver record \"" + name + "\" added.")
    return record


def add_constructor(name, teamPrincipal, nationality, yearsActive, raceEngineer,about):
    record = Constructor.objects.get_or_create(name=name, teamPrincipal=teamPrincipal, nationality=nationality,
                                               yearsActive=yearsActive, raceEngineer=raceEngineer,about=about)[0]
    record.save()
    print("Constructor record \"" + name + "\" added.")
    return record


def add_car(model, horsepower, engine, weight, gearbox, constructor):
    record = Car.objects.get_or_create(model=model, horsepower=horsepower, engine=engine,
                                       weight=weight, gearbox=gearbox,
                                       constructor=Constructor.objects.get(name=constructor))[0]
    record.save()
    print("Car record \"" + model + "\" added.")
    return record


def add_race(location, trackLength, date, laps, time):
    record = Race.objects.get_or_create(location=location, trackLength=trackLength, date=date, laps=laps, time=time)[0]
    record.save()
    print("Race record \"" + location + "\" added.")
    return record


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    news_api.get_news()  # ensures database is populated before running timed calls
    print("Database Populated! This script will continue to run fetching updated news every hour.")
    news_api.run()
