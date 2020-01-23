from unittest import TestCase
import testUtility
import Dominion

class TestCard(TestCase):
    def setUp(self):
        # Data setup
        self.player_names = ["Annie", "*John", "*Colin", "*Ruth"]
        self.box = testUtility.getBox(self.player_names)

        # get the card supply for this instance of the game
        self.supply = testUtility.getSupply(self.box, self.player_names)

        # get the player objects
        self.players = testUtility.getPlayers(self.player_names)

        self.player = Dominion.Player('Annie')

    def test_init(self):
        # initialize test data
        self.setUp()
        cost = 1
        buypower = 5

        # instantiate the card object
        card = Dominion.Coin_card(self.player.name,cost,buypower)

        # verify that the class variables have the expected values)
        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost,card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        pass