from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Ivan', 10, 100, 50)
        self.defender = Hero('Stamat', 10, 100, 50)

    def test_proper_init(self):
        username = 'Ivan'
        level = 10
        health = 100
        damage = 50
        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_hero_str_returns_proper_string(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual_result = str(self.hero)

        self.assertEqual(expected_result, actual_result)

    def test_battle_raises_when_attack_himself(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle_raises_when_hero_is_dead(self):
        for heath in [0, -50]:
            self.hero.health = heath
            with self.assertRaises(Exception) as context:
                self.hero.battle(self.defender)
            self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(context.exception))

    def test_battle_raises_when_defender_is_dead(self):
        for health in [0, -50]:
            self.defender.health = health
            with self.assertRaises(Exception) as context:
                self.hero.battle(self.defender)
            self.assertEqual(f'You cannot fight {self.defender.username}. He needs to rest', str(context.exception))

    def test_when_battle_is_drawn(self):
        result = self.hero.battle(self.defender)

        self.assertEqual('Draw', result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.defender.health)

    def test_when_battle_is_won(self):
        defender = Hero("stamat", 1, 100, 50)
        result = self.hero.battle(defender)

        self.assertEqual('You win', result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(-400, defender.health)

    def test_when_battle_is_lost(self):
        hero = Hero('Ivan', 1, 100, 50)
        defender = Hero('Stamat', 1, 100, 50)
        result = hero.battle(defender)

        self.assertEqual('You lose', result)
        self.assertEqual(1, hero.level)
        self.assertEqual(50, hero.health)
        self.assertEqual(55, defender.health)
        self.assertEqual(55, defender.damage)
        self.assertEqual(2, defender.level)




if __name__ == '__main__':
    main()