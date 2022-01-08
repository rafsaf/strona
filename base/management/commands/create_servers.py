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

from typing import Tuple

from django.conf import settings
from django.core.management.base import BaseCommand

from base.models import Server


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        server_info: Tuple[str, str]
        for server_info in settings.TRIBAL_WARS_SUPPORTED_SERVERS:
            _, created = Server.objects.get_or_create(
                dns=server_info[0], prefix=server_info[1]
            )
            self.stdout.write(
                self.style.SUCCESS(f"Created: {created}, Server: {server_info[0]}")
            )
        self.stdout.write(
            self.style.SUCCESS(
                f"Success, {len(settings.TRIBAL_WARS_SUPPORTED_SERVERS)} TW servers"
            )
        )
