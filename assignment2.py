#  Initialize a person's profile
class Person:
    def __init__(self, age, gender, is_pregnant=False, is_breastfeeding=False):
        self.age = age
        self.gender = gender.lower()
        self.is_pregnant = is_pregnant
        self.is_breastfeeding = is_breastfeeding

    # Validate the inputs for the person
    def validate(self):
        if not (0 < self.age < 120):
            raise ValueError("Invalid age. Please enter a valid age.")
        # Check for valid gender
        if self.gender not in ["male", "female"]:
            raise ValueError("Invalid gender. Please enter 'male' or 'female'.")


class DietRecommendation:
    # Initialize with a person's profile and generate recommendations and default value is 0
    def __init__(self, person):
        self.person = person
        self.recommendations = {
            "vegetables": 0,
            "fruits": 0,
            "grains": 0,
            "meats": 0,
            "dairy": 0
        }
        self.generate_recommendations()
    # Generate diet recommendations based on age, gender, special conditions
    def generate_recommendations(self):
        age = self.person.age
        gender = self.person.gender
        pregnant = self.person.is_pregnant
        breastfeeding = self.person.is_breastfeeding
        # Recommendations for male
        if gender == "male":
            if 19 <= age <= 50:
                self.recommendations.update({"vegetables": 6, "fruits": 2, "grains": 6, "meats": 3, "dairy": 2.5})
            elif 51 <= age <= 70:
                self.recommendations.update({"vegetables": 5.5, "fruits": 2, "grains": 6, "meats": 2.5, "dairy": 2.5})
            elif 2 <= age <=3:
                self.recommendations.update({"vegetables":2.5, "fruits":1 , "grains":4, "meats":1 , "dairy":1.5 })
            elif 4 <= age <=8:
                self.recommendations.update({"vegetables":4.5 , "fruits":1.5, "grains":4 , "meats":1.2 , "dairy":2 })
            elif 9 <= age <= 11:
                self.recommendations.update({"vegetables":5 , "fruits":2, "grains":5 , "meats":2.5 , "dairy":2.5 })
            elif 12 <= age <= 13:
                self.recommendations.update({"vegetables":5.5, "fruits":2, "grains":6 , "meats":2.5 , "dairy":3.5 })
            elif 14 <= age <= 18:
                self.recommendations.update({"vegetables":5.5, "fruits":2, "grains":7 , "meats":2.5 , "dairy":3.5 })
            else:
                self.recommendations.update({"vegetables": 5, "fruits": 2, "grains": 4.5, "meats": 2.5, "dairy": 3.5})
        # Recommendations for female
        elif gender == "female":
            if pregnant:
                self.recommendations.update({"vegetables": 5, "fruits": 2, "grains": 8.5, "meats": 2.5, "dairy": 2.5})
            elif breastfeeding:
                self.recommendations.update({"vegetables": 7.5, "fruits": 2, "grains": 9, "meats": 2.5, "dairy": 2.5})
            elif 2 <= age <=3:
                self.recommendations.update({"vegetables":2.5 , "fruits":1 , "grains":4, "meats":1 , "dairy":1.5 })
            elif 4 <= age <=8:
                self.recommendations.update({"vegetables":4.5 , "fruits":1.5 , "grains":4, "meats":1.5 , "dairy":1.5 })
            elif 9 <= age <= 11:
                self.recommendations.update({"vegetables":5 , "fruits":2, "grains":4 , "meats":2.5 , "dairy":3 })
            elif 12 <= age <= 13:
                self.recommendations.update({"vegetables":5.5, "fruits":2, "grains":5 , "meats":2.5 , "dairy":3.5 })
            elif 14 <= age <= 18:
                self.recommendations.update({"vegetables":5.5, "fruits":2, "grains":7 , "meats":2.5 , "dairy":3.5 })
            elif 19 <= age <= 50:
                self.recommendations.update({"vegetables": 5, "fruits": 2, "grains": 6, "meats": 2.5, "dairy": 2.5})
            elif 51 >= age <70:
                self.recommendations.update({"vegetables": 5, "fruits": 2, "grains": 4, "meats": 2, "dairy": 4})
            else:
                self.recommendations.update({"vegetables":5, "fruits":2, "grains": 3, "meats":2 , "dairy":4 })

    # Display All the Recommendations
    def display_recommendations(self):
        print("Based on your inputs, the minimum recommended servings are:")
        for group, servings in self.recommendations.items():
            print(f"{group.capitalize()}: {servings} servings per day")
        print("\nAdditionally, each food category single serving recommendations are detailed as shown as follows:\n")
        self.display_serving_details()

    @staticmethod
    # Display detailed information about single servings estimates for users
    def display_serving_details():
        print("""VEGETABLES
A vegetables single serve is 75g (100-350kJ). Here are some examples of single serve of Vegetable:
• 0.5 cup of cooked green or orange vegetables (like broccoli, spinach, carrots, or pumpkin)
• 0.5 cup of cooked dried or canned beans, peas, or lentils
• 1 cup of green leafy or raw salad vegetables
• 0.5 cup of sweet corn
• 0.5 of a medium potato or other starchy vegetables (such as sweet potato, taro, or cassava)
• 1 medium tomato

FRUITS
A fruits single serve is 150g (350kJ). Here are some examples of single serve of fruit:
• 1 medium apple, banana, orange, or pear
• 2 small apricots, kiwi fruits, or plums
• 1 cup of diced or canned fruit (with no added sugar)

GRAINS
A grains single serve is (500kJ). Here are some examples of single serve of grain:
• 1 slice (40g) of bread
• 0.5 medium (40g) roll or flat bread
• 0.5 cup (75-120g) of cooked rice, pasta, noodles, barley, buckwheat, semolina, polenta, bulgur or quinoa
• 0.5 cup (120g) of cooked porridge
• 0.66 cup (30g) of wheat cereal flakes
• 0.75 cup (30g) of muesli
• 3 (35g) crispbreads
• 1 (60g) crumpet
• 1 small (35g) English muffin or scone

MEAT
A meat single serve is (500-600kJ). Here are some examples of single serve of meat:
• 65g cooked lean red meats such as beef, lamb, veal, pork, goat, or kangaroo (about 90-100g raw)
• 80g cooked lean poultry such as chicken or turkey (100g raw)
• 100g cooked fish fillet (about 115g raw) or one small can of fish
• 2 large (120g) eggs
• 1 cup (150g) cooked or canned legumes/beans such as lentils, chickpeas, or split peas
• 170g tofu
• 30g nuts, seeds, peanut or almond butter, tahini, or other nut or seed paste

DAIRY
A single serve of dairy is (500-600kJ). Here are some examples of single serve of dairy:
• 1 cup (250ml) of fresh, UHT long life, reconstituted powdered milk or buttermilk
• 0.5 cup (120ml) of evaporated milk
• 2 slices (40g) or a 4 x 3 x 2 cm cube (40g) of hard cheese, such as cheddar
• 0.5 cup (120g) of ricotta cheese
• 0.25 cup (200g) of yoghurt
• 1 cup (250ml) of soy, rice or other cereal drink with at least 100mg of added calcium per 100ml
""")

    # Export diet recommendations to a text file
class FileHandler:
    @staticmethod
    def export_to_file(data, filename="DietaryRecommendations.txt"):
        with open(filename, "w") as file:
            file.write(data)
        print(f"Recommendations have been exported to {filename}")


# Main Program
try:
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")

    is_pregnant = False
    is_breastfeeding = False

    if gender.lower() == "female" and age >= 18:
        is_pregnant = input("Are you pregnant? (yes/no): ").strip().lower() == "yes"
        is_breastfeeding = input("Are you breastfeeding? (yes/no): ").strip().lower() == "yes"

    # Validate User by age gender, special condition,..
    user = Person(age, gender, is_pregnant, is_breastfeeding)
    user.validate()

    diet = DietRecommendation(user)
    diet.display_recommendations()
    # Ask User if the want to export the recommendations as a file or not
    export = input("Would you like to export these recommendations? (yes/no): ").strip().lower()
    if export == "yes":
        filename = input("Enter a filename (leave blank for 'DietaryRecommendations.txt'): ").strip()
        filename = filename if filename else "DietaryRecommendations.txt"

        recommendations_text = "Based on your inputs, the minimum recommended servings are:\n"
        recommendations_text += "\n".join(
            [f"{group.capitalize()}: {servings} servings per day" for group, servings in diet.recommendations.items()]
        )
        # export a recommendations file
        FileHandler.export_to_file(recommendations_text, filename)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")