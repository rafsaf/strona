import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from base import models
from tribal_wars import basic


class TestTargetWeightQueries(TestCase):
    def setUp(self):
        self.server = models.Server.objects.create(
            dns="testserver",
            prefix="te",
        )
        self.world1 = models.World.objects.create(
            server=self.server,
            postfix="1",
            paladin="inactive",
            archer="inactive",
            militia="active",
        )
        self.admin = User.objects.create_user("admin", None, None)
        self.outline = models.Outline.objects.create(
            owner=self.admin,
            date=datetime.date.today(),
            name="name",
            world=self.world1,
            ally_tribe_tag=["pl1", "pl2"],
            enemy_tribe_tag=["pl3", " pl4"],
        )

        self.state = models.WeightMaximum.objects.create(
            outline=self.outline,
            start="100|100",
            player="player1",
            off_max=100,
            off_state=100,
            off_left=0,
            nobleman_max=2,
            nobleman_state=2,
            nobleman_left=2,
        )
        self.outline_time = models.OutlineTime.objects.create(
            outline=self.outline
        )

        self.period = models.PeriodModel.objects.create(
            status='all',
            outline_time=self.outline_time,
            unit='ram',
        )

        self.target = models.TargetVertex.objects.create(
            outline=self.outline,
            player="player2",
            target="101|101",
            outline_time=self.outline_time,
        )
        self.weight = models.WeightModel.objects.create(
            start="100|100",
            player="player1",
            target=self.target,
            state=self.state,
            distance=1,
            off=20,
            nobleman=1,
            order=1,
        )
        self.target_query = basic.TargetWeightQueries(self.outline)
        self.targets = list(self.target_query.targets)

    def test____weights(self):
        with self.assertNumQueries(1):
            list(self.target_query._TargetWeightQueries__weights())

    def test___time_periods(self):
        with self.assertNumQueries(1):
            list(self.target_query._TargetWeightQueries__time_periods())

    def test_target_period_dictionary(self):
        with self.assertNumQueries(1):
            self.target_query.target_period_dictionary()

    def test___dict_with_village_ids(self):
        with self.assertNumQueries(1):
            self.target_query._TargetWeightQueries__dict_with_village_ids([0])

    def test___target_dict_with_weights_extendeds(self):
        with self.assertNumQueries(1):
            self.target_query.target_dict_with_weights_extended()

    def test_target_dict_read_correct_dictionary(self):
        dict_true = {}
        weight = self.weight
        weight.distance = "0.0"
        dict_true[self.target] = [weight]
        self.assertEqual(
            self.target_query.target_dict_with_weights_read(), dict_true
        )

    def test_target_dict_read_correct_number_of_queries(self):
        with self.assertNumQueries(1):
            self.target_query.target_dict_with_weights_read()

    def test___create_target_dict_correct_dict(self):
        dict_result = {}
        dict_result[self.target] = []
        self.assertEqual(
            dict_result,
            self.target_query._TargetWeightQueries__create_target_dict(),
        )


