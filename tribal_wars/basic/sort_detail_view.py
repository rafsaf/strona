from django.core.paginator import Paginator
from django.db.models import F

from .village import dist
from base import models


class SortAndPaginRequest:
    def __init__(self, outline, GET_request: str, PAGE_request, target):
        self.outline = outline
        self.target = target.target
        self.page = PAGE_request
        VALID = [
            "distance",
            "-distance",
            "-off_left",
            "-nobleman_left",
            "closest_offs",
            "farthest_offs",
            "closest_noblemans",
            "farthest_noblemans",
            "closest_noble_offs",
            "farthest_noble_offs",
        ]
        if GET_request is None:
            self.sort = "distance"
        if GET_request in VALID:
            self.sort = GET_request
        else:
            self.sort = "distance"

    def __nonused(self):
        nonused_vertices = models.WeightMaximum.objects.filter(
            outline=self.outline
        ).exclude(off_left=0, nobleman_left=0)

        return nonused_vertices

    def __pagin(self, lst_or_query):
        paginator = Paginator(lst_or_query, 16)
        page_obj = paginator.get_page(self.page)
        return page_obj

    def sorted_query(self):
        query = self.__nonused()

        if self.sort == "distance":
            query = list(query)
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance)
            return self.__pagin(query)

        elif self.sort in {"-off_left", "-nobleman_left"}:
            query = self.__pagin(query.order_by(self.sort))
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            return query

        elif self.sort == "-distance":
            query = list(query)
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance, reverse=True)
            return self.__pagin(query)

        elif self.sort == "closest_offs":
            query = list(query.filter(off_left__gte=self.outline.initial_outline_min_off))
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance)
            return self.__pagin(query)

        elif self.sort == "farthest_offs":
            query = list(query.filter(off_left__gte=self.outline.initial_outline_min_off))
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance, reverse=True)
            return self.__pagin(query)

        elif self.sort == "closest_noblemans":
            query = list(query.filter(nobleman_left__gte=1))
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance)
            return self.__pagin(query)

        elif self.sort == "farthest_noblemans":
            query = list(query.filter(nobleman_left__gte=1))
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance, reverse=True)
            return self.__pagin(query)

        elif self.sort == "closest_noble_offs":
            query = list(query.filter(
                nobleman_left__gte=1,
                off_left__gte=self.outline.initial_outline_min_off))
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance)
            return self.__pagin(query)

        elif self.sort == "farthest_noble_offs":
            query = list(query.filter(
                nobleman_left__gte=1,
                off_left__gte=self.outline.initial_outline_min_off))
            for weight in query:
                weight.distance = round(dist(weight.start, self.target), 1)
            query.sort(key=lambda weight: weight.distance, reverse=True)
            return self.__pagin(query)
