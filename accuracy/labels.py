#ground-truth boxes for the accuracy check, marked by eye on pairs/<pair>/<half>.png
#each box is (pair, half, label, x1, y1, x2, y2, what)
#label: 1 = vegetation (living plants: forest, trees, grass, crops), 0 = not vegetation
#x1, y1 = top-left corner, x2, y2 = bottom-right corner, in pixels
#only clear areas are labelled; mixed or unsure areas (dry grass, gardens, thin text over the photo) are left out
BOXES = [
 ("01","before",1,150,120,230,200,"rainforest"), ("01","before",1,440,250,500,320,"rainforest"),
 ("01","before",0,160,15,350,45,"date text"), ("01","before",0,20,505,140,545,"scale bar box"),
 ("01","after",1,50,100,150,200,"rainforest"), ("01","after",1,420,380,490,450,"rainforest"),
 ("01","after",0,240,380,290,440,"cleared land"), ("01","after",0,95,380,140,440,"cleared land"),
 ("01","after",0,160,10,345,45,"date text"),
 ("02","before",1,100,250,200,350,"rainforest"), ("02","before",1,250,450,350,530,"rainforest"),

 ("02","after",1,270,350,320,410,"forest patch"), ("02","after",1,185,560,225,590,"forest (national park)"),
 ("02","after",0,120,425,140,440,"cleared land"), ("02","after",0,170,400,190,415,"cleared land"),
 ("03","before",1,160,695,185,720,"tree"), ("03","before",1,355,560,385,585,"tree"), ("03","before",1,800,750,825,775,"tree"),
 ("03","before",0,400,90,500,100,"road"), ("03","before",0,815,815,850,845,"bare sand"),
 ("03","after",1,420,430,620,550,"grass park"), ("03","after",0,515,110,580,120,"road"),
 ("03","after",0,750,900,850,940,"bare earthworks"),
 ("04","before",1,80,250,160,320,"green crop field"), ("04","before",0,92,52,110,75,"bare soil field"),
 ("04","before",0,10,440,100,485,"2010 label"), ("04","before",0,230,470,270,520,"industrial roofs"),
 ("04","after",1,10,270,50,320,"green field"), ("04","after",0,60,180,100,225,"construction site"),
 ("04","after",0,160,260,210,300,"buildings"),
 ("05","before",1,150,25,220,55,"forest and grass"), ("05","before",1,280,360,340,395,"forest"),
 ("05","before",0,290,280,330,320,"bare construction"), ("05","before",0,15,15,100,40,"date label"),
 ("05","before",0,70,262,90,282,"roof"), ("05","before",0,128,88,145,105,"pond"),
 ("05","after",1,150,25,220,55,"forest and grass"), ("05","after",1,260,340,330,375,"forest"),
 ("05","after",0,180,280,230,320,"bare construction"), ("05","after",0,10,10,100,35,"date label"),
 ("05","after",0,128,88,145,105,"pond"),
 ("06","before",1,330,110,560,320,"green forest"), ("06","before",1,100,250,170,290,"forest edge"),
 ("06","before",0,300,390,420,470,"car park/buildings"), ("06","before",0,0,120,50,260,"car park"),
 ("06","after",1,100,180,215,320,"brown autumn trees"), ("06","after",1,740,80,840,180,"brown autumn trees"),
 ("06","after",0,520,90,595,300,"warehouse roof"), ("06","after",0,380,150,460,280,"bare soil"),
 ("06","after",0,303,90,315,150,"pond"),
 ("07","before",1,200,850,450,1100,"forest hills"), ("07","before",0,5,140,45,185,"lake"),
 ("07","after",1,400,960,580,1150,"forest hills"),
 ("07","after",0,200,450,400,650,"dense city"), ("07","after",0,435,120,475,165,"lake"),
 ("08","before",1,55,340,95,375,"grass field"), ("08","before",1,200,180,260,240,"green field"),
 ("08","before",0,380,380,430,420,"industrial roofs"),
 ("08","after",1,55,340,95,375,"grass field"), ("08","after",1,10,95,55,135,"dark green field"),
 ("08","after",0,292,305,330,335,"construction site"), ("08","after",0,380,380,430,420,"industrial roofs"),
]
