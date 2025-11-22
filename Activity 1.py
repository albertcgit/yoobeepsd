name = "John Doe"
age = 28
skills = ["Python", "SQL", "Power BI"]
education =	("BSc Computer Science", 2020)
contactDetails = {"email": "...", "phone": "..."}
certifications	= {"Azure", "AWS", "Azure"}

print(f"{'Component':<20}{'Data Type':<15}{'Example'}")
print("-" * 65)
print(f"{'Name':<20}{'String':<15}{name}")
print(f"{'Age':<20}{'Integer':<15}{age}")
print(f"{'Skills':<20}{'List':<15}{skills}")
print(f"{'Education':<20}{'Tuple':<15}{education}")
print(f"{'Contact Details':<20}{'Dictionary':<15}{contactDetails}")
print(f"{'Certifications':<20}{'Set':<15}{certifications}")