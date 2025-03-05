#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "ce627f37-ea77-4b45-bfd4-25a8bbe2ec21")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "DmR8Q~lRR.gLLSf4ouVjJsiQlXt~qip3~u.UEaDz")
