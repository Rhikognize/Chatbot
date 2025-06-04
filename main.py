import random
from transformations import transform_text, transform_age, transform_interest
from excel import save_to_excel, answers

questions = [
    "Bot: Bună! Cum te cheamă?",
    "Bot: Câți ani ai?",
    "Bot: Ce îți place să faci?",
    "Bot: Vrei să continui conversația? (da/nu)"
]


def greet_user(name):
    name = transform_text(name).capitalize()
    greetings = [
        f"Salut {name}!",
        f"Bună {name}!",
        f"Hei {name}!",
        f"Salutare, {name}!"
    ]
    return random.choice(greetings)


def main():
    end = False
    while not end:
        answers.clear()
        print(questions[0])
        answers.append(questions[0])
        try:
            name = input("Tu: ")
            if not name.strip():
                raise ValueError("Numele nu poate fi gol.")
        except ValueError as e:
            print(f"Bot: {e}")
            continue
        answers.append(f"Tu: {name}")
        print(questions[1])
        answers.append(questions[1])
        try:
            age = int(input("Tu: "))
            if age < 0:
                raise ValueError(
                    "Bot: Te rog să introduci un număr valid pentru vârstă.")
        except ValueError as e:
            print(f"Bot: {e}")
            continue
        answers.append(f"Tu: {age}")
        new_age = transform_age(age)
        print(questions[2])
        answers.append(questions[2])
        try:
            interest = input("Tu: ")
            if not interest.strip():
                raise ValueError("Interesul nu poate fi gol.")
        except ValueError as e:
            print(f"Bot: {e}")
            continue
        answers.append(f"Tu: {interest}")
        new_interest = transform_interest(interest)
        greeting = greet_user(name)
        response = f"Bot: {greeting} Este minunat că {new_age} {new_interest}!"
        answers.append(response)
        print(response)
        while True:
            print("Bot: Vrei să continui conversația? (da/nu)")
            try:
                end_input = input("Tu: ").strip().lower()
                if end_input not in ["da", "nu"]:
                    raise ValueError("Răspunsul trebuie să fie 'da' sau 'nu'.")
                answers.append(questions[3])
                answers.append(f"Tu: {end_input}")
                end = end_input == "nu"
                break
            except ValueError as e:
                print(f"Bot: {e}")
                continue
        save_to_excel()


if __name__ == "__main__":
    main()
