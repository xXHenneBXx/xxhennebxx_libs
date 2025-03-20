#
# Copyright (C) 2022 Sebastiano Barezzi
# Copyright (C) 2025 xXHenneBXx
# SPDX-License-Identifier: Apache-2.0
#
"""Logging utils."""

from logging import basicConfig, INFO, DEBUG
from logging import debug, info, warning, error, fatal
from colorama import Fore, Style

def LOGD(message):
	print(f"{Fore.BLUE}[DEBUG] {Style.RESET_ALL}",{message})

def LOGI(message):
	print(f"{Fore.GREEN}[INFO] {Style.RESET_ALL}",{message})

def LOGW(message):
	print(f"{Fore.YELLOW}[WARNING] {Style.RESET_ALL}",{message})

def LOGE(message):
	print(f"{Fore.MAGENTA}[ERROR] {Style.RESET_ALL}",{message})

def LOGF(message):
	print(f"{Fore.RED}[FATAL] {Style.RESET_ALL}",{message})

def setup_logging(verbose: bool = False):
	if verbose:
		basicConfig(format='[%(filename)s:%(lineno)s %(levelname)s] %(funcName)s: %(message)s',
		            level=DEBUG)
	else:
		basicConfig(format='[%(levelname)s] %(message)s', level=INFO)
