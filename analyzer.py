import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
id = input("Podaj identyfikator produktu:")

opinions = pd.read_json(f"opinions/{id}.json")

opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",",".")))
opinions_count = len(opinions.index)
# opinions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()

average_score = opinions.stars.mean().round(2)

recommendation = opinions.recommendation.value_counts(dropna = False).sort_index().reindex(["Polecam", None, "Nie Polecam"])
recommendation.plot.pie(
    label="", 
    autopct="%1.1f%%", 
    colors=["forestgreen", "lightskyblue", "crimson"],
    labels=["Polecam", "Nie mam zdania", "Nie polecam"]
)

plt.title("Rekomendacja")
plt.savefig(f"opinions/{id}_recommendations.png")
plt.close()

stars = opinions.stars.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
stars.plot.bar()
plt.title("Oceny produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True)
plt.xticks(rotation=0)
plt.show()
