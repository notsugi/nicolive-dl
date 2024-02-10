#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from getpass import getpass

from . import LIVE_URL_PREFIX, NicoLiveDL


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Username/Email address")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument(
        "-l",
        "--live-id",
        help=f"Live ID or Live URL. Valid format of Live URL: {LIVE_URL_PREFIX}lv0123456789, lv0123456789 is the Live ID in this case",
    )
    parser.add_argument(
        "--otp-required",
        action="store_true",
        help="Whether an OTP is required to login (2FA enabled)",
    )
    parser.add_argument(
        "--save-comments",
        action="store_true",
        help="Whether to save comments. Comments will be saved in the same directory as the video",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    username = args.username or input("Account: ")
    password = args.password or getpass("Password: ")
    live_id = args.live_id or input("Live Id: ")

    nldl = NicoLiveDL()
    nldl.login(username, password, args.otp_required)
    nldl.download(live_id, save_comments=args.save_comments)


if __name__ == "__main__":
    main()
