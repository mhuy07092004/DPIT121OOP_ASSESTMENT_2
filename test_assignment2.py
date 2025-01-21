import unittest
import os
from assignment2 import Person, DietRecommendation, FileHandler

class TestPerson(unittest.TestCase):
    def test_valid_person(self):
        """Test the Person class for valid inputs"""
        # Test male adult
        male = Person(25, "male")
        male.validate()  # Should not raise exception
        self.assertEqual(male.age, 25)
        self.assertEqual(male.gender, "male")
        self.assertFalse(male.is_pregnant)
        self.assertFalse(male.is_breastfeeding)

        # Test female adult
        female = Person(30, "female", False, False)
        female.validate()  # Should not raise exception
        self.assertEqual(female.age, 30)
        self.assertEqual(female.gender, "female")
        self.assertFalse(female.is_pregnant)
        self.assertFalse(female.is_breastfeeding)

    def test_invalid_age(self):
        """Test the Person class for invalid age input"""
        invalid_ages = [-1, 0, 120, 150]
        for age in invalid_ages:
            with self.assertRaises(ValueError):
                person = Person(age, "male")
                person.validate()

    def test_invalid_gender(self):
        """Test the Person class for invalid gender input"""
        with self.assertRaises(ValueError):
            person = Person(25, "other")
            person.validate()

    def test_minor_pregnancy(self):
        """Test pregnancy validation for minors"""
        with self.assertRaises(ValueError):
            person = Person(17, "female", True, False)
            person.validate()

        with self.assertRaises(ValueError):
            person = Person(17, "female", False, True)
            person.validate()


class TestDietRecommendation(unittest.TestCase):
    def setUp(self):
        """Setup method to create test cases"""
        # Male age groups
        self.male_2_3 = Person(3, "male")
        self.male_4_8 = Person(6, "male")
        self.male_9_11 = Person(10, "male")
        self.male_12_13 = Person(13, "male")
        self.male_14_18 = Person(16, "male")
        self.male_19_50 = Person(30, "male")
        self.male_51_70 = Person(60, "male")
        self.male_over_70 = Person(80, "male")

        # Female age groups
        self.female_2_3 = Person(3, "female")
        self.female_4_8 = Person(6, "female")
        self.female_9_11 = Person(10, "female")
        self.female_12_13 = Person(13, "female")
        self.female_14_18 = Person(16, "female")
        self.female_19_50 = Person(30, "female")
        self.female_51_70 = Person(60, "female")
        self.female_over_70 = Person(80, "female")

        # Special conditions
        self.pregnant_woman = Person(25, "female", True, False)
        self.breastfeeding_woman = Person(25, "female", False, True)

    def test_male_age_groups(self):
        """Test diet recommendations for all male age groups"""
        # Test male 2-3 years
        diet = DietRecommendation(self.male_2_3)
        self.assertEqual(diet.recommendations["vegetables"], 2.5)
        self.assertEqual(diet.recommendations["fruits"], 1)
        self.assertEqual(diet.recommendations["grains"], 4)
        self.assertEqual(diet.recommendations["meats"], 1)
        self.assertEqual(diet.recommendations["dairy"], 1.5)

        # Test male 19-50 years
        diet = DietRecommendation(self.male_19_50)
        self.assertEqual(diet.recommendations["vegetables"], 6)
        self.assertEqual(diet.recommendations["fruits"], 2)
        self.assertEqual(diet.recommendations["grains"], 6)
        self.assertEqual(diet.recommendations["meats"], 3)
        self.assertEqual(diet.recommendations["dairy"], 2.5)

    def test_female_age_groups(self):
        """Test diet recommendations for all female age groups"""
        # Test female 4-8 years
        diet = DietRecommendation(self.female_4_8)
        self.assertEqual(diet.recommendations["vegetables"], 4.5)
        self.assertEqual(diet.recommendations["fruits"], 1.5)
        self.assertEqual(diet.recommendations["grains"], 4)
        self.assertEqual(diet.recommendations["meats"], 1.5)
        self.assertEqual(diet.recommendations["dairy"], 1.5)

        # Test female 19-50 years
        diet = DietRecommendation(self.female_19_50)
        self.assertEqual(diet.recommendations["vegetables"], 5)
        self.assertEqual(diet.recommendations["fruits"], 2)
        self.assertEqual(diet.recommendations["grains"], 6)
        self.assertEqual(diet.recommendations["meats"], 2.5)
        self.assertEqual(diet.recommendations["dairy"], 2.5)

    def test_special_conditions(self):
        """Test diet recommendations for pregnant and breastfeeding women"""
        # Test pregnant woman
        diet = DietRecommendation(self.pregnant_woman)
        self.assertEqual(diet.recommendations["vegetables"], 5)
        self.assertEqual(diet.recommendations["fruits"], 2)
        self.assertEqual(diet.recommendations["grains"], 8.5)
        self.assertEqual(diet.recommendations["meats"], 2.5)
        self.assertEqual(diet.recommendations["dairy"], 2.5)

        # Test breastfeeding woman
        diet = DietRecommendation(self.breastfeeding_woman)
        self.assertEqual(diet.recommendations["vegetables"], 7.5)
        self.assertEqual(diet.recommendations["fruits"], 2)
        self.assertEqual(diet.recommendations["grains"], 9)
        self.assertEqual(diet.recommendations["meats"], 2.5)
        self.assertEqual(diet.recommendations["dairy"], 2.5)

# Test file handling
class TestFileHandler(unittest.TestCase):
    def setUp(self):
        """Setup method for file handling tests"""
        self.test_filename = "test_diet_recommendations.txt"
        self.test_content = "Test diet recommendations"

    def tearDown(self):
        """Cleanup method to remove test files"""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_file_export(self):
        """Test the file export functionality"""
        # Test with custom filename
        FileHandler.export_to_file(self.test_content, self.test_filename)
        self.assertTrue(os.path.exists(self.test_filename))

        with open(self.test_filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, self.test_content)


if __name__ == '__main__':
    unittest.main()