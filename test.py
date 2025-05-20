from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/brands')
def brands():
    return render_template('brands.html')

@app.route('/translationtest')
def translationtest():
    return render_template('translationtest.html')


products_indus = [
    {"id": 1, "name": "Industrial Robot A", "price": 5000, "image": "Indus.jpg", 
     "short_description": "A powerful industrial robot for precise operations.", 
     "long_description": "This robot is designed for repetitive tasks like assembly and material handling, offering high precision and speed.", "brand":"DBT"},
    
    {"id": 2, "name": "Industrial Robot B", "price": 7500, "image": "Indus.jpg", 
     "short_description": "Versatile robot for a variety of industries.", 
     "long_description": "Ideal for industries such as automotive and electronics, it ensures reliability and flexibility in its operations.","brand":"UBT"},
    
    {"id": 3, "name": "Industrial Robot X", "price": 6000, "image": "Indus.jpg", 
     "short_description": "A high-speed industrial robot for automated processes.", 
     "long_description": "Built to handle high-volume tasks in fast-paced environments, the Robot X optimizes production efficiency."},
    
    {"id": 4, "name": "Industrial Robot Y", "price": 3000, "image": "Indus.jpg", 
     "short_description": "Compact robot for small-scale automation.", 
     "long_description": "Perfect for smaller production lines, the Robot Y is designed to automate light tasks with high efficiency."},
    
    {"id": 5, "name": "Industrial Robot Z", "price": 8500, "image": "Indus.jpg", 
     "short_description": "Advanced robot with AI capabilities.", 
     "long_description": "Equipped with AI, this robot can learn and adapt to different tasks, improving its efficiency over time."},
    
    {"id": 6, "name": "Industrial Robot", "price": 9000, "image": "Indus.jpg", 
     "short_description": "Multi-purpose robot for diverse applications.", 
     "long_description": "Highly adaptable, this robot can handle a range of tasks from welding to assembly and material handling."},
    
    {"id": 7, "name": "Industrial Robot", "price": 4000, "image": "Indus.jpg", 
     "short_description": "Efficient robot for logistics and warehousing.", 
     "long_description": "This robot specializes in picking, sorting, and moving items efficiently in a warehouse or logistics environment."},
    
    {"id": 8, "name": "Industrial Robot", "price": 12000, "image": "Drone1.jpg", 
     "short_description": "High-end robot for precision tasks.", 
     "long_description": "The Drone 1 is designed to handle precision tasks such as inspection and small-scale assembly."},
    
    {"id": 9, "name": "Industrial Robot", "price": 12000, "image": "Drone2.jpg", 
     "short_description": "Robotic arm designed for intricate operations.", 
     "long_description": "Specially designed for delicate tasks, this robotic arm excels in precision-driven operations."},
    
    {"id": 10, "name": "Industrial Robot", "price": 12000, "image": "Drone3.jpg", 
     "short_description": "Versatile drone robot for heavy-duty tasks.", 
     "long_description": "Built for heavy-duty applications, the Drone 3 can carry large payloads and perform complex operations."},
    
    {"id": 11, "name": "Industrial Robot", "price": 12000, "image": "Drone4.jpg", 
     "short_description": "Drone robot with advanced navigation capabilities.", 
     "long_description": "Equipped with advanced sensors, this robot can navigate autonomously in complex environments."},
    
    {"id": 12, "name": "Industrial Robot", "price": 12000, "image": "Drone5.jpg", 
     "short_description": "Compact robot ideal for small spaces.", 
     "long_description": "With its compact design, this robot can maneuver in tight spaces, making it ideal for confined environments."},
    
    {"id": 13, "name": "Industrial Robot", "price": 12000, "image": "Drone6.jpg", 
     "short_description": "High-speed robot designed for assembly lines.", 
     "long_description": "This robot excels at high-speed assembly, helping to maximize throughput on assembly lines."},
    
    {"id": 14, "name": "Industrial Robot", "price": 12000, "image": "Drone7.jpg", 
     "short_description": "Robot with exceptional flexibility for various tasks.", 
     "long_description": "Its flexible design allows the robot to perform tasks ranging from painting to welding with high precision."},
    
    {"id": 15, "name": "Industrial Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Robust robot for harsh environments.", 
     "long_description": "Built to withstand extreme conditions, this robot performs flawlessly in harsh manufacturing environments."},

     {"id": 16, "name": "Industrial Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Robust robot for harsh environments.", 
     "long_description": "Built to withstand extreme conditions, this robot performs flawlessly in harsh manufacturing environments."},

     {"id": 17, "name": "Industrial Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Robust robot for harsh environments.", 
     "long_description": "Built to withstand extreme conditions, this robot performs flawlessly in harsh manufacturing environments."},

     {"id": 18, "name": "Industrial Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Robust robot for harsh environments.", 
     "long_description": "Built to withstand extreme conditions, this robot performs flawlessly in harsh manufacturing environments."},

     {"id": 19, "name": "Industrial Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Robust robot for harsh environments.", 
     "long_description": "Built to withstand extreme conditions, this robot performs flawlessly in harsh manufacturing environments."},

     {"id": 20, "name": "Industrial Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Robust robot for harsh environments.", 
     "long_description": "Built to withstand extreme conditions, this robot performs flawlessly in harsh manufacturing environments."},

     {"id": 21, "name": "Industrial Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Robust robot for harsh environments.", 
     "long_description": "Built to withstand extreme conditions, this robot performs flawlessly in harsh manufacturing environments."},
    
]


products_service = [
    {"id": 22, "name": "Service Robot A", "price": 5000, "image": "Service.jpg", 
     "short_description": "Compact and efficient service robot.", 
     "long_description": "The Service Robot A is designed for handling basic tasks like cleaning, assisting in logistics, and customer service in small to medium spaces."},
     
    {"id": 23, "name": "Service Robot B", "price": 7500, "image": "Service.jpg", 
     "short_description": "Versatile robot for various services.", 
     "long_description": "Service Robot B is equipped with advanced AI and can be used for a range of services, from monitoring to delivering items in offices and public spaces."},
     
    {"id": 24, "name": "Service Robot X", "price": 6000, "image": "Service.jpg", 
     "short_description": "High-performance robot for healthcare.", 
     "long_description": "Service Robot X is specifically built for healthcare environments. It provides remote monitoring, basic medical services, and aids in medical data collection."},
     
    {"id": 25, "name": "Service Robot Y", "price": 3000, "image": "Service.jpg", 
     "short_description": "Educational robot for learning environments.", 
     "long_description": "The Service Robot Y is aimed at educational institutions, assisting teachers and students with interactive lessons and providing remote learning tools."},
     
    {"id": 26, "name": "Service Robot Z", "price": 8500, "image": "Service.jpg", 
     "short_description": "AI-powered service robot.", 
     "long_description": "Service Robot Z is built with advanced AI capabilities. It can adapt to various tasks like customer service, security monitoring, and smart home automation."},
     
    {"id": 27, "name": "Service Robot Medical", "price": 9000, "image": "Service.jpg", 
     "short_description": "Robot designed for medical assistance.", 
     "long_description": "The Service Robot Medical is specialized in healthcare environments. It helps with patient monitoring, data collection, and facilitating doctor-patient interactions in hospitals."},
     
    {"id": 28, "name": "Service Robot Logistics", "price": 4000, "image": "Service.jpg", 
     "short_description": "Efficient robot for logistics tasks.", 
     "long_description": "Service Robot Logistics is built for warehousing and logistics. It assists with sorting, packing, and delivering goods within warehouses or retail spaces."},
     
    {"id": 29, "name": "Service Robot Drone 1", "price": 12000, "image": "Service.jpg", 
     "short_description": "High-tech drone for surveillance.", 
     "long_description": "The Service Robot Drone 1 is equipped with cameras and sensors to provide 24/7 surveillance and monitoring for large outdoor areas or industrial sites."},
     
    {"id": 30, "name": "Service Robot Drone 2", "price": 12000, "image": "Drone2.jpg", 
     "short_description": "Advanced drone for delivery services.", 
     "long_description": "Drone 2 is a delivery robot designed for transporting small packages efficiently. It can navigate urban environments and deliver items to residential or business locations."},
     
    {"id": 31, "name": "Service Robot Drone 3", "price": 12000, "image": "Drone3.jpg", 
     "short_description": "Autonomous drone for inspection tasks.", 
     "long_description": "Drone 3 is equipped with advanced sensors for inspecting hard-to-reach places, like rooftops, construction sites, and power lines. It ensures high accuracy and efficiency in inspections."},
     
    {"id": 32, "name": "Service Robot Drone 4", "price": 12000, "image": "Drone4.jpg", 
     "short_description": "Smart drone for agricultural applications.", 
     "long_description": "Drone 4 is built specifically for agricultural purposes. It can monitor crop health, distribute fertilizers, and even plant seeds in large agricultural fields."},
     
    {"id": 33, "name": "Service Robot Drone 5", "price": 12000, "image": "Drone5.jpg", 
     "short_description": "Drone for environmental monitoring.", 
     "long_description": "Drone 5 is equipped with environmental sensors to monitor air quality, temperature, and humidity. It's perfect for urban planning, climate research, and disaster management."},
     
    {"id": 34, "name": "Service Robot Drone 6", "price": 12000, "image": "Drone6.jpg", 
     "short_description": "Drone with thermal imaging for search and rescue.", 
     "long_description": "Drone 6 comes equipped with thermal imaging to detect heat signatures in search and rescue operations, especially in emergency situations like forest fires or natural disasters."},
     
    {"id": 35, "name": "Service Robot Drone 7", "price": 12000, "image": "Drone7.jpg", 
     "short_description": "Compact drone for surveillance and reconnaissance.", 
     "long_description": "Drone 7 is a compact, agile drone ideal for surveillance, reconnaissance, and mapping. Its small size allows it to reach confined spaces with ease."},
     
    {"id": 36, "name": "Service Robot Drone 8", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "Heavy-duty drone for industrial inspections.", 
     "long_description": "Drone 8 is a heavy-duty drone designed for inspections of industrial equipment, pipelines, and machinery. Its robust design allows it to carry heavy payloads and withstand harsh conditions."},
     
    {"id": 37, "name": "Service Robot Drone 9", "price": 12000, "image": "Drone9.jpg", 
     "short_description": "Specialized drone for mapping and surveying.", 
     "long_description": "Drone 9 is specifically designed for large-scale mapping and surveying projects. Equipped with GPS and LIDAR, it provides high-precision geographic data for construction and development projects."},
     
    {"id": 38, "name": "Service Robot Drone 10", "price": 12000, "image": "Drone10.jpg", 
     "short_description": "Autonomous drone for security patrols.", 
     "long_description": "Drone 10 can patrol large estates, private properties, and commercial complexes, ensuring enhanced security with automated patrol routes and real-time alerts."},
     
    {"id": 39, "name": "Service Robot Drone 11", "price": 12000, "image": "Drone11.jpg", 
     "short_description": "Drone for real-time traffic monitoring.", 
     "long_description": "Drone 11 is designed to monitor traffic flow, congestion, and incidents in real-time. It's equipped with cameras and AI to analyze traffic patterns and optimize road usage."},

    {"id": 40, "name": "Service Robot Drone 11", "price": 12000, "image": "Drone11.jpg", 
        "short_description": "Drone for real-time traffic monitoring.", 
        "long_description": "Drone 11 is designed to monitor traffic flow, congestion, and incidents in real-time. It's equipped with cameras and AI to analyze traffic patterns and optimize road usage."},

    {"id": 41, "name": "Service Robot Drone 11", "price": 12000, "image": "Drone11.jpg", 
     "short_description": "Drone for real-time traffic monitoring.", 
     "long_description": "Drone 11 is designed to monitor traffic flow, congestion, and incidents in real-time. It's equipped with cameras and AI to analyze traffic patterns and optimize road usage."},

    {"id": 42, "name": "Service Robot Drone 11", "price": 12000, "image": "Drone11.jpg", 
     "short_description": "Drone for real-time traffic monitoring.", 
     "long_description": "Drone 11 is designed to monitor traffic flow, congestion, and incidents in real-time. It's equipped with cameras and AI to analyze traffic patterns and optimize road usage."},

]



products_educ = [
    {"id": 43, "name": "educ Robot A", "price": 5000, "image": "Educ.jpg", 
     "short_description": "Compact robot for educational purposes.", 
     "long_description": "educ Robot A is designed for schools and universities. It assists in interactive lessons, hands-on learning, and educational demonstrations in various subjects."},
     
    {"id": 44, "name": "educ Robot B", "price": 7500, "image": "Educ.jpg", 
     "short_description": "Robotic assistant for modern classrooms.", 
     "long_description": "educ Robot B is a versatile robot equipped with sensors and a touchscreen interface. It enhances the learning experience by offering interactive tasks and real-time feedback."},
     
    {"id": 45, "name": "educ Robot X", "price": 6000, "image": "Educ.jpg", 
     "short_description": "Perfect for STEM education.", 
     "long_description": "educ Robot X is a high-tech educational tool designed for STEM (Science, Technology, Engineering, and Mathematics) classrooms. It can be programmed to perform various experiments and activities."},
     
    {"id": 46, "name": "educ Robot Robot Y", "price": 3000, "image": "Educ.jpg", 
     "short_description": "Budget-friendly educational robot.", 
     "long_description": "educ Robot Y is an affordable solution for schools and educational institutions looking to introduce robotics into their curriculum. It can be used for basic programming exercises and mechanical tasks."},
     
    {"id": 47, "name": "educ Robot Z", "price": 8500, "image": "Educ.jpg", 
     "short_description": "AI-powered robot for advanced learning.", 
     "long_description": "educ Robot Z integrates Artificial Intelligence to help students understand advanced concepts like machine learning, robotics, and automation. It's ideal for tech-savvy classrooms."},
     
    {"id": 48, "name": "educ Robot", "price": 9000, "image": "Educ.jpg", 
     "short_description": "Healthcare-focused educational robot.", 
     "long_description": "educ Robot is designed for healthcare-related courses. It simulates medical procedures and allows students to practice diagnostic techniques in a controlled environment."},
     
    {"id": 49, "name": "educ Robot", "price": 4000, "image": "Educ.jpg", 
     "short_description": "Logistics training robot.", 
     "long_description": "educ Robot is used for teaching logistics and supply chain management. With its advanced tracking and delivery simulations, students can learn real-world logistics skills."},
     
    {"id": 50, "name": "educ Robot", "price": 12000, "image": "Educ.jpg", 
     "short_description": "Drone robot for advanced education.", 
     "long_description": "educ Robot is equipped with drone technology to teach students about flight dynamics, GPS, and robotics. Ideal for advanced technical courses in universities."},
     
    {"id": 51, "name": "educ Robot", "price": 12000, "image": "Drone2.jpg", 
     "short_description": "Educational drone for physics lessons.", 
     "long_description": "This robot is specifically designed for physics lessons, where students can learn the principles of flight, aerodynamics, and remote control technology."},
     
    {"id": 52, "name": "educ Robot", "price": 12000, "image": "Drone3.jpg", 
     "short_description": "STEM-focused educational drone.", 
     "long_description": "This drone is equipped with a variety of sensors that help students study and experiment with real-time data, making it a great educational tool for STEM programs."},
     
    {"id": 53, "name": "educ Robot", "price": 12000, "image": "Drone4.jpg", 
     "short_description": "Hands-on learning with drone robotics.", 
     "long_description": "educ Robot offers hands-on experience in drone programming and flight control, helping students master advanced technology concepts."},
     
    {"id": 54, "name": "educ Robot", "price": 12000, "image": "Drone5.jpg", 
     "short_description": "Multi-functional educational drone.", 
     "long_description": "Designed for hands-on learning, this drone is perfect for teaching various robotics concepts and applications like aerial photography and geographical data collection."},
     
    {"id": 55, "name": "educ Robot", "price": 12000, "image": "Drone6.jpg", 
     "short_description": "Interactive drone for learning robotics.", 
     "long_description": "This interactive robot helps students learn the complexities of flight and robotics by offering multiple practical activities for experimenting with drone mechanics and control systems."},
     
    {"id": 56, "name": "educ Robot", "price": 12000, "image": "Drone7.jpg", 
     "short_description": "STEM learning through aerial robotics.", 
     "long_description": "educ Robot offers an engaging way to learn STEM subjects, with a focus on flight control, robotics programming, and real-world applications of drone technology."},
     
    {"id": 57, "name": "educ Robot", "price": 12000, "image": "Drone8.jpg", 
     "short_description": "STEM-focused educational drone robot.", 
     "long_description": "educ Robot is a complete educational package that teaches students drone construction, programming, and flight, making it ideal for advanced technical programs."},
     
    {"id": 58, "name": "educ Robot", "price": 12000, "image": "Drone9.jpg", 
     "short_description": "Advanced drone for technical training.", 
     "long_description": "This robot drone is perfect for technical education programs focused on the principles of aviation, engineering, and high-tech manufacturing."},
     
    {"id": 59, "name": "educ Robot", "price": 12000, "image": "Drone10.jpg", 
     "short_description": "High-tech educational drone for lessons.", 
     "long_description": "This high-tech drone integrates advanced flight technology and is ideal for teaching students about aviation and aerodynamics in a hands-on environment."}
]



PRODUCTS_PER_PAGE = 10


@app.route('/industrialrobotics')
def industrialrobotics():
    page = request.args.get('page', 1, type=int)
    sort = request.args.get('sort', '')

    sorted_products = products_indus[:]

    if sort == 'price_asc':
        sorted_products.sort(key=lambda x: x['price'])
    elif sort == 'price_desc':
        sorted_products.sort(key=lambda x: x['price'], reverse=True)
    elif sort == 'name_asc':
        sorted_products.sort(key=lambda x: x['name'].lower())
    elif sort == 'name_desc':
        sorted_products.sort(key=lambda x: x['name'].lower(), reverse=True)

    start = (page - 1) * PRODUCTS_PER_PAGE
    end = start + PRODUCTS_PER_PAGE
    total_pages = (len(products_indus) + PRODUCTS_PER_PAGE - 1) // PRODUCTS_PER_PAGE
    return render_template(
        'industrialrobotics.html',
        products_indus=sorted_products[start:end],
        page=page,
        total_pages=total_pages
    )



@app.route('/servicerobotics')
def servicerobotics():
    page = request.args.get('page', 1, type=int)
    sort = request.args.get('sort', '')

    sorted_products = products_service[:]

    if sort == 'price_asc':
        sorted_products.sort(key=lambda x: x['price'])
    elif sort == 'price_desc':
        sorted_products.sort(key=lambda x: x['price'], reverse=True)
    elif sort == 'name_asc':
        sorted_products.sort(key=lambda x: x['name'].lower())
    elif sort == 'name_desc':
        sorted_products.sort(key=lambda x: x['name'].lower(), reverse=True)

    start = (page - 1) * PRODUCTS_PER_PAGE
    end = start + PRODUCTS_PER_PAGE
    total_pages = (len(products_service) + PRODUCTS_PER_PAGE - 1) // PRODUCTS_PER_PAGE

    return render_template(
        'servicerobotics.html',
        products_service=sorted_products[start:end],
        page=page,
        total_pages=total_pages
    )


@app.route('/educrobotics')
def educrobotics():
    page = request.args.get('page', 1, type=int)
    sort = request.args.get('sort', '')

    sorted_products = products_educ[:]

    if sort == 'price_asc':
        sorted_products.sort(key=lambda x: x['price'])
    elif sort == 'price_desc':
        sorted_products.sort(key=lambda x: x['price'], reverse=True)
    elif sort == 'name_asc':
        sorted_products.sort(key=lambda x: x['name'].lower())
    elif sort == 'name_desc':
        sorted_products.sort(key=lambda x: x['name'].lower(), reverse=True)

    start = (page - 1) * PRODUCTS_PER_PAGE
    end = start + PRODUCTS_PER_PAGE
    total_pages = (len(products_educ) + PRODUCTS_PER_PAGE - 1) // PRODUCTS_PER_PAGE

    return render_template(
        'educrobotics.html',
        products_educ=sorted_products[start:end],
        page=page,
        total_pages=total_pages
    )


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    all_products = products_indus + products_service + products_educ
    product = None
    prev_product = None
    next_product = None

    for i, p in enumerate(all_products):
        if p['id'] == product_id:
            product = p
            if i > 0:
                prev_product = all_products[i - 1]
            if i < len(all_products) - 1:
                next_product = all_products[i + 1]
            break

    if product is None:
        return "Produit non trouvé", 404
    
    if product is None:
        return "Produit non trouvé", 404
    
    return render_template('product_detail.html', product=product,prev_product=prev_product, next_product=next_product)



if __name__ == '__main__':
    app.run(debug=True)



