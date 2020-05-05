import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=3, num_sentences=4):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)
            full_sentence = F"{t.capitalize()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = f"{full_sentence} "
            forecast = forecast + full_sentence

        prophecies.append(forecast)
     
    return prophecies

def generate_listing():
    listing = []

    for i in range(len(times)):
        new_list = times[i]
        listing.append(new_list)
    return listing
