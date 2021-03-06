"""
    Copyright (C) 2017, ContraxSuite, LLC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    You can also be released from the requirements of the license by purchasing
    a commercial license from ContraxSuite, LLC. Buying such a license is
    mandatory as soon as you develop commercial activities involving ContraxSuite
    software without disclosing the source code of your own applications.  These
    activities include: offering paid services to customers as an ASP or "cloud"
    provider, processing documents on the fly in a web application,
    or shipping ContraxSuite within a closed source product.
"""
# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_auth.views import PasswordChangeSerializer, PasswordResetConfirmSerializer, \
    PasswordResetSerializer, LoginSerializer, LoginView, LogoutView, PasswordChangeView, \
    PasswordResetView, PasswordResetConfirmView
from rest_framework import serializers

# Project imports
from apps.common.schemas import CustomAutoSchema
from apps.users.authentication import TokenSerializer

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-contraxsuite/blob/1.8.0/LICENSE"
__version__ = "1.8.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class RestAuthCommonResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()


class LoginViewSchema(CustomAutoSchema):
    request_serializer = LoginSerializer()
    response_serializer = TokenSerializer()


class LogoutViewSchema(CustomAutoSchema):
    response_serializer = RestAuthCommonResponseSerializer()


class PasswordResetViewSchema(CustomAutoSchema):
    request_serializer = PasswordResetSerializer()
    response_serializer = RestAuthCommonResponseSerializer()


class PasswordResetConfirmViewSchema(CustomAutoSchema):
    request_serializer = PasswordResetConfirmSerializer()
    response_serializer = RestAuthCommonResponseSerializer()


class PasswordChangeViewSchema(CustomAutoSchema):
    request_serializer = PasswordChangeSerializer()
    response_serializer = RestAuthCommonResponseSerializer()


urlpatterns = [
    url(r'^login/$',
        LoginView.as_view(schema=LoginViewSchema()),
        name='rest_login'),
    url(r'^logout/$',
        LogoutView.as_view(schema=LogoutViewSchema()),
        name='rest_logout'),
    url(r'^password/reset/$',
        PasswordResetView.as_view(schema=PasswordResetViewSchema()),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$',
        PasswordResetConfirmView.as_view(schema=PasswordResetConfirmViewSchema()),
        name='rest_password_reset_confirm'),
    url(r'^password/change/$',
        PasswordChangeView.as_view(schema=PasswordChangeViewSchema()),
        name='rest_password_change'),
]
