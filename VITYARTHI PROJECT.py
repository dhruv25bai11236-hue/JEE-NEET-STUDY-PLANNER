import random
import math
import datetime
syllabus = {'Physics': ['Mechanics (Kinematics, Laws of motion, Work-power-energy, Rotational motion, Center of mass, Gravitation, Fluid mechanics, Simple Harmonic Motion)',
        'Thermodynamics (Laws of thermodynamics, Heat transfer, Thermal properties of matter, Calorimetry)','Electromagnetism (Electrostatics, Current electricity, Magnetic effects, Electromagnetic induction, Alternating current, Electromagnetic waves)',
        'Optics (Ray optics, Wave optics, Optical instruments, Defects of vision)', 'Modern Physics (Dual nature of matter, Atomic physics, Nuclear physics, Photoelectric effect, X-rays)',
        'Waves & Oscillations (Progressive waves, Standing waves, Sound, Doppler effect)','Fluid Mechanics (Properties of fluids, Archimedes’ principle, Pascal’s law, Bernoulli’s theorem)',
        'Gravitation (Universal law, Kepler’s laws, Satellites, Escape velocity)'],
       
        'Chemistry': ['Physical Chemistry (Atomic structure, Chemical bonding, Equilibrium, Thermodynamics, Electrochemistry, Solutions, Solid state, Surface chemistry)',
        'Organic Chemistry (General organic chemistry, Hydrocarbons, Haloalkanes, Alcohols, Phenols, Ethers, Carbonyls, Carboxylic acids, Amines, Polymers, Biomolecules, Environmental chemistry)',
        'Inorganic Chemistry (Periodic table, s/p/d/f-block elements, Coordination compounds, Metallurgy, Qualitative analysis, Hydrogen, Group chemistry)',
        'Chemical Bonding (Types of bonding, Molecular orbital theory, VSEPR theory, Hybridization, Bond parameters)', 'Equilibrium (Chemical equilibrium, Ionic equilibrium, Buffer solutions, Solubility product, Common ion effect)',
        'Electrochemistry (Electrolytes, Conductivity, EMF, Electrochemical cells, Corrosion)','Coordination Compounds (Nomenclature, Isomerism, Bonding theories, Applications)'],
        
         'Mathematics': [ 'Algebra (Quadratic equations, Sequences & series, Binomial theorem, Complex numbers, Matrices & determinants)','Calculus (Limits & continuity, Differentiation, Application of derivatives, Integration, Definite integrals, Differential equations)',
        'Trigonometry (Basic formulas, Identities, Heights & distances, Inverse trigonometric functions)','Coordinate Geometry (Straight lines, Circles, Parabola, Ellipse, Hyperbola, Conic sections)',
        'Vectors & 3D Geometry (Vector algebra, Dot/Cross product, Lines & planes in space)','Probability & Statistics (Basic probability, Conditional probability, Bayes’ theorem, Mean, Median, Mode, Standard deviation)',
        'Differential Equations (Formation, Solution methods, Applications)'],

         'Biology': ['Cell Biology (Cell structure, Cell cycle, Prokaryotes & eukaryotes, Biomolecules)','Genetics (Mendelian genetics, Chromosomes, DNA/RNA, Genetic disorders, Biotechnology basics)','Ecology (Ecosystems, Biodiversity, Food chains/webs, Conservation, Environmental issues)',
        'Human Physiology (Digestive, Respiratory, Circulatory, Excretory, Nervous, Endocrine, Reproductive systems)','Plant Physiology (Photosynthesis, Respiration, Transpiration, Mineral nutrition, Growth regulators)',
        'Evolution (Darwinism, Natural selection, Speciation, Human evolution)','Biotechnology (Genetic engineering, PCR, Cloning, Biotech in health & agriculture)',
        'Reproduction (Reproductive health, Sexual/Asexual reproduction, Gametogenesis, Fertilization)']}

Exams = {'1':{'name':'JEE','Subjects':['Physics','Chemistry','Mathematics']},
         '2':{'name':'NEET','Subjects':['Physics','Chemistry','Biology']}}

Books = {'JEE':{'Physics':['HC Verma', 'DC Pandey', 'NCERT Physics'],
                 'Chemistry': ['NCERT Chemistry', 'OP Tandon', 'MS Chouhan'],
                'Mathematics': ['RD Sharma', 'Cengage', 'NCERT Mathematics', 'Black Book']},
         'NEET': {'Physics': ['NCERT Physics', 'DC Pandey', 'HC Verma'],
                 'Chemistry': ['NCERT Chemistry', 'OP Tandon', 'MS Chouhan'],
                'Biology': ['NCERT Biology', 'Trueman', 'GR Bathla Biology']}}

Tips = {'Physics': ['Focus on numerical problems', 'Practice with diagrams', 'Solve past papers', 'Review key formulas'],
    'Chemistry': ['Make reaction charts', 'Practice naming compounds', 'Revise periodic trends', 'Work on exceptions'],
    'Mathematics': ['Practice regularly', 'Revise formulas', 'Time your solves', 'Focus on weak areas'],
    'Biology': ['Make mind maps', 'Draw diagrams', 'Memorize NCERT lines', 'Use mnemonics for terms']}

def header(Heading):
    print("\n" + "="*40)
    print(" " + Heading)
    print("="*40 + "\n")

def timetable(days_left):
    if (days_left<90):
        return 12
    elif(days_left<180):
        return 10
    elif (days_left < 300):
        return 8
    else:
        return 6
    
def  Schedule(hrs):
    session = math.ceil(hrs/2)
    time = 6
    Schedule = []
    for i in range (session):
        Schedule.append("{:02d}:00 to {:02d}:00 |Study sessions {}.".format(int(time),int(time)+2,i+1))
        time +=2
        if i<session-1:
            Schedule.append("{:02d}:0 to {:02d}:30 | Break".format(int(time),int(time)))
            time += 0.5
    return Schedule

def Days(Subjects, total_days):
    chapters=[]
    for sub in Subjects:
        for chap in syllabus [sub]:
            chapters.append((sub,chap))
    random.shuffle(chapters)
    Days = total_days - 31
    chaptersnumber = len(chapters)  
    basedays = Days // chaptersnumber
    extradays = Days % chaptersnumber
    plan = []  
    presentday = 1
    for i in range(len(chapters)):
      Day = basedays + (1 if i <extradays else 0) 
      startday = presentday
      endday = presentday + Day-1
      plan.append((startday,endday,chapters[i][0],chapters[i][1]))
      presentday = endday + 1
    return plan , presentday

def main():
    header("Welcome to JEE/NEET Study Planner")
    print("Which Exam are you Targeting ? ")
    print(" 1. JEE ")
    print(" 2. NEET ")
    ExamChoice = input("Enter 1 for JEE or 2 for NEET : ").strip()
    while ExamChoice not in Exams :
        ExamChoice = input("OOPS! Please Enter 1 or 2 as per your path: ").strip()
    exam = Exams[ExamChoice]
    print(f"Success Roadmap - {exam['name']} Prepration")

    while True:
        dateinput = input("When is your Exam scheduled? (Type as DD-MM-YY): ").strip()
        try:
            examdate = datetime.datetime.strptime(dateinput,"%d-%m-%Y")
            daysleft = (examdate - datetime.datetime.now()).days
            if daysleft <=0:
                print("Exam date should be upcomming.Please re-enter a future date.")
            else:
                break
        except:
            print("Couldn't understand the date.Please use DD-MM-YY format (e.g.,07-03-2025)")

    print(f"You have {daysleft} days left - Let's make each one count!")
    print("Choose the subject(s) you want to plan for today:")
    for i,sub in enumerate(exam["Subjects"] , 1 ):
        print(f" {i}.{sub}")
    print(f"{len(exam["Subjects"])+1}.All listed Subjects")
    subjectchoice = input("Type the number of your choice: ").strip()
    if subjectchoice == str(len(exam["Subjects"])+1):
        selectedsubjects = exam["Subjects"]
    else:
        try:
            selectedsubjects = [exam["Subjects"][int(subjectchoice)-1]]
        except:
            print("Input wasn't recognized. So let's cover all subjects for maximum benifits ! ")
            selectedsubjects = exam["Subjects"]

    header("Prepration Tips and Recommended Books")
    for sub in selectedsubjects:
        print(f"{sub}")
        print("Tips:" + "|" .join(Tips[sub][:2]))
        print("Best Books: " + ",".join(Books[exam["name"]][sub]))

    # Daily Routine
    header("Your Daily Schedule")
    studyhours = timetable(daysleft) 
    print(f"Recommended Study Hours: {studyhours}.") 
    for line in Schedule(studyhours):
        print(line)
    #chapter allocation
    header("Your Chapter-by-Chapter Path")
    plan , revisionstart = Days(selectedsubjects,daysleft)
    currentsub = ""
    for start , end , sub , chap in plan:
        if sub != currentsub:
            print(f"{sub.upper()}")
            print("-"*36)
            currentsub =sub
        daytext = f"Day{start}" if start == end else f"Day {start}--{end}"
        print(f"{daytext}:{chap}")
        
        if random.random()>0.75:
            print("Spend extra time on challenging topics topics today. ",
                  "Attempt more practice MCQs.","Summarize concepts in our own words.","Revise errors from last mock test.")
            
    # Final week strategy
    print("\n Your 3-Day Countdown Strategy")
    print(f"Day {revisionstart}: Rapid revision from notes and flashcards.")
    print(f"Day {daysleft - 1}: Take a mock test, then clamly review your mistakes.")
    print(f"Day {daysleft}: Exam Day! Light review and bring your confidence!")

    # Succes mantras
    header("Stay Inspired -Your Success Mantras.")
    mantras = ["Small steps done consistently lead to greatness.","Keep your mind healthy and take mindful breaks"
               "Small steps done consistently lead to greaatness","Avoid last minute cramming & Trust your preparation."]
    print(mantras)

    header("All the Best!")
    print(f"You have {daysleft} days to reach your dream. Trust yoursellf, and let each day's effort bring you closer! ")
    print("Remember, Success comes from dedication,not pressure. you're on a path to greatness!")

if __name__ == "__main__":
    main()   