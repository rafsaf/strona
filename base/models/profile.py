# Copyright 2021 Rafał Safin (rafsaf). All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import datetime
from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

if TYPE_CHECKING:
    from base.models import Message


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    server = models.ForeignKey(
        "Server", on_delete=models.SET_NULL, null=True, default=None
    )
    validity_date = models.DateField(
        default=datetime.date(year=2021, month=2, day=25), blank=True, null=True
    )
    messages = models.IntegerField(default=0)

    def is_premium(self) -> bool:
        if self.validity_date is None:
            return False
        today = timezone.localdate()
        if today > self.validity_date:
            return False
        return True

    def latest_messages(self) -> "QuerySet[Message]":
        from base.models.message import Message

        return Message.objects.order_by("-created")[:6]
