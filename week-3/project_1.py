import pandas as pd

# Data for girls
girls = [
    ("Evelyn", 17, 5.5, 80),
    ("Jessica", 16, 6.0, 85),
    ("Somto", 17, 5.4, 70),
    ("Edith", 18, 5.9, 60),
    ("Liza", 16, 5.5, 76),
    ("Madonna", 18, 6.5, 66),
    ("Waje", 17, 5.6, 87),
    ("Tola", 20, 6.0, 95),
    ("Aisha", 19, 5.7, 50),
    ("Latifa", 17, 5.5, 49),
]

# Data for boys
boys = [
    ("Chinedu", 19, 5.7, 74),
    ("Liam", 16, 5.9, 87),
    ("Wale", 18, 5.8, 75),
    ("Gbenga", 17, 6.1, 68),
    ("Abiola", 20, 5.9, 66),
    ("Kola", 19, 5.5, 78),
    ("Kunle", 16, 6.1, 98),
    ("George", 18, 5.4, 54),
    ("Thomas", 17, 5.8, 60),
    ("Wesley", 19, 5.7, 56),
]

# Combine both lists
students = girls + boys

# Convert to DataFrame
df = pd.DataFrame(students, columns=["Name", "Age", "Height", "Score"])

# Display the table
print(df)
