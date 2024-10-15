import os
import json

class MostPopular:
    def __init__(self, data):
        self.data = data

    def fit(self):
        all_interactions = [user[id]["history_interaction"] for user in self.data for id in user.keys()]
        interations_count = {}
        for user_interactions in all_interactions:
            for interaction in user_interactions:
                if interaction in interations_count:
                    interations_count[interaction] += 1
                else:
                    interations_count[interaction] = 1

        self.popular = max(interations_count, key=interations_count.get)

    def recommend(self, user_id):
        return self.popular
    

if __name__ == "__main__":
    data = []
    with open(os.path.join("data", "Books", "final_data.jsonl"), "r") as f:
        for line in f:
            data.append(json.loads(line))

    model = MostPopular(data)
    model.fit()
    print(model.recommend(1))