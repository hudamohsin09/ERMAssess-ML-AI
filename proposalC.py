import openai
from pprint import pprint

# Replace with your OpenAI API key
openai.api_key = ' '


# Define the classification categories
categories = [
    "General Safety and Compliance",
    "Hazard and Risk Management",
    "Equipment and Operational Safety",
    "Contractor and On-Site Management",
    "Emergency Planning and Response",
    "Regulatory and Training Compliance",
    "Specialized Safety Conditions",
    "Environmental and Waste Management",
    "Construction and High-Risk Work",
    "Transportation and Vehicle Safety",
    "Specific Safety Protocols",
    "Personal Safety and Protective Measures",
    "Communication and Management"
]

# List of tags to classify
tags = [
    "Amazon K-Net Training", "Amazon Robotics", "Amazon Special Safety Conditions (Canada)", "Amazon Special Safety Conditions (ROW)",
    "Avetta Implementation", "Avetta Worksite Safety Tool", "Bakery Operations", "Biological Safety", "CalOSHA", "Chemical Safety",
    "Compressed Gas Safety", "Confined Space Entry", "Construction", "Construction Safety", "Consultation, representation and participation",
    "Contractor Activity Tracking", "Contractor Chemical Management", "Contractor Emergency Evacuation Procedures", "Contractor Emergency Management",
    "Contractor Management KPIs", "Contractor On-Site Roster", "Contractor Onsite Management", "Contractor Points of Contact", "Contractor Pre-Qualification Process",
    "Contractor Risk Assessments", "Contractor Roster Management", "Contractor Safety Observations", "Contractor Training / Certifications", "CRM Training Curriculum",
    "CSO - Quality", "CSO Quality / Adherance", "Demolition and Refurbishment", "Driving Safety / Fleet Safety", "Electrical Safety", "Emergency Planning / Response",
    "End of Project Evaluations", "Environmental", "Equipment / Tool Loaning", "Equipment Safety", "Exterior Building Work Activities", "Fire Safety",
    "General Safety Conditions", "Hazardous Materials", "Hazardous Materials Management", "Health and Safety Committee", "Health and Safety Policy",
    "Heavy vehicle national law", "High Risk", "High-Hazard Work", "Hot Work", "Housekeeping", "Implementation", "Incident Investigation",
    "Industrial Hygiene", "KPI Monitoring", "Lifting Operations and Material Handling", "Low Risk", "Material Handling", "Occupational Health",
    "Occupational Safety", "Operational Control", "Organizational Regulation", "Permit to Work", "Permit to Work Implementation", "Personal Protective Equipment",
    "Point of Contact Management", "Post-Work", "Post-Work Evaluation", "Powered Industrial Vehicles", "Powered Platforms, Manlifts",
    "Pre-qualification", "Process Safety", "Project Kickoff Meeting", "Project Pre-Task Meeting", "Psychosocial Risk", "Risk Assessments",
    "Safety Management Systems", "SSC", "Tier 2a - Annual Review Process", "Training & Certification Review", "Transport", "Virtual Contractor Orientation",
    "Waste Management", "Work at Heights", "Workplace Safety", "Workplace Violence and Harassment", "Yard Work", "Yard Work Safety"
]

# Function to classify a tag using GPT-3.5 Turbo
def classify_tag(tag, categories):
    prompt = f"""
    You are an expert in safety and risk management. Classify the following tag into one of the predefined categories. and Each category is designed to cover specific aspects of safety and management.

    Tag: "{tag}"
    Categories:
    {', '.join(categories)}
    
    Provide the most suitable category for the given tag and briefly explain your reasoning.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that classifies safety-related tags into predefined categories."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    return response.choices[0].message['content'].strip()

# Classify all tags and store the results
classified_tags = {category: [] for category in categories}
uncategorized_tags = []

for tag in tags:
    print(f"Classifying tag: {tag}")
    classification = classify_tag(tag, categories)
    
    # Parse the output for the category
    category_found = False
    for category in categories:
        if category in classification:
            classified_tags[category].append(tag)
            category_found = True
            break
    
    if not category_found:
        uncategorized_tags.append(tag)

# Display the classification result
print("\nClassified Tags:")
pprint(classified_tags)

if uncategorized_tags:
    print("\nUncategorized Tags:")
    pprint(uncategorized_tags)
else:
    print("\nAll tags were successfully classified.")
