from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('name', 'mammal_type', 'sound')


    def test_mammal_init(self):
        name = 'Name'
        mammal_type = 'mammal'
        sound = 'sound'
        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(mammal.name, name)
        self.assertEqual(mammal.type, mammal_type)
        self.assertEqual(mammal.sound, sound)
        self.assertEqual(mammal._Mammal__kingdom, 'animals')

    def test_make_sound_returns_proper_string(self):
        expected_result = f"{self.mammal.name} makes {self.mammal.sound}"
        actual_result = self.mammal.make_sound()

        self.assertEqual(actual_result, expected_result)

    def test_get_kingdom_returns_animals(self):
        self.assertEqual(self.mammal.get_kingdom(), self.mammal._Mammal__kingdom)

    def test_info_returns_proper_string(self):
        expected_result = f"{self.mammal.name} is of type {self.mammal.type}"
        actual_result = self.mammal.info()

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()