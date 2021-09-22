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

from django.urls import reverse

from base.tests.test_utils.mini_setup import MiniSetup


class PaymentDone(MiniSetup):
    def test_payment_done___302_not_auth_redirect_login(self):
        PATH = reverse("base:payment_done")

        response = self.client.get(PATH)
        assert response.status_code == 302
        assert response.url == self.login_page_path(next=PATH)

    def test_payment_done___200_foreign_user_works_ok(self):
        self.login_foreign_user()
        PATH = reverse("base:payment_done")

        response = self.client.get(PATH)
        assert response.status_code == 200

    def test_payment_done___200_auth_works_ok(self):
        PATH = reverse("base:payment_done")

        self.login_me()
        response = self.client.get(PATH)
        assert response.status_code == 200
