"""Indian delivery zones, cities, and states for synthetic Swiggy-style data."""

import random

# All states and union territories of India
INDIAN_STATES = (
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi",
    "Jammu and Kashmir",
    "Ladakh",
    "Lakshadweep",
    "Puducherry",
)

# Delivery zones keyed by city (locality / service area names)
ZONES_BY_CITY = {
    "Mumbai": [
        "Andheri West", "Andheri East", "Bandra West", "Bandra East", "Borivali",
        "Chembur", "Colaba", "Dadar", "Goregaon", "Juhu", "Kandivali", "Khar",
        "Lower Parel", "Malad", "Mulund", "Powai", "Santacruz", "Thane West",
        "Versova", "Worli", "Bhandup", "Ghatkopar", "Vikhroli", "Matunga",
    ],
    "Navi Mumbai": [
        "Vashi", "Nerul", "Belapur", "Kharghar", "Panvel", "Airoli", "Kopar Khairane",
        "Sanpada", "Seawoods", "Turbhe",
    ],
    "Thane": [
        "Ghodbunder Road", "Hiranandani Estate", "Kolshet", "Majiwada", "Naupada",
        "Wagle Estate", "Kasarvadavali", "Manpada",
    ],
    "Delhi": [
        "Connaught Place", "Dwarka", "Hauz Khas", "Karol Bagh", "Lajpat Nagar",
        "Malviya Nagar", "Mayur Vihar", "Model Town", "Pitampura", "Rohini",
        "Saket", "Vasant Kunj", "Rajouri Garden", "Janakpuri", "Greater Kailash",
        "Defence Colony", "Preet Vihar", "Paschim Vihar", "Shahdara", "Civil Lines",
    ],
    "New Delhi": [
        "Connaught Place", "Chanakyapuri", "Karol Bagh", "Paharganj", "Civil Lines",
        "Lodi Road", "India Gate", "Kashmere Gate", "ITO", "Pragati Maidan",
    ],
    "Noida": [
        "Sector 18", "Sector 62", "Sector 15", "Sector 50", "Sector 76",
        "Sector 137", "Greater Noida", "Sector 44", "Sector 34", "Sector 16",
    ],
    "Gurgaon": [
        "DLF Phase 1", "DLF Phase 2", "DLF Phase 3", "DLF Phase 4", "DLF Phase 5",
        "Cyber City", "Sohna Road", "MG Road", "Sector 14", "Sector 29",
        "Sector 56", "Palam Vihar", "South City", "Udyog Vihar",
    ],
    "Ghaziabad": [
        "Indirapuram", "Vaishali", "Kaushambi", "Raj Nagar", "Crossings Republik",
        "Vaishali Extension", "Sahibabad", "Vasundhara",
    ],
    "Faridabad": [
        "Sector 15", "Sector 21", "Sector 28", "NIT Faridabad", "Ballabgarh",
        "Old Faridabad", "Greenfield Colony",
    ],
    "Bangalore": [
        "Koramangala", "Indiranagar", "HSR Layout", "Whitefield", "Jayanagar",
        "Marathahalli", "Electronic City", "BTM Layout", "Malleshwaram", "Rajajinagar",
        "Hebbal", "Yelahanka", "Banashankari", "Bellandur", "Sarjapur Road",
        "MG Road", "Frazer Town", "Basavanagudi", "JP Nagar", "Ulsoor",
        "Domlur", "CV Raman Nagar", "Mahadevapura", "Brookefield",
    ],
    "Hyderabad": [
        "Banjara Hills", "Jubilee Hills", "Hitech City", "Gachibowli", "Madhapur",
        "Kondapur", "Kukatpally", "Secunderabad", "Begumpet", "Ameerpet",
        "Miyapur", "LB Nagar", "Uppal", "Manikonda", "Financial District",
        "Kompally", "Nacharam", "Tarnaka", "Abids", "Charminar",
    ],
    "Secunderabad": [
        "Paradise", "Secunderabad Station", "Trimulgherry", "Marredpally",
        "Bowenpally", "Alwal", "Malkajgiri", "Tarnaka",
    ],
    "Chennai": [
        "Anna Nagar", "T Nagar", "Adyar", "Velachery", "OMR", "Porur",
        "Nungambakkam", "Mylapore", "Kodambakkam", "Ambattur", "Tambaram",
        "Chromepet", "Guindy", "Egmore", "Royapettah", "Perungudi",
        "Sholinganallur", "Thoraipakkam", "Medavakkam", "Pallavaram",
    ],
    "Kolkata": [
        "Park Street", "Salt Lake", "New Town", "Ballygunge", "Gariahat",
        "Howrah", "Dum Dum", "Behala", "Jadavpur", "Rajarhat", "Esplanade",
        "Alipore", "Tollygunge", "Sealdah", "Bhowanipore", "Kasba",
    ],
    "Pune": [
        "Koregaon Park", "Hinjewadi", "Kothrud", "Viman Nagar", "Baner",
        "Aundh", "Wakad", "Hadapsar", "Kalyani Nagar", "Camp", "Deccan",
        "Magarpatta", "Kharadi", "Pimple Saudagar", "Bavdhan", "Sinhgad Road",
    ],
    "Ahmedabad": [
        "Satellite", "Vastrapur", "Navrangpura", "Maninagar", "Bopal",
        "SG Highway", "Prahlad Nagar", "Thaltej", "Gota", "Naranpura",
        "Ashram Road", "Ellisbridge", "Vejalpur", "Chandkheda",
    ],
    "Surat": [
        "Adajan", "Vesu", "Athwa", "Piplod", "City Light", "Varachha",
        "Katargam", "Pal", "Udhna", "Dumas Road",
    ],
    "Vadodara": [
        "Alkapuri", "Gotri", "Fatehgunj", "Manjalpur", "Akota", "Sayajigunj",
        "Karelibaug", "Vasna", "Subhanpura",
    ],
    "Rajkot": [
        "Kalawad Road", "University Road", "Raiya Road", "150 Feet Ring Road",
        "Yagnik Road", "Gondal Road",
    ],
    "Jaipur": [
        "Malviya Nagar", "Vaishali Nagar", "C Scheme", "Mansarovar", "Raja Park",
        "Tonk Road", "Jagatpura", "Bani Park", "Sitapura", "Vidhyadhar Nagar",
        "Pratap Nagar", "Jhotwara",
    ],
    "Jodhpur": [
        "Ratanada", "Shastri Nagar", "Paota", "Sardarpura", "Chopasni Housing Board",
        "Pal Road", "Mandore",
    ],
    "Udaipur": [
        "Hiran Magri", "Fatehpura", "Sector 4", "Saheli Marg", "Bhuwana",
        "Malla Talai", "Sukhadia Circle",
    ],
    "Lucknow": [
        "Gomti Nagar", "Hazratganj", "Aliganj", "Indira Nagar", "Mahanagar",
        "Alambagh", "Aminabad", "Jankipuram", "Vikas Nagar", "Hussainganj",
    ],
    "Kanpur": [
        "Swaroop Nagar", "Kakadeo", "Civil Lines", "Kidwai Nagar", "Panki",
        "Barra", "Govind Nagar", "Arya Nagar",
    ],
    "Agra": [
        "Sadar Bazaar", "Tajganj", "Dayal Bagh", "Sikandra", "Kamla Nagar",
        "Shahganj", "Fatehabad Road",
    ],
    "Varanasi": [
        "Lanka", "Sigra", "Bhelupur", "Cantt", "Lahurabir", "Godowlia",
        "Mahmoorganj", "Assi",
    ],
    "Chandigarh": [
        "Sector 17", "Sector 22", "Sector 35", "Sector 8", "Sector 9",
        "Sector 10", "Sector 11", "Sector 26", "Sector 34", "Sector 43",
        "Manimajra", "Panchkula Border",
    ],
    "Ludhiana": [
        "Model Town", "Sarabha Nagar", "BRS Nagar", "Pakhowal Road",
        "Ferozepur Road", "Civil Lines", "Dugri",
    ],
    "Amritsar": [
        "Ranjit Avenue", "Lawrence Road", "Mall Road", "Batala Road",
        "GT Road", "Cantt", "Hall Bazaar",
    ],
    "Patiala": [
        "Model Town", "Urban Estate", "Rajpura Road", "Sirhind Road",
        "Tripuri", "Adalat Bazaar",
    ],
    "Kochi": [
        "Edappally", "Kakkanad", "Marine Drive", "Fort Kochi", "Palarivattom",
        "Kaloor", "Vyttila", "Aluva", "Thripunithura", "MG Road Kochi",
    ],
    "Thiruvananthapuram": [
        "Kowdiar", "Pattom", "Kazhakootam", "Technopark", "Vellayambalam",
        "Statue", "Palayam", "Sreekaryam",
    ],
    "Kozhikode": [
        "Mavoor Road", "Beach Road", "Palayam", "Nadakkavu", "Feroke",
        "Medical College",
    ],
    "Coimbatore": [
        "RS Puram", "Peelamedu", "Saibaba Colony", "Gandhipuram", "Singanallur",
        "Saravanampatti", "Race Course", "Town Hall", "Ganapathy",
    ],
    "Madurai": [
        "KK Nagar", "Anna Nagar Madurai", "Simmakkal", "Bypass Road",
        "Tallakulam", "Goripalayam",
    ],
    "Indore": [
        "Vijay Nagar", "Palasia", "Sapna Sangeeta", "AB Road", "Rau",
        "Bhanwarkuan", "Scheme 54", "MG Road Indore", "Bhawarkua",
    ],
    "Bhopal": [
        "MP Nagar", "Arera Colony", "New Market", "Kolar Road", "Hoshangabad Road",
        "Bairagarh", "Shahpura", "TT Nagar",
    ],
    "Nagpur": [
        "Civil Lines Nagpur", "Sadar", "Dharampeth", "Wardha Road", "Manish Nagar",
        "Hingna", "Kamptee Road", "Sitabuldi",
    ],
    "Nashik": [
        "College Road", "Gangapur Road", "Panchavati", "Satpur", "CIDCO",
        "Ambad", "Dwarka Nashik",
    ],
    "Pimpri-Chinchwad": [
        "Pimpri", "Chinchwad", "Wakad", "Ravet", "Nigdi", "Akurdi",
        "Bhosari", "Thergaon",
    ],
    "Visakhapatnam": [
        "MVP Colony", "Dwaraka Nagar", "Gajuwaka", "Madhurawada", "Siripuram",
        "Beach Road Vizag", "Jagadamba Junction", "PM Palem",
    ],
    "Vijayawada": [
        "Benz Circle", "Governorpet", "Labbipet", "Patamata", "Guntur Road",
        "Auto Nagar", "Poranki",
    ],
    "Warangal": [
        "Hanamkonda", "Kazipet", "Subedari", "NIT Warangal", "Hunter Road",
    ],
    "Patna": [
        "Boring Road", "Kankarbagh", "Bailey Road", "Patliputra", "Fraser Road",
        "Rajendra Nagar", "Danapur", "Exhibition Road",
    ],
    "Ranchi": [
        "Main Road", "Lalpur", "Harmu", "Doranda", "Kanke", "Morabadi",
        "Hinoo", "Ashok Nagar Ranchi",
    ],
    "Jamshedpur": [
        "Bistupur", "Sakchi", "Kadma", "Sonari", "Telco", "Baridih",
    ],
    "Bhubaneswar": [
        "Patia", "Saheed Nagar", "Nayapalli", "Khandagiri", "Chandrasekharpur",
        "Master Canteen", "Unit 4", "Damana",
    ],
    "Cuttack": [
        "Buxi Bazaar", "College Square", "Choudhury Bazar", "CDA Sector 6",
        "Link Road",
    ],
    "Guwahati": [
        "GS Road", "Zoo Road", "Dispur", "Paltan Bazaar", "Beltola",
        "Six Mile", "Hatigaon", "Maligaon",
    ],
    "Shillong": [
        "Police Bazaar", "Laitumkhrah", "Laban", "Nongthymmai", "Mawlai",
    ],
    "Dehradun": [
        "Rajpur Road", "Clement Town", "Ballupur", "Prem Nagar", "Dalanwala",
        "Indira Nagar Dehradun", "Clock Tower",
    ],
    "Haridwar": [
        "Ranipur", "Jwalapur", "Har Ki Pauri", "Sapta Rishi Road", "Kankhal",
    ],
    "Raipur": [
        "Pandri", "Telibandha", "Shankar Nagar", "Civil Lines Raipur",
        "Devendra Nagar", "Mowa",
    ],
    "Bilaspur": [
        "Link Road Bilaspur", "Vyapar Vihar", "Torwa", "Mangla", "Koni",
    ],
    "Goa": [
        "Panaji", "Margao", "Mapusa", "Calangute", "Candolim", "Porvorim",
        "Vasco da Gama", "Anjuna", "Baga",
    ],
    "Mangalore": [
        "Kadri", "Hampankatta", "Bejai", "Kankanady", "Surathkal", "Lalbagh",
    ],
    "Mysore": [
        "Vijayanagar Mysore", "Gokulam", "Saraswathipuram", "Hebbal Mysore",
        "Kuvempunagar", "Bannimantap",
    ],
    "Hubli": [
        "Vidyanagar", "Gokul Road", "Deshpande Nagar", "Keshwapur", "Station Road Hubli",
    ],
    "Siliguri": [
        "Sevoke Road", "Hill Cart Road", "Pradhan Nagar", "Salugara", "Matigara",
    ],
    "Gangtok": [
        "MG Marg", "Deorali", "Tadong", "Arithang", "Ranipool",
    ],
    "Imphal": [
        "Paona Bazaar", "Thangal Bazaar", "Lamphelpat", "Kwakeithel", "Singjamei",
    ],
    "Agartala": [
        "Battala", "GB Bazaar", "Durjaynagar", "Kunjaban", "Nagarjala",
    ],
    "Shimla": [
        "Mall Road Shimla", "Sanjauli", "Summer Hill", "Lakkar Bazaar", "Boileauganj",
    ],
    "Srinagar": [
        "Lal Chowk", "Rajbagh", "Boulevard", "Hazratbal", "Nowgam", "Hyderpora",
    ],
    "Jammu": [
        "Gandhi Nagar Jammu", "Trikuta Nagar", "Bahu Plaza", "Narwal", "Channi",
    ],
    "Amravati": [
        "Rajapeth", "Camp Amravati", "Badnera", "Walgaon Road",
    ],
    "Aurangabad": [
        "Cidco", "Jalna Road", "Station Road Aurangabad", "Garkheda", "Paithan Gate",
    ],
    "Solapur": [
        "Akkalkot Road", "Pandharpur Road", "Siddheshwar", "Hotgi Road",
    ],
    "Kolhapur": [
        "Tarabai Park", "Rajarampuri", "Laxmipuri", "Shahupuri", "Rankala",
    ],
    "Tiruchirappalli": [
        "Cantonment Trichy", "Thillai Nagar", "Srirangam", "Woraiyur", "Chatram Bus Stand",
    ],
    "Salem": [
        "Fairlands", "Suramangalam", "Hasthampatti", "Five Roads", "Gugai",
    ],
    "Tiruppur": [
        "Avinashi Road", "Kumar Nagar", "PN Road", "Velampalayam",
    ],
    "Vellore": [
        "Katpadi", "Sathuvachari", "Gandhi Road Vellore", "Bagayam",
    ],
    "Pondicherry": [
        "White Town", "Mission Street", "Heritage Town", "Lawspet", "Muthialpet",
    ],
    "Guntur": [
        "Brodipet", "Arundelpet", "Lakshmipuram", "Autonagar Guntur", "Nallapadu",
    ],
    "Nellore": [
        "Trunk Road", "Stonehouse Pet", "Gandhi Nagar Nellore", "Balaji Nagar",
    ],
    "Tirupati": [
        "Renigunta Road", "RC Road", "Air Bypass Road", "Tiruchanoor Road",
    ],
    "Muzaffarpur": [
        "Maripur", "Bochaha Road", "Motijheel", "Club Road Muzaffarpur",
    ],
    "Gorakhpur": [
        "Golghar", "Civil Lines Gorakhpur", "Railway Colony", "Geeta Vihar",
    ],
    "Allahabad": [
        "Civil Lines Prayagraj", "Katra", "George Town", "Tagore Town", "Naini",
    ],
    "Meerut": [
        "Shastri Nagar Meerut", "Begum Bridge", "Delhi Road Meerut", "Modipuram",
    ],
    "Moradabad": [
        "Civil Lines Moradabad", "Delhi Road Moradabad", "Mauza Salampur",
    ],
    "Bareilly": [
        "Civil Lines Bareilly", "Pilibhit Bypass", "Rajendra Nagar Bareilly",
    ],
    "Aligarh": [
        "Center Point", "Dodhpur", "Great Value", "Ramghat Road",
    ],
    "Mathura": [
        "Dampier Nagar", "Highway Plaza", "Govardhan Road", "Station Road Mathura",
    ],
    "Rohtak": [
        "Model Town Rohtak", "Delhi Road Rohtak", "Sector 14 Rohtak",
    ],
    "Panipat": [
        "GT Road Panipat", "Model Town Panipat", "Sector 25 Panipat",
    ],
    "Karnal": [
        "Sector 7 Karnal", "Kunjpura Road", "Sector 13 Karnal",
    ],
    "Sonipat": [
        "Sector 14 Sonipat", "GT Road Sonipat", "Murthal Road",
    ],
    "Bathinda": [
        "Model Town Bathinda", "Cantt Bathinda", "Mall Road Bathinda",
    ],
    "Jalandhar": [
        "Model Town Jalandhar", "Civil Lines Jalandhar", "GT Road Jalandhar",
    ],
}

# City -> state (every city in ZONES_BY_CITY must appear here)
CITY_STATE = {
    "Mumbai": "Maharashtra",
    "Navi Mumbai": "Maharashtra",
    "Thane": "Maharashtra",
    "Delhi": "Delhi",
    "New Delhi": "Delhi",
    "Noida": "Uttar Pradesh",
    "Gurgaon": "Haryana",
    "Ghaziabad": "Uttar Pradesh",
    "Faridabad": "Haryana",
    "Bangalore": "Karnataka",
    "Hyderabad": "Telangana",
    "Secunderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Kolkata": "West Bengal",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Surat": "Gujarat",
    "Vadodara": "Gujarat",
    "Rajkot": "Gujarat",
    "Jaipur": "Rajasthan",
    "Jodhpur": "Rajasthan",
    "Udaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh",
    "Kanpur": "Uttar Pradesh",
    "Agra": "Uttar Pradesh",
    "Varanasi": "Uttar Pradesh",
    "Chandigarh": "Chandigarh",
    "Ludhiana": "Punjab",
    "Amritsar": "Punjab",
    "Patiala": "Punjab",
    "Kochi": "Kerala",
    "Thiruvananthapuram": "Kerala",
    "Kozhikode": "Kerala",
    "Coimbatore": "Tamil Nadu",
    "Madurai": "Tamil Nadu",
    "Indore": "Madhya Pradesh",
    "Bhopal": "Madhya Pradesh",
    "Nagpur": "Maharashtra",
    "Nashik": "Maharashtra",
    "Pimpri-Chinchwad": "Maharashtra",
    "Visakhapatnam": "Andhra Pradesh",
    "Vijayawada": "Andhra Pradesh",
    "Warangal": "Telangana",
    "Patna": "Bihar",
    "Ranchi": "Jharkhand",
    "Jamshedpur": "Jharkhand",
    "Bhubaneswar": "Odisha",
    "Cuttack": "Odisha",
    "Guwahati": "Assam",
    "Shillong": "Meghalaya",
    "Dehradun": "Uttarakhand",
    "Haridwar": "Uttarakhand",
    "Raipur": "Chhattisgarh",
    "Bilaspur": "Chhattisgarh",
    "Goa": "Goa",
    "Mangalore": "Karnataka",
    "Mysore": "Karnataka",
    "Hubli": "Karnataka",
    "Siliguri": "West Bengal",
    "Gangtok": "Sikkim",
    "Imphal": "Manipur",
    "Agartala": "Tripura",
    "Shimla": "Himachal Pradesh",
    "Srinagar": "Jammu and Kashmir",
    "Jammu": "Jammu and Kashmir",
    "Amravati": "Maharashtra",
    "Aurangabad": "Maharashtra",
    "Solapur": "Maharashtra",
    "Kolhapur": "Maharashtra",
    "Tiruchirappalli": "Tamil Nadu",
    "Salem": "Tamil Nadu",
    "Tiruppur": "Tamil Nadu",
    "Vellore": "Tamil Nadu",
    "Pondicherry": "Puducherry",
    "Guntur": "Andhra Pradesh",
    "Nellore": "Andhra Pradesh",
    "Tirupati": "Andhra Pradesh",
    "Muzaffarpur": "Bihar",
    "Gorakhpur": "Uttar Pradesh",
    "Allahabad": "Uttar Pradesh",
    "Meerut": "Uttar Pradesh",
    "Moradabad": "Uttar Pradesh",
    "Bareilly": "Uttar Pradesh",
    "Aligarh": "Uttar Pradesh",
    "Mathura": "Uttar Pradesh",
    "Rohtak": "Haryana",
    "Panipat": "Haryana",
    "Karnal": "Haryana",
    "Sonipat": "Haryana",
    "Bathinda": "Punjab",
    "Jalandhar": "Punjab",
}

ALL_INDIAN_CITIES = tuple(ZONES_BY_CITY.keys())
ALL_INDIAN_ZONES = tuple(zone for zones in ZONES_BY_CITY.values() for zone in zones)


def pick_indian_location():
    """Return (city, state, zone) with zone belonging to the chosen city."""
    city = random.choice(ALL_INDIAN_CITIES)
    zone = random.choice(ZONES_BY_CITY[city])
    state = CITY_STATE[city]
    return city, state, zone


def get_state_for_city(city):
    return CITY_STATE.get(city)


def get_zones_for_city(city):
    return ZONES_BY_CITY.get(city, ())
